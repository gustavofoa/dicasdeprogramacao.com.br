Title: Estrutura de repetição REPITA-ATÉ
Date: 2013-04-24 10:00
Author: gustavo.foa
Category: Iniciante
Tags: Algoritmos, controle de fluxo, estrutura de repetição, REPEAT, REPEAT-UNTIL, REPITA, REPITA-ATÉ
Slug: estrutura-de-repeticao-repita-ate
Status: published

Frequentemente precisamos implementar uma estrutura de repetição em
nossos algoritmos para resolver algum problema. Um recurso para fazer
isso é a estrutura ENQUANTO, ([clique aqui e leia o artigo sobre a
estrutura
ENQUANTO](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto/ "Estrutura de repetição ENQUANTO")).
Uma outra estrutura de repetição interessante é a **REPITA-ATÉ**
(Repeat-Until). A diferença desta estrutura é que ela é um **LOOP
PÓS-TESTADO**, isto é, o teste para verificar se o bloco será executado
novamente, acontece no final do bloco. Isso garante que as instruções
dentro deste bloco serão executadas ao menos uma vez. Veja como é o
esquema do **REPITA-ATÉ**.

> **REPITA**
>
> &lt;instruções a serem executadas repetidamente <span
> style="text-decoration: underline;">até</span> a expressão booleana
> retornar VERDADEIRO&gt;
>
> **ATÉ** &lt;expressão booleana&gt;

Perceba, que além de ser pós-testada, esta estrutura testa o contrário
do ENQUANTO. Na estrutura **REPITA-ATÉ**, as instruções do bloco são
executadas repetidamente <span
style="text-decoration: underline;">enquanto</span> a expressão booleana
resultar FALSO. A partir do momento que a expressão booleana resultar
VERDADEIRO, o fluxo do algoritmo sairá do LOOP. Veja  graficamente o
funcionamento.

[![estrutura-REPITA](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/estrutura-REPITA.png){.aligncenter
.size-full .wp-image-1046 width="397"
height="507"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/estrutura-REPITA.png)

A estrutura REPITA-ATÉ na prática! {#a-estrutura-repita-até-na-prática style="text-align: justify;"}
----------------------------------

Vamos usar o mesmo exemplo que apresentei no artigo sobre a [estrutura
de repetição
ENQUANTO](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto/ "Estrutura de repetição ENQUANTO").
Pois naquele algoritmo, foi preciso repetir uma parte do código para
solucionar uma particularidade da estrutura. Vejamos novamente o exemplo
(Lembrando que estamos utilizando o VisuAlg para implementar os
algoritmos, para mais detalhes [clique
aqui](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Linguagem de programação para iniciantes")).

``` {.lang:default .decode:true}
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

Veja que a leitura de dados é escrita duas vezes neste algoritmo (linhas
8,9,14 e 15), o motivo para fazer isso é que a estrutura ENQUANTO é
<span style="text-decoration: underline;">pré-testada</span>. Logo, não
dá pra testar se o usuário digitou o valor 0 se ele ainda não tiver
digitado valor nenhum. Com a estrutura de repetição REPITA-ATÉ não é
necessário escrever duas vezes a leitura de dados do usuário, pois ela é
<span style="text-decoration: underline;">pós-testada</span>. Observe a
implementação daquele algoritmo com REPITA-ATÉ.

``` {.lang:default .decode:true}
algoritmo "SomaAteValorIgualA0"
var
   valorDigitado : REAL
   soma : REAL
inicio

      soma := 0   

      REPITA
          ESCREVA ("Digite um valor para a soma: ")
          LEIA (valorDigitado)
          soma := soma + valorDigitado
          ESCREVAL ("Total: ", soma)
      ATE valorDigitado = 0

fimalgoritmo
```

Podemos observar que o teste mudou de (**valorDigitado &lt;&gt; 0**) na
estrutura ENQUANTO, para (**valorDigitado = 0**) na estrutura
REPITA-ATÉ. Você saberia explicar por quê? Pense um pouco e responda por
si mesmo. (Se tiver dúvida pode deixar um comentário que explicaremos).
O resultado deste algoritmo pode ser observado abaixo.

[![Resultado
REPITA-ATE](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Resultado-REPITA-ATE.png){.aligncenter
.size-full .wp-image-1051 width="681"
height="251"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Resultado-REPITA-ATE.png)

Pra finalizar, percebemos que é possível utilizar qualquer uma das duas
estruturas para implementar LOOPs, porém cada uma é mais apropriada
dependendo do problema. Neste problema em particular, a estrutura
REPITA-ATÉ se mostrou mais apropriada. Mas essa decisão de qual utilizar
entre as duas, sempre será tomada observando a diferença entre
PRÉ-TESTADA e PÓS-TESTADA.
