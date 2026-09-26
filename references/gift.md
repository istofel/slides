# GIFT para Moodle (referência mínima)

Use só se a skill `moodle-gift` não estiver disponível.

## Estrutura
```
$CATEGORY: $course$/top/<Título do deck>

// Q01 - conceito
::Q01 Chatbot x agente::Qual a diferença prática entre um chatbot e um agente de IA?{
=O agente usa ferramentas em ciclo até cumprir um objetivo.#Isso: raciocinar, agir, observar, repetir.
~O agente sempre usa um modelo maior.#O tamanho do modelo não define um agente.
~O chatbot não usa LLM.#Ambos podem usar LLM.
~Não há diferença.#Há: o agente executa ações.
}
```
Deixe uma linha em branco entre questões.

## Tipos
- Múltipla escolha: `{ =certa ~errada ~errada }`
- Várias corretas (pesos): `{ ~%50%A ~%50%B ~%-100%C }` (somam 100% nas certas)
- Verdadeiro/falso: `{T}` ou `{F}` — com feedback: `{F#feedback se errar#feedback se acertar}`
- Resposta curta: `{ =MCP =Model Context Protocol }`
- Numérica: `{#18.9:0.5}` (valor:tolerância; decimal com ponto)
- Associação: `{ =RAG -> Busca trechos para o contexto =Tool calling -> Pede a execução de uma função }` (mín. 3 pares)
- Dissertativa: `{}`

## Escape obrigatório no texto
Preceda com `\` os caracteres `~ = # { } :` quando forem texto
(ex.: `SELECT COUNT(\*)` não precisa; `a \= b` precisa; `18\:30` precisa).
Código: prefira `[markdown]` no início do enunciado e crases para trechos.

## Conferência antes de entregar
- Toda questão tem título `::…::` único e ao menos uma resposta correta.
- Chaves balanceadas; nenhum `=`, `~`, `#`, `:` solto sem escape no enunciado.
- Arquivo em UTF-8, extensão `.gift`.
