---
title: Javascript: Como ler os dados dos atributos de um objeto JSON
date: 2018-08-29
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: json
slug: javascript-como-ler-os-dados-dos-atributos-de-um-objeto-json
---

Existem duas formas de ler o valor de um atributo de um objeto json.

A primeira é através do ponto (`.`), você escreve o nome do objeto ponto (`.`) e o nome do atributo.

A segunda maneira é com colchetes e uma string com o nome do atributo.

Vamos ver um exemplo...

Suponhamos que temos um objeto como o do exemplo abaixo e queremos acessar o `atributo1`,
podemos fazer isso desses dois jeitos:

```javascript
var objeto = {"atributo1": "valor 1", "atributo2": 23};

console.log(objeto.atributo1);

console.log(objeto['atributo2']);
```

Abaixo um exemplo de execução de leitura de atributos no console do Chrome.

![Exemplo de leitura de atributos de um objeto json em Javascript](/images/javascript-como-ler-os-dados-dos-atributos-de-um-objeto-json/leitura-de-atributos-de-um-json.gif){:style="width:100%;padding:10px;"}
