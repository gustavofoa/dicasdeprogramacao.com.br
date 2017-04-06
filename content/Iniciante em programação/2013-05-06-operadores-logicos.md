title: Conheça os operadores lógicos!
date: 2013-05-06
author: Gustavo Furtado de Oliveira Alves
category: Iniciante em programação
slug: operadores-logicos

As operações lógicas são ensinadas em vários cursos de tecnologia de
diferentes formas, por exemplo, em cursos de eletrônica é ensinado
portas lógicas, já em programação aprendemos os operadores lógicos. Mas
no fundo é a mesma coisa e se você entender a ideia das operações
lógicas você pode usar esse conhecimento em qualquer área da tecnologia.

##Tipo de dados LÓGICO

![operadores lógicos](/images/operadores-logicos/operadores-lógicos.jpg){.alignleft}

O [tipo de dados
primitivo](http://www.dicasdeprogramacao.com.br/tipos-de-dados-primitivos/ "O que são tipos de dados primitivos?"){:target=\_blank}
mais simples é o chamado **booleano** ( ou lógico ). Pra quem não
conhece esse tipo de dados, um dado booleano só pode assumir dois
valores ( **VERDADEIRO** ou **FALSO** ). Em eletrônica, costuma-se
ensinar apresentando como exemplo uma lâmpada, que pode estar acesa
(verdadeiro) ou apagada (falso). Isso é o básico. Na literatura você
pode encontrar esses dados de diferentes formas, por exemplo:
verdadeiro/falso, aceso/apagado, 1/0, ligado/desligado, true/false,
sim/não, etc….

As operações lógicas trabalham sobre valores booleanos, tanto os valores
de entrada como o de saída são desse tipo. Os operadores lógicos são: E,
OU, NÃO, NÃO-E, NÃO-OU, OU-EXCLUSIVO E NÃO-OU-EXCLUSIVO. Abaixo uma
explicação de cada um.

### Operador E (AND)

![porta lógica
AND](/images/operadores-logicos/portas-lógicas-AND.jpg "porta lógica AND"){.alignright}

O Operador “E” ou “AND” resulta em um valor VERDADEIRO se os dois
valores de entrada da operação forem VERDADEIROs, caso contrário o
resultado é FALSO. Abaixo a **tabela-verdade** da operação E.

  **VALOR 1**      |  **VALOR 2**     | **OPERAÇÃO E**
  ---------------- | ---------------- | ----------------
  **VERDADEIRO**   | **VERDADEIRO**   | **VERDADEIRO**
  VERDADEIRO       | FALSO            | FALSO
  FALSO            | VERDADEIRO       | FALSO
  FALSO            | FALSO            | FALSO

### Operador OU (OR)

![porta lógica
OR](/images/operadores-logicos/portas-lógicas-OR.jpg "porta lógica OR"){.alignright}

O Operador “OU” ou “OR” resulta em um valor VERDADEIRO se ao menos UM
dos dois valores de entrada da operação for VERDADEIRO, caso contrário o
resultado é FALSO. Abaixo a **tabela-verdade** da operação OU.

  **VALOR 1**      | **VALOR 2**      | **OPERAÇÃO OU**
  ---------------- | ---------------- | -----------------
  **VERDADEIRO**   | **VERDADEIRO**   | **VERDADEIRO**
  **VERDADEIRO**   | FALSO            | **VERDADEIRO**
  FALSO            | **VERDADEIRO**   | **VERDADEIRO**
  FALSO            | FALSO            | FALSO

### Operador NÃO (NOT)

![porta lógica
NOT](/images/operadores-logicos/portas-lógicas-NOT.jpg "porta lógica NOT"){.alignright}

O Operador “NÃO” ou “NOT” é o único operador que recebe como entrada
apenas um valor, e sua função é simplesmente inverter os valores. Ou
seja, se o valor de entrada for VERDADEIRO, o resultado será FALSO e se
o valor de entrada for FALSO, o resultado será VERDADEIRO. Abaixo a
**tabela-verdade** da operação NÃO.

  **VALOR DE ENTRADA** | **OPERAÇÃO NÃO**
  -------------------- | ----------------
  **VERDADEIRO**       | FALSO
  FALSO                | **VERDADEIRO**

### Operador NÃO-E (NAND)

![porta lógica
NAND](/images/operadores-logicos/portas-lógicas-NAND.jpg "porta lógica NAND"){.alignright}

O Operador “NÃO-E” ou “NAND” é o contrário do operador E (AND), ou seja,
resulta em VERDADEIRO, se ao menos um dos dois valores for FALSO, na
verdade este é o operador E (AND) seguido do operador NÃO (NOT). Abaixo
a **tabela-verdade** da operação NÃO-E.

  **VALOR 1** | **VALOR 2** | **OPERAÇÃO NAND**
  ----------- | ----------- | -----------------
  VERDADEIRO  | VERDADEIRO  | FALSO
  VERDADEIRO  | **FALSO**   | **VERDADEIRO**
  **FALSO**   | VERDADEIRO  | **VERDADEIRO**
  **FALSO**   | **FALSO**   | **VERDADEIRO**

### Operador NÃO-OU (NOR)

![pórta lógica
NOR](/images/operadores-logicos/pórtas-lógicas-NOR.jpg "pórta lógica NOR"){.alignright}

O Operador “NÃO-OU” ou “NOR” é o contrário do operador OU (OR), ou seja,
resulta em VERDADEIRO, se os dois valores forem FALSO, na verdade este é
o operador OU (OR) seguido do operador NÃO (NOT). Abaixo a
**tabela-verdade** da operação NÃO-OU.

  **VALOR 1** | **VALOR 2** | **OPERAÇÃO NOR**
  ----------- | ----------- | ----------------
  VERDADEIRO  | VERDADEIRO  | FALSO
  VERDADEIRO  | FALSO       | FALSO
  FALSO       | VERDADEIRO  | FALSO
  **FALSO**   | **FALSO**   | **VERDADEIRO**

### Operador OU-EXCLUSIVO (XOR)

![porta lógica
XOR](/images/operadores-logicos/portas-lógicas-XOR.jpg "porta lógica XOR"){.alignright}

O Operador “OU-EXCLUSIVO” ou “XOR” é uma variação interessante do
operador OU (OR), ele resulta em VERDADEIRO se apenas um dos valores de
entrada for VERDADEIRO, ou seja, apenas se os valores de entrada forem
DIFERENTES. Abaixo a **tabela-verdade** da operação OU-EXCLUSIVO.

  **VALOR 1**    | **VALOR 2**    | **OPERAÇÃO XOR**
  -------------- | -------------- | ------------------
  VERDADEIRO     | VERDADEIRO     | FALSO
  **VERDADEIRO** | FALSO          | **VERDADEIRO**
  FALSO          | **VERDADEIRO** | **VERDADEIRO**
  FALSO          | FALSO          | FALSO

### Operador NÃO-OU-EXCLUSIVO (XNOR)

![porta lógica
XNOR](/images/operadores-logicos/portas-lógicas-XNOR.jpg "porta lógica XNOR"){.alignright}

O Operador “NÃO-OU-EXCLUSIVO” ou “XNOR” é o contrário do operador
OU-EXCLUSIVO (XOR), ou seja, resulta VERDADEIRO se os valores de entrada
forem IGUAIS. Observe a tabela abaixo:

  **VALOR 1**    | **VALOR 2**    | **OPERAÇÃO XNOR**
  -------------- | -------------- | -------------------
  **VERDADEIRO** | **VERDADEIRO** | **VERDADEIRO**
  VERDADEIRO     | FALSO          | FALSO
  FALSO          | VERDADEIRO     | FALSO
  **FALSO**      | **FALSO**      | **VERDADEIRO**

##Operadores lógicos nas linguagens de programação

Cada linguagem de programação tem uma forma de representar os operadores
lógicos. A simbologia mais encontrada são:

-   **AND**, **OR** e **NOT** em linguagens como: Pascal, Visual Basic
    e SQL.
-   **&&**, **||** e ! em linguagens como: Java  e C\#

Algumas linguagens oferecem operadores lógicos para o nível de bit
(também chamado de operadores bitwise). Ou seja, podemos fazer operações
lógicas com os bits de dois números. Em java, por exemplo esses
operadores são & e |. Veja o código abaixo escrito em java.

```java
public class TesteBitwise {
    public static void main (String []a){
        System.out.println("10 & 7 = " + (10 & 7));
        System.out.println("10 | 7 = " + (10 | 7));
    }
}
```

Abaixo o resultado deste programa.

![resultado
bitwise](/images/operadores-logicos/resultado-bitwise.png){.aligncenter}

Essas operações lógicas são realizadas com os bits dos números de
entrada. Assim:

> Convertemos o número 10 e o número 7 para binário.
>
> 10 = 1010 em binário
>
> 7 = 0111 em binário
>
> depois realizamos as operações lógicas com cada bit dos dois números.
>
> 10 & 7 = 0010 = 2
>
> 10 | 7 = 1111 = 15

##Conclusão

Conhecer esses operadores é muito importante para qualquer área
da tecnologia que você for trabalhar. Em
programação por exemplo, utilizamos esses operadores praticamente o
tempo todo, principalmente para controle de fluxo de execução e tomadas
de decisão. Se você chegou até aqui e não conseguiu entender direito o
que são os operadores lógicos, deixe um comentário aí em baixo parar
sanarmos as dúvidas.
