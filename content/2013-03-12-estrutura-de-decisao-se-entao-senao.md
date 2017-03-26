title: Estrutura de decisão SE-ENTÃO-SENÃO
date: 2013-03-12
author: Gustavo Furtado de Oliveira Alves
category: Iniciante
slug: estrutura-de-decisao-se-entao-senao

A maioria dos algoritmos precisam tomar decisões ao longo de sua
execução. Para isso existem as estruturas de decisão, e a mais utilizada
é a estrutura **SE-ENTÃO-SENÃO **(Em inglês **IF-THEN-ELSE**). O
funcionamento é simples: com base no resultado de uma expressão booleana
(**VERDADEIRO** ou **FALSO**), o fluxo do algoritmo segue para um bloco
de instruções ou não. Observe o esquema da estrutura **SE-ENTÃO-SENÃO**:

> **SE** &lt;expressão booleana&gt; **ENTÃO**
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

![estrutura
IF](/images/estrutura-de-decisao-se-entao-senao/estrutura-IF.png){.aligncenter}

##SE-ENTÃO-SENÃO na prática!

Vejamos um exemplo de utilização desta estrutura com um algoritmo, para
isso vamos utilizar o VisuAlg (para mais informações leia o [artigo
sobre linguagens de programação para
iniciantes](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Linguagem de programação para iniciantes"){:target=\_blank}).
Neste algoritmo, vamos simular um caixa eletrônico quando vamos sacar
dinheiro. O caixa eletrônico verifica se o valor que desejamos sacar é
menor que o saldo disponível. Assumiremos que há R\$ 1000 de saldo
disponível para o saque.

```
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

![Sacar dinheiro menor que
1000](/images/estrutura-de-decisao-se-entao-senao/Sacar-dinheiro-menor-que-10001.png){.aligncenter}

Agora a execução do mesmo algoritmo, porém inserindo um valor maior que
1000 para saque.

![Sacar dinheiro maior que
1000](/images/estrutura-de-decisao-se-entao-senao/Sacar-dinheiro-maior-que-1000.png){.aligncenter}

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
