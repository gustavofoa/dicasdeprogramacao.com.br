title: Exercício: Algorítmo Par ou Ímpar
date: 2018-06-27
author: Gustavo Furtado de Oliveira Alves
category: Iniciante em programação
tags: Exercícios
slug: exercicio-algoritmo-par-ou-impar

Lógica de programação se aprende com muita prática.
Por isso quero mostrar para quem está aprendendo, como implementar os algorítmos básicos de lógica de programação.

Neste post, você vai aprender como implementar um algorítmo que verifica se um número é PAR ou ÍMPAR.

## Passo 1: Esqueleto do algorítmo

O primeiro passo é criar a estrutura do algorítmo. Todo algorítmo tem um **nome** uma área para a **declaração das variáveis** e um **corpo**.

```
Algoritmo "ParOuImpar"

Var

Inicio

Fimalgoritmo
```

## Passo 2: Solicitação do número para o usuário

O segundo passo é solicitar que o usuário digite o número, para verificarmos se ele é par ou ímpar.

Pense que é uma conversa, você diz ao usuário o que ele precisa fazer, o usuário informa o valor que a gente pedi e em seguida a gente armazena esse valor em uma variável.

Se vamos usar uma variável, também precisamos declará-la na sessão de variáveis. Veja

```
Algoritmo "ParOuImpar"

Var
    numero : inteiro
Inicio

    escreva("Informe um número: ")
    leia(numero)

Fimalgoritmo
```

Veja a execução deste algorítmo no [Visualg 3](https://dicasdeprogramacao.com.br/downloads/visualg){:target=\_blank}.

![Lendo o valor digitado pelo usuário em uma variável](/images/exercicio-algoritmo-par-ou-impar/lendo-valor-na-variavel.gif){:width=100%}

## Passo 3: Verificação se o número é par ou ímpar

Agora que nós já obtemos o valor que o usuário digitou, podemos verificar se o número é par ou ímpar e dar essa informação pra ele.

Pra isso, vamos utilizar a estrutura de controle [SE-ENTÃO-SENÃO](https://dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/){:target=\_blank}.

E a verificação que vamos utilizar é: **Se o resto da divisão do número por 2 for igual a 0, então o número é par, senão o número é ímpar.**

Mas como obter o resto de uma divisão? utilizando o [operador](https://dicasdeprogramacao.com.br/operadores-aritmeticos/){:target=\_blank}
**MOD**.

Veja o algorítimo final

```
Algoritmo "ParOuImpar"

Var

    numero : inteiro

Inicio

       escreva("Escreva um número: ")
       leia(numero)

       se numero mod 2 = 0 entao
           escreva("O número ", numero, " é par!")
       senao
           escreva("O número ", numero, " é ímpar!")
       fimse

Fimalgoritmo
```

Perceba que nas mensagens que apresentamos ao usuário,
nós _concatenamos_ o valor da variável número com o texto.

## Video

Eu gravei um video implementando este algorítmo passo-a-passo.

Assim você pode ver como eu faço na prática!

<div class="youtube youtube-16x9">
<iframe src="https://www.youtube.com/embed/CI9P9hD74G4" allowfullscreen seamless frameBorder="0"></iframe>
</div>

Gostou do post? Você pode ter acesso GRATUITO a um minicurso e um e-book
de lógica de programação para iniciantes. Basta se inscrever no link abaixo.

[>> Quero me inscrever no minicurso GRATUITO de lógica de programação!](https://mclp.dicasdeprogramacao.com.br)

Escreva aqui em baixo nos comentários o que você achou do post e do video.

E se você ficou com alguma dúvida, fique a vontade para perguntar nos comentários que eu respondo!