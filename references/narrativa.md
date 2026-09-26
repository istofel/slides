# Narrativa, pedagogia, tempo e notas

## Arco padrão (adapte ao material)

| # | Slide | Função | Exemplo no deck de referência |
|---|---|---|---|
| 1 | Capa | Tema + promessa em uma frase | `cover.html` |
| 2 | Roteiro ou Objetivos | Mapa da aula | `roteiro.html` |
| 3 | Contexto | Por que isso importa agora / qual problema | `paradigma.html` |
| 4 | Nivelamento | Conceito-base que o público precisa | `agente.html` |
| 5 | Modelo mental | Um diagrama que organiza o assunto todo | `anatomia.html` |
| 6 | Evidências | Dados que sustentam a relevância | `mercado.html` |
| 7 | Visão geral do núcleo | Mapa das seções centrais | `pilares.html` |
| 8…n | Núcleo | Um slide por ideia (pilar, etapa, técnica) | `pilar1`…`pilar5` |
| — | Pausa para pensar | Pergunta à turma (em aulas ≥ 20 min) | padrão novo |
| n+1 | Filtro / armadilhas | Erros comuns, mitos, hype | `hype.html` |
| n+2 | Aplicação | Perfil, projetos, próximos passos | `perfil-t`, `portfolio` |
| n+3 | Fechamento | Tese central + "Perguntas?" (fundo de destaque) | `encerramento.html` |
| n+4 | Fontes | Referências para consulta | `fontes.html` |

Nem todo material tem todas as etapas: tutorial técnico passo a passo, por
exemplo, troca "Evidências" por "Demonstração" (blocos de código, pipeline).

## Duração → tamanho

| Formato | Slides | Pedagógicos extras |
|---|---|---|
| Relâmpago (10–15 min) | 8–10 | nenhum |
| Seminário (20–30 min) | 14–18 | 1 pausa para pensar (opcional) |
| Aula (45–50 min) | 20–26 | objetivos + 2 pausas + checagem final |
| Minicurso / 2 aulas | divida em 2 decks com recapitulação no início do 2º | |

A quantidade é só ponto de partida; o que manda é a soma dos tempos abaixo.

## Tempo por slide (calcular pelo assunto)

Classifique cada slide e atribua o tempo-base, depois ajuste pelo público:

| Tipo de slide | Tempo-base |
|---|---|
| Capa, roteiro, fontes | 0,5 min |
| Transição, declaração, fechamento | 0,5–1 min |
| Estatísticas / números grandes | 1,5 min |
| Conceito conhecido, lista curta, cards | 1,5–2 min |
| Contraste, comparação, tabela | 2 min |
| Conceito novo com diagrama (loop, hub, pipeline) | 3 min |
| Bloco de código explicado linha a linha | 3–4 min |
| Pausa para pensar / discussão | 2–3 min (tempo da atividade) |
| Demonstração ao vivo | o tempo informado pelo usuário |

Ajustes: público iniciante ou conceito central da aula → +30 a 50%; público
avançado ou assunto de apoio → −25%. Some tudo; se passar da duração, corte ou
funda slides de apoio (nunca o nivelamento nem o núcleo); se sobrar, acrescente
uma pausa para pensar ou um exemplo. Deixe ~10% de folga para perguntas.

Registre o tempo no início das notas de cada slide (`[~2 min]`) e informe o
total por bloco na entrega.

## Slides pedagógicos (melhorias em relação ao roteiro "puro")

- **Objetivos de aprendizagem** (aulas ≥ 45 min, ou quando o usuário pedir):
  3 cards com verbos observáveis (Compreender, Identificar, Aplicar,
  Comparar, Avaliar). Pode substituir o roteiro.
- **Pausa para pensar**: slide escuro com uma pergunta grande; resposta
  esperada nas notas. Coloque depois do nivelamento ou no meio do núcleo.
- **Checagem final**: 3 perguntas rápidas antes do fechamento; as respostas
  ficam nas notas. É também a base do quiz GIFT oferecido na entrega.
- **Glossário** (opcional): quando o material tem muitos termos em inglês.

## Notas do apresentador

Cada slide tem `<aside>` com 60–120 palavras (máx. 4.000 caracteres):
- Comece pela ideia principal em linguagem falada, não repita o slide.
- Inclua 1 exemplo concreto ou analogia quando o conceito é abstrato.
- Em slides com números: cite a fonte e um cuidado de interpretação.
- Onde couber, uma pergunta para a turma.
- Sempre comece com o tempo calculado: "[~2 min]".
- Qualquer um que abre o deck lê as notas: nada de comentários privados.

## Textos na tela

- Título: tema do slide, até ~38 caracteres a 72px (1 linha).
- Frase de apoio: até 2 linhas.
- Itens de lista: 2–6 palavras cada; máximo 4–5 por bloco.
- Declarações de impacto (fechamento, contraste) podem ter 1 frase longa em 96px.
