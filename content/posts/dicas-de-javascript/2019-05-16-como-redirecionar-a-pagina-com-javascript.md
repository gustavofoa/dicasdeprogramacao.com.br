---
title: Como redirecionar a página com javascript
date: 2019-05-16
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante
slug: como-redirecionar-a-pagina-com-javascript
---

Quando temos um link em HTML com a tag `<a href='/outra-pagina'>` e um usuário clica neste link,
o navegador redireciona a navegação para o endereço informado no atributo `href` da tag.
Mas como fazer isso com Javascript? Como redirecionar a navegação do navegador para uma nova página usando Javascript?

Existem várias formas de fazer isso com o Javascript, vou mostrar aqui duas delas através da propriedade `window.location`,
uma que simula o clique do mouse em um link HTML e outra que simula um redirecionamento HTTP, ou seja,
quando uma requisição HTTP retorna os códigos `301` ou `302`.

## Simulando o clique em um link

A forma mais comum de mudar a página de um navegador é clicando em um link, certo?
Para simular o clique em um link com javascript basta alterar o valor do atributo `window.location.href`, com o endereço a ser redirecionado.
Confira no gif abaixo.

![Simulando redirecionamento href com Javascript](/images/como-redirecionar-a-pagina-com-javascript/redirect-href.gif){:style="width:100%;padding:10px"}

## Simulando o redirecionamento HTTP

Outra maneira de mudar a página de um navegador é quando a resposta de uma requisição HTTP indica um redirecionamento,
através dos códigos de resposta HTTP 301 e 302.
Para simular este tipo de redirecionamento com javascript basta fazer uma chamada na função `window.location.replace()`,
passando o novo endereço como parâmetro.
Confira no gif abaixo.

![Simulando redirecionamento HTTP com Javascript](/images/como-redirecionar-a-pagina-com-javascript/redirect-http.gif){:style="width:100%;padding:10px"}

## Referências

1. [Mozila: Window.location](https://developer.mozilla.org/pt-BR/docs/Web/API/Window/location){:target=\_blank}
2. [Mozila: Location](https://developer.mozilla.org/pt-BR/docs/Web/API/Location){:target=\_blank}