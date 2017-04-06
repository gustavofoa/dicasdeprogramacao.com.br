title: Você sabe usar os Operadores Aritméticos em programação?
date: 2013-04-19
author: Gustavo Furtado de Oliveira Alves
category: Iniciante em programação
slug: operadores-aritmeticos

Todo mundo já usou operadores aritméticos na escola! Nos primeiros anos
de estudo aprendemos a fazer continhas de soma, subtração, multiplicação
e divisão. Em algoritmos eles também são simples e têm a mesma
simbologia em todas as linguagens de programação ( +, -, \* e / ).

Além desses mais simples, dois outros operadores aritméticos não recebem
muita atenção e pode ser que você não os conhece, eles são o **div** e
o **mod**, que resultam, respectivamente, o **quociente **(a
parte inteira do resultado da divisão) e o **resto** da divisão. Observe
as operações abaixo:

> 14 **/** 4 = 3,5
>
> 14 **div** 4 = 3
>
> 14 **mod** 4 = 2

O operador **mod** em muitas linguagens de programação (java por
exemplo) é representado pelo símbolo “**%**“, assim:

> 14 **%** 4 = 2

![operadores
aritméticos](/images/operadores-aritmeticos/operadores-aritméticos.jpg){.aligncenter}

Um outro operador aritmético que existe em algumas linguagens de
programação é o **^** e executa a operação de potência, mas geralmente
essa operação é realizada através de uma função chamada **pow**, bem
como a operação de radiciação (função **sqrt)**. Veja um exemplo do
operador ^:

> 2 **^** 5 = 32 (dois elevado a cinco)

Operadores aritméticos de radiciação também são fornecidos por algumas
linguagens de programação, mas esses são bem mais raros. O Postgres por
exemplo oferece os símbolos **|/** e **||/** para operações de raiz
quadrada e raiz cúbica, respectivamente.

##Precedência entre os operadores aritméticos

Da mesma forma que na matemática, os operadores
de multiplicação e divisão têm precedência de execução em relação aos
operadores de soma e subtração. Aliás se tiver parênteses na expressão
estes têm precedência ainda maior. A tabela abaixo indica a precedência
dos operadores.

  | **Prioridade** | **Operadores**                                                         |
  |----------------|------------------------------------------------------------------------|
  | 1º             | Parênteses internos                                                    |
  | 2º             | potência (**^**) e raiz (quando a linguagem oferece esses operadores) |
  | 3º             | \* / **div** e **mod**                                                 |
  | 4º             | + e -                                                                  |

Os operadores de mesma prioridade são interpretados da esquerda para a
direita. Para exemplificar essa questão de precedência, observe a
expressão:

> **5 + 3 \* ( 3 – 1 ) – 2 ^ 5 / 4 – 1**

O computador executa o cálculo na seguinte sequência:

> 5 + 3 \* <span style="text-decoration: underline;">**2**</span> - 2 ^
> 5 / 4 – 1
>
> 5 + 3 \* 2 - <span style="text-decoration: underline;">**32**</span> /
> 4 – 1
>
> 5 + <span style="text-decoration: underline;">**6**</span> - 32 / 4 –
> 1
>
> 5 + 6 - <span style="text-decoration: underline;">**8**</span> – 1
>
> <span style="text-decoration: underline;">**11**</span> - 8 - 1
>
> <span style="text-decoration: underline;">**3**</span> – 1
>
> <span style="text-decoration: underline;">**2**</span>

Os operadores aritméticos realmente todo mundo deve saber desde criança,
mas para criarmos algoritmos é muito importante conhecermos mais
detalhes, como o operador **mod** ou a ordem de precedência de cada um.
Ainda assim, um dia você pode ser surpreendido com um resultado que você
não esperava de uma expressão.
