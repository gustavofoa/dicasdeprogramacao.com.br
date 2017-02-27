Title: Absolutamente tudo que você precisa saber sobre TIPOS DE DADOS EM JAVA
Date: 2015-05-05 15:34
Author: gustavo.foa
Category: Java, Programação
Tags: java, tipos de dados
Slug: tudo-sobre-tipos-de-dados-em-java
Status: draft

<span style="color: #555555;">Entender como funcionam os tipos de
dados é obrigação de qualquer desenvolvedor para programar em qualquer
linguagem. Algumas linguagens de programação não requerem tipo de dados
para declarar variáveis, outras exigem que o tipo seja informado e há
também aquelas em que o tipo de dados é opcional. Os tipos de dados que
a linguagem oferece é uma informação muito importante a saber para tomar
boas decisões na hora de escrever códigos.</span>

<span style="color: #555555;">Java é uma linguagem fortemente
“</span>*tipada*<span style="color: #555555;">“, talvez você já tenha
ouvido essa frase em algum lugar (ou não). Ser fortemente
"*tipada*" significa que todas as variáveis que nós declaramos em java
TEM que ser de um tipo <span
style="text-decoration: underline;">explicitamente</span> declarado.
Para declarar uma variável em java, primeiro dizemos de que tipo ela é e
depois o nome dela, por exemplo:</span>

``` {.lang:java .decode:true}
int idade;
double altura;
String nome;
```

<span style="color: #555555;">Nas declarações de variáveis do exemplo
acima, *idade* é do tipo inteiro, isso significa que só podem ser
atribuídos valores inteiros a essa variável, caso contrário o compilador
java vai apontar um erro. Por exemplo o código abaixo não compila, pois
tentamos atribuir um valor decimal à variável idade que é do tipo
inteiro.</span>

``` {.lang:java .decode:true}
public class TesteTipoVariavel{
    public static void main(String a[]){
        int idade = 1.4;
    }
}
```

<span style="color: #555555;">Ao tentar compilar esse código, o
compilador retorna o seguinte erro:</span>

![erro de tipo de dados em
java](http://www.dicasdeprogramacao.com.br/wp-content/uploads/erro-tipoagem1.png){.aligncenter
.wp-image-1907 .size-full width="606" height="194"}

<span style="color: #555555;">Por ser uma linguagem fortemente
“</span>*tipada*<span style="color: #555555;">“, o compilador do Java
não aceita atribuição de valores de tipo diferente, como mostrado acima.
O mesmo acontece para os outros tipos, se tentarmos adicionar um valor
numérico em uma variável do tipo String também haverá erro de
compilação.</span>

Os 8 tipos de dados primitivos de Java
--------------------------------------

Já falei aqui no **{ Dicas de Programação }** sobre os [tipos de dados
básicos e os tipos de dados
customizados](http://www.dicasdeprogramacao.com.br/tipos-de-dados-primitivos/ "O que são tipos de dados primitivos?").
Existem 8 tipos de dados primitivos em java que são a base para a
criação de qualquer outro tipo de dado (arrays, classes e interfaces).
São chamados de primitivos porque são os tipos mais básicos da
linguagem. Vejamos as características de cada um deles:

### 1. boolean

É o tipo de dados utilizado para armazenar valores binários
(verdadeiro/falso, 1/0, ligado/desligado etc). Este tipo só aceita os
dois valores: true ou false. Exemplo:

``` {.lang:java .decode:true}
boolean lampadaAcesa = true;
boolean somLigado = false;
```

### 2. char

O char é usado para armazenar um único caractere. Se você deseja
armazenar vários caracteres sucessivos, use o tipo String, falaremos
sobre o String mais adiante.

Voltando ao char, este tipo de dados na verdade é um número positivo de
16 bits (valores entre **0** e **65.535**, ou **2^16^**-1), que é o
necessário para representar os caracteres de qualquer local do mundo,
utilizando os códigos
[Unicode](http://pt.wikipedia.org/wiki/Unicode "Unicode"). Por ser um
número, todos os [operadores
aritméticos](http://www.dicasdeprogramacao.com.br/operadores-aritmeticos/ "Você sabe usar os Operadores Aritméticos em programação?")
estão disponíveis para o char, mas se o objetivo é realizar cálculos, o
tipo de dados que deve ser usado é o *short*.

Em uma variável do tipo char, pode-se atribuir valores numéricos,
códigos unicode utilizando o prefíxo "\\u" e literais. Estes
dois último ficam entre aspas simples. Veja abaixo um código exemplo que
mostra diferentes formas de atribuir valores à uma variável do tipo
*char*.

``` {.lang:java .decode:true}
public class TestChar {
    public static void main(String args[]) {
        char a = 'a';//Valor literal 'a'
        char b = 98;//Código ASCII para a letra 'b'
        char c = '\u0063';//Código Unicode para a letra 'c'
        System.out.println("Valor da variável a: " + a);
        System.out.println("Valor da variável b (98): " + b);
        System.out.println("Valor da variável c (\\u0063): " + c);
    }
}
```

Veja o resultado da execução deste código.

![resultado atribuições
char](http://www.dicasdeprogramacao.com.br/wp-content/uploads/resultado-atribuições-char.png){.aligncenter
.wp-image-1914 .size-full width="357" height="192"}

É importante notar que não é possível atribuir valores negativos nem
valores acima de **65.535** a uma variável do tipo char. Isto causa um
**erro de compilação**. As seguintes atribuições NÃO compilam em java (a
não ser que haja uma conversão explícita).

``` {.lang:java .decode:true}
char e = -29;
char f = 70000;
```

###  3. int

Este é um tipo de dados inteiro de 32 bits que aceita valores negativos.

O intervalo de valores deste tipo vão de **-2.147.483.648** a
**2.147.483.647** (Ou -**2^32^** a **2^32^-1**).

Além de valores numéricos deste intervalo, também é possível atribuir
valores hexadecimais à variáveis inteiros colocando 0x no início. Isto
serve para qualquer tipo de dados numéricos (char, byte, short, long,
float e double), desde que seja obedecido o intervalo aceitável de cada
tipo.

**[Saiba como converter números hexadecimais em números
decimais](http://www.dicasdeprogramacao.com.br/as-10-conversoes-numericas-mais-utilizadas-na-computacao/ "As 10 conversões numéricas mais utilizadas na computação")**

Exemplos de atribuições de valores em variáveis do tipo *int*.

``` {.lang:java .decode:true}
int a = 23876;//OK
int b = 23 + 234;//OK
int c = 0x3A;//OK, no caso é o número 58 em decimal
int d = 3000000000;//Não compila! Valor acima de 2.147.483.647
```

Os tipos de dados *byte* e *short* têm as mesmas características
do *int*, a única diferença é o intervalo de números aceitáveis em cada
um.

### 4. byte

O *byte* é um tipo de dados inteiro de 8 bits que aceita valores
negativos.

O intervalo de valores deste tipo vão de **-128** a **127** (Ou
-**2^8^** a **2^8^-1**)

É possível atribuir qualquer valor inteiro deste intervalo à uma
variável do tipo *byte*.

``` {.lang:default .decode:true}
byte a = 34;      //OK aqui
byte b = -200;    //Não compila! Valor abaixo de -128
byte c = 128;     //Não compila! Valor acima de 127
```

### 5. short

O *short* é um tipo de dados inteiro de 16 bits que aceita valores
negativos.

O intervalo de valores deste tipo vão de **-32.768** a **32.767** (Ou
-**2^16^** a **2^16^-1**)

É possível atribuir qualquer valor inteiro deste intervalo à uma
variável do tipo *short*.

``` {.lang:default .decode:true}
short a = 1000;     //OK aqui
short b = -33000;   //Não compila! Valor abaixo de -32.768
short b = 33000;   //Não compila! Valor acima de 32.767
```

### 6. long

O *long* é um tipo de dados inteiro de 64 bits que aceita valores
negativos.

O intervalo de valores deste tipo vão
de **-9.223.372.036.854.775.808** a **9.223.372.036.854.775.807** (Ou
-**2^64^** a **2^64^-1**)

É possível atribuir qualquer valor inteiro deste intervalo à uma
variável do tipo *long*. Entretanto para valores que não cabem em uma
variável *int* é necessário acrescentar a letra "L" (maiúsculo ou
minúsculo) ao final do número, caso contrário acontecerá um erro de
compilação. Veja o exemplo.

``` {.lang:default .decode:true}
long a = 1000;     //OK aqui
long b = 1000000000000000000;   //Não compila! Valor que não cabe em uma variável int sem a letra "L" no final
long c = 1000000000000000000L;  //OK aqui
```

Quando se coloca a letra "L" no final do número, o valor é
automaticamente um número long, logo não é possível atribuí-lo em uma
variável do tipo *int* por exemplo (a não ser que haja uma conversão
explícita).

``` {.lang:default .decode:true}
int a = 10L;//Não compila, pois é um valor do tipo long
```

### 7. double

 

### 8. float

 

Classes: Tipos customizados
---------------------------

 

Bônus: A classe String
----------------------

 
