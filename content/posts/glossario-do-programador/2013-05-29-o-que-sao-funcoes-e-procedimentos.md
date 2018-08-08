title: O que são Funções e Procedimentos?
date: 2013-05-29
author: Gustavo Furtado de Oliveira Alves
category: Glossário do programador
slug: o-que-sao-funcoes-e-procedimentos

Me responda essa pergunta: Você saberia fazer um algoritmo para calcular
a raiz quadrada de um número? Reflita um pouquinho sobre a complexidade
de tal algoritmo. E um algoritmo para gerar um número aleatório, você
faz ideia de como fazer? Bom, não são algoritmos tão triviais para se
implementar. Mas e se você precisar descobrir a raiz quadrada de um
número ou mesmo gerar um número aleatório no seu algoritmo, o que fazer?

Aha! Já existem algoritmos que executam essas operações. O que
precisamos é apenas solicitar a execução desses algoritmos dentro do
nosso. Esse tipo de algoritmo que solicitamos a execução de dentro do
nosso algoritmo são chamados de **funções** (ou **procedimentos** caso
não retornem um resultado).

![função](/images/o-que-sao-funcoes-e-procedimentos/função.png){.aligncenter}

##Função ou Procedimento?

As **funções** (**functions**), também conhecidas como  sub-rotinas, são
muito utilizadas em programação. Um dos grandes benefícios é não
precisar copiar o código todas as vezes que precisar executar aquela
operação, além de deixar a leitura do código mais intuitiva. No exemplo
anterior, caso precisássemos descobrir a raiz quadrada de 10 números,
bastaria chamar a **função** que calcula a raiz quadrada 10 vezes.

Os **procedimentos **(**procedures**) diferem das funções apenas por não
retornarem resultado, imagine um procedimento que envia e-mail. Precisa
retornar resultado? Nos algoritmos apresentados aqui no **{ Dicas de
Programação }** nós já utilizamos muitos **procedimentos** sem perceber.
Por exemplo, para ler o valor digitado por um usuário nós já utilizamos
o procedimento **LEIA** e para mostrar um texto na tela nós utilizamos o
procedimento **ESCREVA**.

##Parâmetros

**Funções** (e **procedimentos**) podem ou não receber parâmetros. No
caso da função de raiz quadrada, é necessário passar como parâmetro o
número que se deseja calcular a raiz, o procedimento **ESCREVA**, requer
um texto como parâmetro para apresentar na tela do usuário.

##Usando funções na prática!

Acho que já deu pra entender o que são funções e procedimentos, vamos
ver agora como utilizá-las. Abaixo a um algoritmo que calcula a
hipotenusa de um triângulo retângulo, dado os lados, utilizando a função
RAIZQ do
[Visualg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank}.

```
algoritmo "Hipotenusa"
var
    a, b, c : REAL
inicio

      ESCREVA ("Digite o lado A do triângulo retângulo: ")
      LEIA (a)
      ESCREVA ("Digite o lado B do triângulo retângulo: ")
      LEIA (b)

      c := RAIZQ ( a*a + b*b )//Cálculo da hipotenusa utilizando a FUNÇÃO RAIZQ,

      ESCREVA ("O valor da hipotenusa é: ", c)

fimalgoritmo
```

Observe que utilizamos a função RAIZQ para calcular a raiz quadrada do
valor que passamos como parâmetro (valor entre parênteses) "a\*a +
b\*b", o valor retornado por essa função armazenamos na variável "c".

-   [Saiba o que é uma
    variável](http://www.dicasdeprogramacao.com.br/o-que-e-variavel-e-constante/ "O que é variável e constante?"){:target=\_blank}

Abaixo um exemplo da execução desse algoritmo.

![resultado algoritmo
hipotenusa](/images/o-que-sao-funcoes-e-procedimentos/resultado-algoritmo-hipotenusa.png){.aligncenter}

##Criando as próprias Funções e Procedimentos

Para se criar uma **função** no Visualg utilizamos a seguinte sintaxe:

```
funcao <nome-de-função> [(<seqüência-de-declarações-de-parâmetros>)]: <tipo-de-dado>
// Seção de Declarações Internas
inicio
// Seção de Comandos
fimfuncao
```

Já para criar um procedimento no Visualg utilizamos a seguinte sintaxe:

```
procedimento <nome-de-procedimento> [(<seqüência-de-declarações-de-parâmetros>)]
// Seção de Declarações Internas
inicio
// Seção de Comandos
fimprocedimento
```

Para exemplificar a criação e utilização das nossas próprias funções e
procedimentos, vamos criar um algoritmo para resolver equações de
segundo grau, onde criaremos uma função chamada *calcula\_delta*.

-   [<span style="line-height: 13px;">Dúvida sobre como calcular uma
    equação de segundo
    grau?</span>](http://www.brasilescola.com/matematica/equacao-2-grau.htm "Equação do segundo grau"){:target=\_blank}

```
algoritmo "EquaçãoDoSegundoGrau"
var
   a, b, c, delta, x1, x2: REAL

funcao calcula_delta(): REAL
var
   delta : REAL
inicio
      delta := b*b - 4*a*c
      RETORNE delta
fimfuncao

inicio
      ESCREVA ("Informe o valor de A: ")
      LEIA (a)
      ESCREVA ("Informe o valor de B: ")
      LEIA (b)
      ESCREVA ("Informe o valor de C: ")
      LEIA (c)

      delta := calcula_delta()
      SE ( delta < 0 ) ENTAO
         ESCREVA ("Esta equação não possui raízes reais.")
      SENAO
           SE (delta = 0) ENTAO
              x1 := (-b + RAIZQ(delta)) / (2*a)
              ESCREVA ("Esta equação possui apenas uma raiz: ", x1)
           SENAO
                x1 := (-b + RAIZQ(delta)) / (2*a)
                x2 := (-b - RAIZQ(delta)) / (2*a)
                ESCREVA ("Esta equação possui duas raízes: ", x1, " e ", x2)
           FIMSE
      FIMSE
fimalgoritmo
```

Veja que declaramos a função *calcula\_delta* no inicio do código, e
então podemos chamar essa função de dentro do algoritmo. Simples né? Pra
criar procedimento é a mesma coisa, só que não retorna resultado e
usamos a outra sintaxe apresentada anteriormente. Um possível resultado
da execução desse algoritmo é esse:

![resultado equação do segundo
grau](/images/o-que-sao-funcoes-e-procedimentos/resultado-equação-do-segundo-grau.png){.aligncenter}

##Conclusão

**Funções** e **procedimentos** são utilizados com muita frequência em
desenvolvimento de softwares. São vários benefícios como: evita
duplicação de código quando precisamos executar a mesma operação várias
vezes, deixa o entendimento do algoritmo mais intuitívo, pois tiramos a
parte complexa do código do fluxo principal do algoritmo, etc.

Em linguagens orientada a objeto como java, C++ e C\#, funções e
procedimentos são chamados de **MÉTODO**. Mais por uma questão de
conceito de Orientação a Objetos, mas no fundo é a mesma coisa, podem
receber parâmetros e retornam ou não um resultado.

Pratique identificando no seu código, onde você pode utilizar funções e
procedimentos. Um exemplo, é unir em um só procedimento aquele código de
leitura de valores do usuário que sempre utilizamos:

> ESCREVA ("Informe o valor de A: ")
>
> LEIA (a)

Já imagina como fazer isso? Qualquer dúvida, deixe nos comentários aí em
baixo.
