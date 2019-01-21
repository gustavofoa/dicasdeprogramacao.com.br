title: VS Code: Uma super IDE leve!
date: 2019-01-21
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Programação }
tags: Blogs
slug: vs-code-uma-super-ide-leve

O **Visual Studio Code** ou **VS Code** para os íntimos,
é uma das melhores ferramentas de desenvolvimento de softwares criada nos últimos tempos,
pelo menos na minha opinião. =P

Não digo isso por ela ser da Microsoft, nunca fui fã da Microsoft que,
diga-se de passagem, está surpreendendo muita gente com o abraço ao Open Source.

Digo que o **VS Code** é bom na minha opinião, porque eu testei.
Assim como testei o Sublime Text([que já foi tema de um post aqui no **{ Dicas de Programação }**](https://dicasdeprogramacao.com.br/sublime-text-o-queridinho-dos-programadores/){:target=\_blank})
o Atom e o Brackets.
Também uso o **Vim** em alguns momentos, mas confesso que não sou um JEDI com ele, quem sabe um dia...

# Mas o VS Code é uma IDE?

Já entrei em discussões sobre o que é ou não uma IDE e na minha opinião,
como o próprio nome diz, IDE é um "Integrated Development Environment"
ou em bom português "Ambiente de desenvolvimento integrado".

Ou seja, um ambiente onde você tem, de forma "integrada" as ferramentas que precisa para desenvolver
o que você precisa desenvolver.

No meu caso o VS Code ofereceu, nativamente, uma integração excelente com o git (1 ponto).
Editor com highlight para todas as linguagens que usei até o momento (+ 1 ponto).
Integração simples com o terminal (Ctrl+'), tanto no Linux quanto no Windows (+ 2 pontos).

E este último foi cruscial para colocar o **VS Code** em primeiro lugar no meu gosto pessoal,
pois com o terminal integrado, sem enrosco nenhum, sem precisar instalar plugin
e com opção de iniciar vários terminais (bash) ao mesmo tempo,
pude executar facilmente vários comandos excenciais para um desenvolvedor como `mvn`, `node(mon?)`, `gulp`, `python`, `npm`, `pip`, etc.

Embora temos IDEs que são TOP para o objetivo a que foram desenvolvidas,
e aqui posso citar o próprio [Visual Studio](https://visualstudio.microsoft.com/){:target=\_blank},
todas as IDEs da [Jetbrains](https://www.jetbrains.com/){:target=\_blank}
([IntelliJ IDEA](https://dicasdejava.com.br/tag/intellij-idea/){:target=\_blank}, ReSharper, Rider, PyCharm, PHPStorm, etc.),
[Eclipse](http://www.eclipse.org/){:target=\_blank}, 
[NetBeans](https://netbeans.org/downloads/){:target=\_blank}, e muitas outras, o **VS Code** se destaca muito pela simplicide e desempenho.

Em poucos segundos eu entro na pasta do projeto que quero trabalhar,
clico com o botão direito, escolho a opção "Abrir com VS Code" e pá!
Estou pronto pra trabalhar, desenvolver em qualquer linguagem, ou escrever um post como este.
Já que este blog (como todos os outros que mantenho) 
[é um SSG](https://dicasdeprogramacao.com.br/migracao-do-blog-para-site-estatico/){:target=\_blank}
e escrevo posts em uma IDE (neste momento o VS Code).

> Na verdade, eu uso uns atalhos mais rápidos ainda, pelo prompt de comandos do windows eu digito `code <pasta do projeto>`.
Ou, estando na pasta do projeto que vou trabalhar, digito `code .` e pronto.

Foi por essas e outras que eu virei fã do **VS Code**
e agora eu vou te mostrar como é fácil instalar o VS Code no seu computador.

## Instalação do VS Code no Windows

Primeiro, acesse o site oficial  https://code.visualstudio.com/ e clique para baixar o instalador.
Você pode escolher em qual Sistema Operacional você deseja instalar o VS Code,
mas o site já deve pré-selecionar o que você estiver usando, no meu caso é o Windows.

![Página de download do VS Code.](/images/vscode-uma-super-ide-leve/pagina-download-vscode.png){:style="padding:10px;"}

Após baixar o instalador, execute-o.
A primeira tela da instalação oferece a opção de selecionar o idioma.
Como não tem português na lista, deixei o inglês mesmo.
Selecione o idioma de sua preferência e clique em `OK`.

![Seleção de idioma da instalação do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-01-selecao-de-idioma.png)

A tela seguinte do instalador é só uma tela de apresentação e boas vindas do instalador, basta clicar em `Next`.

![Tela de boas vindas da instalação do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-02-boas-vindas.png){:style="padding:10px;"}

Na sequência o instalador apresenta os termos de licença de utilização do VS Code.
Leia os termos e, se concordar, marque a opção de aceite (`I accept the agreement`) e clique em `Next`.

![Tela de termos de licença do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-03-termos-de-licenca.png){:style="padding:10px;"}

Agora o instalador pergunta em que pasta vamos instalar o VS Code, você pode alterar se quiser.
Escolha o local de instalação e clique em `Next`.

![Tela de seleção de local de instalação do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-04-local-de-instalacao.png){:style="padding:10px;"}

A próxima tela, diz que vai criar uma pasta com atalhos no menu iniciar, você pode escolher o nome da pasta,
ou selecionar que não quer que o instalador crie atalhos no menu iniciar.
Escolha o que for de sua preferência e clique em `Next`. Eu costumo deixar o instalador criar os atalhos no menu iniciar.

![Tela de seleção de pasta de atalho do menu iniciar](/images/vscode-uma-super-ide-leve/instalacao-vscode-05-atalho-iniciar.png){:style="padding:10px;"}

Por fim, o instalador oferece a opção de executar algumas tarefas adicionais:

- Criar um ícone na área de trabalho
- Adicionar a opção "Abrir com VS Code" no menu de contexto (botão direito do mouse) para arquivos e pastas
- Registrar o VS Code como editor padrão para alguns arquivos
- Adicionar o VS Code na variável de ambiente PATH. Isso permite abrir o VS Code pelo prompt de comandos digitando `code`.

Selecione as opções que você desejar e clique em `Next`.
Eu só não marquei a opção de criar atalho na área de trabalho.

![Opções adicionais da instalação do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-06-tarefas-adicionais.png){:style="padding:10px;"}

Na última tela do instalador ele apresenta um resumo do que será instalado e pronto.
É hora de começar a instalação clicando no botão `Install`.

![Executar o procedimento de instalação do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-07-instalar.png){:style="padding:10px;"}

Após o instalador executar o procedimento de instalação, basta finalizar o instalador clicando em `Finish`.
Se você deixar marcado a opção `Launch Visual Studio Code`, o **VS Code** abrirá em seguida.

![Finalizar o instalador do VS Code](/images/vscode-uma-super-ide-leve/instalacao-vscode-08-finalizacao.png){:style="padding:10px;"}

E é só isso! Seu VS Code já está instalado e pronto para utilização.

## Primeiros passos no VS Code

