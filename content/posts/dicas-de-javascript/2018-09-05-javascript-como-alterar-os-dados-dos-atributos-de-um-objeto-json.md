---
title: Javascript: Como alterar os dados dos atributos de um objeto JSON
date: 2018-09-05
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: json
slug: javascript-como-alterar-os-dados-dos-atributos-de-um-objeto-json
---

Assim como para [ler os atributos de um json](https://dicasdeprogramacao.com.br/javascript-como-ler-os-dados-dos-atributos-de-um-objeto-json/){:target=\_blank},
existem duas formas de alterar o valor de um atributo de um objeto json.

A primeira é através do ponto (`.`), você escreve o nome do objeto, ponto (`.`) e o nome do atributo, em seguida o sinal igual (`=`) e, por fim, o novo valor do atributo.

A segunda maneira é com colchetes e uma string com o nome do atributo, também seguido do sinal de igual
(`=`) e o novo valor do atributo.

Exemplo:

```javascript
objeto.atributo = 'valor';
objeto['atributo'] = 'valor';
```

Até aqui, tudo simples. Mas tem um detalhe muito importante que você deve saber sobre a linguagem javascript.

Da mesma forma que você pode alterar o valor de um atributo, em Javascript você pode adicionar um novo atributo ao objeto JSON.

Vamos ver um exemplo...

Suponhamos que temos um objeto como o do exemplo abaixo.
Vamos alterar o valor do `atributo1` e incluir um novo atributo que não existia, chamado `atributo3`,
podemos fazer isso desses dois jeitos:

```javascript
var objeto = {"atributo1": "valor 1", "atributo2": 23};

objeto.atributo1 = 'outro valor'
objeto['atributo3'] = 'atributo que não existia'

console.log(objeto.atributo1);
console.log(objeto.atributo3);
```

Abaixo um exemplo de execução de alteração de atributos no console do Chrome.

![Exemplo de alteração e adição de atributos em um objeto json em Javascript](/images/javascript-como-alterar-os-dados-dos-atributos-de-um-objeto-json/alteracao-de-atributos-de-um-json.gif){:style="width:100%;padding:10px;"}
