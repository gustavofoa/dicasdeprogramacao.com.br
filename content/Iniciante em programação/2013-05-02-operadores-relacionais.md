title: Conheça os Operadores Relacionais!
date: 2013-05-02
author: Gustavo Furtado de Oliveira Alves
category: Iniciante em programação
slug: operadores-relacionais

Operadores relacionais são utilizados para comparar valores, o resultado
de uma expressão relacional é um valor
[booleano](http://www.dicasdeprogramacao.com.br/tipos-de-dados-primitivos/ "Conheça os tipos de dados básicos em programação!"){:target=\_blank} (VERDADEIRO
ou FALSO). Os operadores relacionais são: **igual**, **diferente**,
**maior**, **menor**, **maior ou igual**, **menor ou igual**. Não é
necessário explicar cada um, pois eles são auto-explicativos. Mas para
quem é iniciante em desenvolvimento de softwares algumas informações
podem ser importantes, principalmente pelo fato de haver diferença entre
linguagens de
programação.
![Operadores-relacionais](/images/operadores-relacionais/Operadores-relacionais.jpg){.aligncenter}

Os operadores relacionais são diferente dependendo da linguagem de
programação, mas conhecendo os símbolos mais comuns, a maioria da
linguagens de programação fica mais fácil aprender. No
[VisuAlg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank},
os símbolos dos operadores relacionais são: =, &lt;&gt;, &gt;, &lt;,
&gt;=, &lt;=. Vamos testar esses operadores no
[Visualg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank}
com
o algoritmo abaixo.

```
algoritmo "TesteOperadoresRelacionais"
var
  numero1 : INTEIRO
  numero2 : INTEIRO
  resultado : LOGICO
inicio

      numero1 := 5
      numero2 := 3
      resultado := numero1 = numero2
      ESCREVAL (numero1, " =  ", numero2, "? ", resultado)
      resultado := numero1 <> numero2
      ESCREVAL (numero1, " <> ", numero2, "? ", resultado)
      resultado := numero1 > numero2
      ESCREVAL (numero1, " >  ", numero2, "? ", resultado)
      resultado := numero1 < numero2
      ESCREVAL (numero1, " <  ", numero2, "? ", resultado)
      resultado := numero1 >= numero2
      ESCREVAL (numero1, " >= ", numero2, "? ", resultado)
      resultado := numero1 <= numero2
      ESCREVAL (numero1, " <= ", numero2, "? ", resultado)

      numero1 := 5
      numero2 := 5
      resultado := numero1 = numero2
      ESCREVAL (numero1, " =  ", numero2, "? ", resultado)
      resultado := numero1 <> numero2
      ESCREVAL (numero1, " <> ", numero2, "? ", resultado)
      resultado := numero1 > numero2
      ESCREVAL (numero1, " >  ", numero2, "? ", resultado)
      resultado := numero1 < numero2
      ESCREVAL (numero1, " <  ", numero2, "? ", resultado)
      resultado := numero1 >= numero2
      ESCREVAL (numero1, " >= ", numero2, "? ", resultado)
      resultado := numero1 <= numero2
      ESCREVAL (numero1, " <= ", numero2, "? ", resultado)

      numero1 := 5
      numero2 := 8
      resultado := numero1 = numero2
      ESCREVAL (numero1, " =  ", numero2, "? ", resultado)
      resultado := numero1 <> numero2
      ESCREVAL (numero1, " <> ", numero2, "? ", resultado)
      resultado := numero1 > numero2
      ESCREVAL (numero1, " >  ", numero2, "? ", resultado)
      resultado := numero1 < numero2
      ESCREVAL (numero1, " <  ", numero2, "? ", resultado)
      resultado := numero1 >= numero2
      ESCREVAL (numero1, " >= ", numero2, "? ", resultado)
      resultado := numero1 <= numero2
      ESCREVAL (numero1, " <= ", numero2, "? ", resultado)

fimalgoritmo
```

Algoritmo grande né? Como exercício pense em uma forma melhor de fazer
esse algoritmo. A intenção é mostrar o funcionamento dos operadores
relacionais com 3 possibilidades de valores: um número menor que o
outro, dois números iguais e um número maior que outro. Abaixo o
resultado da execução.

![resultado operadores
relacionais](/images/operadores-relacionais/resultado-operadores-relacionais.png){.aligncenter}

##Operadores Relacionais e linguagens de programação

Em todas as linguagens de programação existem símbolos para executarmos
essas operações. As operações **maior**, **menor**, **maior ou
igual** e **menor ou igual** na maioria das linguagens de programação
são os mesmos símbolos (até hoje não encontrei uma linguagem que tenha
símbolo diferente para estes
operadores): **&gt;** (maior), **&lt;** (menor), **&gt;=** (maior ou
igual) e **&lt;=**(menor ou igual). Mas os vilões dos iniciantes são os
símbolos para testar igualdade e diferença. Em cada linguagem é de um
jeito! Em java, C, C\#, javascript, etc. Por exemplo,
os símbolos de igual e diferente são: **==** e **!=**. Já em Pascal,
SQL, Visual Basic, ... os símbolos de igual e diferente
são: **=** e **&lt;&gt;**. Então fique esperto quando for aprender
alguma dessas linguagens!

Em java, não é possível testar Strings com o operador de igualdade
(**==**), pois String é uma classe e não um tipo primitivo, e para
testar a igualdade entre objetos deve-se utilizar o método equals.
Assim: nome.equals(“João”).

Em algumas linguagens de [](){#spiderWordFound3}programação (Python por
exemplo) é possível utilizar os operadores **maior **e **menor** para
verificar a precedência alfabética de um [](){#spiderWordFound4}texto em
relação a outro. Por exemplo: ”Pedro” &lt; “Paulo” resulta em **FALSO**,
pois o texto “Pedro” alfabeticamente aparece depois do texto “Paulo”.

##Conclusão

Os operadores relacionais são muito utilizados em programação, as
decisões dos algoritmos geralmente são tomadas nas operações
relacionais, ou seja, as decisões baseiam-se em testes do estado das
variáveis. Então é muito importante entender o que é uma operação
relacional e quais os operadores utilizados nesse tipo de expressão.
