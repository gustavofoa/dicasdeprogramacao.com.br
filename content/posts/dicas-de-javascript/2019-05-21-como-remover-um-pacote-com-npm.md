---
title: Como remover pacotes corretamente com NPM
date: 2019-05-21
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: nodejs, npm
slug: como-remover-pacotes-corretamente-com-npm
---

Você instalou um pacote no seu projeto nodejs, mas agora não vai mais usá-lo?
Para remover um pacote do seu projeto você pode simplesmente apagar a linha dessa dependência do seu `package.json`,
mas isso não desinstala o pacote do projeto que está no seu computador.

Para remover um pacote de forma correta com o NPM você deve executar o comando abaixo:

```
npm uninstall <nome-do-pacote>
```

Este comando remove o pacote do seu projeto, da pasta `node_modules` e também remove a dependência do seu `package.json`.
Confira o gif abaixo em que removemos o pacote `restify-clients` do nosso projeto de exemplo.

![Exemplo de execução do npm uninstall](/images/como-remover-pacotes-corretamente-com-npm/exemplo-npm-uninstall.gif){:style="width:100%;padding:10px;"}

Perceba que na pasta `node_modules` foi removido a pasta do pacote `restify-clients`
e também todos os outros módulos que foram instalados junto com ele.

O **npm** gerencia todas as dependências necessárias para o seu projeto funcionar, instalando e removendo os pacotes que são ou não necessários.
Por isso é importante sempre instalar e desinstalar pacotes utilizando o **npm** ao invés de tentar fazer isso manualmente.