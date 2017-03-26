title: Algoritmo para Validar CPF
date: 2015-01-19
author: Gustavo Furtado de Oliveira Alves
category: Iniciante
slug: algoritmo-para-validar-cpf

Quando se está trabalhando em um sistema corporativo, é comum a
necessidade de validar CPF. Muita gente não sabe que um CPF para ser
válido não basta apenas atender à máscara
**"\#\#\#.\#\#\#.\#\#\#-\#\#"** (o caractere '\#' representa um número),
existe uma regra matemática que também deve ser verificada para um CPF
ser considerado válido. Se você acha que é complicado verificar se um
CPF é válido ou não, você vai se surpreender!

![exemplo de
CPF](http://www.dicasdeprogramacao.com.br/wp-content/uploads/cpf-exemplo.jpg){.aligncenter}

##Regra para validar CPF

O cálculo para validar um CPF é especificado pelo [Ministério da
Fazenda](http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/consultapublica.asp "Consulta para validação de CPF"){:target=\_blank}, que
disponibiliza no próprio site as
[funções](http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/funcoes.js "Funções para validação de CPF"){:target=\_blank}
(em javascript) para validação de CPF. Vamos entender como funciona.

O CPF é formado por 11 dígitos numéricos que seguem a máscara
"\#\#\#.\#\#\#.\#\#\#-\#\#", a verificação do CPF acontece utilizando os
9 primeiros dígitos e, com um cálculo simples, verificando se o
resultado corresponde aos dois últimos dígitos (depois do sinal "-").

> Vamos usar como exemplo, um CPF fictício "529.982.247-25".

### Validação do primeiro dígito

Primeiramente multiplica-se os 9 primeiros dígitos pela sequência
decrescente de números de 10 à 2 e soma os resultados. Assim:

> 5 \* **10** + 2 \* **9** + 9 \* **8** + 9 \* **7** + 8 \* **6** + 2 \*
> **5** + 2 \* **4** + 4 \* **3** + 7 \* **2**

O resultado do nosso exemplo é:

> **295**

O próximo passo da verificação também é simples, basta multiplicarmos
esse resultado por 10 e dividirmos por 11.

> 295 \* **10** / **11**

O resultado que nos interessa na verdade é o RESTO da divisão. Se ele
for igual ao **primeiro dígito verificador** (primeiro dígito depois do
'-'), a primeira parte da validação está correta.

**Observação Importante:** Se o resto da divisão for igual a 10, nós o
consideramos como 0.

Vamos conferir o primeiro dígito verificador do nosso exemplo:

> O resultado da divisão acima é '268' e o RESTO é **2**

Isso significa que o nosso CPF exemplo passou na validação do primeiro
dígito.

### Validação do segundo dígito

A validação do segundo dígito é semelhante à primeira, porém vamos
considerar os 9 primeiros dígitos, mais o primeiro dígito verificador, e
vamos multiplicar esses 10 números pela sequencia decrescente de 11 a 2.
Vejamos:

> 5 \* **11** + 2 \* **10** + 9 \* **9** + 9 \* **8** + 8 \* **7** + 2
> \* **6** + 2 \* **5** + 4 \* **4** + 7 \* **3** + 2 \* **2**

O resultado é:

> **347**

Seguindo o mesmo processo da primeira verificação, multiplicamos por 10
e dividimos por 11.

> 347 \* **10** / **11**

Verificando o RESTO, como fizemos anteriormente, temos:

> O resultado da divisão é '315' e o RESTO é **5**

Verificamos, se o resto corresponde ao segundo dígito verificador.

Com essa verificação, constatamos que o CPF 529.982.247-25 é válido.

##CPFs inválidos conhecidos

Existe alguns casos de CPFs que passam nessa validação que expliquei,
mas que ainda são inválidos. É os caso dos CPFs com dígitos repetidos
(111.111.111-11, 222.222.222-22, ...)

Esses CPF atendem à validação, mas ainda são considerados inválidos.

No nosso algoritmo, vamos verificar se todos os dígitos do CPF são
iguais e, neste caso, considerar que ele é inválido.

##Algoritmo para validar CPF

Agora que já aprendemos como acontece a validação de um CPF, vamos ver
como ficaria um algoritmo para validar CPF. Vamos escrever o algoritmo
em Portugal utilizando o
[Visualg](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank}.

No algoritmo abaixo, eu criei uma função chamada
**validaCPF(cpf:CARACTER)** que retorna **verdadeiro** ou **falso** se o
CPF for ou não válido.

Se você não sabe o que é uma função, [leia este
artigo](http://www.dicasdeprogramacao.com.br/o-que-sao-funcoes-e-procedimentos/ "O que são Funções e Procedimentos?"){:target=\_blank}.

```
algoritmo "Validação de CPF"

funcao validaCPF(cpf:CARACTER) : LOGICO
var
   num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, soma1, soma2 : inteiro
   resto1, resto2 : REAL
inicio

      //extrai os dígitos do CPF
      num1 := Caracpnum( Copia(cpf, 1, 1) )
      num2 := Caracpnum( Copia(cpf, 2, 1) )
      num3 := Caracpnum( Copia(cpf, 3, 1) )
      num4 := Caracpnum( Copia(cpf, 5, 1) )
      num5 := Caracpnum( Copia(cpf, 6, 1) )
      num6 := Caracpnum( Copia(cpf, 7, 1) )
      num7 := Caracpnum( Copia(cpf, 9, 1) )
      num8 := Caracpnum( Copia(cpf, 10, 1) )
      num9 := Caracpnum( Copia(cpf, 11, 1) )
      num10 := Caracpnum( Copia(cpf, 13, 1) )
      num11 := Caracpnum( Copia(cpf, 14, 1) )

      //Validação dos CPFs inválidos conhecidos
      SE (num1 = num2) E (num2 = num3) E (num3 = num4) E (num4 = num5) E (num5 = num6) E (num6 = num7) E (num7 = num8) E (num8 = num9) E (num9 = num10) E (num10 = num11) ENTAO
         RETORNE FALSO
      SENAO

         soma1 := num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2

         resto1 := (soma1 * 10) mod 11

         SE resto1 = 10 ENTAO
             resto1 := 0
         FIMSE

         soma2 := num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 + num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + num10 * 2

         resto2 := (soma2 * 10) mod 11

         SE resto2 = 10 ENTAO
             resto2 := 0
         FIMSE

         SE ( resto1 = num10) E (resto2 = num11) ENTAO
            RETORNE VERDADEIRO
         SENAO
            RETORNE FALSO
         FIMSE

      FIMSE

fimfuncao

var
   cpf : CARACTER
inicio

      //Verificação de um CPF inválido
      cpf := "123.456.789-12"
      SE validaCPF(cpf) = VERDADEIRO ENTAO
         ESCREVAL("O CPF ", cpf, " é válido!")
      SENAO
         ESCREVAL("O CPF ", cpf, " é inválido!")
      FIMSE

      //Verificação de um CPF válido
      cpf := "529.982.247-25"
      SE validaCPF(cpf) = VERDADEIRO ENTAO
         ESCREVAL("O CPF ", cpf, " é válido!")
      SENAO
         ESCREVAL("O CPF ", cpf, " é inválido!")
      FIMSE

      //Verificação de CPF com dígitos iguais
      cpf := "777.777.777-77"
      SE validaCPF(cpf) = VERDADEIRO ENTAO
         ESCREVAL("O CPF ", cpf, " é válido!")
      SENAO
         ESCREVAL("O CPF ", cpf, " é inválido!")
      FIMSE

fimalgoritmo
```

Perceba que testamosa nossa função com três CPFs, um inválido e outro
válido e um inválido conhecido. O resultado da execução deste algoritmo
é esse.

```
O CPF 123.456.789-12 é inválido!
O CPF 529.982.247-25 é válido!
O CPF 777.777.777-77 é inválido!
```

Também utilizei algumas funções pré-definidas pelo Visualg para extrair
cada caracter da variável *cpf* e para convertê-los em números inteiros.
As funções que utilizei foram:

-   **Caracpnum (c : caracter): inteiro**
    -   Esta função serve para converter um valor do tipo texto em um
        valor do tipo inteiro
-   **Copia (c : caracter ; p, n : inteiro): caracter**
    -   Esta função serve para extrair sub-textos de variáveis texto.
    -   Ela recebe três parâmetros, o primeiro é o texto de onde vamos
        extrair o sub-texto, o segundo é a posição de inicio do
        sub-texto e o terceiro parâmetro é a quantidade de caracteres
        que vamos extrair.

No nosso caso, nós extraímos os dígitos do cpf através da função
**copia** e convertemos o resultado desta função em inteiro através da
função **caracpnum**.

Por exemplo, para o cpf *"529.982.247-25"* a linha abaixo atribui o
valor inteiro 8 à variável num5, pois este é o caracter da posição 6
(contando o caracter ponto ".").

```
num5 := Caracpnum( Copia(cpf, 6, 1) )
```

Outro detalhe interessante é o operador *mod* que retorna o resto da
divisão.

Claro que pode-se implementar de outras formas,
com [Vetores](http://www.dicasdeprogramacao.com.br/o-que-sao-vetores-e-matrizes-arrays/ "O que são Vetores e Matrizes (arrays)"){:target=\_blank},
[LOOPs](http://www.dicasdeprogramacao.com.br/estrutura-de-repeticao-enquanto/ "Estrutura de repetição ENQUANTO"){:target=\_blank},
etc. Entretanto eu tentei implementar de uma forma mais simples de
entender a regra.

Se quiser entender cada recurso utilizado neste algoritmo leia os
artigos abaixo.

**[Estrutura de decisão
SE-ENTAO-SENAO](http://www.dicasdeprogramacao.com.br/estrutura-de-decisao-se-entao-senao/ "Estrutura de decisão SE-ENTÃO-SENÃO"){:target=\_blank}**

**[O que são Funções e
Procedimentos?](http://www.dicasdeprogramacao.com.br/o-que-sao-funcoes-e-procedimentos/ "O que são Funções e Procedimentos?"){:target=\_blank}**

**[Você sabe usar os Operadores Aritméticos em
programação?](http://www.dicasdeprogramacao.com.br/operadores-aritmeticos/ "Você sabe usar os Operadores Aritméticos em programação?"){:target=\_blank}**

**[Conheça os Operadores Relacionais!
](http://www.dicasdeprogramacao.com.br/operadores-relacionais/ "Conheça os Operadores Relacionais!"){:target=\_blank}**

**[O
que são tipos de dados primitivos?
](http://www.dicasdeprogramacao.com.br/tipos-de-dados-primitivos/ "O que são tipos de dados primitivos?"){:target=\_blank}**

**[Quer
aprender programação? Saiba qual a melhor
linguagem!](http://www.dicasdeprogramacao.com.br/linguagem-de-programacao-para-iniciantes/ "Quer aprender programação? Saiba qual a melhor linguagem!"){:target=\_blank}**

Entendendo como funciona o algoritmo, você torna-se capaz de validar CPF
em qualquer linguagem.
