Title: Você precisa saber o que é SQL!
Date: 2013-04-26 09:20
Author: gustavo.foa
Category: Bancos de dados
Tags: banco de dados, DCL, DDL, DML, DTL, sql, Structured Query Language
Slug: o-que-e-sql
Status: published

**SQL  **(Structured Query Language) é a linguagem padrão universal para
manipular [bancos de
dados](http://www.dicasdeprogramacao.com.br/o-que-e-um-banco-de-dados/ "O que é um Banco de Dados?") relacionais
através dos
[SGBDs](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?").
Isso significa que todos os SGBDRs (Sistema de Gerenciamento de Banco de
Dados Relacionais) oferecem uma interface para acessar o banco de dados
utilizando a linguagem SQL, embora com algumas variações. Logo, saber o
que é SQL e como utilizá-la é fundamental para qualquer desenvolvedor de
softwares.

A "Linguagem Estruturada de Consultas" (SQL, traduzida para o português)
é utilizada para interagir com o SGBD e executar várias tarefas como
inserir e alterar registros, criar objetos no banco de dados, gerenciar
usuário, consultar informações, controlar transações, etc. Todas as
operações realizadas no banco de dados podem ser solicitadas ao SGBD
utilizando esta linguagem.

[![SQL](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/04/SQL1.png){.aligncenter
.size-full .wp-image-1288 width="325"
height="149"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/04/SQL1.png)

A linguagem SQL é dividida em 4 agrupamentos de acordo com o tipo de
operação a ser executada no banco de dados. A saber, DML (Data
Manipulation Language, ou Linguagem de Manipulação de Dados e
português), DDL (Data Definition Language, ou Linguagem de Definição de
Dados em português), DCL (Data Control Language, ou Linguagem de
Controle de Dados em português) e DTL (Data Transaction Language, ou
Linguagem de Transação de Dados em português). Alguns autores
classificam também uma divisão da linguagem para consultas, a DQL (Data
Query Language, Linguagem de Consulta de Dados), que tem apenas um
comando (SELECT), porém é mais comum encontrar este comando como
integrante da DML, juntamente com os comandos INSERT, UPDATE e DELETE.
Vejamos os comandos SQL de cada agrupamento.

DML - Data Manipulation Language
--------------------------------

**DML** (Linguagem de Manipulação de [](){#spiderWordFound5}Dados) é o
subconjunto mais utilizado da linguagem **SQL**, pois é através da DML
que operamos sobre os <span
style="text-decoration: underline;">dados</span> dos bancos de dados com
instruções de inserção, atualização, exclusão e consulta de informações.
Os comandos SQL desse subconjunto são:

-   **<span style="line-height: 13px;">INSERT</span>**<span
    style="line-height: 13px;">: utilizado para inserir registros
    (tuplas), em uma tabela.</span>
    -   <span style="line-height: 13px;">Exemplo: <span
        style="text-decoration: underline;">INSERT into
        CLIENTE(ID, NOME) values(1,'José');</span></span>
-   **UPDATE**: utilizado para alterar valores de uma ou mais
    linhas (tuplas) de uma tabela.
    -   Exemplo: <span style="text-decoration: underline;">UPDATE
        CLIENTE set NOME = 'João'  WHERE ID = 1;</span>
-   **DELETE**: utilizado para excluir um ou mais registros (tupla) de
    uma tabela.
    -   Exemplo: <span style="text-decoration: underline;">DELETE FROM
        CLIENTE WHERE ID = 1;</span>
-   **SELECT**: O principal comando da SQL, o comando select é utilizado
    para efetuar consultas no banco de dados.
    -   Exemplo: <span style="text-decoration: underline;">SELECT ID,
        NOME FROM CLIENTE;</span>

> <span style="text-decoration: underline;">Nota:</span> **Registro**,
> **Linha** e **Tupla** são palavras sinônimas para referenciar a uma
> linha da tabela.

DDL - Data Definition Language
------------------------------

**DDL** (Linguagem de Definição de Dados) é o subconjunto da **SQL**
utilizado para gerenciar a estrutura do banco de dados. Com a DDL
podemos criar, alterar e remover objetos (tabelas, visões, funções,
etc.) no banco de dados. Os comandos deste subconjunto são:

-   <span style="line-height: 13px;">**CREATE**: utilizado para criar
    objetos no banco de dados.</span>
    -   Exemplo (criar uma tabela): <span
        style="text-decoration: underline;">CREATE TABLE CLIENTE ( ID
        INT PRIMARY KEY, NOME VARCHAR(50));</span>
-   **ALTER**: utilizado para alterar a estrutura de um objeto.
    -   Exemplo (adicionar uma coluna em uma tabela existente): <span
        style="text-decoration: underline;">ALTER TABLE CLIENTE ADD SEXO
        CHAR(1);</span>
-   **DROP**: utilizado para remover um objeto do banco de dados.
    -   Exemplo (remover uma tabela): <span
        style="text-decoration: underline;">DROP TABLE CLIENTE;</span>

DCL - Data Control Language
---------------------------

**DCL** (Linguagem de Controle de Dados) é o subconjunto da **SQL**
utilizado para controlar o acesso aos dados, basicamente com dois
comandos que permite ou bloqueia o acesso de usuários a dados. Vejamos
estes comandos:

-   **GRANT**: Autoriza um usuário a executar alguma operação.
    -   Exemplo (dar permissão de consulta na tabela cliente para o
        usuário carlos): <span style="text-decoration: underline;">GRANT
        select ON cliente TO carlos;</span>
-   **REVOKE**: Restringe ou remove a permissão de um usuário executar
    alguma operação.
    -   Exemplo (não permitir que o usuário carlos crie tabelas no banco
        de dados): REVOKE CREATE TABLE FROM carlos;

DTL - Data Transaction Language
-------------------------------

**DTL** (Linguagem de controle de transações) é o subconjunto da **SQL**
que fornece mecanismos para controlar transações no banco de dados. São
3 comandos: iniciar uma transação (BEGIN TRANSACTION), efetivar as
alterações no banco de dados (COMMIT) e cancelar as alterações
(ROLLBACK).

Conclusão
---------

Quem quer trabalhar com desenvolvimento de softwares precisa aprender a
SQL, pois a maioria dos sistemas de informação interage com banco de
dados, e essa é a linguagem universal para fazer qualquer coisa nos
bancos de dados relacionais (o tipo de banco de dados mais utilizado na
industria). Pode haver pequenas variações na linguagem dependendo do
[SGBD](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?"),
mas a sintaxe dos comandos são muito parecidas.

Cada comando citado neste artigo possui uma série de recursos, o comando
que tem mais recursos, obviamente, é o comando SELECT. O objetivo deste
artigo é apenas apresentar a linguagem SQL e seus comandos, continue
ligado aqui no **{ Dicas de Programação }** que vamos ver os detalhes de
cada comando desta linguagem.
