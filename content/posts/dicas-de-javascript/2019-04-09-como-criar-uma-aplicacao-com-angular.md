---
title: Como criar uma aplicação com Angular
date: 2019-04-09
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: angular
slug: como-criar-uma-aplicacao-com-angular
---

Dar os primeiros passos com o Angular não é algo muito complicado.
Primeiro você precisa instalar o NodeJS e o NPM e depois o Angular-Cli.
Essas instalações já foram explicadas aqui no **{ Dicas de Programação }**.

[**>> Instalação do NodeJS e npm no Windows (Passo a passo!)**](https://dicasdeprogramacao.com.br/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/){:target=\_blank}

[**>> Como instalar o Angular no Windows**](https://dicasdeprogramacao.com.br/como-instalar-o-angular-no-windows/){:target=\_blank}

Com esses pré-requisitos instalados, o próximo passo é criar o seu primeiro projeto com o Angular.
Você pode fazer isso com apenas um comando do Angular-Cli.

```
ng new nome-da-sua-aplicacao
```

Este comando cria o seu projeto Angular já com um esqueleto, seguindo as boas práticas.

Além de podermos dar qualquer nome para a aplicação, o `ng new` dá a opção de duas customizações.

1. Se queremos que ele já configure uma rota para a aplicação. Eu recomendo que responda sim (y), pois as rotas permitem que naveguemos de uma view para outra, então provavelmente você vai precisar na sua nova aplicação.
2. Qual formato de folha de estilo queremos usar (CSS, Sass, Less, Stylus). Esta é uma escolha pessoal, eu gosto do Sass, mas vai da sua preferência.

E claro, o Angular-Cli é em [**inglês**](https://dicasdeprogramacao.com.br/quer-ser-programador-aprenda-ingles/){:target=\_blank}. Veja abaixo, como o angular-cli oferece essas opções.

![Execução do 'ng new'](/images/como-criar-uma-aplicacao-com-angular/ng-new-options.gif){:style="width:100%;"}

Por fim, o Angular CLI criará o esqueleto do seu projeto e instalará os pacotes _npm_ necessários para a sua aplicação. Isso pode demorar alguns minutos.

Ao final do processo você terá uma pasta com o nome que você escolheu pra sua aplicação, esta pasta contém:

- O esqueleto inicial do seu projeto (na pasta `src`)
- Um projeto de teste end-to-end (na pasta `e2e`)
- Arquivos de configuração do seu projeto (`angular.json`, `package.json`, `tsconfig.json`, `tslint.json` e `.gitignore`)
- Um `README.md` para você descrever a sua aplicação seguindo as prática da comunidade open source.

Não vou entrar em detalhes sobre a estrutura do projeto neste post, mas se você quiser executar a sua nova aplicação Angular, basta entrar na pasta do projeto e executar o comando `ng serve --open`.
O Angular CLI vai criar um servidor local para executar a sua aplicação e o parâmetro `--open` abrirá o browser com a sua aplicação automaticamente.

![Executando a sua aplicação Angular com 'ng serve --open'](/images/como-criar-uma-aplicacao-com-angular/ng-serve--open.gif){:style="width:100%;"}

Pronto, a primeira aplicação Angular está criada e rodando, agora é mão na massa para customizá-la.

## Referencias

[1. Angular.IO Guide](https://angular.io/guide/quickstart){:target=\_blank}