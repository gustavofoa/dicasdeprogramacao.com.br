Title: Estrutura de repetição ENQUANTO
Date: 2013-04-22 09:00
Author: gustavo.foa
Category: Iniciante
Tags: Algoritmos, controle de fluxo, ENQUANTO, estrutura de repetição, lógica de programação, WHILE
Slug: estrutura-de-repeticao-enquanto
Status: published

Em nossos algoritmos, hora ou outra precisamos executar alguns passos
<span style="text-decoration: underline;">mais de uma vez</span>. Ou
mesmo executar repetidamente alguns passos até que alguma condição seja
atendida. A partir dessa necessidade surgem as estruturas de
repetição, também conhecidas como **LOOP**. Neste artigo, vamos tratar
de forma especial a estrutura de repetição **ENQUANTO** (em inglês,
**WHILE**). Seu funcionamento é tão simples quanto a [estrutura de
decisão ](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de decisão SE-ENTÃO-SENÃO")**[SE-ENTÃO](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de decisão SE-ENTÃO-SENÃO").**
A diferença é que os passos dentro deste bloco, são repetidos <span
style="text-decoration: underline;">enquanto</span> a expressão booleana
(VERDADEIRO ou FALSO) resultar VERDADEIRO. Veja o esquema abaixo:

> **ENQUANTO **&lt;expressão booleana&gt; **FAÇA**
>
> &lt;instruções a serem executadas <span
> style="text-decoration: underline;">enquanto</span> a expressão
> booleana resultar em VERDADEIRO&gt;
>
> **FIM-ENQUANTO**

Esta estrutura de repetição é também chamada de loop <span
style="text-decoration: underline;">pré-testado</span>, pois a expressão
booleana é verificada antes da primeira execução. Se inicialmente ela já
resultar em FALSO, as instruções que estão dentro do bloco não são
executadas nenhuma vez.

[![estrutura-ENQUATO](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/estrutura-ENQUATO.png){.aligncenter
.size-full .wp-image-1034 width="400"
height="515"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/estrutura-ENQUATO.png)

Estrutura ENQUANTO na prática! {#estrutura-enquanto-na-prática style="text-align: justify;"}
------------------------------

Para entender na prática como usamos essa estrutura de repetição,
vejamos um exemplo de algoritmo utilizando a ferramenta [<span
style="text-decoration: underline;">VisuAlg</span>](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Linguagem de programação para iniciantes").
Vamos implementar um algoritmo para somar valores até o usuário digitar
o valor 0. Ou seja, vamos somar todos os valores que o usuário digitar,
porém quando ele digitar 0 o "loop" acaba, a cada iteração do loop vamos
apresentar o resultado atual da soma.

``` {.lang:default .decode:true title="Algoritmo SomaEnquantoValorDiferenteDe0"}
algoritmo "SomaEnquantoValorDiferenteDe0"
var
   valorDigitado : REAL
   soma : REAL
inicio

      soma := 0
      ESCREVA ("Digite um valor para a soma: ")
      LEIA (valorDigitado)

      ENQUANTO valorDigitado <> 0 FACA
          soma := soma + valorDigitado
          ESCREVAL ("Total: ", soma)
          ESCREVA ("Digite um valor para a soma: ")
          LEIA (valorDigitado)
      FIMENQUANTO

      ESCREVAL ("Resultado: ", soma)

fimalgoritmo
```

Observe o resultado deste algoritmo.

[![Resultado algoritmo
ENQUANTO](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Resultado-algoritmo-ENQUANTO.png){.aligncenter
.size-full .wp-image-1022 width="682"
height="292"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Resultado-algoritmo-ENQUANTO.png)

As estruturas de repetição são muito utilizadas em desenvolvimento de
softwares. Entender como funciona é muito importante para resolver
problemas que precisam executar tarefas repetidas vezes. Para praticar a
utilização da estrutura ENQUANTO, implemente um algoritmo no
[VisuAlg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Linguagem de programação para iniciantes")
para calcular uma multiplicação através de somas consecutivas, para
facilitar assuma que os dois fatores da multiplicação são positivos.
Caso não consiga, acesse o artigo [O que é
Algoritmo](http://www.dicasdeprogramacao.com.br/o-que-e-algoritmo/ "O que é Algoritmo?"),
que tem um exemplo desse cálculo.
