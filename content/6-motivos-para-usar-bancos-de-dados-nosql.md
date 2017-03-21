title: 6 motivos para usar bancos de dados NoSQL
date: 2015-06-10
author: Gustavo Furtado de Oliveira Alves
category: Bancos de dados, NoSQL
slug: 6-motivos-para-usar-bancos-de-dados-nosql

Você deve imaginar a velocidade em que a Web está crescendo hoje em dia.
O crescimento contínuo de dispositivos conectados a internet é
surpreendente. A **Internet das Coisas** já é realidade, onde tudo pode
estar conectado à rede.

E a quantidade de dados gerados a todo momento é algo gigantesco. Em
todos os setores, imagina a quantidade de transações que acontecem o
tempo inteiro em bancos de dados do mundo inteiro. Pra você ter uma
ideia, um Boeing 737 gera **240 terabytes** de dados por voo nos EUA.
Imagina a quantidade de posts no Facebook ou Twitter a cada segundo? Na
telefonia, ligações, mensagens, etc. Geramos MUITOS dados a cada segundo
que passa. Estamos na Era do **Big Data**.

**[&gt;&gt; O que é um Banco de
Dados?](http://www.dicasdeprogramacao.com.br/o-que-e-um-banco-de-dados/){:target=\_blank}**

**[&gt;&gt; O que é um
SGBD?](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/){:target=\_blank}**

**[&gt;&gt; A história dos bancos de
dados](http://www.dicasdeprogramacao.com.br/a-historia-dos-bancos-de-dados/){:target=\_blank}**

Para utilizarmos todos esses dados que geramos a todo momento, e extrair
informações, é necessário ferramentas especiais. Dentre todas
as ferramentas, desde ferramentas para armazenamento, extração, análise,
formatação, etc. Começamos pela forma como armazenamos essa grande
quantidades de dados. É aí que entra o **NoSQL**!

O que é NoSQL?
--------------

![NoSQL](/images/6-motivos-para-usar-bancos-de-dados-nosql/NoSQL.png){.alignright}

O constante crescimento da tecnologia em geral, tem feito os
desenvolvedores reavaliarem como eles armazenam e mantém esses dados. Os
bancos de dados precisam prover escalabilidade, flexibilidades,
segurança e eficiência para o massivo fluxo de dados que vivemos.

Desenvolvedores especialistas analisam a dificuldade, às vezes a
impossibilidade, de utilizar modelos relacionais para armazenar todos
esses dados mantendo uma escalabilidade dinâmica e a
performance necessária com o aumento dos dados.

**[&gt;&gt; Você precisa saber o que é
SQL!](http://www.dicasdeprogramacao.com.br/o-que-e-sql/){:target=\_blank}**

O NoSQL, que a propósito significa *Not Only SQL* (Não apenas SQL),
nasceu com o propósito de ser o banco de dados para os **super-dados**
do boom da internet. Devido à flexibilidade oferecida por esse modelo
muitos estão optando pelo NoSQL. Não é a toa que o [mercado global NoSQL
tem previsão de chegar a US \$ 3,4 bilhões em
2020](http://www.marketresearchmedia.com/?p=568){:target=\_blank}, uma taxa de
crescimento anual de 21% para o período 2015-2020.

O termo NoSQL é usado simplesmente para descrever uma família de bancos
de dados que não são relacionais, podendo variar em vários pontos entre
eles. No geral, existem 4 tipos de bancos de dados NoSQL, são eles:

-   **Chave-Valor**: Armazena dados no padrão chave-valor, como
    tabelas hash. Ex. MemcacheD, Riak, REDIS;
-   **Grafos**: Armazena dados na forma de grafo (vértices
    e arestas). Ex. Sesame, Neo4j;
-   **Colunas**: Armazena dados em linhas particulares de tabela
    no disco. Ex. Cassandra, Hbase;
-   **Documento**: Armazena os dados como "documentos", onde um
    documento pode ser um dado aninhado em formato chave-valor (por
    exemplo o padrão JSON). Ex. MongoDB, CouchDB.

![exemplos-nosql](/images/6-motivos-para-usar-bancos-de-dados-nosql/exemplos-nosql.gif){.aligncenter
.size-full .wp-image-2198 width="800" height="314"}

Embora os diferentes tipos de bancos de dados NoSQL tenham diferenças
entre si, todos eles têm as mesmas premissas. Abaixo descrevo **6
motivos para usar NoSQL** que se aplicam a <span
style="text-decoration: underline;">qualquer tipo de banco de dados
NoSQL</span>.

##1. Flexibilidade

Estruturas de dados intuitivas e flexíveis são funcionalidades que mais
atraem desenvolvedores que trabalham em times de desenvolvimento ágil. A
maioria dos bancos de dados NoSQL tem essas qualidades.

A grande flexibilidade dos bancos de dados NoSQL é muito popular por
suportar as práticas de desenvolvimento ágil, pois elimina a
complexidade de mudanças dos bancos de dados gerando um bom suporte para
adaptações rápidas.

##2. Escalabilidade

A maioria dos bancos de dados NoSQL são construídos para escalar
horizontalmente, distribuindo os dados por clusters melhor que os SGBDs
relacionais, que sofrem muito em performance quando executa consultas
com "joins" em ambientes clusterizados. Como o NoSQL evita "joins"
naturalmente, a performance das consultas permanece alta.

A escalabilidade NoSQL aplica-se tanto ao crescimento dos dados quanto
ao número de usuários agindo simultaneamente sobre os dados.

##3. Disponibilidade

A indisponibilidade de um banco de dados pode causar sérios prejuízos,
incluindo perda de clientes. A maioria dos bancos de dados NoSQL
oferecem eficientes arquiteturas de replicação de dados que proporciona
aos NoSQLs maior disponibilidade. Ou seja, se um ou mais servidores (ou
nós) cai um outro nó do cluster está apto a continuar o trabalho
automaticamente sem perda de dados.

##4. Raízes open source

Muitos bancos de dados NoSQL tem raízes na comunidade open
source. Talvez isso tenha sido fundamental para o rápido crescimento do
seu uso e popularidade. Nota-se que as companhias que oferecem versões
comerciais de bancos NoSQL com uma forte estrutura de suporte e
serviços, estão ao mesmo tempo participando direta ou indiretamente de
comunidades de bancos de dados NoSQL open source. Exemplos são
Apache-&gt;Cassandra, IBM-&gt;CouchDB, MongoDB-&gt;MongoDB open source,
entre outros.

##5. Baixo custo operacional

Devido ao peso do **open source** no NoSQL, o custo para iniciar a
utilização desses bancos de dados também se torna muito baixo ou zero. É
comum ouvir dizerem que a transição **relacional -&gt; NoSQL** diminuiu
muito os custos enquanto obteve um desempenho melhor ou igual ao
anterior.

Grandes bancos de dados relacionais requerem computadores ou mainframes
caros. Com o NoSQL, esse custo também diminui, pois este foi
desenvolvido para trabalhar em ambientes distribuídos.

##6. Funcionalidades especiais

Também com o peso do **open source** sobre o NoSQL, muitos
distribuidores de bancos de dados NoSQL oferecem algumas funcionalidades
especiais para incentivar e atrair mais usuários. Índices específicos,
capacidade de consulta de dados geoespaciais, replicação automática de
dados, funcionalidades para sincronização, APIs RESTful são exemplos de
funcionalidades especiais oferecidas pelos diferentes distribuidores
NoSQL.

##Conclusão

Na hora de escolher o banco de dados que você vai utilizar na sua
próxima aplicação, considere usar um banco de dados NoSQL. Não é atoa
que a popularidade do NoSQL cresceu tão rápido nos últimos anos.

Além de optar pela utilização de um NoSQL, há uma grande variedade de
bancos de dados NoSQL com diferentes funcionalidades que podem lhe
ser muito útil durante o desenvolvimento.

Uma coisa é certa: se você pretende desenvolver um software que vai
crescer (escalar) MUITO, a melhor alternativa é um NoSQL.
