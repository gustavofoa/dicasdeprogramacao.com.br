title: As 10 conversões numéricas mais utilizadas na computação
date: 2013-05-16
author: Gustavo Furtado de Oliveira Alves
category: Iniciante
slug: as-10-conversoes-numericas-mais-utilizadas-na-computacao

**Conversões numéricas** são utilizadas em muitos casos na computação.
Isso porque nós somos acostumados com a base numérica **decimal** (0, 1,
2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, ...), mas no mundo da tecnologia
digital os dispositivos eletrônicos trabalham em baixo nível com a base
numérica **binária** (0 ou 1), pois os números binários são facilmente
representados na eletrônica através de pulsos elétricos. Além desses
dois, as bases numéricas **octal** e **hexadecimal** também são muito
utilizadas pela fácil representação.

##Simbologia

A **base numérica** representa a quantidade de símbolos possíveis para
representar um determinado número. Veja a tabela abaixo, sobre quais
símbolos podem ser utilizados em cada sistema de numeração.

  **Base Numérica** | **Símbolos**
  ----------------- | ------------
  Decimal           | 0, 1, 2, 3, 4, 5, 6, 7, 8 e 9
  Binário           | 0 e 1
  Octal             | 0, 1, 2, 3, 4, 5, 6 e 7
  Hexadecimal       | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E e F

Olhando pra essa tabela é mais fácil perceber que, ao contarmos, quando
chegamos no último símbolo precisamos incrementar o número da esquerda
para representar o próximo. Por exemplo, ao contarmos na base
**decimal**, quando chegamos no 9, precisamos do símbolo 1 para formar o
próximo número 10. O mesmo vale para as outras bases numéricas. Por
exemplo, no **octal**, quando chegamos no 7, o próximo número é 10, ao
chegar no 17, o próximo é 20 e assim sucessivamente. No **binário**,
contamos assim: 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, ...
Deu pra entender a ideia?

##Representação de base numérica

Quando falamos de números da base **decimal** geralmente não
representamos explicitamente a base numérica, quando vemos um número
qualquer sem base numérica sub-entendemos ser um número da base decimal.
Mas para números de outras bases é necessário informar explicitamente a
base numérica do número. Esta é representada por um número sub-escrito
no final do número. Por exemplo:

-   1010001011<sub>2</sub>
-   453234<sub>8</sub>
-   23AF6D<sub>16</sub>
-   1024<sub>10</sub> (nesse caso, por ser base decimal, podemos representar ou o
    número sem a base, apenas **1024**)

Entendido isso, vamos ver agora como converter os números entre as bases
decimais.

##1ª Conversão numérica: Decimal para Binário

A conversão numérica de números **decimais** para números **binários** é
realizada através de divisões consecutivas. Como? Dividimos o número da
base decimal por 2 até que não seja mais divisível, ao final, o número
binário é o **resultado da última divisão <span
style="text-decoration: underline;">ajuntado</span> dos restos das
demais divisões "de baixo para cima"**. Bom, é melhor vemos um exemplo
pra ficar claro...

Vamos converter o número 34 para a base binária.

![conversao decimal para
binário](/images/as-10-conversoes-numericas-mais-utilizadas-na-computacao/conversao-decimal-para-binário.png){.aligncenter}

Fácil né!? Não se esqueça de utilizar o resultado da última divisão para
formar o número binário! Só pra confirmar que você aprendeu, leia
novamente a frase em negrito do parágrafo anterior.

##2ª Conversão Numérica: Decimal para Octal

A conversão numérica de **Decimal** para **Octal** é quase idêntica a
anterior, a diferença é que agora dividimos por 8. Veja o exemplo
abaixo, onde convertemos o número 2834 da base **decimal** para a base
**octal**:

![conversao decimal para
octal](/images/as-10-conversoes-numericas-mais-utilizadas-na-computacao/conversao-decimal-para-octal.png){.aligncenter}

##3ª Conversão Numérica: Decimal para Hexadecimal

Já dá pra imaginar como é a conversão de números **decimais** para a
base **hexadecimal**? Acertou! É a mesma coisa que a anterior, só que
agora dividimos por 16. Mas tem um pequeno detalhe, ao final não podemos
utilizar os números 10, 11, 12, 13, 14, e 15, no lugar desse números
utilizamos A, B, C, D, E e F. Veja o exemplo abaixo, onde convertemos o
número 2834 da base **decimal** para a base **hexa-decimal**:

![conversao decimal para
hexadecimal](/images/as-10-conversoes-numericas-mais-utilizadas-na-computacao/conversao-decimal-para-hexadecimal.png){.aligncenter}


Viu como é fácil? Não se esqueça de trocar os valores acima de 9 por
letras!

##4ª Conversão Numérica: Binário para Decimal

Agora vamos entrar na conversão de números <span
style="text-decoration: underline;">para</span> a base **decimal**, mas
vamos ver que após aprender uma forma, as outras são bem parecidas
também. A conversão de números **binários** para números **decimais** é
realizada através de uma somatória dos algarismos binários **da direita
pra a esquerda** onde cada termo da somatória é multiplicado por 2
elevado a um número sequencial iniciado em 0. Parece complicado, mas não
é. Você pode seguir uns passos simples como apresentado abaixo:

Vamos converter o número 100010<sub>2</sub> para a base **decimal**.

1.  Primeiro invertermos o número para fazermos a somatória **da direita
    para a esquerda do número original**.

    > **100010** -&gt; **010001**

2.  Agora vamos somar cada número, multiplicando por 2 elevado a um
    número sequencial iniciado em 0.

    > **0 \* 2 <sup>0</sup> + 1 \* 2 <sup>1</sup> + 0 \* 2 <sup>2</sup> + 0 \* 2 <sup>3</sup> + 0 \* 2 <sup>4</sup> + 1 \* 2 <sup>5</sup>**

3.  Podemos eliminar os termos que multiplicam por 0. Certo?

    > **<del>0 \* 2 <sup>0</sup></del> + 1 \* 2 <sup>1</sup> + <del>0 \* 2 <sup>2</sup></del> + <del>0 \* 2 <sup>3</sup></del> + <del>0 \* 2 <sup>4</sup></del> + 1 \* 2 <sup>5</sup>**
    >
    > Ficamos com ...
    >
    > **1 \* 2 <sup>1</sup> + 1 \* 2 <sup>5</sup>**

4.  Fazemos o cálculo do expoente e somamos.

    > **2 + 32**

5.  Resultado: **34**

Pode conferir com a <span
style="text-decoration: underline;">primeira</span> conversão deste
artigo...

##5ª Conversão Numérica: Octal para Decimal

A conversão de números da base **octal** para a base **decimal** é
semelhante a anterior, porém utilizamos 8 no lugar do número 2. Vamos
converter o número 5422<sub>8</sub> para a base **decimal** seguindo os mesmos
passos da conversão anterior.

1.  Primeiro invertermos o número para fazermos a somatória **da direita
    para a esquerda do número original**.

    > **5422** -&gt; **2245**

2.  Agora vamos somar cada número, multiplicando por 8 elevado a um
    número sequencial iniciado em 0.

    > **2 \* 8 <sup>0</sup> + 2 \* 8 <sup>1</sup> + 4 \* 8 <sup>2</sup> + 5 \* 8 <sup>3</sup>**

3.  Fazemos o cálculo do expoente e obtemos os termos da soma.

    > **2 \* 1 + 2 \* 8 + 4 \* 64 + 5 \* 512**
    >
    > Ficamos com ...
    >
    > ****2 + 16 + 256 + 2560**

4.  Resultado: **2834**

Pode conferir com a <span
style="text-decoration: underline;">segunda</span> conversão deste
artigo...

##6ª Conversão Numérica: Hexadecimal para Decimal

Adivinha! Mesma coisa que a anterior, só que agora utilizando 16, mas
lembre-se: é necessário substituir as letras A, B, C, D, E e F por 10,
11, 12, 13, 14 e 15. Vamos converter o número B12<sub>16</sub> para a
base **decimal** seguindo os mesmos passos da conversão anterior.

1.  Primeiro invertermos o número para fazermos a somatória **da direita
    para a esquerda do número original**.

    > **B12** -&gt; **21B**

2.  Agora vamos somar cada número, multiplicando por 16 elevado a um
    número sequencial iniciado em 0.

    > **2 \* 16 <sup>0</sup> + 1 \* 16 <sup>1</sup> + B \* 16 <sup>2</sup>**
    >
    > Substituimos B por 11, ficamos com ...
    >
    > **2 \* 16 <sup>0</sup> + 1 \* 16 <sup>1</sup> + 11 \* 16 <sup>2</sup>**

3.  Fazemos o cálculo do expoente e obtemos os termos da soma.

    > **2 \* 1 + 1 \* 16 + 11 \* 256**
    >
    > Ficamos com ...
    >
    > **2 + 16 + 2816**

4.  Resultado: **2834**

Pode conferir com a <span
style="text-decoration: underline;">terceira</span> conversão deste
artigo...

##7ª Conversão Numérica: Binário para Octal

A conversão de números da base **binária** para a base ** octal**, é
parecida com a conversão **binário-decimal**, mas antes é preciso
separar os dígitos binários **de 3 em 3 da direita para a esquerda**.
Vejamos um exemplo, vamos converter o número 10011011101<sub>2</sub> para
**octal**.

1.  Separamos os dígitos binários **de 3 em 3 da direita para a
    esquerda**.

    > **10 011 011 101**

2.  Agora fazemos a conversão **binário-decimal** para cada
    grupo separadamente. (Veja a 4ª conversão deste artigo)

    > **2 3 3 5**

3.  Unimos novamente os dígitos e temos o número na base **octal**.

    > **2335<sub>8</sub>**

##8ª Conversão Numérica: Binário para Hexadecimal

A conversão de números da base **binária** para a
base ** hexadecimal** é quase idêntica à anterior, só que agora
separamos os dígitos binários **de 4 em 4 da direita para a esquerda** e
antes de unir os dígitos ao final, trocamos os números 10, 11, 12, 13,
14 e 15 por A, B, C, D, E e F. Vejamos um exemplo, vamos converter o
número 10011011101<sub>2</sub> para **hexadecimal**.

1.  Separamos os dígitos binários **de 4 em 4 da direita para a
    esquerda**.

    > **100 1101 1101**

2.  Agora fazemos a conversão **binário-decimal** para cada
    grupo separadamente. (Veja a 4ª conversão deste artigo)

    > **4 13 13**

3.  Trocamos os números maiores que 9 por letra.

    > **4 D D**

4.  Unimos novamente os dígitos e temos o número na base
    **hexadecimal**.

    > **4DD<sub>16</sub>**

##9ª Conversão Numérica: Octal para Binário

Nessa conversão temos que pensar no contrário da conversão
**binário-octal**. Convertemos cada dígito do número **octal** para a
base **binária** separadamente. Vamos converter o número 2335<sub>8</sub> para a
base **binária**.

1.  Separamos os dígitos do número **octal**.

    > **2 3 3 5**

2.  Agora fazemos a conversão de cada dígito separadamente para binário
    como se fosse número da base **decimal**. (Veja a 1ª conversão deste
    artigo)

    > **010 011 011 101 **

3.  Unimos novamente os dígitos e temos o número na base **binária**
    (neste momento podemos eliminar os 0s a esquerda).

    > **10011011101<sub>2</sub>**

Pode conferir este resultado com a 7ª conversão.

##10ª Conversão Numérica: Hexadecimal para Binário

Da mesma forma que a anterior, nessa conversão temos que pensar no
contrário da conversão **binário-hexadecimal**. Convertemos cada dígito
do número **hexadecimal** para a base **binária** separadamente. Vamos
converter o número 4DD<sub>16</sub> para a base **binária**.

1.  Separamos os dígitos do número **hexadecimal**.

    > **4 D D**

2.  Convertemos as letras para número seguindo aquela ordem já
    mencionada.

    > **4 13 13**

3.  Agora fazemos a conversão de cada dígito separadamente para binário
    como se fosse número da base **decimal**. (Veja a 1ª conversão deste
    artigo)

    > **0100 1101 1101**

4.  Unimos novamente os dígitos e temos o número na
    base **binária** (neste momento podemos eliminar os 0s a esquerda).

    > **10011011101<sub>2</sub>**

Pode conferir este resultado com a 8ª conversão.

##Exercitar!

Como todo cálculo matemático, para aprender bem essas conversões
numéricas é preciso praticar, fazer bastante exercícios. Com o tempo só
de olhar para alguns números você já sabe como representá-lo em outras
bases numéricas. Então, pegue o lápis e um papel e comece a fazer
conversões. Não vou deixar exemplos de exercícios de conversão, basta
escolher um número aleatoriamente e convertê-lo para as outras bases.
Para conferir o resultado você pode utilizar a calculadora do seu
computador, basta colocá-la no modo "Programador" e alterar a base dos
números.

![calculadora modo
programador](/images/as-10-conversoes-numericas-mais-utilizadas-na-computacao/calculadora-modo-programador.png){.alignleft}

![base numérica na calculadora do
windows](/images/as-10-conversoes-numericas-mais-utilizadas-na-computacao/base-numérica-na-calculadora-do-windows.png){.alignleft}

 
