#!/usr/bin/env python3
"""Valida os arquivos de um deck do tipo Slides antes de publicar.

Uso: python validar_deck.py <pasta-do-deck>/project

Checa deck.json, estrutura de cada slide e regras do formato que já causaram
problemas. Imprime ERROS (corrigir) e AVISOS (avaliar) e, no fim, os lotes de
publicação (file_path + até 15 arquivos; deck.json no último lote).
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ICONES = set(
    "Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe "
    "GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search "
    "Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench".split()
)
TAGS = {
    "section", "h1", "h2", "h3", "p", "ul", "ol", "li", "br", "b", "i", "u", "a",
    "span", "div", "img", "table", "tr", "th", "td", "svg", "hr", "x-shape",
    "x-icon", "x-connector", "x-embed", "aside",
}
VOID = {"br", "hr", "img"}
ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
LARGURA_UTIL = 1664


class Slide(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.erros, self.avisos = [], []
        self.pilha = []
        self.n_elem = 0
        self.secoes = []
        self.filhos_secao = []
        self.lixo_fora = False
        self.aside_txt = ""
        self.em_svg = 0
        self.titulos = []  # (tag, font_size, width, texto)
        self._titulo = None

    def _estilo(self, tag, estilo):
        decls = [d.strip() for d in estilo.split(";") if d.strip()]
        props = {}
        for d in decls:
            if ":" not in d:
                continue
            k, v = d.split(":", 1)
            k, v = k.strip().lower(), v.strip()
            props[k] = v
            if k in ("margin", "margin-top", "margin-bottom", "margin-left", "margin-right"):
                self.erros.append(f"<{tag}>: '{k}' não é suportado (use gap/padding)")
            if k == "z-index" or k == "float":
                self.erros.append(f"<{tag}>: '{k}' não é suportado")
            if "var(" in v:
                self.erros.append(f"<{tag}>: var() não é suportado")
            if k != "letter-spacing" and re.search(r"\d(?:\.\d+)?(em|rem|vw|vh)\b", v):
                self.erros.append(f"<{tag}>: unidade relativa em '{k}: {v}' (use px)")
            if k == "font-size":
                m = re.match(r"([\d.]+)px", v)
                if m and float(m.group(1)) < 24:
                    self.erros.append(f"<{tag}>: font-size {v} < 24px")
        return props

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        profundidade = len(self.pilha)
        self.n_elem += 1
        if self.em_svg:
            if tag not in VOID:
                self.pilha.append(tag)
                self.em_svg += 1
            return
        if profundidade == 0:
            if tag == "section":
                self.secoes.append(a.get("id"))
            else:
                self.lixo_fora = True
        elif profundidade == 1 and self.pilha[0] == "section":
            self.filhos_secao.append(tag)
        if tag not in TAGS:
            self.erros.append(f"tag <{tag}> não suportada")
        if "class" in a:
            self.avisos.append(f"<{tag}>: atributo class é ignorado")
        props = self._estilo(tag, a.get("style") or "")
        if tag == "section" and "background" not in props:
            self.erros.append("section sem background")
        if tag == "x-icon" and a.get("name") not in ICONES:
            self.erros.append(f"x-icon com nome inválido: {a.get('name')!r}")
        if tag == "img":
            src = a.get("src")
            if src and not re.match(r"^/?_blob/", src):
                self.erros.append(f"img com src não permitido: {src[:60]!r} (faça upload como asset)")
        if tag == "div":
            divs = sum(1 for t in self.pilha if t == "div") + 1
            if divs > 15:
                self.erros.append("mais de 15 <div> aninhados")
        if tag in ("h1", "h2") and "position" not in props:
            fs = re.match(r"([\d.]+)px", props.get("font-size", ""))
            w = re.match(r"([\d.]+)px", props.get("width", ""))
            self._titulo = [tag, float(fs.group(1)) if fs else None,
                            float(w.group(1)) if w else None, ""]
        if tag == "svg":
            self.em_svg = 1
        if tag not in VOID:
            self.pilha.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.pilha and self.pilha[-1] == tag:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.em_svg:
            self.em_svg -= 1
        if self._titulo and tag == self._titulo[0]:
            self.titulos.append(tuple(self._titulo))
            self._titulo = None
        if self.pilha and self.pilha[-1] == tag:
            self.pilha.pop()
        else:
            self.erros.append(f"fechamento </{tag}> fora de ordem")
            if tag in self.pilha:
                while self.pilha and self.pilha.pop() != tag:
                    pass

    def handle_data(self, data):
        if not self.pilha and data.strip():
            self.lixo_fora = True
        if self.pilha and self.pilha[-1] == "aside":
            self.aside_txt += data
        if self._titulo:
            self._titulo[3] += data


def validar(proj: Path):
    erros, avisos = [], []
    deck_path = proj / "deck.json"
    slides_dir = proj / "slides"
    if not slides_dir.is_dir():
        print(f"ERRO: pasta {slides_dir} não existe")
        return 1
    arquivos = sorted(p.stem for p in slides_dir.glob("*.html"))
    order = []
    if deck_path.exists():
        try:
            deck = json.loads(deck_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"ERRO: deck.json inválido: {e}")
            return 1
        order = deck.get("order", [])
        if not deck.get("title"):
            erros.append("deck.json: falta 'title'")
        if "createdOnFiles" not in deck:
            avisos.append("deck.json: falta 'createdOnFiles' (obrigatório num índice novo)")
        for sid in order:
            if not ID_RE.match(sid):
                erros.append(f"deck.json: id inválido em order: {sid!r}")
            elif sid not in arquivos:
                erros.append(f"deck.json: '{sid}' está em order mas slides/{sid}.html não existe")
        if len(set(order)) != len(order):
            erros.append("deck.json: ids repetidos em order")
        for sid in arquivos:
            if sid not in order:
                avisos.append(f"slides/{sid}.html não está em order (aparece no fim)")
        if deck.get("cover") and deck["cover"] not in order:
            erros.append("deck.json: 'cover' não está em order")
        for k, s in (deck.get("sections") or {}).items():
            if s.get("start") not in order:
                erros.append(f"deck.json: seção {k} começa em slide inexistente {s.get('start')!r}")
        faces = deck.get("faces") or {}
        if len(faces) > 4:
            erros.append("deck.json: mais de 4 faces")
        for k, f in faces.items():
            esperado = f.get("family", "").lower().replace(" ", "-")
            if k != esperado:
                erros.append(f"deck.json: chave de face {k!r} deveria ser {esperado!r}")
            href = f.get("href")
            if href and not href.startswith("https://fonts.googleapis.com/css2?"):
                erros.append(f"deck.json: href de fonte não permitido em {k!r}")
    else:
        avisos.append("deck.json não encontrado (ok só se estiver revisando slides existentes)")

    for sid in arquivos:
        texto = (slides_dir / f"{sid}.html").read_text(encoding="utf-8")
        p = Slide()
        p.feed(texto)
        p.close()
        pre = f"[{sid}]"
        for e in p.erros:
            erros.append(f"{pre} {e}")
        for a in p.avisos:
            avisos.append(f"{pre} {a}")
        if len(p.secoes) != 1:
            erros.append(f"{pre} precisa de exatamente 1 <section> (achou {len(p.secoes)})")
        elif p.secoes[0] != sid:
            erros.append(f"{pre} id da section ({p.secoes[0]!r}) difere do nome do arquivo")
        if p.lixo_fora:
            erros.append(f"{pre} há conteúdo fora da <section>")
        if p.n_elem > 200:
            erros.append(f"{pre} {p.n_elem} elementos (máx. 200)")
        if "aside" in p.filhos_secao:
            if p.filhos_secao[-1] != "aside":
                erros.append(f"{pre} <aside> precisa ser o último filho da section")
            if len(p.aside_txt) > 4000:
                erros.append(f"{pre} notas com {len(p.aside_txt)} caracteres (máx. 4000)")
        else:
            avisos.append(f"{pre} sem notas do apresentador (<aside>)")
        for tag, fs, w, txt in p.titulos:
            if not fs:
                continue
            larg = w or LARGURA_UTIL
            linhas = -(-len(txt.strip()) * 0.6 * fs // larg)
            if tag == "h2" and linhas > 1:
                avisos.append(f"{pre} título h2 deve quebrar em {int(linhas)} linhas: '{txt.strip()[:50]}'")

    for e in erros:
        print("ERRO:", e)
    for a in avisos:
        print("AVISO:", a)
    print(f"\n{len(arquivos)} slides · {len(erros)} erro(s) · {len(avisos)} aviso(s)")

    ordem = [s for s in order if s in arquivos] + [s for s in arquivos if s not in order]
    caminhos = [str((slides_dir / f"{s}.html").resolve()) for s in ordem]
    if deck_path.exists():
        caminhos.append(str(deck_path.resolve()))
    print("\nLotes de publicação (file_path = 1º item; files = o resto):")
    for i in range(0, len(caminhos), 16):
        lote = caminhos[i:i + 16]
        print(f"  Lote {i // 16 + 1}: file_path={lote[0]}")
        print(f"           files={json.dumps(lote[1:], ensure_ascii=False)}")
    return 1 if erros else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(validar(Path(sys.argv[1])))
