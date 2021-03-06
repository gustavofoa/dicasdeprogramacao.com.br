title: Estrutura de repetição PARA
date: 2013-04-29
author: Gustavo Furtado de Oliveira Alves
category: Iniciante em programação
slug: estrutura-de-repeticao-para

Já precisou implementar um LOOP com número de iterações pré-definido?
(<span style="text-decoration: underline;">iteração</span> é cada vez
que as instruções do bloco do loop são executadas) Por exemplo, um
[algoritmo](http://www.dicasdeprogramacao.com.br/o-que-e-algoritmo/ "O que é Algoritmo?"){:target=\_blank}
que realiza a soma dos números de 1 a 100, terá um número de iterações
pré-definido (100).

Podemos implementar esse LOOP com qualquer estrutura
de repetição (saiba mais sobre as
estruturas [ENQUANTO](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto "Estrutura de repetição ENQUANTO"){:target=\_blank}
e
[REPITA-ATÉ](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-repita-ate "Estrutura de repetição REPITA-ATÉ"){:target=\_blank}),
mas para isso é necessário utilizar um contador, uma
[variável](http://www.dicasdeprogramacao.com.br/o-que-e-variavel-e-constante/ "O que é variável e constante?"){:target=\_blank}
que será utilizada para contar quantas iterações foram executadas até o
momento (o algoritmo de multiplicação utilizado [no artigo sobre
algoritmos](http://www.dicasdeprogramacao.com.br/o-que-e-algoritmo/ "O que é Algoritmo?"){:target=\_blank} implementa
um contador com a estrutura de repetição
[ENQUANTO](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto "Estrutura de repetição ENQUANTO"){:target=\_blank}). A
estrutura de repetição PARA, implementa um contador implicitamente. Veja
como é o seu esquema.

>**PARA** &lt;variável contadora&gt; **DE** &lt;valor inicial&gt; **ATE**
&lt;valor final&gt; \[**PASSO** &lt;valor de incremento&gt;\] **FAÇA**
>
>&lt;instruções a serem executadas repetidamente até a &lt;variável
contadora&gt; atingir o valor final&gt;
>
>**FIM**-PARA

O passo de incremento é opcional, esse recurso serve pera definir qual o
valor do incremento do contador, por exemplo de 1 em 1 (padrão), de 2 em
2, de 3 em 3, etc. Essa estrutura de repetição realiza o incremento de
um contator de forma implícita, vejamos graficamente como funciona.

![estrutura-PARA](/images/estrutura-de-repeticao-para/estrutura-PARA.png){.aligncenter}

A <span style="text-decoration: underline;">inicialização</span> da
variável contadora é realizada implicitamente, com o &lt;valor
inicial&gt; informado da declaração da estrutura PARA. A <span
style="text-decoration: underline;">condição</span> para executar a
iteração é que o valor da variável contadora não tenha atingido o
&lt;valor final&gt;. E ao final de cada iteração, o valor da variável
contadora é <span
style="text-decoration: underline;">incrementado</span> em 1 (ou o valor
declarado como PASSO ou &lt;valor de incremento&gt;).

##Estrutura PARA na prática!

Vamos implementar como exemplo um algoritmo para calcular o fatorial de
um número. Para quem não sabe, fatorial é a multiplicação de todos os
números de 1 até ao número que se está calculando. Por exemplo: Fatorial
de 5 (5!) = 1 \* 2 \* 3 \* 4 \* 5 = 120. Vamos criar um algoritmo
utilizando o ENQUANTO primeiro.

```
algoritmo "FatorialComENQUANTO"

var
   numero : INTEIRO
   fatorial : INTEIRO
   contador : INTEIRO
inicio

      ESCREVA ("Digite o número para calcular o fatorial: ")
      LEIA (numero)

      fatorial := 1
      contador := 1
      ENQUANTO contador <= numero FACA
          fatorial := fatorial * contador
          contador := contador + 1
      FIMENQUANTO

      ESCREVA ("O fatorial de ", numero, " é : ", fatorial)

fimalgoritmo
```

Veja que foi necessário incrementar o contador explicitamente (linha
16). Com a estrutura de repetição PARA, isso não é necessário. Vejamos
agora o mesmo algoritmo implementado com o PARA.

```
algoritmo "FatorialComPARA"

var
   numero : INTEIRO
   fatorial : INTEIRO
   contador : INTEIRO
inicio

      ESCREVA ("Digite o número para calcular o fatorial: ")
      LEIA (numero)

      fatorial := 1
      PARA contador DE 1 ATE numero FACA
          fatorial := fatorial * contador
      FIMPARA

      ESCREVA ("O fatorial de ", numero, " é : ", fatorial)

fimalgoritmo
```

Nesta estrutura, não é necessário incrementar nem inicializar o
contador, isso é feito automaticamente. O resultado dos dois algoritmos
é o mesmo.

![Resultado
Fatorial](/images/estrutura-de-repeticao-para/Resultado-Fatorial.png){.aligncenter}

LOOPs podem ser implementados com qualquer estrutura de repetição,
porém, em alguns casos uma estrutura se mostra mais adequada que outras,
como nesse caso do fatorial a mais adequada é a estrutura PARA. Conhecer
essas estruturas de repetição é muito importante para criar programas
melhores. Conheça as estruturas de
repetição [ENQUANTO](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto "Estrutura de repetição ENQUANTO"){:target=\_blank} e [REPITA-ATÉ](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-repita-ate "Estrutura de repetição REPITA-ATÉ"){:target=\_blank}.
