title: Como criar um projeto de banco de dados
date: 2013-04-17
author: Gustavo Furtado de Oliveira Alves
category: Banco de dados
slug: como-criar-um-projeto-de-banco-de-dados

O banco de dados, muitas vezes, é a parte mais importante do sistema,
pois é onde fica a informação. Por consequência, um projeto de banco de
dados é essencial para o desenvolvimento de sistemas de informação. Um
projeto de banco de dados bem ou mal realizado pode determinar o sucesso
ou insucesso do sistema.

Muitas vezes a falta de clareza ao entender a
natureza exata do ambiente onde o banco de dados será aplicado, leva à
criação de bancos de dados ruins, que não alcançam o objetivo esperado
pelo cliente. Neste artigo vou apresentar as etapas de um projeto de
banco de dados.

**[O que é um banco de
dados?](http://www.dicasdeprogramacao.com.br/o-que-e-um-banco-de-dados/ "O que é um Banco de Dados?"){:target=\_blank}**

[**A história dos bancos de
dados**](http://www.dicasdeprogramacao.com.br/a-historia-dos-bancos-de-dados/ "A história dos bancos de dados"){:target=\_blank}

##As etapas de um projeto de banco de dados

Um projeto de banco de dados é sub-dividido em etapas onde o objetivo é
a criação de um banco de dados otimizado que atenda as expectativas do
cliente. E nesse contexto, os modelos de dados são muito importantes
para a transmissão de idéias entre o cliente e o projetista, bem como
facilitar a manutenção do banco de dados no futuro.

O projeto de banco
de dados é basicamente, dividido em **Projeto Conceitual**, **Projeto
Lógico** e **Projeto Físico**. Porém antes de começar a projetar o banco
de dados é necessário a realização de análise de requisitos junto ao
cliente.

Essa talvez seja a fase mais importante do projeto, pois é
nessa hora que as necessidades e expectativas do cliente são
transmitidas para o projetista. Veja o fluxo do projeto de banco de
dados na figura abaixo.

![Projeto de banco de dados](/images/como-criar-um-projeto-de-banco-de-dados/Projeto-de-banco-de-dados.png){.aligncenter}

##Primeira etapa: Análise de Requisitos

A primeira etapa do projeto de banco de dados é a identificação dos
requisitos que o banco de dados deve atender. Nesta fase devem ser
realizadas entrevistas com as pessoas envolvidas no processo, cria-se
uma descrição textual macro do processo (texto conhecido como
mini-mundo), modelos externos (que devem ser entendidos por todos).

Este é o momento em que as regras de negócio devem ser identificadas, se
a fase de análise de requisitos for mal executada e se identificar
regras de negócio que não representam a realidade, tudo o que for feito
em seguida no projeto será perda de tempo. Por isso, esta é considerada
a **parte mais importante do projeto**.

##Segunda Etapa: Projeto Conceitual

O **Projeto Conceitual** se baseia na especificação de requisitos criada
na etapa anterior. A partir deste insumo de informações é gerado um
esquema conceitual do banco de dados. Esquema conceitual é uma visão
macro do banco de dados, uma descrição de alto nível da estrutura.

Os **modelos de Entidade-Relacionamento** são muito utilizados para
descrever os esquemas conceituais. É importante frisar que nesta fase
descreve-se o <span style="text-decoration: underline;">conteúdo de
informação</span> e não a estrutura onde elas serão armazenadas
(tabelas, colunas, visões, etc...)

![projeto](/images/como-criar-um-projeto-de-banco-de-dados/projeto.jpg){.aligncenter}

##Terceira etapa: Projeto Lógico

O **Projeto Lógico** é a etapa onde mapeamos o conceito dos modelos de
entidade-relacionamento em objetivos de bancos de dados. Nesta fase
criamos os **modelos internos** de bancos de dados, com detalhes sobre
tabelas, relacionamentos, regras, metadados das colunas (tipo, tamanho,
obrigatoriedade, ...), visões, etc.

Ao final, o resultado de um projeto
lógico é um <span style="text-decoration: underline;">esquema do banco
de dados</span> parecido com o modelo conceitual, porém com mais
detalhes de banco de dados e não apenas conceitos.

##Quarta Etapa: Projeto Físico

O **Projeto Físico** é a parte final do projeto de banco de dado, nesta
etapa define-se detalhes técnicos da implementação do banco de dados,
por exemplo a forma como os dados serão armazenados, os scripts para a
criação dos objetos no banco de dados (tabelas, visões, colunas,
funções, ...), permissão de acesso de usuário, etc. Esta etapa é
fortemente ligada ao
[SGBD](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?")
que será utilizado. A otimização de desempenho do banco de dados é
trabalhada nesta fase do projeto.

![servidor-de-banco-de-dados](/images/como-criar-um-projeto-de-banco-de-dados/servidor-de-banco-de-dados.jpg){.aligncenter}

##Conclusão

Projetar bem o banco de dados é vital para o sucesso do sistema que está
sendo desenvolvido. As primeiras etapa do projeto são de grande
importância para se criar um banco de dados que realmente atenda as
necessidades do cliente, enquanto as últimas etapas do projeto estão
mais ligadas à tecnologia de Banco de dados que será adotada,
principalmente o projeto físico.
