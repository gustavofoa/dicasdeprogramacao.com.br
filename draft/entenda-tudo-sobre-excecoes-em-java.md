Title: Entenda tudo sobre Exceções em Java
Date: 2016-05-10 09:58
Author: gustavo.foa
Category: Iniciante, Java
Slug: entenda-tudo-sobre-excecoes-em-java
Status: draft

O **tratamento de erros na linguagem Java** é uma daquelas
características da linguagem que gera amantes e odiadores. Sempre tem
aquela turma que dá uma lida rápida em como funcionam as exceções em
Java e sai lançando ou tratando Exception em todo método que pode dar
algum erro, já que **Exception** é a superclasse de todas as exceções.
Ou seja, na cabeça do sujeito ele fica "imune" de qualquer erro. Mal
sabe ele que está criando um problema muito maior que um simples
NullPointerException.

Neste post explico tudo sobre exceções em java, como acontece e como
resolver da forma correta.

``` {.lang:java .decode:true}
try {
 ...
} catch (Exception e) {
 ...
}
```

O código acima da uma sensação de que qualquer erro que acontecer na
execução do código será "resolvido". Mas se você faz esse tipo de coisa,
isso só mostra que você não entende todas as possibilidades de execução
do seu código. Isso significa que você é um mau programador.

Então deixo aqui um pedido: Não faça isso! Para o bem da sua carreira.
Ao invés de tratar Exception, entenda o que o seu código faz,
identifique os erros que podem acontecer e trate especificamente os
erros identificados.

Exceções
--------

Uma **exceção**, como o próprio nome diz, é uma situação que normalmente
não ocorre. Embora seja uma situação anormal, as exceções podem
acontecer. Por isso nós, como bons programadores que somos, precisamos
prever o seu acontecimento e saber agir para tratar e, se possível,
corrigir o problema.

Em java, as exceções são trabalhadas com recursos de orientação a
objetos e o modelo de abstração para as exceções classifica os erros da
seguinte forma.

-   Todas as classes que representam erros implementam a interface
    **Throwable**.
-   Os erros relativos a Hardware ou um erro do sistema operacional, são
    classes filhas da classe **Error** (que implementa Throwable). Nós
    não temos muito a fazer quando acontece um erro desses. Por
    exemplo, o erro OutOfMemoryError que acontece quando acaba a memória
    do computador.
-   Todos os outros erros são filhos da classe **Exception**.
-   Dentre os erros filhos de Exception há um grupo de erros que o
    compilador nos obriga a tratar. Estes são os erros filhos
    de RuntimeException.
-   Todos os erros que não herdam de Error ou de RuntimeException,
    precisam ser tratados (try-catch) ou lançados (throws), caso
    contrário o código não compila. Vamos falar disso mais abaixo.

A figura abaixo mostra a hierarquia das classes de Erro de java e um
exemplo dos tipos de erros possíveis.

![exceptions em
java](http://www.dicasdeprogramacao.com.br/wp-content/uploads/exceptions1.png){.aligncenter
.size-full .wp-image-2673 width="583" height="312"}

Tratamento de Exceções em Java
------------------------------

Conhecendo a hierarquia dos erros, agora você já sabe que todo erro que
não seja filho de **Error** ou **RuntimeException** precisa ser
resolvido por você. Mas como?

Basicamente você precisa conhecer três coisas: as palavras-chave
**throw** e **throws** e a estrutura ****try-catch-finally** **.

A diferença entre **throw** e **throws** é exatamente o que estas
palavras significam em inglês. Se você não sabe, ou pelo menos não
estuda inglês, comece já! Escrevi um post isto, vale a pena a leitura.

**&gt;&gt; Quer ser programador? Aprenda inglês!**

Primeiro vamos falar do **throw**, que significa "lançar" ou "jogar" em
inglês. Quando acontece um erro, em qualquer lugar, é esta palavra que é
usada para "lançar" o erro. Depois da palavra throw, é necessário
informar o objeto de erro que será lançada. Para isso você pode criar um
objeto de erro ou informar um objeto de erro já existente.

O erro é lançado assim:

``` {.lang:java .decode:true}
throw <objeto do erro>
```

O objeto pode ser criado na hora (com o *new*) ou ser acessado através
de uma variável.

``` {.lang:default .decode:true}
throw new IOException();
```

Lembrando que o objeto que será lançado dever ser instância de uma
classe que está em algum ponto da hierarquia que falamos anteriormente.
Ou seja, este objeto implementa *Throwable,* pode ser um *Error *ou
uma *Exception*, e também pode ser uma *RuntimeException*.

Simples assim, o *throw* serve só para lançar um erro. Mas o que eu
quero dizer com lançar o erro? Lançar o erro significa que você está
enviando este problema para quem chamou o método. Por exemplo, no código
abaixo o método m1() está lançando o erro para o método m2().

``` {.lang:java .decode:true}
void m1() {
 throw new Exception();
}

void m2() {
 m1();
}
```

E a palavra-chave **throws** serve pra quê? Lembra que eu disse que as
exceções filhas de *Exception*, que não sejam filhas de
*RuntimeException*, precisam ser resolvidas? O seu código java será
compilado com sucesso enquanto você não resolver essas exceções. Para
resolver uma exceção você pode fazer duas coisas. Tratá-la usando o
try-catch (já vou falar sobre ele) ou lançar essa exceção para  quem
chamou o método. É para isso que serve a palavra-chave **throws**.

**Inglês \~&gt; **Throws em inglês também significa lançar, mas
conjugado para a terceira pessoa do singular. Ele/ela **lança**.

Então significa que **o método ... "lança" tal exceção**.

Agora olhe para o código que escrevi acima. Ele não compila! Por que?
Você sabe? Olha o erro de compilação que acontece.

![Erro Exception não
tratada](http://www.dicasdeprogramacao.com.br/wp-content/uploads/Erro-Exception-não-tratada.png){.aligncenter
.size-full .wp-image-2677 width="500" height="155"}

Como eu estou lançando uma exceção **Exception** eu preciso resolver
essa exceção de alguma forma. Ela deve ser capturada (com *try-catch*)
ou lançada (com o throws) para o método que chamou o método que deu o
erro.

Vamos falar de Stack Trace
--------------------------

Este post não é para falar de tratamento de exceções. a **dica** acima
para os iniciantes de programação em Java.

, mas quero falar aos iniciantes em programação, especialmente em Java,
sobre aquele texto de fonte vermelha e tabulada que aparece no console e
dá um susto quando o pobre programador esperava um funcionamento bonito,
calmo e sereno do código que acabara de escrever. Isso, estou falando
do **Stack Trace Exception**!

Cá entre nós, eu sempre fiquei com pena do coitado do aluno iniciante
que esperava que o seu programinha funcionasse bunitinho, mas recebe o
tão angustiante erro na cara. Especialmente quando o malvado do
professor digita uma letra quando o programa esperava ler um número. É
comovente ver o semblante do aluno mudar de orgulho para decepção. Mas
faz parte do aprendizado, todo programador passa por isso,
principalmente os bons!

Voltemos ao **Stack Trace Exception**. O que, a princípio, dá um susto
pode se tornar o caminho para alcançar o caminho a luz no fim do tunel.
No Stack Trace Exception (ou pilha de exceções) está a notificação de um
problema, mas também está o que causou o problema, o nome da Classe, a
linha e a hierarquia das chamadas de métodos, deste o início da execução
do programa a té o ponto em que o erro aconteceu.
