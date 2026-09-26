# Design do deck

## Canvas e orçamento de espaço (o que evita estouro)

- Canvas 1920×1080. Section com `padding:128px 128px 160px` quando há rodapé
  → área útil 1664×792. Sem rodapé (capa, fechamento): `padding:128px` → 1664×824.
- Cabeçalho padrão (eyebrow 24px + gap 16 + h2 72px em 1 linha) ≈ 130px; com o
  gap de 48 da section sobram **~610px** para o corpo. Se o h2 quebrar em 2
  linhas, sobram ~530px.
- Largura estimada do texto: `caracteres × 0,6 × font-size` (negrito/caixa-alta: 0,65).
  h2 a 72px cabe ~38 caracteres por linha; texto a 32px em 640px cabe ~33.
- Altura: título ≈ size × linhas × 1,1; parágrafo ≈ size × linhas × 1,4;
  card = conteúdo + padding (nunca fixe altura menor que isso).
- Caixas devem ser mais largas que a palavra mais longa (texto só quebra em espaço).
- Rodapé: um único `<p>` pinado em `bottom:64px`, 24px: "NN" ou "NN · Fonte: …".
- Máx. 200 elementos por slide; fonte mínima 24px em tudo.

## Escala tipográfica (fixa)

120 (número grande) · 96 (capa/declaração) · 72 (título) · 44 (subtítulo, card
de destaque) · 32 (texto) · 24 (eyebrow, rótulo, rodapé, notas visuais).
104px só para números grandes em 3 colunas (evita estouro).

## Paletas

Escolha pelo tema; use exatamente estes hex. "Texto seguro" = cor de destaque
com contraste ≥ 4,5:1 sobre o fundo claro (use para texto); a cor "preenchimento"
é para formas, fundos e texto grande sobre escuro.

### A. Tech noturno (computação, IA, dados, engenharia) — padrão
| Papel | Hex |
|---|---|
| Fundo escuro / texto principal | #121826 |
| Fundo claro | #F4F2EC |
| Fundo alternativo claro | #EAE6DC |
| Card claro / borda | #FBFAF6 / #DEDAD0 |
| Texto secundário (claro) / rodapé | #4A5263 / #5A6070 |
| Card escuro / borda escura | #1E2638 / #3A4458 |
| Texto secundário (escuro) / rodapé escuro | #B8C0CF / #8A93A6 |
| Destaque preenchimento / texto seguro | #F2994A / #A2520F |
| Secundária (ícones, números) claro / escuro | #2F5DB8 / #7FA7F5 |
Fontes: Space Grotesk (títulos) + IBM Plex Sans (texto) + JetBrains Mono (rótulos, código).

### B. Acadêmico sóbrio (educação, metodologia, humanas, pesquisa)
| Papel | Hex |
|---|---|
| Fundo escuro / texto | #1C2B33 |
| Fundo claro / alternativo | #F5F1EA / #EBE4D8 |
| Card / borda | #FCFAF6 / #E0D9CC |
| Texto secundário / rodapé | #4B565C / #5C666B |
| Card escuro / borda escura | #26363F / #3B4C55 |
| Texto secundário escuro / rodapé escuro | #B9C4C8 / #8E9BA0 |
| Destaque preenchimento / texto seguro | #3E8E82 / #2A6B61 |
| Secundária preenchimento / texto seguro | #D08A3E / #8C5214 |
Fontes: Libre Baskerville (títulos) + Public Sans (texto) + JetBrains Mono (rótulos).

### C. Vibrante (introdutório, calouros, eventos, divulgação)
| Papel | Hex |
|---|---|
| Fundo escuro / texto | #1B1F3B |
| Fundo claro / alternativo | #FBF6EC / #F1E9DA |
| Card / borda | #FFFCF6 / #E6DCCB |
| Texto secundário / rodapé | #4A4E69 / #5B5F78 |
| Card escuro / borda escura | #262B52 / #3B416E |
| Texto secundário escuro / rodapé escuro | #C3C6E0 / #9A9EC0 |
| Destaque preenchimento / texto seguro | #FF6B4A / #B83A1E |
| Secundária preenchimento / texto seguro | #4D6BFE / #2F45C4 |
Fontes: Rubik (títulos) + Nunito Sans (texto) + Fira Code (rótulos, código).

Se o usuário tiver um design system (a listagem de "Design System" retornar um
padrão), ele substitui a paleta e as fontes.

### Entradas `faces` do deck.json

```json
"space-grotesk":{"family":"Space Grotesk","href":"https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400..700&display=swap"},
"ibm-plex-sans":{"family":"IBM Plex Sans","href":"https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap"},
"jetbrains-mono":{"family":"JetBrains Mono","href":"https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap"},
"libre-baskerville":{"family":"Libre Baskerville","href":"https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap"},
"public-sans":{"family":"Public Sans","href":"https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&display=swap"},
"rubik":{"family":"Rubik","href":"https://fonts.googleapis.com/css2?family=Rubik:wght@400..700&display=swap"},
"nunito-sans":{"family":"Nunito Sans","href":"https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap"},
"fira-code":{"family":"Fira Code","href":"https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap"}
```
Use no máximo 4 faces (normalmente 3).

## Ritmo visual

- Alterne fundos: maioria clara; 2–4 slides escuros para momentos de impacto
  (capa, evidências, "a maior mudança", pausa); 1 slide de fundo destaque
  (fechamento).
- Cabeçalho sempre no mesmo lugar (topo), nunca centralizado com o corpo.
- Cor nunca carrega significado sozinha: escreva também a palavra.

## Blocos base (paleta A; troque os hex para outras paletas)

Section clara:
```html
<section id="ID" data-transition="fade" style="background:#F4F2EC; color:#121826; font-family:'IBM Plex Sans', Arial, sans-serif; padding:128px 128px 160px; display:flex; flex-direction:column; gap:48px">
```
Cabeçalho:
```html
<div style="display:flex; flex-direction:column; gap:16px">
<p style="font-family:'JetBrains Mono', 'Courier New', monospace; font-size:24px; color:#A2520F; letter-spacing:2px; text-transform:uppercase">EYEBROW</p>
<h2 style="font-family:'Space Grotesk', Arial, sans-serif; font-size:72px; font-weight:600; line-height:1.1; color:#121826">Título</h2>
</div>
```
Rodapé:
```html
<p style="position:absolute; left:128px; bottom:64px; width:1664px; font-family:'JetBrains Mono', 'Courier New', monospace; font-size:24px; color:#5A6070">NN · Fonte: …</p>
```
Card claro: `background:#FBFAF6; border:1px solid #DEDAD0; border-radius:20px; padding:32px`
Card escuro: `background:#121826; border-radius:24px; padding:48px` (texto #F4F2EC / #B8C0CF)

Ícones disponíveis (`<x-icon name="…">`, nomes exatos):
Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe
GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search
Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench
