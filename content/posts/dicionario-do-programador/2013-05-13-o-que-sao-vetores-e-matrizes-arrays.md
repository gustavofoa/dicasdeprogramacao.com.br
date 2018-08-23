title: O que são Vetores e Matrizes (arrays)
date: 2013-05-13
author: Gustavo Furtado de Oliveira Alves
category: Dicionário de programador
slug: o-que-sao-vetores-e-matrizes-arrays

**Vetores** e **Matrizes** são estruturas de dados muito simples que
podem nos ajudar muito quando temos muitas variáveis do mesmo tipo em um
algoritmo. Imagine o seguinte problema: Você precisa criar um algoritmo
que lê o nome e as 4 notas de 50 alunos, calcular a média de cada aluno
e informar quais foram aprovados e quais foram reprovados.

Conseguiu imaginar quantas variáveis você vai precisar? Muitas né?
Vamos fazer uma conta rápida: 50 variáveis para armazenar os nomes dos alunos,
(4 \* 50 = ) 200 variáveis para armazenar as 4 notas de cada aluno e por fim,
50 variáveis para armazenar as médias de cada aluno. 300 variáveis no
total, sem contar a quantidade de linhas de código que você vai precisar
para ler todos os dados do usuário, calcular as médias e apresentar os
resultados. Mas eu tenho uma boa notícia pra você. Nós não precisamos
criar 300 variáveis! Podemos utilizar **Vetores** e **Matrizes** (também
conhecidos como **ARRAYs**)!

##O que são Vetores e Matrizes?

**Vetor** (**array** uni-dimensional) é uma variável que armazena várias
variáveis do mesmo tipo. No problema apresentado anteriormente, nós
podemos utilizar um <span
style="text-decoration: underline;">vetor</span> de 50 posições para
armazenar os nomes dos 50 alunos.

**Matriz** (**array** multi-dimensional) é um **vetor** de **vetores**.
No nosso problema, imagine uma matriz para armazenar as 4 notas de cada
um dos 50 alunos. Ou seja, um vetor de 50 posições, e em cada posição do
vetor, há outro vetor com 4 posições. Isso é uma matriz.

Cada item do vetor (ou matriz) é acessado por um número chamado de
**índice**.

Vamos representar os vetores e matrizes graficamente para facilitar o
entendimento do conceito.

![vetor e matriz
(array)](/images/o-que-sao-vetores-e-matrizes-arrays/vetor-e-matriz.png){.aligncenter}

Podemos ver na imagem acima que cada posição do vetor é identificado por
um número (chamado de índice), no caso da matriz são dois números (um na
vertical e um na horizontal).

##Vetores e Matrizes na prática!

Tomando o exemplo apresentado no início deste artigo, vamos implementar
o algoritmo utilizando o
[Visualg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank}.
Nele, vamos usar algumas estruturas básicas já apresentadas aqui, tais
como A [estrutura de repetição
PARA](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-para/ "Estrutura de repetição PARA"){:target=\_blank}
e a [estrutura de decisão
SE-ENTÃO-SENÃO](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de decisão SE-ENTÃO-SENÃO"){:target=\_blank}.
(Neste algoritmo vamos reduzir o número de alunos de 50 para 5, para
facilitar a visualização do resultado.)

[Saiba o que é o Visualg, como instalar e criar os seus primeiros
algoritmos!](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank}

**Preste muita atenção no modo como é criado o Vetor e a Matriz e também
a forma como é acessada cada posição.**

```
algoritmo "MediaDe5Alunos"
// Função : Calcular a média das notas de 10 alunos e apresentar quem foi aprovado ou reprovado
// Autor : Gustavo
// Seção de Declarações
var

   nomes: vetor [1..5] de caractere
   notas: vetor [1..5,1..4] de real
   medias: vetor [1..5] de real
   contadorLoop1, contadorLoop2: inteiro

inicio

      //Leitura dos nomes e as notas de cada aluno
      PARA contadorLoop1 DE 1 ATE 5 FACA
           ESCREVA("Digite o nome do aluno(a) número ", contadorLoop1, " de 5: ")
           LEIA(nomes[contadorLoop1])
           PARA contadorLoop2 DE 1 ATE 4 FACA
                ESCREVA("Digite a nota ", contadorLoop2, " do aluno(a) ", nomes[contadorLoop1], ": ")
                LEIA(notas[contadorLoop1, contadorLoop2])
           FIMPARA
           //CÁLCULO DAS MÉDIAS
           medias[contadorLoop1] := (notas[contadorLoop1, 1] + notas[contadorLoop1, 2] + notas[contadorLoop1, 3] + notas[contadorLoop1, 4]) / 4
      FIMPARA

      //APRESENTAÇÃO DOS RESULTADOS
      PARA contadorLoop1 DE 1 ATE 5 FACA
           SE medias[contadorLoop1] >= 6 ENTAO
              ESCREVAL("O aluno(a) ", nomes[contadorLoop1], " foi aprovado com as notas (", notas[contadorLoop1, 1], ", ", notas[contadorLoop1, 2], ", ", notas[contadorLoop1, 3], ", ", notas[contadorLoop1, 4], ") e média: ", medias[contadorLoop1])
           SENAO
              ESCREVAL("O aluno(a) ", nomes[contadorLoop1], " foi reprovado com as notas (", notas[contadorLoop1, 1], ", ", notas[contadorLoop1, 2], ", ", notas[contadorLoop1, 3], ", ", notas[contadorLoop1, 4], ") e média: ", medias[contadorLoop1])
           FIMSE
      FIMPARA

fimalgoritmo
```

Repare que os <span style="text-decoration: underline;">arrays</span>
(vetores ou matrizes) aliados a estrutura de repetição PARA é um ótimo
recurso para algoritmos que precisam de muitas variáveis do mesmo tipo.

Se você é iniciante em programação este algoritmo pode parecer complexo
para você, se houver dúvidas não se acanhe em deixar um comentário aí em
baixo que vamos te ajudar. Pra aprender programação (e qualquer outra
coisa) o mais importante é a força de vontade!

Um resultado do algoritmo acima pode ser observado a seguir:

> Digite o nome do aluno(a) número 1 de 5: Gustavo
>
> Digite a nota 1 do aluno(a) Gustavo: 9
>
> Digite a nota 2 do aluno(a) Gustavo: 10
>
> Digite a nota 3 do aluno(a) Gustavo: 9,5
>
> Digite a nota 4 do aluno(a) Gustavo: 8
>
> Digite o nome do aluno(a) número 2 de 5: João
>
> Digite a nota 1 do aluno(a) João: 5
>
> Digite a nota 2 do aluno(a) João: 6
>
> Digite a nota 3 do aluno(a) João: 4,5
>
> Digite a nota 4 do aluno(a) João: 7
>
> Digite o nome do aluno(a) número 3 de 5: Pedro
>
> Digite a nota 1 do aluno(a) Pedro: 7
>
> Digite a nota 2 do aluno(a) Pedro: 8,5
>
> Digite a nota 3 do aluno(a) Pedro: 6
>
> Digite a nota 4 do aluno(a) Pedro: 7
>
> Digite o nome do aluno(a) número 4 de 5: Luciana
>
> Digite a nota 1 do aluno(a) Luciana: 10
>
> Digite a nota 2 do aluno(a) Luciana: 7
>
> Digite a nota 3 do aluno(a) Luciana: 7,5
>
> Digite a nota 4 do aluno(a) Luciana: 8
>
> Digite o nome do aluno(a) número 5 de 5: Augusto
>
> Digite a nota 1 do aluno(a) Augusto: 5
>
> Digite a nota 2 do aluno(a) Augusto: 5,5
>
> Digite a nota 3 do aluno(a) Augusto: 7,5
>
> Digite a nota 4 do aluno(a) Augusto: 6
>
> O aluno(a) Gustavo foi aprovado com as notas ( 9, 10, 9.5, 8) e média:
> 9.125
>
> O aluno(a) João foi reprovado com as notas ( 5, 6, 4.5, 7) e média:
> 5.625
>
> O aluno(a) Pedro foi aprovado com as notas ( 7, 8.5, 6, 7) e média:
> 7.125
>
> O aluno(a) Luciana foi aprovado com as notas ( 10, 7, 7.5, 8) e média:
> 8.125
>
> O aluno(a) Augusto foi aprovado com as notas ( 5, 5.5, 7.5, 6) e
> média: 6
>
> \*\*\* Fim da execução.\
> \*\*\* Feche esta janela para retornar ao Visualg.

##Conclusão

Como você pode perceber nesse artigo, Vetores e Matrizes são, na
verdade, a mesma coisa: **array** a diferença é que o vetor é um array
de apenas 1 dimensão e a matriz é um array de 2 (ou mais) dimensões.

**Array** é uma das estruturas de dados mais simples que existe e uma
das mais utilizadas também. Acho que todas as linguagens de programação
têm **arrays**, pelo menos ainda não conheço uma linguagem que não tem.
Porém, os índices podem mudar dependendo da linguagem, algumas começam
os índices do array com 1 e outras com 0, essa é a grande diferença que
geralmente encontramos entre linguagens. No caso das linguagens que
começam os arrays com o índice 0, o último elemento do array recebe o
índice (&lt;tamanho do array&gt; - 1).

Gostou de conhecer os Arrays (Vetores e Matrizes)?

Recente mente eu criei um minicurso GRATUITO de lógica de programação
para ajudar quem está começando agora. Neste minicurso você receberá as
aulas por e-mail e terá bastante exercícios para resolver. Eu envio
minhas soluções para os exercícios por e-mail, assim você pode tentar
resolver sozinho e comprar a sua resposta com a minha. E caso não
consiga fazer sozinho, pode entender a minha solução que vai junto com
uma explicação detalhada.

**[&gt;&gt; CLIQUE AQUI e se inscreva no minicurso GRATUITO de lógica> de programação !](http://mclp.dicasdeprogramacao.com.br/)**

Um grande abraço!
