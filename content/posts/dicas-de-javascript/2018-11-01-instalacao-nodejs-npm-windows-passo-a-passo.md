---
title: Instalação do NodeJS e npm no Windows (Passo a passo!)
date: 2018-11-01
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: instalação, windows, nodejs, npm
slug: instalacao-do-nodejs-e-npm-no-windows-passo-a-passo
---

Para instalar o nodejs e o npm no Windows, primeiro você precisa acessar a página de downloads do
[**site oficial**](https://nodejs.org/en/download/current/){:target=\_blank}
para baixar o instalador.

Geralmente tem duas versões a LTS que tem suporte de longo prazo e a Current que é a última versão.
Neste momento a versão LTS é a **10.13.0** (com npm 6.4.1) e a última versão é a **11.0.0** (com npm 6.4.1).

![Página de download do NodeJS e npm](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/pagina-de-download-nodejs.png){:style="width:100%;padding:10px;"}

Escolha a versão de sua preferência e baixe o instalador para o seu sistema operacional,
no meu caso é o Windows 64 bits.

Após baixar, exercute o instalador.

A primeira tela do instalador do NodeJs apresenta uma mensagem de boas vindas do instalador
informando que será instalado o Node.js no seu computador, basta clicar em **Next** para continuar.

![Instalador NodeJS - Tela de boas vindas](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/instalador-nodejs-01-tela-boas-vindas.png){:style="width:100%;padding:10px;"}

A segunda tela do instalador do NodeJs pede para ler a licença de uso e aceitar os termos.
Se você concordar com os termos, marque a caixinha **I accept ...** e clique em **Next** para continuar.

![Instalador NodeJS - Termos de uso](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/instalador-nodejs-02-termos-de-uso.png){:style="width:100%;padding:10px;"}

A tela seguinte oferece a opção de alterar a pasta onde o NodeJS será instalado, escolha o local da instalação e clique em **Next** para continuar.

![Instalador NodeJS - local da instalação](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/instalador-nodejs-03-local-da-instalacao.png){:style="width:100%;padding:10px;"}

Em seguida o instalador permite personalizar algumas opções da instalação como adicionar ou não o caminho do node e npm na variável PATH, etc.
Eu deixo todas as opções marcadas. Clique em **Next** para continuar.

![Instalador NodeJS - Personalização](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/instalador-nodejs-04-personalizar-instalacao.png){:style="width:100%;padding:10px;"}

Na sequência o instalador pergunta se queremos instalar as ferramentas necessárias para compilar módulos nativos.
Se você marcar a caixinha para instalar essas ferramentas, o instalador vai iniciar outra janela para instalar essas ferramentas.
Eu marquei, escolha se você deseja essa opção e Clique em **Next** para continuar.

![Instalador NodeJS - Módulos Nativos](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/instalador-nodejs-05-ferramenta-compilacao-modulos-nativos.png){:style="width:100%;padding:10px;"}

Pronto! Agora basta clicar em **Install** para iniciar a instalação.
O Windows vai pedir permissão de administrador para instalar o NodeJS.

![Instalador NodeJS - Finalização](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/instalador-nodejs-06-Install.png){:style="width:100%;padding:10px;"}

Terminada a instalação clique em **Finish** e pronto.

Se você marcou a opção de instalar as ferramentas de compilação, neste momento será executado como a imagem abaixo,
um script para instalar o python 2.7, o Visual Studio Build Tools, o Chocolatey e atualizações do Windows que forem necessárias.

Se quiser desistir de instalar estas ferramentas basta fechar a janela, caso contrário basta pressionar ENTER.

Se você optar pela instalação dessas ferramentas, tudo será baixado e instalado automaticamente.
Você só precisará dar permissão de administrador para o instalador.

Para verificar se o node e o npm foi instalado corretamente,
basta executar `node --version` e `npm --version` na linha de comando conforme a imagem abaixo.

![Verificação da instalaçãõ do NodeJS e NPM](/images/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/verificacao-instalacao-node-npm-windows.png){:style="width:100%;padding:10px;"}

Se tiver alguma dúvida sobre a instalação do NodeJS e do NPM,
fique avontade para postar aí nos comentários.