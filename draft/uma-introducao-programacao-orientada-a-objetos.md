Title: Introdução à Programação Orientada a Objetos
Date: 2014-11-03 07:03
Author: gustavo.foa
Category: Técnicas e Metodologias
Tags: POO, programação orientada a objetos
Slug: uma-introducao-programacao-orientada-a-objetos
Status: draft

Uma das técnicas de programação mais utilizadas hoje em dia é a
Programação Orientação à Objetos (POO). As linguagens de programação
mais utilizadas pelo mercado atualmente são ditas Linguagens Orientadas
a Objeto, tais como Java, C\#, C++, PHP, Python, Ruby, Scala, etc. E as
ofertas de emprego para programador raramente não pedem conhecimento em
tais linguagens ou POO.

Evidentemente, pra ser um bom programador hoje - e se destacar no
mercado de trabalho - é muito importante conhecer Programação Orientada
a Objetos, e principalmente saber como e quando usar os recursos desta
técnica. Neste post vou mostrar a ideia básica por trás da POO e
seus recursos.

![Programação Orientada a
Objetos](http://www.dicasdeprogramacao.com.br/wp-content/uploads/Programação-Orientada-a-Objetos.png){.aligncenter
.wp-image-1902 .size-full width="600" height="397"}

Antes, um pouquinho de história...
----------------------------------

Nos primórdios da programação, os códigos eram criados em um bloco único
e para controlar a execução do programa utilizava-se o comando
*goto* que realiza saltos no código. Dar manutenção num código desses
poderia ser considerado motivo para suicídio.

Depois nasceu uma técnica conhecida como "**Programação Estruturada**"
para desenvolvimento de softwares, que usa basicamente estruturas de
controle
([if-then-else](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de decisão SE-ENTÃO-SENÃO"),
[switch-case](http://www.dicasdeprogramacao.com.br/estrutura-de-selecao-multipla-escolha-caso/ "Estrutura de seleção multipla ESCOLHA-CASO")
etc.), estruturas de repetição
([while](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto/ "Estrutura de repetição ENQUANTO"),
[repeat-until](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-repita-ate/ "Estrutura de repetição REPITA-ATÉ"),
[for](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-para/ "Estrutura de repetição PARA")),
[funções e
procedimentos](http://www.dicasdeprogramacao.com.br/o-que-sao-funcoes-e-procedimentos/ "O que são Funções e Procedimentos?").
Com isso acabou a sina do *goto* e ainda trouxe a possibilidade de
reutilização de código utilizando funções e procedimentos para
modularizar o código.

A Programação Estruturada trouxe muitos benefícios para a indústria de
desenvolvimento de softwares. Nós conseguimos criar códigos um mínimo
organizado, entretanto lidar com dados ainda era uma grande dificuldade.
Então a programação estruturada evoluiu para a "**Programação Orientada
a Objetos**".

A POO trouxe conceitos que possibilitaram a estruturação dos dados e da
lógica do sistema. Com a POO é possível agrupar em um só lugar dados e
operações relacionados a uma determinada "entidade". Dessa forma a POO
iniciou uma nova maneira de programar através de abstrações de
conceitos, resolvendo vários problemas enfrentados na antiga programação
estruturada. Para compreender isso é preciso entender os principais
conceitos e recursos da Programação Orientada a Objetos.

Principais conceitos e recursos da POO
--------------------------------------

A POO tem muitos recursos e quando se utiliza corretamente padrões de
projetos (design patterns) o código fica lindo! Vou explicar aqui os
principais recursos deste paradigma.

Eu já disse que o grande benefício da Orientação a Objetos é agrupar
dados e operações de uma determinada entidade em um só lugar.
Basicamente nós conseguimos isso através do conceito de classes e
objetos.

### Classes e Objetos

Classes são tipos de dados customizados. Além do tipos de dados
primitivos com inteiro, real, etc. as linguagens de programação
orientadas a objeto permitem a criação de novos tipos de dados, as
classes.

 
