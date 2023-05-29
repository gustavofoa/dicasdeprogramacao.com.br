---
title: Javascript: Como converter string em objeto JSON
date: 2018-08-27
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: string, json, converter
slug: javascript-como-converter-objeto-json-em-string
---

Suponha que você tenha uma String que representa um JSON válido e queira transformar esta String em um objeto JSON no javascript.

Para fazer isso, basta utilizar o método `JSON.parse(texto)`, passando a string como parâmetro.

Veja um exemplo no código abaixo:

```javascript
var texto = '{"atributo1": "valor 1", "atributo2": 23}';

var objeto = JSON.parse(texto);

console.log(objeto);
```

Abaixo um exemplo de execução deste código no console do Chrome.

![Exemplo de conversão de uma string em um objeto json em Javascript](/images/javascript-como-converter-objeto-json-em-string/converte-string-para-json-em-javascript.gif){:style="width:100%;padding:10px;"}

## Referências

1. [Mozila: JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse){:target=\_blank}