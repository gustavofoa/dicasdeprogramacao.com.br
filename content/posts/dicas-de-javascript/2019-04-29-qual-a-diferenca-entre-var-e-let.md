---
title: Javascript: qual a diferença entre VAR e LET?
date: 2019-04-29
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante, var, let, variáveis
image: /images/logo-javascript.png
---

Após o lançamento do Javascript 6 (ECMAScript 6 ou ES2015) uma das grandes dúvidas que surgiram foi:
**Qual é a diferença entre _var_ e _let_?**

Isso porque o _let_ não existia no javascript e foi incorporado nesta versão da linguagem.
As duas palavras-chave (_var_ e _let_) são utilizadas para declarar variáveis e funcionam quase do mesmo jeito.
A única diferença entre as duas é o escopo em que essas variáveis existem.

Enquanto as variáveis declaradas com _let_ têm _escopo de bloco, instrução ou expressão_,
as variáveis declaradas com _var_ têm _escopo global_ ou _escopo de função_.

Antes de tudo é necessário entender o que é **escopo** de variáveis:
Escopo de variáveis nada mais é do que **onde uma variável existe**.

Faça-se a seguinte pergunta: se eu declarar uma variável dentro de um bloco de **if** por exemplo,
esta variável deve existir **fora** deste bloco de if?

Se a sua resposta foi _sim_, você deve usar _var_ para declará-la.
Mas se a sua resposta foi _não_, ou seja, esta variável deve existir **apenas dentro do if**,
você deve usar _let_ para declará-la neste caso.

A ideia funciona para qualquer tipo de **bloco**: _if, for, while, função, etc._

Veja essa diferença na prática, criando uma variável dentro de um bloco if e tentando acessá-la fora do bloco.

```javascript
if( true ){
    var variavel1 = 'teste';
}
console.log(variavel1);// <-- Funciona com "var"
```

Sendo bem direto essa é a diferença básica entre o **var** e o **let**.
Se você declarar a variável com **var** dentro de um bloco **if** por exemplo,
esta variável pode ser acessível fora desse bloco, como no exemplo acima.

Entretanto se você declarar a variável com **let** ela só existirá dentro daquele bloco.
Ou seja, o código abaixo dá erro na última linha.

```javascript
if( true ){
    let variavel2 = 'teste';
    console.log(variavel2);// <-- Funciona dentro do bloco do IF
}
console.log(variavel2);// <-- NÃO funciona com "let"
```

Veja esses exemplos funcionando no console do meu browser.

![Teste var e let](/images/javascript-qual-a-diferenca-entre-var-e-let/teste-var-let.gif){:style="width:100%;padding:10px"}

Claro que tem outros conceitos sobre escopos em Javascript que merecem outro post mais detalhado.

A minha dica é que você use o _let_ sempre que possível,
pois desta forma você estará liberando espaço de memória sempre que o escopo de bloco da variável terminar.
O que não acontece com o _var_ que mantém o espaço da variável ocupado na memória,
mesmo depois que que a execução do bloco termina.

Também é importante notar que declarar variáveis com _let_, faz o javascript mais parecido
com outras linguagens de programação, como o java por exemplo,
onde as variáveis respeitam as regras de escopos de bloco.

Lembre-se: **as variáveis declaradas com _let_ têm _escopo de bloco, instrução ou expressão_
e as variáveis declaradas com _var_ têm _escopo global de função_**.

## Referências

1. [Mozila: LET](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/let){:target=\_blank}
2. [Mozila: VAR](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/var){:target=\_blank}
