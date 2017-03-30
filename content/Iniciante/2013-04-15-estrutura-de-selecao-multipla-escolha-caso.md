title: Estrutura de seleção multipla ESCOLHA-CASO
date: 2013-04-15
author: Gustavo Furtado de Oliveira Alves
category: Iniciante
slug: estrutura-de-selecao-multipla-escolha-caso

A estrutura ESCOLHA-CASO (em inglês SWITCH-CASE), é uma solução elegante
quanto se tem várias [estruturas de
decisão](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de Decisão SE-ENTÃO-SENÃO"){:target=\_blank}
(SE-ENTÃO-SENÃO) aninhadas. Isto é, quando outras verificações são
feitas caso a anterior tenha falhado (ou seja, o fluxo do algoritmo
entrou no bloco SENÃO). A proposta da estrutura ESCOLHA-CASO é permitir
ir direto no bloco de código desejado, dependendo do valor de uma
variável de verificação. Veja o esquema abaixo.

> **ESCOLHA** &lt;variável de verificação&gt;
>
> **CASO** &lt;valor1&gt; **FAÇA**
>
> "instruções a serem executadas caso &lt;variável de verificação&gt; =
> &lt;valor1&gt;"
>
> **CASO** &lt;valor2&gt; **FAÇA**
>
> "instruções a serem executadas caso &lt;variável de verificação&gt; =
> &lt;valor2&gt;"
>
> **CASO** &lt;valor3&gt; **FAÇA**
>
> "instruções a serem executadas caso &lt;variável de verificação&gt; =
> &lt;valor3&gt;"
>
> ...
>
> **FIM-ESCOLHA**

Veja o esquema desta estrutura de seleção.

![estrutura-ESCOLHA](/images/estrutura-de-selecao-multipla-escolha-caso/estrutura-ESCOLHA.png){.aligncenter}

##ESCOLHA-CASO na prática!

Para exemplificar a melhoria oferecida por essa estrutura, imagine a
seguinte situação: Você deseja criar um algoritmo para uma calculadora,
o usuário digita o primeiro número, a operação que deseja executar e o
segundo número. Dependendo do que o usuário informar como operador, o
algoritmo executará um cálculo diferente (soma, subtração, multiplicação
ou divisão). Vejamos como seria esse algoritmo implementado no
[VisuAlg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Linguagem de programação para iniciantes"){:target=\_blank} com
[SE-ENTÃO-SENÃO](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de decisão SE-ENTÃO-SENÃO"){:target=\_blank}.

```
algoritmo "CalculadoraBasicaComSE"
var
   numero1 : REAL
   numero2 : REAL
   operacao : CARACTERE
   resultado : REAL
inicio

      ESCREVA ("Digite o primeiro número: ")
      LEIA (numero1)
      ESCREVA ("Digite a operação: ")
      LEIA (operacao)
      ESCREVA ("Digite o segundo número: ")
      LEIA (numero2)

      SE operacao = "+" ENTAO
         resultado := numero1 + numero2
      SENAO
         SE operacao = "-" ENTAO
            resultado := numero1 - numero2
         SENAO
            SE operacao = "*" ENTAO
               resultado := numero1 * numero2
            SENAO
               SE operacao = "/" ENTAO
                  resultado := numero1 / numero2
               FIMSE
            FIMSE
         FIMSE
      FIMSE

      ESCREVA ("Resultado: ", resultado)

fimalgoritmo
```

Veja como os SEs aninhados (dentro dos SENÃOs) deixam o código mais
complexo. Dá pra entender a lógica, mas não é muito elegante. Agora
vamos ver como ficaria a mesma lógica com a estrutura ESCOLHA-CASO.

```
algoritmo "CalculadoraBasicaComSE"
var
   numero1 : REAL
   numero2 : REAL
   operacao : CARACTERE
   resultado : REAL
inicio

      ESCREVA ("Digite o primeiro número: ")
      LEIA (numero1)
      ESCREVA ("Digite a operação: ")
      LEIA (operacao)
      ESCREVA ("Digite o segundo número: ")
      LEIA (numero2)

      ESCOLHA operacao
         CASO "+"
            resultado := numero1 + numero2
         CASO "-"
            resultado := numero1 - numero2
         CASO "*"
            resultado := numero1 * numero2
         CASO "/"
            resultado := numero1 / numero2
      FIMESCOLHA

      ESCREVA ("Resultado: ", resultado)

fimalgoritmo
```

Bem mais bonito! Agora a lógica tá mais visível e elegante. O resultado
dos dois algoritmos é o mesmo, veja um exemplo de execução deste
programa.

![Resultado do Algoritmo de Calculadora
básica](/images/estrutura-de-selecao-multipla-escolha-caso/Resultado-do-Algoritmo-de-Calculadora-básica.png){.aligncenter}

##Caso não tratado na estrutura (OUTROCASO)

Existe uma opção a mais nessa estrutura, justamente para tratar quando o
valor da variável não é equivalente a nenhum valor informado como opção
nos CASOs, ou seja, é um "OUTROCASO". No algoritmo listado
anteriormente, imagine se o usuário digitasse um valor diferente de "+",
"-", "\*" e "/". Caso quiséssemos apresentar uma mensagem para o usuário
informando que ele digitou uma opção inválida, utilizaríamos esse
recurso da estrutura ESCOLHA-CASO. Veja.

```
      ESCOLHA operacao
         CASO "+"
            resultado := numero1 + numero2
         CASO "-"
            resultado := numero1 - numero2
         CASO "*"
            resultado := numero1 * numero2
         CASO "/"
            resultado := numero1 / numero2
         OUTROCASO
            ESCREVA("A operação digitada é inválida!")
      FIMESCOLHA
```

Como pudemos observar, em termos de organização de código a estrutura
ESCOLHA-CASO é uma opção muito elegante quando se tem muitos
SE-ENTÃO-SENÃO para verificar a mesma variável. Facilita a leitura do
algoritmo e a manutenção do código.

Como exercício para praticar essa
estrutura de controle de fluxo, crie um algoritmo em que o usuário
digita uma letra qualquer, e o programa verifica qual a ordem dessa
letra no alfabeto, por exemplo: se o usuário digitar a letra 'G' o
programa deve imprimir na tela, "G é a sétima letra do alfabeto".
Implemente com a estrutura ESCOLHA-CASO e depois com a estrutura
SE-ENTÃO-SENÃO para perceber a diferença. Qualquer dúvida deixe nos
comentários aqui em baixo.
