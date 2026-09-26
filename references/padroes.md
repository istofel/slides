# Catálogo de padrões visuais

Cada padrão aponta para um slide pronto em `assets/exemplo-deck/slides/`.
Abra o arquivo, copie a estrutura e troque textos, ícones e cores. Os números
de geometria (posições pinadas) já estão calculados e testados.

## Padrões do deck de referência

| Padrão | Arquivo | Quando usar | Notas de adaptação |
|---|---|---|---|
| Capa com hub decorativo | `cover.html` | Abertura | Título em caixa de 1200px para não colidir com o hub (canto sup. direito). Troque os 4 ícones pelo tema. |
| Roteiro numerado | `roteiro.html` | Mapa da aula | 5 linhas de 44px; até 6 cabem. |
| Antes → depois | `paradigma.html` | Mudança, evolução, problema → solução | Card claro (antes) + conector + card escuro (agora) + frase-âncora com borda de destaque. |
| Loop de 4 etapas | `agente.html` | Ciclos (PDCA, ciclo de vida, loop de agente, TDD) | Texto à esquerda (640px) + host 960×560. Caixas 320×160; conectores `hv`/`vh` já posicionados. |
| Hub com 6 satélites | `anatomia.html` | Arquitetura, componentes de um sistema, responsabilidades | Host 1664×580; centro 400×140; satélites 440×120. Títulos ≤ 16 caracteres, descrições ≤ 22. |
| Números grandes | `mercado.html` | 2–3 estatísticas | Fundo escuro. 104px em 3 colunas. Rodapé com fonte obrigatório. |
| Pirâmide de camadas | `pilares.html` | Pré-requisitos, níveis, visão geral de N seções | Larguras crescentes de baixo para cima; base em escuro = fundação. |
| Número + chips | `pilar1.html` | Habilidade com dado de mercado + lista de competências | Coluna 620px + grade 2×4 de chips (ícone + ≤ 19 caracteres). |
| Pipeline + pills | `pilar2.html` | Etapas lineares (até 6) + conceitos relacionados | Caixas 210px, palavras ≤ 9 caracteres a 32px. Etapa principal em escuro. |
| Fan-out | `pilar3.html` | Um componente acionando vários recursos | Host 1664×420; entrada → centro (destaque) → 5 destinos. |
| Grade de mini-diagramas | `pilar4.html` | Tipos/padrões/estratégias (6) | Grade 3×2; cada card com mini-desenho de formas (44px). |
| Tiles de métricas | `pilar5.html` | Critérios, métricas, requisitos (8) | Frase de impacto 44px + grade 4×2 + dado final. |
| Contraste | `hype.html` | Mito × fato, errado × certo, hype × sinal | Card alternativo claro × card escuro + frase de síntese. |
| Diagrama em T | `perfil-t.html` | Amplitude × profundidade, base × especialização | Barra de 5 segmentos + coluna de 4 blocos em degradê de destaque. |
| Cards de projetos | `portfolio.html` | Ideias práticas, exercícios, projetos (6) | Grade 3×2; ícone + título + 2 linhas. |
| Declaração final | `encerramento.html` | Fechamento | Fundo destaque, h1 96px com a tese central. |
| Fontes | `fontes.html` | Referências | Lista 32px + aviso de conferência. |

### Padrões de aula (em `assets/exemplo-deck/slides-aula/`)

Vieram do deck de 50 min para profissionais de TI; use-os como base antes dos trechos abaixo.

| Padrão | Arquivo | Quando usar |
|---|---|---|
| Objetivos de aprendizagem | `objetivos.html` | Aulas ≥ 45 min; substitui o roteiro |
| Pausa para pensar | `pausa1.html` | Pergunta em duplas; resposta esperada nas notas |
| Código + passos | `toolcalling.html` | Trecho de código (≤ 10 linhas) ao lado de 4 passos numerados |
| Tabela de aplicação | `avaliacao.html` | Transformar métricas/conceitos em plano concreto |
| Roteiro de adoção | `roadmap.html` | Linha do tempo de 4 passos "por onde começar" |
| Checagem final | `checagem.html` | 3 perguntas; respostas nas notas (base do quiz GIFT) |

## Padrões novos (trechos prontos, paleta A)

Todos entram no corpo, depois do cabeçalho padrão (`design.md`).

### Objetivos de aprendizagem
```html
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:24px">
<div style="display:flex; flex-direction:column; gap:16px; background:#FBFAF6; border:1px solid #DEDAD0; border-top:6px solid #F2994A; border-radius:20px; padding:40px">
<p style="font-family:'JetBrains Mono', 'Courier New', monospace; font-size:24px; color:#A2520F; text-transform:uppercase; letter-spacing:2px">Compreender</p>
<p style="font-size:32px; line-height:1.4; color:#121826">o que muda quando o modelo vira parte de um sistema</p>
</div>
<!-- repetir com Identificar / Aplicar -->
</div>
```

### Pausa para pensar (slide inteiro, fundo escuro)
```html
<section id="pausa1" data-transition="fade" style="background:#121826; color:#F4F2EC; font-family:'IBM Plex Sans', Arial, sans-serif; padding:128px; display:flex; flex-direction:column; justify-content:center; gap:40px">
<div style="display:flex; align-items:center; gap:20px"><x-icon name="Lightbulb" style="color:#F2994A; width:48px; height:48px"></x-icon><p style="font-family:'JetBrains Mono', 'Courier New', monospace; font-size:24px; color:#F2994A; letter-spacing:2px; text-transform:uppercase">Pausa para pensar</p></div>
<h1 style="font-family:'Space Grotesk', Arial, sans-serif; font-size:96px; font-weight:600; line-height:1.1; color:#F4F2EC; width:1500px">Como vocês testariam um agente que gera SQL?</h1>
<p style="font-size:32px; color:#B8C0CF">Discutam em duplas por 2 minutos.</p>
<aside>Respostas esperadas: …</aside>
</section>
```

### Tabela comparativa
```html
<table style="font-size:28px; color:#121826; font-family:'IBM Plex Sans', Arial, sans-serif">
<tr style="background:#121826"><th style="width:28%; color:#F4F2EC">Critério</th><th style="width:36%; color:#F4F2EC">Opção A</th><th style="width:36%; color:#F4F2EC">Opção B</th></tr>
<tr><td>Custo</td><td>Baixo</td><td>Alto</td></tr>
<tr style="background:#FBFAF6"><td>Latência</td><td>…</td><td>…</td></tr>
</table>
```
Linha ≈ 2,1 × font-size por linha de texto: com 28px, até ~9 linhas cabem no corpo.

### Linha do tempo (até 5 marcos)
```html
<div style="display:flex; gap:24px">
<div style="flex:1; display:flex; flex-direction:column; gap:12px; border-top:6px solid #F2994A; padding:24px 0px 0px 0px">
<p style="font-family:'JetBrains Mono', 'Courier New', monospace; font-size:32px; font-weight:600; color:#A2520F">2017</p>
<h3 style="font-family:'Space Grotesk', Arial, sans-serif; font-size:32px; font-weight:600">Transformer</h3>
<p style="font-size:24px; line-height:1.4; color:#4A5263">Arquitetura que viabilizou os LLMs.</p>
</div>
<!-- repetir; o marco atual com border-top:6px solid #121826 -->
</div>
```

### Bloco de código
```html
<div style="display:flex; gap:48px; align-items:center">
<div style="flex:1; background:#121826; border-radius:20px; padding:40px 48px">
<p style="font-family:'JetBrains Mono', 'Courier New', monospace; font-size:28px; line-height:1.6; color:#E6E1D6"><span style="color:#F2994A">SELECT</span> nome, curso<br><span style="color:#F2994A">FROM</span> alunos<br><span style="color:#F2994A">WHERE</span> periodo = 3<br>&#160;&#160;<span style="color:#7FA7F5">AND</span> ativo = <span style="color:#7FA7F5">true</span>;</p>
</div>
<div style="width:520px; display:flex; flex-direction:column; gap:16px">
<p style="font-size:32px; line-height:1.4; color:#4A5263">Explicação curta do que o código faz.</p>
</div>
</div>
```
Código longo: máx. ~14 linhas a 28px. Mais que isso, divida ou mostre só o trecho essencial.
Palavras-chave em laranja, literais/operadores em azul, comentários em #8A93A6.
