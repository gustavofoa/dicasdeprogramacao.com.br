---
title: Javascript: Como obter um array com os atributos/chaves de um objeto JSON
date: 2018-08-24
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: array, json
image: /images/logo-javascript.png
---

Em algum momento da sua vida como desenvolvedor javascript,
você precisará saber quais são os atributos de um objeto JSON dinamicamente.
Ou seja, sem conhecer a estrutura do objeto previamente.

Com javascript nós podemos obter um array com todos os atributos de um objeto JSON utilizando o método
`Object.keys()` passando o objeto JSON como parâmetro.

Confira o código abaixo.

```javascript
var objeto = {
    atributo1 : 'valor 1',
    atributo2 : 25,
    atributo3 : true,
    atributo4 : 50.65
};

console.log(Object.keys(objeto));
```

Saída:

```
["atributo1", "atributo2", "atributo3", "atributo4"]
```

Veja um exemplo executado no console do Google Chrome.

![Exemplo de captura de array com as chaves de um objeto json em Javascript](/images/javascript-como-obter-um-array-com-os-atributoschaves-de-um-objeto-json/array-com-chaves-de-um-objeto-json.gif){:style="width:100%;padding:10px;"}

## Referências

1. [Mozila: Object.keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys){:target=\_blank}
