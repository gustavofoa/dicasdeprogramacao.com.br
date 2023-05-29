---
title: Como criar um projeto NodeJS com NPM
date: 2019-05-17
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: nodejs, npm
slug: como-criar-um-projeto-nodejs-com-npm
---

Se você quer saber como começar com nodejs e criar o seu primeiro projeto,
após a [instalação do Node com o NPM](/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo){:target=\_blank}
o passo seguinte é justamente **criar o seu projeto utilizando o npm**.

Para isso basta abrir o seu prompt de comandos ou terminal,
criar a pasta onde ficará o seu projeto e digitar o comando:

```
npm init
```

Este comando vai criar o arquivo `package.json`, que é onde está toda a configuração do seu projeto,
includindo, nome, versão, descrição, scripts a serem executados, licença, etc.

Após executar o `npm init`, o npm vai perguntar algumas informações básicas para montar o `package.json`.
São elas:

- **package name**: Nome do projeto. (Padrão: nome da pasta onde o comando foi executado)
- **version**: Versão do projeto. (Padrão: 1.0.0)
- **description**: Uma descrição para o projeto.
- **entry point**: Arquivo padrão que será utilizado para executar a aplicação. (Padrão: index.js)
- **test command**: Comando para executar os testes da aplicação.
- **git repository**: URL do repositório git onde o código-fonte da aplicação será armazenado.
- **keyword**: Palavras-chave relevantes para ajudar as pessoas a encontrarem o seu projeto. 
- **author**: Autor do projeto.
- **license** Tipo de licença do projeto. (Padrão: ISC)

Após informar todos esses dados o programa apresenta no console o conteúdo do arquivo `package.json`
que será criado com as informações que passamos.
Para confirmar a criação do arquivo para reponder `yes`.

Feito isso o arquivo `package.json` será criado na pasta raís do seu projeto.

Veja o gif abaixo que mostra um exemplo de execução do `npm init`.

![Exemplo de execução do npm init](/images/como-criar-um-projeto-nodejs-com-npm/exemplo-npm-init.gif){:style="width:100%;padding:10px;"}

Agora nós precisamos criar o primeiro arquivo Javascript da nossa aplicação,
que é justamente o arquivo que você configurou no seu package.json.
Se você escolheu o padrão, o arquivo é o `index.js`.

Após criar o seu arquivo `index.js`,
você está pronto para escrever comandos javascript para executar com o Node,
por exemplo, vamos exibir na tela do console o clássico `Alô mundo!`.

Para isso basta escrever `console.log('Alô mundo!');` no seu arquivo `index.js`.

Confira no gif abaixo a criação do arquivo `index.js` e a execução com o node.

![Exemplo de criação e execução do index.js com Node](/images/como-criar-um-projeto-nodejs-com-npm/criacao-execucao-index-js-com-node.gif){:style="width:100%;padding:10px;"}

Com isso o nosso projeto NodeJS está criado!
Lembrando que um projeto NodeJS não significa um projeto WEB, que é o mais comum.
No próximo post nós vamos ver como transformar um projeto básico NodeJS, como este,
em uma aplicação Web que responda requisições HTTP utilizando a famosa biblioteca **Express**.

E aí, conseguiu criar o seu primeiro projeto NodeJS?
Comente aqui em baixo...