title: Como instalar o GIT no Windows (Passo a passo!)
date: 2019-01-23
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Programação }
tags: GIT, Instalação
slug: como-instalar-o-git-no-windows

O GIT é um dos sistemas de controle de versão mais utilizado por desenvolvedores de softwares.
Principalmente por causa do [Github](https://github.com){:target=\_blank}, recentemente comprado pela Microsoft.

[>> Inclusive, o código deste blog está todo armazenado no github](https://dicasdeprogramacao.com.br/migracao-do-blog-para-site-estatico/){:target=\blank}.

Como a maioria dos iniciantes em programação utilizam o Windows e uma hora ou outra vão precisar instalar o GIT no Windows.
Resolvir escrever este post para mostrar o passo-a-passo da instalação do GIT no Windows,
visto que a instalação do GIT pode gerar algumas dúvidas em quem não está acostumado com algumas ferramentas do Linux.

Enfim, explico abaixo todo o processo de instalação do GIT no Windows,
mas caso você ainda fique com alguma dúvida não hesite em perguntar nos comentários!

Vamos lá?

## Instalação do GIT no Windows

![GIT e Windows](/images/como-instalar-o-git-no-windows/destaque.png){:style="padding:10px;width:100%;"}

Primeiro, acesse o [site oficial](https://git-scm.com/downloads){:target=\_blank} para baixar o instalador do git.
Escolha o sistema operacional que você pretende instalar (no meu caso é o Windows) e baixe o instalador apropriado.

![Página de download do instalador do GIT](/images/como-instalar-o-git-no-windows/site-download-git.png){:style="padding:10px;"}

Após o instalador ser baixado, execute-o.

![Executando o instalador do GIT](/images/como-instalar-o-git-no-windows/executando-o-instalador-do-git.png){:style="padding:10px;"}

A primeira tela do instalador do GIT apresenta os termos da licença de utilização do GIT.
Basta clicar em **Next**.

![Primeira tela do instalador do GIT.](/images/como-instalar-o-git-no-windows/instalador-git-01-termos.png){:style="padding:10px;"}

A segunda tela é para a seleção do local da instalação, eu mantenho o padrão `C:\Program Files\Git`, mas sinta-se livre para alterar.
Após definir o local da instalação do GIT, clique em **Next**.

![Tela de seleção do local de instalação do GIT.](/images/como-instalar-o-git-no-windows/instalador-git-02-local.png){:style="padding:10px;"}

Agora o instalador oferece a possibilidade de selecionar os componentes do GIT que queremos que seja instalado.

Eu não gosto de adicionar ícones no Desktop, por isso eu desmarco. Os demais componentes eu marquei todos:

- Integração com Windows Explorer
- Suporte a arquivos grandes
- Associação de arquivos, e editor de texto padrão
- Permitir que o prompt de comandos seja colorido para as opções do git
- Verificação diária de atualização.

Escolha os componentes de sua preferência e clique em **Next**.

![Tela de seleção de componentes do GIT.](/images/como-instalar-o-git-no-windows/instalador-git-03-componentes.png){:style="padding:10px;"}

Em seguida o instalador do GIT nos indica que criará uma pasta com atalhos no menu iniciar,
se quiser, você pode marcar o _checkbox_ `Don't create a Start Menu folder` para o instalador não criar esta pasta.

No meu caso eu deixei o instalador criar os atalhos no menu Iniciar.

Clique em **Next** para continuar a instalação.

![Tela de criação de atalho do GIT no menu Iniciar](/images/como-instalar-o-git-no-windows/instalador-git-04-atalho-iniciar.png){:style="padding:10px;"}

Na sequência o instalador pede para selecionarmos o editor de texto que deve ser utilizado para editar os conflitos que por ventura acontecerem.

Eu gosto do Vim mesmo, mas você pode não tem muita afinidade com o Vim
você pode alterar para Notepad++, Sublime, Atom, VS Code, ou outro editor de sua preferência.

Após a escolha, clique em **Next** para continuar com a instalação.

![Tela de seleção do editor de conflitos padrão do GIT](/images/como-instalar-o-git-no-windows/instalador-git-05-editor-de-conflitos.png){:style="padding:10px;"}

Neste momento começa algumas partes confusas para quem não conhece muito o GIT.

Na próxima tela o instalador do GIT nos pergunta se queremos usar os comandos do git:

- somente no prompt de comandos do próprio git (chamado de Git Bash), neste caso ele não vai alterar a variável de ambiente PATH.
- no prompt do Windows (Windows Command Prompt), neste caso a variável de ambiente PATH será alterada para incluir o caminho de onde está o executável git.exe.
- no prompt do Windows + comandos utilitários do línux.
Eu sempre marco esta opção, porque o instalador traz para o Windows alguns comando que eu uso muito no Linux,
como `cat`, `ls`, `find`, etc.
Neste caso a variável de ambiente PATH será alterada para incluir o caminho do executável git.exe e dos executáveis de cada comando utilitário do linux.

Escolha a opção que acha mais adequada para você e clique em **Next**.

![Tela de ajuste da variável de ambiente PATH.](/images/como-instalar-o-git-no-windows/instalador-git-05-comandos-linux.png){:style="padding:10px;"}

A tela seguinte do instalador oferece a opção de escolhar a biblioteca de validação de chaves de segurança SSL.

Eu costumo utilizar a OpenSSL, que é compatível com outras plataformas.

Escolha a que achar apropriada e clique em **Next**.

![Tela de seleção de biblioteca de validação de certificados SSL](/images/como-instalar-o-git-no-windows/instalador-git-06-biblioteca-ssl.png){:style="padding:10px;"}

Neste ponto da instalação, nos é perguntado como o git deve tratar o final dos arquivos de texto.

Este é um assunto complicado de explicar em poucas palavras, mas vamos lá ...

Vamos dar uma pequena pausa na instalação do GIT aqui para entender esse assunto.

## Como é tratado o final de linha dos arquivos de textos

O Windows e o Unix, tratam o final de linha dos arquivos texto de formas diferentes.

Pra resumir a história ...
o Windows segue um padrão antigo de comandos de impressora,
chamado de CRLF, que indica para o cabeçote da impressora ir para o início horizontal (Carriage Return)
e para iniciar uma próxima linha (Line Feed).

Como se fosse aquela alavanca da máquina de escrever que funciona dessa forma, _vai pro início e para a próxima linha_.

Já no linux, ficou comum somente o comando LF que teria o mesmo funcionamento do CRLF, ou seja, _próxima linha...início._

Isso significa que o Linux usa um caracter ASCII para a quebra de linha e o Windows usa dois.
Esta é a mesma origem da confusão entre `\n` e `\r`, mas isso é assunto pra outro post.

Por agora entenda as opções que o instalador do GIT oferece:

- converter `LF` para `CRLF` ao baixar arquivos e `CRLF` para `LF` ao comitar.
- baixar como é (não converte nada), mas comitar convertendo `CRLF` para `LF`.
- não converter nada, baixar como é e comitar como estiver.

Eu marco a primeira opção, para evitar problemas de compatibilidade entre as plataformas.

![Tela de configuração de final de linha do instalador do GIT.](/images/como-instalar-o-git-no-windows/instalador-git-07-caracter-de-final-de-linha.png){:style="padding:10px;"}

## Continuando a instalação ...

Na sequência, o instalador oferece a opção de escolher o emulador de terminal (prompt) que queremos usar para o GIT.
Podemos usar o console padrão do Windows (cmd.exe) ou o MinTTY que é um emulador que oferece algumas características melhores na minha opinião.

Em suma, o cmd é usado para compatibilidade com plataformas de 32 bits, ou seja, se o seu windows for 32 bits, é melhor escolher o cmd mesmo,
mas se o seu windows for de 64 bits, é melhor escolher o MinTTY, pq ele oferece alguns recursos melhores para terminal, como por exemplo **maximizar**.

![Tela de escolha de emulador de terminal do GIT.](/images/como-instalar-o-git-no-windows/instalador-git-08-emulador-de-terminal.png){:style="padding:10px;"}

A penúltima tela nos oferece algumas opções extras, são elas:

- habilitar cache de arquivos na memória. Isso melhora o desempenho do git em alguns casos.
- habilitar o gerenciador de credenciais do GIT.
Isso permite autenticação em duas etapas no VSTS e no GitHub, e precisa do framework .NET 4.5 para funcionar.
- habilitar links simbólicos: Sinceramente, não sei o que é isso no Windows e não me fez falta ainda,
se você souber do que se trata, apreciarei muito uma explicação aí nos comentários. ;)

Selecione os itens opcionais que você deseja e clique em **Next**.

![Tela de escolha de ítens opcionais do GIT no Windows](/images/como-instalar-o-git-no-windows/instalador-git-09-opcoes-extras.png){:style="padding:10px;"}

Por fim, última tela do instalador do GIT no Windows (UFA!!!),
o instalador nos oferece alguns componentes que estão em fase de experimentação.

São componentes que não foram muito testados, mas que parecem melhorar bastante a performance.

Você escolhe se que instala ou não ...

Eu não marquei.

Após decidir se instala os componentes experimentais ou não, clique em **Install** para começar a instalação.

![Tela de seleção de componentes experimentais do GIT.](/images/como-instalar-o-git-no-windows/instalador-git-10-componentes-experimentais.png){:style="padding:10px;"}

Depois da instalação, o instalador oferece a opção de já rodar o prompt do GIT (Git Bash)
e ver o arquivo de texto com as notas da versão lançada.

Se quiser uma dessas duas opções, marque-a, eu desmarquei as duas.

Para finalizar, clique em **Finish**.

![Tela final do instalador do GIT](/images/como-instalar-o-git-no-windows/instalador-git-11-finalizar-instalacao.png){:style="padding:10px;"}

Pronto, agora você tem o GIT instalado no seu Windows!

Espero que este post tenha te ajudado na instalação do GIT,
se você ficou com dúvida em alguma parte, comente logo aqui abaixo.