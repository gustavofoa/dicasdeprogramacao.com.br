title: A história dos bancos de dados
date: 2013-04-01
author: Gustavo Furtado de Oliveira Alves
category: Bancos de dados
slug: a-historia-dos-bancos-de-dados

Hoje os [bancos de
dados](http://www.dicasdeprogramacao.com.br/o-que-e-um-banco-de-dados/ "O que é um Banco de Dados?"){:target=\_blank}
são essenciais para muitas empresas e estão no coração de muitos
sistemas computacionais. Ter acesso rápido às informações é muito
importante para a correta tomada de decisões em um negócio.

Se você pretende trabalhar com desenvolvimento de softwares, com certeza
precisará trabalhar com bancos de dados em algum momento. Conhecer a
história dos bancos de dados e como eles evoluíram é muito importante
para entender como os bancos de dados mais comum são organizados. Então
como aconteceu a evolução dos bancos de dados?

##A história dos bancos de dados

Antigamente as empresas armazenavam dados em fichas de papel que eram
organizadas em arquivos físicos através de pastas. Extrair informações e
manter esses arquivos organizado era uma tarefa muito custosa. Além
disso o acesso à informação dependia da localização geográfica dos
arquivos. Enfim esses arquivos físicos evoluíram para arquivos digitais.

No início, cada entidade (clientes, funcionários, produtos, etc) era um
arquivo de dados que eram acompanhados de um "software simples" para
manipular os dados do arquivo, esses softwares permitiam realizer
operações de cadastro, alteração, exclusão e consulta nos arquivos
digitais. De fato melhorou bastante, principalmente a tarefa de consulta
de informações, porém os arquivos digitais eram ainda uma versão
melhorada dos arquivos físicos.

![evolução-humanidade-computador](/images/a-historia-dos-bancos-de-dados/evolução-humanidade-computador.jpg){.aligncenter}

Mas as entidades precisavam relacionar-se, por exemplo um <span
style="text-decoration: underline;">produto</span> é fornecido por
um <span style="text-decoration: underline;">fornecedor</span>, e com os
arquivos digitais relacioná-las não era uma tarefa muito trivial, os
"softwares simples" para manipular os arquivos digitais começaram a
ficar "complexos" para permitir os relacionamentos entre
entidades.

Então, na década de 60 a empresa IBM investiu fortemente em
pesquisas para solucionar estes problemas dos bancos de dados digitais
primitivos. Vários modelos de bancos de dados surgiram nesta época,
dentre eles os modelos hierárquico e rede.

Em junho de 1970, o pesquisador **Edgar Frank "Ted" Codd** da IBM, mudou
a história dos bancos de dados apresentando o <span
style="text-decoration: underline;">modelo relacional</span> no
artigo intitulado **"A Relational Model of Data for Large Shared Data
Banks"**, onde o autor apresentou uma forma de usuários sem conhecimento
técnico armazenarem e extraírem grandes quantidades de informações de um
banco de dados. Este artigo foi o grande impulso para a evolução dos
bancos de dados, a partir do artigo de "Ted" Codd que os cientistas
aprofundaram a ideia de criar o modelo de banco de dados relacional.

##Banco de dados relacional

Apesar de ter sido o marco dos bancos de dados relacionais, o artigo de
Codd não foi muito explorado no início. Só no final da década de 70 que
foi desenvolvido um sistema baseado nas idéias do cientista, o "Sistema
R". Junto com esse sistema foi criado a linguagem de consulta
estruturada (SQL - Structured Query Language) que se tornou a linguagem
padrão para bancos de dados relacionais.

Embora tenha contribuído para a
evolução dos bancos de dados relacionais, o "System R" não foi muito bem
sucedido comercialmente, mas os sistemas de banco de dados seguintes
foram baseados nele.

Nos anos 80 surgiram outros bancos de dados, a Oracle apresentou o
Oracle 2 e a IBM o SQL/DS (que se tornou DB2), ambos sistemas comerciais
de bancos de dados. Na sequencia vieram SQL Server, MySQL, DBase III,
Paradox, etc...

##Bancos de dados hoje

Atualmente existem vários modelos de bancos de dados tais como orientado
a objetos, orientado a documentos, etc. Mas o mais comum ainda é o banco
de dados relacional. A decisão entre qual modelo de banco de dados
utilizar baseia-se no tipo de dados que você pretende armazenar.

Por exemplo, se você for armazenar uma grande quantidade de dados em um
modelo pequeno (imagine um banco de dados pro twitter), é mais indicado
utilizar um banco de dados orientado a documentos a um banco de dados
relacional. Muitas questões envolvem essa decisão, mas não é uma questão
de superioridade entre uma ou outra tecnologia, todas tem prós e contras
e são mais indicadas ou não para cada problema.
