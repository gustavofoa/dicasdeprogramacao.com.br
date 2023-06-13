---
title: Javascript: Porque usar === ao invés de ==
date: 2019-05-28
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante
slug: javascript-porque-usar-ao-inves-de
---

Você já deve ter se deparado com um `if` em javascript que tinha três sinais de igual (`===`) ao invés de dois (`==`), que é mais 'normal' principalmente se você já trabalhou com linguagens fortemente tipadas, como Java, C#, C, etc.

Mas como esses dois operadores funcionam quase do mesmo jeito, você só ignorou e deixou pra lá.

Bom ... Chegou a hora de entender a diferença entre esses dois operadores e entender porque é melhor usar === ao invés de ==.

## Qual a diferença entre `===` e `==`

**Javascript** é originalmente uma linguagem de tipagem dinâmica.
Isso significa que você não precisa especificar o tipo da sua variável quando cria ela.
Você não precisa dizer se é uma variável do tipo inteiro (int), texto (string), lógico (boolean), ou qualquer outro tipo.
O interpretador da linguagem "descobre" o tipo ao longo da execução.
Isso tem vantagens e desvantagens.

Essa tipagem dinâmica é a responsável pelo resultado do operador (dois iguais) `==` apresentar uns resutados não tão "iguais" assim.

Por exemplo, essas duas comparações abaixo resultam `verdadeiro`. Você concorda completamente com isso?

```javascript
0 == false
5 == "5"
```

São valores de tipos diferentes, mas com uma interpretação que podem ser iguais.

Afinal, na lógica _booleana_ por exemplo, 0 é falso e 1 é verdadeiro.
E 5 é cinco independente se a variável é inteiro ou texto, né...?

Enfim, o fato é que nós devemos estudar e entender a linguagem em que estamos programando para sabermos exatamente o que estamos fazendo com a linguagem.

Não precisar nem falar que não precisar dizer o tipo da variável gera uma comodidade para o programador, é menos coisa pra escrever no código não é mesmo? Mas isso faz a linguagem criar alguns artifícios que podem gerar confusão (e alguns bugs), principalmente nos iniciantes, infelizmente.

**A diferença entre `===` e `==` em Javascript** é que com apenas dois iguais a verificação não leva em consideração o tipo da variável, já com três iguais você faz uma verificação mais forte, considerando também o tipo da variável.

Para confirmar isso vamos fazer alguns testes no console do browser.
Confira no GIF abaixo.

![Diferença entre === e == em Javascript](/images/javascript-porque-usar-ao-inves-de/teste-===-vs-==.gif){:style="width:100%;padding:10px"}

## Por que usar `===` ao invés de `==`

A minha dica é que você sempre utilize `===` para fazer suas verificações de igualdade ao invés de `==`,
pois desta forma você estará fazendo um teste "mais forte", verificando o valor e também o tipo da variável.

Se o seu `if` falhar é um grande indício que a sua estrutura de dados não está muito boa, por exemplo armazenando valores booleanos em variáveis do tipo `string`.

É importante observar que existe uma variante deste operador: o `diferente`, que pode ser `!==` ou `!=`. O funcionamento é o mesmo explicado neste post.
Ou seja, enquanto o operador `!==` verifica se os valores e os tipos são _diferentes_, o operador `!=` verifica apenas os valores.

## Referências

1. [Mozilla: Operadores de Comparação](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators){:target=\_blank}
