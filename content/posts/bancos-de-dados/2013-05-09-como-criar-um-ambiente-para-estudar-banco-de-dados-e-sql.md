title: Como criar um ambiente para estudar Banco de Dados e SQL
date: 2013-05-09
author: Gustavo Furtado de Oliveira Alves
category: Banco de dados
slug: como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql

Para aprender banco de
dados e SQL é preciso praticar bastante, ou seja, criar os
próprios bancos de dados, tabelas, visões, inserir e atualizar
registros, fazer consultas, etc.

Pra aprender todos esses conceitos não
há outra maneira senão interagir com um
[**SGBD**](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?"){:target=\_blank} real.

Então, vamos criar um ambiente para isso. Neste artigo vamos ver
como instalar o **Oracle XE** e o **SQL Developer** a fim de criarmos um
ambiente para estudar banco de dados e SQL na prática.

O **Oracle XE** é a versão grátis do <span
style="text-decoration: underline;">Oracle database</span>, criada
justamente para servir de banco de dados de entrada para iniciantes e
profissionais que desejam treinar e desenvolver softwares utilizando
bancos de dados. Como, provavelmente, você utiliza o seu computador para
outras coisas, vou mostrar neste artigo uma forma de não deixar os
serviços do
[**SGBD**](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?"){:target=\_blank} iniciarem
automaticamente,  para não atrapalhar o desempenho do seu computador
enquanto não estiver utilizando o banco de dados. :)

O **SQL Developer** é o software que utilizamos para acessar o
[**SGBD**](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?"){:target=\_blank}
e executar instruções
**[SQL](http://www.dicasdeprogramacao.com.br/o-que-e-sql/ "Você precisa saber o que é SQL!"){:target=\_blank}.**

##Requisitos para a instalação

Alguns requisitos mínimos de Hardware e Software devem ser atendidos
para instalar o Oracle XE como pode ser visto na
[documentação](http://docs.oracle.com/cd/E17781_01/install.112/e18803/toc.htm#autoId2 "Requisitos para instalação do Oracle XE"){:target=\_blank} do
software:

-   Arquitetura de Sistema: **Intel (x86)**
-   Um dos seguintes Sistemas Operacionais:Espaço mínimo em Disco
    (HD): **1,5 GB**
    -   Microsoft Windows XP Professional

    -   Microsoft Windows Server 2003 - todas as edições

    -   Microsoft Windows Server 2003 R2 - todas as edições

    -   Microsoft Windows Server 2008 - Standard, Enterprise,
        Datacenter, Web, e Foundation

    -   Microsoft Windows 7 - Professional, Enterprise, e Ultimate

-   Memória RAM: 256 GB, mas é recomendável no mínimo **512 GB**
-   Microsoft Windows Installer (MSI): **MSI versão 2.0** ou posterior
    (Você pode baixar o MSI aqui:  <http://msdn.microsoft.com/>)

##Instalando o Oracle XE no Windows 7 32 bits

O sistema operacional mais utilizado hoje em dia é o Windows, por isso o
escolhi para mostrar a instalação do Oracle XE, mas a instalação em
ambiente Linux também é suportada. É importante frisar que **a
instalação em Windows 64 bits NÃO é suportada**. Vejamos, então, um
passo-a-passo de como instalá-lo:

-   **Baixar o instalador do Oracle** através do
    site  <http://www.oracle.com/technetwork/products/express-edition/downloads/index.html>.
    É necessário criar uma conta no site da Oracle para isso e aceitar
    os termos de licença.

![página de download do oracle
xe](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/página-de-download-do-oracle-xe.png "página de download do oracle xe"){.size-full}

-   **Descompactar o arquivo Zip **baixado.

![extração do instalador do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/extração-do-instalador-do-Oracle.png){.aligncenter}

-   Entrar na pasta descompactada e **executar o arquivo Setup.exe.**

![executando o instalador do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/executando-o-instalador-do-Oracle-XE.png){.aligncenter}

-   **Ler e aceitar (caso concorde, claro) os termos de licença**
    apresentado na primeira tela da instalação.

![aceitar os termos de licença do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/aceitar-os-termos-de-licença-do-Oracle-XE.png){.aligncenter}

-   **Selecionar o local da instalação** do Oracle.

![selecão do local de instalação do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/selecão-do-local-de-instalação-do-Oracle-XE.png){.aligncenter}

-   **Informar uma senha para os usuários SYS e SYSTEM** do banco de
    dados (estes são os usuários administradores do banco de dados e
    você precisará se lembrar dessa senha depois).

![Senha dos usuários SYS e
SYSTEM](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/Senha-dos-usuários-SYS-e-SYSTEM.png){.aligncenter}

-   Ao final, é apresentada uma tela de resumo da instalação, basta
    **clicar em "Instalar"**.

![resumo da instalação do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/resumo-da-instalação-do-Oracle-XE.png){.aligncenter}

-   <span style="line-height: 13px;">**Pronto!** Agora é só esperar o
    processo de instalação terminar que aparecerá a tela final.
    \\o/</span>

![Oracle XE
instalado!](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/Oracle-XE-instalado.png){.aligncenter}

##Desabilitando a inicialização automática do Oracle

Agora que o Oracle XE está instalado, como prometido, vou mostrar como
não deixar o serviço do banco de dados iniciar automaticamente na
inicialização do Windows, pra não atrapalhar o desempenho do seu
computador enquanto não estiver usando o banco de dados. Também veremos
o que precisamos fazer quando quisermos iniciar o serviço do banco de
dados.

-   Primeiro, clique no iniciar, digite **"services.msc"** e
    tecle ENTER. Veja a figura abaixo.

![iniciar gerenciador de serviços no
windows](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/iniciar-gerenciador-de-serviços-no-windows.png){.aligncenter}

-   Aparecerá uma tela com todos os serviços do Windows, encontre os
    serviços **"OracleServiceXE"** e **"OracleXETNSListener"**.
    Selecione o primeiro (OracleServiceXE) e clique no botão
    propriedade, como indicado na figura abaixo.

![Serviços do Oracle XE
ativos](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/Serviços-do-Oracle-XE-ativos.png){.aligncenter}

-   Na tela de propriedades selecione o tipo de inicialização "Manual" e
    clique em OK.

![Serviços do Oracle XE com inicialização
manual](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/Serviços-do-Oracle-XE-com-inicialização-manual.png){.aligncenter}

-   Execute os últimos 2 passos para o serviço
    **"OracleXETNSListener"**.
-   Ao final desse processo, na tela de serviços do Windows deve listar
    os dois serviços mencionados com tipo de inicialização
    **"Manual".** Dessa forma os serviços do Oracle XE não iniciaram
    automaticamente na inicialização do Windows, isso fará com que seu
    computador não fique lento enquanto não estiver usando o Oracle XE.

![inicialização manual dos serviços do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/inicialização-manual-dos-serviços-do-Oracle-XE.png){.aligncenter}

-   Quando você for usar o Oracle XE para estudar, você precisará
    iniciar os serviços do Oracle usando o atalho: **Iniciar -&gt; Todos
    os Programas -&gt; Oracle Database 11g Express Edition -&gt; Iniciar
    Banco de Dados**

![iniciar serviços do Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/iniciar-serviços-do-Oracle-XE.png){.aligncenter}

Tudo instalado, agora já podemos usar o nosso banco de dados! A forma
mais simples pra isso é executar o aplicativo básico do Oracle XE para
comandos SQL (Na figura anterior, é o item acima do que usamos, ou seja,
**"Executar Linha de Comandos SQL"**). Esse aplicativo disponibiliza
apenas uma tela para inserirmos comandos SQL, para nos conectar ao banco
de dados precisamos digitar **"connect system"** e em seguida informar
aquela senha que inserimos no processo de instalação. Conforme a figura
abaixo:

![Executar Linha de Comandos SQL no Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/Executar-Linha-de-Comandos-SQL-no-Oracle-XE.png){.aligncenter}

Feito isso, já estamos conectados ao banco de dados e podemos executar
os comandos SQL para criar tabelas, inserir registros, consultar
informações, etc. Mas essa tela não é muito boa pra isso né? O que
precisamos é instalar o **SQL Developer**!

##Instalando o SQL Developer no Windows 7

Achou a instalação do Oracle XE simples? A instalação do **SQL
Developer** é mais simples ainda! Vamos então ao passo-a-passo.

-   <span style="line-height: 13px;">**Baixar o instalador** **do SQL
    Developer** através do
    site <http://www.oracle.com/technetwork/developer-tools/sql-developer/downloads/index.html>.
    Baixe a opção **"Windows 32-bit - zip file includes the
    JDK1.6.0\_35"**, é necessário criar uma conta no site da Oracle para
    isso e aceitar os termos de licença.\
    </span>

![página de download do SQL
Developer](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/página-de-download-do-SQL-Developer.png){.aligncenter}

-   **Descompactar o arquivo Zip **baixado.

![extração do SQL
Developer](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/extração-do-SQL-Developer.png){.aligncenter}

-   Entrar na pasta descompactada e **executar o
    arquivo sqldeveloper.exe.**

![executando o SQL
Developer](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/executando-o-SQL-Developer.png){.aligncenter}

-   <span style="line-height: 13px;">Pronto, você já está executando o
    SQL Developer. Não tem processo de instalação! (rs)</span>
-   Após a tela do SQL Developer abrir, o que precisamos fazer é criar
    uma conexão com o nosso banco de dados, utilizando o botão indicado
    na figura abaixo.

![botão para criar uma conexão com banco de dados no SQL
Developer](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/botão-para-criar-uma-conexão-com-banco-de-dados-no-SQL-Developer.png){.aligncenter}

-   <span style="line-height: 13px;">Na tela que aparece em seguida,
    informe os dados para conexão com o Oracle XE e um nome para essa
    conexão (você pode criar outras, com outros bancos de dados e
    outros usuários).</span>

![tela para criar conexão com o banco de dados no SQL
Developer](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/tela-para-criar-conexão-com-o-banco-de-dados-no-SQL-Developer.png){.aligncenter}

-   Após conectar-se no banco de dados, já é possível executar os
    comandos SQL.

![SQL Developer conectado ao Oracle
XE](/images/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/SQL-Developer-conectado-ao-Oracle-XE.png){.aligncenter}

##Conclusão

Com isso, nesse artigo nós criamos um ambiente para estudar bancos de
dados e SQL. Mostrei a instalação do Oracle XE, a configuração para que
os serviços do Oracle XE não fiquem ligados direto enquanto não
estivermos usando o banco de dados e por fim vimos o SQL Developer que é
um software muito bom para executarmos os nossos comandos SQL, bem
melhor que aquela telinha preta do aplicativo padrão do Oracle XE
(sqlplus).

Se tiver alguma dúvida no processo de instalação, deixe um comentário
aqui em baixo.
