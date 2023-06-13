---
title: Javascript: Como converter objeto JSON em String
date: 2018-08-28
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: string, json, converter
slug: javascript-como-converter-objeto-json-em-string
---

Suponha que você tenha um objeto JSON e deseja transformar este objeto JSON em uma String no javascript.

Para fazer isso, basta utilizar o método `JSON.stringify(texto)`, passando a string como parâmetro.

Veja um exemplo no código abaixo:

```javascript
var objeto = {"atributo1": "valor 1", "atributo2": 23};

var texto = JSON.stringify(objeto);

console.log(texto);
```

Abaixo um exemplo de execução deste código no console do Chrome.

![Exemplo de conversão de uma string em um objeto json em Javascript](/images/javascript-como-converter-objeto-json-em-string/converte-json-para-string-em-javascript.gif){:style="width:100%;padding:10px;"}

## Referências

1. [Mozila: JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify){:target=\_blank}