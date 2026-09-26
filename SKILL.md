---
name: istofel-slides
description: >
  Transforma tutoriais, artigos, PDFs, links, anotações ou apenas um tema em uma
  apresentação didática completa em português (pt-BR): minimalista, visual
  (diagramas, números grandes, ícones, fluxos), com notas do apresentador em
  todos os slides e tempo de fala calculado slide a slide, publicada como deck
  editável e exportável (PPTX/PDF). Antes de montar, faz 3–4 perguntas sobre o
  conteúdo (público-alvo, duração, foco). Use SEMPRE que o usuário trouxer um material e pedir
  "apresentação", "slides", "deck", "seminário", "aula", "palestra", "transforma
  isso em apresentação", "prepara uma apresentação sobre", ou colar um texto com
  ideias de slides — mesmo sem dizer "skill" ou "istofel-slides". Use também
  para revisar, expandir ou traduzir um deck criado por ela. Se o usuário pedir
  explicitamente um arquivo .pptx, use esta skill para o conteúdo e o design e a
  skill pptx para gerar o arquivo.
---

# istofel-slides

Pega qualquer material-fonte e entrega uma apresentação rica, em português,
pronta para dar aula: arco narrativo pensado para o público, uma ideia por
slide, conteúdo traduzido em visuais e um roteiro de fala em cada slide.

O deck de referência que originou esta skill está em `assets/exemplo-deck/`
(17 slides sobre agentes de IA). Ele é o padrão de qualidade: quando estiver em
dúvida sobre markup, proporção ou tom, abra o slide equivalente e adapte.

## Padrões fixos

| Item | Padrão |
|---|---|
| Idioma | Português do Brasil, mesmo se a fonte estiver em outro idioma |
| Apresentador | Campo em branco `[Nome do apresentador]` na capa e no encerramento |
| Estilo | Minimalista; paleta escolhida pelo tema (ver `references/design.md`) |
| Notas | Em todos os slides, começando pelo tempo de fala `[~X min]` |
| Formato | Artifact do tipo Slides; sem ele, veja `references/pipeline.md` |

Público, duração e foco **não têm padrão**: vêm sempre do briefing (passo 3).

## Fluxo

### 1. Ler a fonte

- Texto colado: já está no contexto.
- Arquivo: PDF → skill `pdf-reading`; .docx/.pptx → skills correspondentes.
- Link: `web_fetch`.
- Só um tema: pesquise (5–10 buscas, fontes primárias) antes de estruturar.
- Se o usuário mandou um roteiro de slides junto, trate-o como **proposta**:
  preserve a intenção, reorganize e complete livremente, e explique o que mudou.

### 2. Analisar criticamente (antes de desenhar)

Monte, para uso próprio, um mapa do conteúdo:

1. **Tese central** em uma frase — vira o slide de fechamento.
2. **Conceitos-chave** e a relação entre eles (sequência? ciclo? hierarquia? comparação?).
3. **Dados numéricos** com a fonte de cada um. Nunca invente estatística ou
   citação; número sem fonte fica fora ou vira `[dado a confirmar]`.
4. **Lacunas para o público**: que conceito a turma precisa antes de entender o
   resto? Isso vira um slide de nivelamento (no exemplo: "O que é um agente?").
5. **Erros e imprecisões** da fonte ou da tradução (no exemplo: "MCP" traduzido
   errado). Corrija no deck e relate na entrega.
6. **Afirmações recentes ou surpreendentes** (números de mercado, anúncios,
   versões): se houver busca disponível, confira as mais importantes; se não
   der, marque nas notas "conforme o material-fonte".
7. **Falta de exemplo concreto**: crie um exemplo próximo da realidade dos
   alunos (ex.: um banco de dados acadêmico, um sistema da própria instituição).

### 3. Briefing com o usuário (obrigatório)

Só depois de ler e analisar a fonte, faça **3 ou 4 perguntas** — perguntas
específicas deste conteúdo rendem um deck muito mais rico do que qualquer
padrão. Não comece a construir antes das respostas.

Sempre pergunte:
1. **Público-alvo** (ex.: calouros, alunos avançados, ensino técnico,
   profissionais, gestores). Define nível, vocabulário e exemplos.
2. **Duração total** da apresentação. Define o número de slides e o tempo de cada um.

E mais 1–2 perguntas nascidas da análise do passo 2, por exemplo:
- Foco: qual parte do material merece mais tempo (ex.: "mercado e carreira" ×
  "como construir na prática")?
- Profundidade técnica: visão conceitual, com exemplos de código, ou com demonstração?
- Contexto dos alunos: o que já sabem, ou em que disciplina/projeto isso se encaixa?
- Tratamento de algo polêmico, datado ou fraco na fonte (manter, atualizar, cortar?).

Como perguntar: uma frase curta de contexto (o que você entendeu do material,
em 1–2 linhas) e depois o `ask_user_input` com até 3 perguntas de opções curtas
(limite da ferramenta). Se houver uma 4ª pergunta, escreva-a na frase de
contexto, antes da ferramenta. Pule só as perguntas que o usuário já respondeu
na mensagem.

### 4. Arquitetura narrativa

Leia `references/narrativa.md` para o arco padrão, a tabela duração → número de
slides, o **cálculo do tempo por slide**, os slides pedagógicos (objetivos,
pausa para pensar, checagem) e as regras das notas do apresentador.

O tempo de cada slide depende do assunto dele, não de uma média fixa: um
diagrama que explica um conceito novo leva mais que uma estatística ou uma
transição. Estime cada slide, some e ajuste até bater a duração informada.

Regras que não mudam:
- Uma ideia por slide. Se não cabe, divida — nunca diminua a fonte.
- Títulos introduzem o tema, com a mesma gramática no deck todo.
- Lista longa é sinal de que falta um diagrama: veja o passo 4.

### 5. Traduzir conteúdo em visual

Para cada slide, identifique a **forma** do conteúdo e escolha o padrão em
`references/padroes.md` (catálogo com o arquivo de exemplo de cada um e trechos
prontos de padrões novos). Resumo:

| Forma do conteúdo | Padrão |
|---|---|
| Mudança / antes e depois | Dois cards + conector |
| Processo cíclico | Loop pinado com 4 caixas |
| Sistema com partes | Hub (centro + satélites) |
| Etapas em sequência | Pipeline horizontal |
| Um agente/serviço acionando várias coisas | Fan-out |
| Estatísticas | Números grandes (até 3) |
| Camadas / pré-requisitos | Pirâmide de camadas |
| Lista de habilidades/itens curtos | Grade de chips com ícones |
| Vários padrões/tipos | Grade de cards com mini-diagramas |
| Métricas / critérios | Grade de tiles com ícones |
| Certo × errado, mito × fato | Contraste claro/escuro |
| Amplitude × profundidade | Diagrama em T |
| Comparação com vários atributos | Tabela |
| Evolução histórica | Linha do tempo |
| Código, SQL, comando | Bloco de código |

Imagens: só use arquivos que o usuário enviou (faça upload como asset). Não
busque fotos na web para o deck. Ofereça inserir fotos se o usuário tiver.

### 6. Design

Leia `references/design.md`: escolha a paleta pelo tema, use a escala
tipográfica fixa e respeite o orçamento de espaço (é o que evita texto
estourando o slide).

### 7. Construir, validar e publicar

Leia `references/pipeline.md` e siga na ordem. Resumo: listar tipos → ler o
tipo Slides (as instruções dele têm prioridade sobre esta skill em caso de
conflito) → checar design system → criar o deck vazio → escrever todos os
slides e o `deck.json` numa pasta → rodar o validador:

```bash
python /mnt/skills/user/istofel-slides/scripts/validar_deck.py <pasta-do-deck>/project
```

(ajuste o caminho para onde a skill estiver instalada). Corrija todos os
**ERROS** e avalie os **AVISOS**; o script também imprime os lotes de
publicação (máx. 16 arquivos por chamada, `deck.json` no último lote).

### 8. Entregar (curto e objetivo)

```
A apresentação está pronta: <link>

<N> slides, <estilo>, para <público> em <duração>, com notas e tempo de fala em todos.

Tempo por bloco: Abertura ~X min · <bloco> ~X min · … · Fechamento ~X min

O que mudei em relação à sua proposta:
- <mudança 1>
- ...

Correções na fonte: <se houver>

Para revisar:
- Preencher [Nome do apresentador] na capa e no encerramento
- <outros placeholders, suposições, números a conferir>

Posso também gerar um quiz no Moodle (GIFT) a partir da checagem ou um resumo de uma página para os participantes?
```

Termine a entrega **exatamente** com essa pergunta.

Não descreva o mecanismo (arquivos, JSON, chamadas); diga o que o usuário recebe.

### 9. Extras (só se o usuário aceitar)

**Quiz GIFT (Moodle)**
1. Se a skill `moodle-gift` estiver disponível, leia o `SKILL.md` dela e siga-a.
   Se não, use `references/gift.md`.
2. Monte 8–12 questões a partir da checagem final e dos conceitos centrais de
   cada bloco (misture múltipla escolha, V/F, associação e resposta curta), com
   feedback nas alternativas, categoria com o título do deck e dificuldade
   adequada ao público do briefing.
3. Salve em `/mnt/user-data/outputs/<tema-em-kebab-case>.gift` (UTF-8) e
   entregue com `present_files`.
4. Resposta: **só o arquivo** e, no máximo, uma linha ("Quiz com N questões,
   pronto para importar no Moodle."). Sem explicar o formato.

**Resumo de uma página**
Leia a skill `pdf`, gere um PDF de 1 página em pt-BR (tese central, 5–7 ideias
principais, 1 diagrama simples ou tabela, referências) com a mesma paleta do
deck e entregue só o arquivo, com no máximo uma linha de texto.

## Português

- pt-BR com acentuação correta; revise ortografia antes de publicar.
- Termos técnicos consagrados ficam em inglês (tool calling, embedding,
  guardrails), com explicação curta na primeira aparição (nas notas ou no slide).
- Números no formato brasileiro: 18,9%; US$ 2 bi; 177 mil.
- Nada de tradução literal truncada: reescreva a ideia em português natural.

## Revisões posteriores

Pedidos de ajuste ("troca o slide 5", "deixa mais curto", "muda a cor"): siga o
fluxo de revisão do tipo Slides — leia os arquivos atuais do deck (o usuário
pode ter editado à mão), altere só o que foi pedido, valide e publique só os
arquivos alterados. Mudou quantidade de slides? Atualize `order` e os números
de página nos rodapés.

## Checklist antes de publicar

- [ ] Todo número tem fonte (rodapé ou notas); nada inventado
- [ ] Slide de nivelamento se o público precisa de um conceito-base
- [ ] Nenhuma lista longa onde caberia um diagrama
- [ ] Briefing respondido (público, duração e 1–2 perguntas do conteúdo)
- [ ] Soma dos tempos `[~X min]` das notas = duração informada (±10%)
- [ ] `[Nome do apresentador]` como campo em branco, sem nome fixo
- [ ] Rodapés com número de página corretos e em sequência
- [ ] Notas em todos os slides, em pt-BR, com fala natural
- [ ] Placeholders `[...]` listados na entrega
- [ ] Validador sem ERROS
- [ ] Entrega termina com a pergunta do quiz/resumo
