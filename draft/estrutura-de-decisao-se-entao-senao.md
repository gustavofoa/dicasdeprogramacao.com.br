Title: Estrutura de decisão SE-ENTÃO-SENÃO
Date: 2013-03-12 16:25
Author: gustavo.foa
Category: Iniciante
Tags: Algoritmos, controle de fluxo, estrutura condicional, estrutura de decisão, estrutura de seleção, IF-THEN-ELSE, lógica de programação, se então senão
Slug: estrutura-de-decisao-se-entao-senao
Status: published

A maioria dos algoritmos precisam tomar decisões ao longo de sua
execução. Para isso existem as estruturas de decisão, e a mais utilizada
é a estrutura **SE-ENTÃO-SENÃO **(Em inglês **IF-THEN-ELSE**). O
funcionamento é simples: com base no resultado de uma expressão booleana
(**VERDADEIRO** ou **FALSO**), o fluxo do algoritmo segue para um bloco
de instruções ou não. Observe o esquema da estrutura **SE-ENTÃO-SENÃO**:

> **SE** &lt;expressão booleana&gt;
>
> **ENTÃO**
>
> &lt;instruções a serem executadas caso a expressão booleana resulte em
> **VERDADEIRO**&gt;
>
> **SENÃO**
>
> &lt;instruções a serem executadas caso a expressão booleana resulte em
> **FALSO**&gt;
>
> **FIM-SE**

O bloco de código **SENÃO** é opcional. É comum encontrar instruções de
decisão apenas com **SE-ENTÃO** sem o bloco **SENÃO**. Veja um esquema
gráfico desta estrutura de decisão.

[![estrutura
IF](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/estrutura-IF.png){.aligncenter
.size-full .wp-image-981 width="580"
height="515"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/estrutura-IF.png)

SE-ENTÃO-SENÃO na prática! {#se-então-senão-na-prática style="text-align: justify;"}
--------------------------

Vejamos um exemplo de utilização desta estrutura com um algoritmo, para
isso vamos utilizar o VisuAlg (para mais informações leia o [artigo
sobre linguagens de programação para
iniciantes](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Linguagem de programação para iniciantes")).
Neste algoritmo, vamos simular um caixa eletrônico quando vamos sacar
dinheiro. O caixa eletrônico verifica se o valor que desejamos sacar é
menor que o saldo disponível. Assumiremos que há R\$ 1000 de saldo
disponível para o saque.

``` {.lang:default .decode:true title="Algoritmo Sacar Dinheiro"}
algoritmo "SacarDinheiro"
var
   SaldoDisponivel : REAL
   ValorDoSaque : REAL
inicio

      SaldoDisponivel := 1000 //Assumimos que há 1000 reais de saldo na conta disponível para saque
      ESCREVA ("Informe o valor do Saque: ")
      LEIA (ValorDoSaque)
      SE ValorDoSaque <= SaldoDisponivel ENTAO
         SaldoDisponivel := SaldoDisponivel - ValorDoSaque
         ESCREVAL ("Sacando R$ ", ValorDoSaque, ".")
      SENAO
         ESCREVAL ("O valor solicitado é maior que o valor disponível para saque!")
      FIMSE

      ESCREVAL ("Saldo disponível: R$ ", SaldoDisponivel)

fimalgoritmo
```

Abaixo a execução do algoritmo acima quando informamos valores menores
que 1000.

[![Sacar dinheiro menor que
1000](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Sacar-dinheiro-menor-que-10001.png){.aligncenter
.size-full .wp-image-975 width="681"
height="199"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Sacar-dinheiro-menor-que-10001.png)

Agora a execução do mesmo algoritmo, porém inserindo um valor maior que
1000 para saque.

[![Sacar dinheiro maior que
1000](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Sacar-dinheiro-maior-que-1000.png){.aligncenter
.size-full .wp-image-976 width="681"
height="228"}](http://www.dicasdeprogramacao.com.br/wp-content/uploads/2013/03/Sacar-dinheiro-maior-que-1000.png)

Perceba que o fluxo do algoritmo tomou rumos diferentes.

Essa é a estrutura de controle de fluxo mais utilizada na criação de
programas de computador. Pratique-a criando algoritmos que tomam
decisão. Como exercício, crie um algoritmo para verificar se um aluno
foi aprovado ou reprovado no final do ano, assim: O usuário digita as 4
notas (de 0 a 10) bimestrais do aluno e o algoritmo deve calcular a
média e verificar se é maior que 6. Caso afirmativo, exibe na tela uma
mensagem informando que o aluno foi aprovado, caso contrário, uma
mensagem informando que ele foi reprovado.

Pratique!
