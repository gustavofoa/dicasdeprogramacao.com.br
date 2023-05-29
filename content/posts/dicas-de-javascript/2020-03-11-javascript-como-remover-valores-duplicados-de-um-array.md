---
title: Javascript: Como remover valores repetidos de um array
date: 2020-03-11
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante
slug: javascript-como-remover-valores-repetidos-de-um-array
---
Imagina que você tem um array em javascript que possui alguns valores duplicados. Como no exemplo abaixo.

```javascript
const numeros = [2, 5, 6, 8, 5, 1 ,4, 6, 2, 8, 5, 6];
```

Perceba que alguns valores se repetem no array.

Se você quiser remover os valores repetidos do array, a linha abaixo faz este trabalho pra você.

```javascript
const numerosSemRepeticao = [...new Set(numeros)];
```

Dá uma olhada na execução deste código no console do meu navegador.

![Limpando valores repertidos de um array em javascript](/images/javascript-como-remover-valores-repetidos-de-um-array/limpando-array-com-valores-repetidos.gif){:style="width:100%;padding:10px"}

O `Set` é uma estrutura de dados muito utilizada em várias linguagens de programação que, por padrão, não aceita valores repetidos. Ao contrário do array ou do `List`.

Portanto, o `Set` é muito apropriado para este caso em que queremos limpar um array removendo os valores repetidos.

Além disso nós utilizamos o *Spread Operator* para criar um novo array com os valores do nosso Set (que não aceita valores repetidos).

Espero que tenha gostado da dica. Em caso de dúvida, fique à vontade para postar nos comentários.

## Referências

1. [[Documentação Mozilla] Set](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Set){:target=_blank}
2. [[Documentação Mozilla] Spread Operator](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Spread_operator){:target=_blank}