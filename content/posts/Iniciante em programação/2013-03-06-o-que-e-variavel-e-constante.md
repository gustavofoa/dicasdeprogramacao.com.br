title: O que é variável e constante?
date: 2013-03-06
author: Gustavo Furtado de Oliveira Alves
category: Iniciante em programação
slug: o-que-e-variavel-e-constante

Programas de computador utilizam os recursos de hardware mais básicos
para executar
[algoritmos](http://www.dicasdeprogramacao.com.br/o-que-e-algoritmo/ "O que é Algoritmo?"){:target=\_blank}.
Enquanto o processador executa os cálculos, a memória é responsável por
armazenar dados e servi-los ao processador. O recurso utilizado nos
programas para escrever e ler dados da memória do computador é conhecido
como <span style="text-decoration: underline;">variável</span>, que é
simplesmente um espaço na memória o qual reservamos e damos um nome. Por
exemplo, podemos criar uma variável chamada "idade" para armazenar a
idade de uma pessoa. Você pode imaginar uma variável como uma gaveta
"etiquetada" em um armário.

![gaveta](/images/o-que-e-variavel-e-constante/variável.jpg "Variável - gaveta"){.aligncenter}

Quando criamos uma variável em nosso programa especificamos que tipo de
dados pode ser armazenado nela (dependendo da linguagem de programação).
Por exemplo, a variável <span
style="text-decoration: underline;">nome</span> só poderia armazenar
valores do tipo texto. Já a variável <span
style="text-decoration: underline;">idade</span>, só poderia armazenar
valores do tipo número (inteiro).

Chamamos este espaço alocado na memória de **variável**, porque o valor
armazenado neste espaço de memória pode ser alterado ao longo do tempo,
ou seja, o valor ali alocado é "variável" ao longo do tempo. Diferente
das **constantes**, que é um espaço reservado na memória para armazenar
um valor que não muda com o tempo. Por exemplo, o valor PI
(3.14159265359...) que nunca vai mudar!

##Veja como funciona uma variável com um [algoritmo](http://www.dicasdeprogramacao.com.br/o-que-e-algoritmo/ "O que é Algoritmo?"){:target=\_blank}

Para não restar dúvidas, vamos mostrar como funciona uma variável em um
algoritmo.

> Algoritmo **Teste de Variável**
>
> **Declaração das variáveis**
>
> nome : Texto
>
> **Inicio**
>
> nome &lt;- "João"
>
> imprimir(nome)
>
> nome &lt;- "Maria"
>
> imprimir(nome)
>
> **Fim**

Neste algoritmo, declaramos uma variável chamada "nome" do tipo "Texto".
Inicialmente armazenamos o texto "João" na variável nome, e mandamos
imprimir na tela o valor desta variável. Neste momento aparece na tela o
texto "João", em seguida alteramos o valor da variável para "Maria"
neste momento o texto "João" é apagado da memória e em seu lugar é
armazenado o texto "Maria". Em seguida, mandamos imprimir na tela
novamente o valor da variável, então aparece na tela o texto "Maria".

Só mais um exemplo pra garantir. rs

> Algoritmo **Soma**
>
> **Declaração de variáveis**
>
> numero1 : Inteiro
>
> numero2: Inteiro
>
> resultado: Inteiro
>
> **Inicio**
>
> numero1 &lt;- 5
>
> numero2 &lt;- 4
>
> resultado &lt;- numero1 + numero2
>
> imprimir(resultado)
>
> numero2 &lt;- 2
>
> resultado &lt;- resultado \* numero2
>
> imprimir(resultado)
>
> **Fim**

O resultado deste algoritmo é imprimir na tela o valor "9" e depois o
valor "18". Ainda resta dúvidas?

Saber como ler e escrever dados na memória do computador é muito
importante para criar um algoritmo. E a forma como fazemos isso é
através das <span style="text-decoration: underline;">variáveis</span>.
