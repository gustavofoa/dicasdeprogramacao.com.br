---
title: Como instalar o Angular no Windows
date: 2019-02-18
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: instalação, windows, angular, nodejs, npm
slug: como-instalar-o-angular-no-windows
---

Para quem se interessou em aprender **Angular**, a primeira coisa que tem que fazer é
justamente instalar o **Angular Cli** para ter um ambiente de desenvolvimento para estudo.

![Angular](/images/como-instalar-o-angular-no-windows/logo-angular.png){:style="float:right;"}

O requisito para instalar o Angular no seu computador é ter instalado o NodeJS e o **npm**.

Você não vai precisar usar o NodeJS, esse requisito é necessário porque o angular é instalado através do **npm**,
que é o gerenciador de pacotes que é instalado junto como NodeJS.

Aqui no **{ Dicas de Javascript }** tem um passo-a-passo de como instalar o NodeJS e o **npm** no seu computador.
Basta clicar no link abaixo e seguir tutorial.

[**>> Instalação do NodeJS e npm no Windows (Passo a passo!)**](https://dicasdeprogramacao.com.br/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/){:target=\_blank}

Com o **npm** instalado, agora podemos instalar o **Angular CLI** para podermos criar aplicações,
executar o servidor local com a nossa aplicação, criar componentes, módulos, serviços, etc.

Para instalar o Angular CLI usando o npm, abra o prompt de comandos (cmd no windows) e execute o seguinte comando.

```
npm install -g @angular/cli
```

O parâmetro `-g` significa que o Angular Cli será instalado globalmente no seu sistema operacional.

O processo de instalação pode demorar alguns minutos,
devido a várias verificações e o download de todas as dependências.

Abaixo você pode ver como executar o comando de instalação do **Angular Cli**.

![Instalação do angular cli pelo npm](/images/como-instalar-o-angular-no-windows/instalacao-angular-cli-com-npm.gif){:style="width:100%;"}

Após o npm baixar todas as dependências e instalar o **Angular Cli**, você já está pronto para usá-lo através do comando `ng`.

A imagem abaixo mostra um exemplo da utilização do comando ``ng`` para mostrar a versão do **Angular Cli**.

![Instalação do angular cli pelo npm](/images/como-instalar-o-angular-no-windows/verificacao-do-comando-ng.gif){:style="width:100%;"}

Isso mostra que o **Angular Cli** está instalado. Divirta-se!

## Referencias

[1. Angular.IO Guide](https://angular.io/guide/quickstart){:target=\_blank}