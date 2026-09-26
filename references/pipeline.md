# Pipeline de construção e publicação (claude.ai, ferramenta Artifact)

As instruções do próprio tipo Slides (retornadas ao lê-lo) são a autoridade;
este resumo registra o caminho que funcionou e os limites já aprendidos.

## Passo a passo

1. `Artifact` → `action:"list"`, `scope:"types"`. Anote o `type_url` do tipo **Slides**.
2. `Artifact` → `action:"read"`, `type_url:<Slides>`. Leia as instruções (formato
   do slide, deck.json, limites). Se algo divergir desta skill, vale o tipo.
3. `Artifact` → `action:"list"`, `type:"Design System"`.
   - Um marcado como padrão → use (tokens e fontes dele; instale conforme o tipo manda).
   - Vários sem padrão → pergunte qual usar.
   - Nenhum → use a paleta de `design.md`.
4. Criar o deck vazio: `action:"publish"`, `type_url:<Slides>`, `title:<título>`,
   sem arquivos. Guarde o `url` retornado e **nunca** crie outro deck para o mesmo trabalho.
5. `action:"read"`, `url:<deck>` → cria a pasta local
   `/mnt/user-data/outputs/artifacts/<id>/`. Escreva tudo em `<pasta>/project/`:
   - `project/slides/<id>.html` — um `<section id="<id>">` por arquivo, nada fora dele.
   - `project/deck.json` — índice (modelo abaixo).
   Escreva todos os slides de uma vez (um único comando bash com heredocs `<<'EOF'`).
6. Validar: `python <skill>/scripts/validar_deck.py <pasta>/project`. Corrija ERROS.
7. Publicar em lotes: `action:"publish"`, `url:<deck>`, `file_path:<1º arquivo>`,
   `files:[até 15 caminhos absolutos]`. `deck.json` vai no **último** lote.
   O validador imprime os lotes prontos.
8. Não renderize, não abra no navegador e não releia o deck para "conferir"
   depois de publicar, a menos que o usuário peça.

## Modelo de deck.json

```json
{"v":4,
 "createdOnFiles":{"v":1,"at":"<agora ISO-8601>"},
 "title":"<título>",
 "order":["cover","roteiro","..."],
 "cover":"cover",
 "sections":{"s1":{"description":"<frase>","start":"cover"},"s2":{"description":"<frase>","start":"<id>"}},
 "faces":{ "<chave>": {"family":"<Nome>","href":"https://fonts.googleapis.com/css2?..."} },
 "designSystems":[]}
```
Ids: `[A-Za-z0-9_-]{1,64}`, iguais ao nome do arquivo e ao `id` da section.

## Limites que já causaram problema

- Só estilos inline, em px. Sem `margin`, `em/rem/vw/vh`, `var()`, `z-index`, classes, `<style>`.
- Fonte mínima 24px. Máx. 200 elementos por slide, 15 níveis de `<div>`.
- Elementos pinados (`position:absolute`) vêm antes do conteúdo em fluxo se ficarem atrás dele.
- Host pinado (`position:relative` com filhos absolutos): máx. 24 filhos; conectores contam.
- `<x-connector>` sem coordenadas = seta em fluxo (`style="width:48px"` numa linha);
  com coordenadas = relativo ao host (`x1 y1 x2 y2`, `route="hv|vh|elbow"`, `head="none|both"`).
- `flex:1` só funciona em filhos `<div>`; envolva `<p>` num `<div>` para dividir espaço.
- `<span>` não aceita tamanho/fonte; use blocos separados.
- Imagens só via upload (`asset:true`) → `src="/_blob/<id>"`. Nunca URL externa ou data URI.
- Notas: `<aside>` como último filho da section, texto puro, ≤ 4.000 caracteres.
- Recuo em código: espaços colapsam; use `&#160;`. Máx. 100 marcações inline por bloco.

## Se não houver o tipo Slides

- Usuário quer arquivo editável → leia a skill `pptx` e gere .pptx com o mesmo
  arco, paleta e padrões (diagramas como formas nativas).
- Caso contrário → um único HTML de slides (16:9, navegação por setas) publicado
  como artifact comum, seguindo as regras de páginas publicadas.
