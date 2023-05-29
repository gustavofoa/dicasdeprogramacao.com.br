---
title: Como instalar um pacote com NPM
date: 2019-05-20
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: nodejs, npm
slug: como-instalar-um-pacote-com-npm
---

Quem está começando a jornada com NodeJS, após
[criar um projeto com o NPM](/como-criar-um-projeto-nodejs-com-npm){:target=\_blank},
precisa saber instalar pacotes para dar mais poder à aplicação.

O comando para instalar pacotes com o NPM é simples:

```
npm install <nome do pacote>
```

Como exemplo vamos instalar o pacote `restify-clients`, que nos ajuda a criar requisições HTTP em uma API REST.
Para instalar esse pacote, basta executar o comando abaixo na pasta do seu projeto.

```
npm install restify-clients
```

Veja abaixo o resultado da execução deste comando em um projeto node de exemplo.

![Exemplo de execução do npm install](/images/como-instalar-um-pacote-com-npm/exemplo-npm-install.gif){:style="width:100%;padding:10px;"}

Perceba que após a execução do comando, o arquivo `package.json` deste projeto de exemplo foi alterado.
O `npm install` adicionou o pacote `restify-clients` como dependência do projeto no arquivo `package.json`.

> Nota: Nas versões anteriores à **5** do `npm` era necessário incluir o parâmetro `--save` ao comando para que
o pacote fosse incluído como dependência no `package.json`.
**Mas a partir da versão 5 do npm o --save é executado por padrão, não sendo mais necessário incluí-lo no comando.**

Outra coisa a se notar é que o npm baixa o pacote que estamos instalando e todas as suas dependências e os adiciona na pasta `node_modules`.

Com o pacote instalado, nós podemos agora usar esse pacote em nosso código node através da função `require`.

Por exemplo, o código de exemplo abaixo, faz uma requisição GET usando o _restify-clients_ que acabamos de instalar.

```javascript
var restifyClients = require('restify-clients');

var cliente = restifyClients.createJsonClient({
    url: 'https://dicasdejavascript.com.br'
});

cliente.get('/exemplo.txt', (error, req, res, retorno) => {
    console.log('consumindo serviço de cartões');
    console.log(retorno);
});
```

O _gif_ abaixo mostra a execução deste código de exemplo como o node.

![Exemplo de execução do npm install](/images/como-instalar-um-pacote-com-npm/exemplo-request-com-restify.gif){:style="width:100%;padding:10px;"}

## Referências

1. [NPMJS: Downloading and installing packages locally](https://docs.npmjs.com/downloading-and-installing-packages-locally){:target=\_blank}
