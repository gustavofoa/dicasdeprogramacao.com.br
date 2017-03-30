title: O que são tipos de dados primitivos?
date: 2013-03-12
author: Gustavo Furtado de Oliveira Alves
category: Iniciante
slug: tipos-de-dados-primitivos

Nos
[algoritmos](http://www.dicasdeprogramacao.com.br/o-que-e-um-algoritmo/ "O que é Algoritmo?"){:target=\_blank}
criados para realizar tarefas na computação utilizamos
[variáveis](http://www.dicasdeprogramacao.com.br/o-que-e-variavel-e-constante/ "O que é variável e constante?"){:target=\_blank} para
manipular dados, por exemplo: nome, idade, altura, peso, data de
nascimento, sexo, saldo, etc. Para otimizar a utilização da memória,
cada variável armazena apenas um tipo de dados.

A variável **nome**,
deve armazenar <span style="text-decoration: underline;">textos</span>,
já a variável **idade** deve armazenar apenas <span
style="text-decoration: underline;">números inteiros</span> (sem casa
decimal), na variável **sexo** podemos armazenar apenas um <span
style="text-decoration: underline;">caractere</span> ("M" ou "F"). Seria
correto armazenarmos o valor "M" na variável **idade**? Não né, por isso
devemos especificar em nossos algoritmos o tipo de cada variável.

![tipos de
dados](/images/tipos-de-dados-primitivos/tipos-de-dados.jpg){.aligncenter}

##Quais são os tipos de dados primitivos?

Em computação existem apenas 4 tipos de dados primitivos, algumas
linguagens subdividem esses tipos de dados em outros de acordo com a
capacidade de memória necessária para a variável. Mas de modo geral, os
tipos de dados primitivos são:

-   **<span style="line-height: 13px;">INTEIRO</span>**<span
    style="line-height: 13px;">: Representa valores numéricos negativo
    ou positivo sem casa decimal, ou seja, valores inteiros.</span>
-   **REAL**: Representa valores numéricos negativo ou positivo com casa
    decimal, ou seja, valores reais. Também são chamados de <span
    style="text-decoration: underline;">ponto flutuante</span>.
-   **LÓGICO**: Representa valores <span
    style="text-decoration: underline;">booleanos</span>, assumindo
    apenas dois estados, VERDADEIRO ou FALSO. Pode ser representado
    apenas um bit (que aceita apenas 1 ou 0).
-   **TEXTO**: Representa uma sequencia de um ou mais de caracteres,
    colocamos os valores do tipo TEXTO entre " " (aspas duplas).

Algumas linguagens de programação, dividem esses tipos primitivos de
acordo com o espaço necessário para os valores daquela variável. Na
linguagem <span style="text-decoration: underline;">Java</span> por
exemplo, o tipo de dados inteiro é dividido em 4 tipos primitivos:
**byte**, **short**, **int** e **long**. A capacidade de armazenamento
de cada um deles é diferente.

-   <span style="line-height: 13px;">**byte**: é capaz de armazenar
    valores entre -128 até 127.</span>
-   **short**: é capaz de armazenar valores entre – 32768 até 32767.
-   **int**: é capaz de armazenar valores entre –2147483648
    até 2147483647.
-   **long**: é capaz de armazenar valores
    entre –9223372036854775808 até 9223372036854775807.

Mas essa divisão é uma particularidade da linguagem de programação que
está sendo utilizada. O objetivo é otimizar a utilização da memória. Em
algumas linguagens de programação não é necessário especificar o tipo de
dados da variável, eles são identificados dinamicamente. Porém, é
necessário informar o tipo de dados de cada variável em algoritmos.

##Tipos de dados customizados

A partir dos tipos de dados primitivos podemos criar outros tipos de
dados utilizando uma combinação de variáveis.  São estruturas de dados,
classes, vetores, matrizes, etc.

Uma classe chamada Carro é um tipo de dados que agrupa outras variáveis
básicas como **marca**, **cor**, **ano**, **modelo**, etc. Um vetor é um
agrupamento de variáveis, uma matriz é um agrupamento de vetores. Enfim,
a base de todos os tipos de dados são os tipos de dados primitivos,
independente da linguagem de programação.

![classe
carro](/images/tipos-de-dados-primitivos/classe-carro.jpg){.aligncenter}

O conceito de estruturas de dados e classes é bem mais complexo que
isto, por exemplo classes têm operações além de atributos, mas aqui é
importante apenas frisar que também são tipos de dados. Diferente dos
tipos de dados primitivos que já são implementados internamente pelas
linguagens de programação, esses tipos de dados são criados pelo
programador.
