title: O que é JSON?
date: 2018-08-21
author: Gustavo Furtado de Oliveira Alves
category: Dicionário de programador
slug: o-que-e-json

Por ser um dos formatos mais utilizados para comunicação entre serviços web (webservices),
principalmente quando estamos falando de **APIs REST**, entender o que é e como funciona um JSON é primordial para qualquer pessoa que deseja trabalhar com desenvolvimento de softwares.
E neste post você vai aprender tudo que precisa saber para trabalhar com o famoso JSON.

Neste post você vai ver:

-   O que é JSON
-   Porque saber usar JSON é essencial para sua carreira
-   A Sintaxe básica do JSON
-   Os Tipos de dados do JSON
-   Como trabalar com JSON no Javascript
-   Como trabalar com JSON no Python
-   O que estudar depois de saber JSON

## O que é JSON

JSON é um formado de representação de dados baseado na linguagem de programação [Javascript](https://dicasdejavascript.com.br/), daí o nome _JavaScript Object Notation_.
Ou seja, _Notação de Objeto em Javascript_.

Vamos pensar no exemplo de um objeto _pessoa_ com nome **Pedro** e altura **1,90**.
A representação deste objeto em JSON ficaria assim:

```javascript
{
    "nome": "Pedro",
    "altura": 1.90
}
```

Este é um exemplo bem simples, mas neste post você vai ver que o JSON não vai muito além disso.

O mais importante que você precisa saber sobre o JSON é que ele é composto por **chave/valor** (ou no inglês _key/value_), as chaves representam os nomes dos atributos da classe e os valores, bem, são os valores do objeto.

No exemplo acima, temos as chaves _nome_ e _altura_ e os valores _Pedro_ e _1.90_, respectivamente.

## Porque saber usar JSON é essencial para sua carreira

Dificilmente se cria softwares que sejam isolados do mundo, sem comunicação com outros sistemas.
Seja em uma aplicação Web, Mobile, ou até mesmo Sistemas Embarcados,
quase sempre é necessário fazer um software se comunicar com outro.

Quem quer criar aplicações para usuários finais (aplicativos mobile, web, desktop, etc.) deve se preocupar com os formatos de dados e os protocolos de comunicação mais comuns para este fim. E neste contexto dois formatos de dados são os mais usados para comunicação na WEB. São eles: **XML** e **JSON**.

Para sistemas mais modernos o **JSON** é muito mais utilizado para comunicação do que o XML.
Por isso, se você pretende trabalhar com aplicações mobile e web, entender JSON é de extrema importância.

Mas pode ficar tranquilo que JSON é muito fácil de entender. Vamos começar pelo básico!

## A Sintaxe básica do JSON

A sintaxe de um JSON é bem simples como já adiantei anteriormente, mas agora vamos aprofundar um pouco mais.

Vejamos os elementos básicos do JSON.

1.  **`{` e `}`** - delimita um _objeto_.
2.  **`[` e `]`** - delimita um _array_.
3.  **`:`** - separa chaves (atributos) de valores.
4.  **`,`** - separa os atributos chave/valor.

Entendendo estes quatro elementos básicos você já será capaz de ler um JSON com mais facilidade.

A leitura simples de um JSON é que ele representa um objeto que tem atributos e cada atributo tem valores.

Os JSONs são estruturados em _objetos_ e/ou _arrays_ (ou listas).
Os objetos são representados por chaves `{ }` e os arrays são representados por colchetes `[ ]`.

Essa é a primeira coisa que você deve olhar no JSON: Onde estão as chaves e os colchetes?

Identificando estes dois tipos de estruturas voce já sabe se os dados serão acessados por chaves (quando for um objeto), ou por índices/números (quando for um array).

Além disso, tem algumas outras regras, nos **objetos** os atributos devem seguir de um caracter `:` (dois-pontos) e o valor do atributo. E os atributos devem ser separados por `,` vírgulas.

Já os **arrays** só podem ser de um determinado tipo de dados (veja a próxima sessão), não pode misturar texto com número, por exemplo.

//LINK POST DE VETORES E MATRIZES

Veja abaixo um exemplo de objeto e um exemplo de array.

```javascript
{
    "atributo1": "valor1",
    "atributo2": 2,
    "atributo3": true
}

[2,4,5,6]
```

Outro ponto interessante é que um _objeto_ JSON pode ter atributos do tipo _array_
e um _array_ pode ser do tipo _objeto_ ou _array_. Confuso? Veja o exemplo abaixo pra entender melhor.

```javascript

{
    "atritutoDoTipoArray" : [1,2,3,54]
}

[{
    "a":1
},{
    "b":1
]
```

Ah! Tanto array quando objeto podem ser vazios em JSON. Assim:

```javascript
{}
[]
```

## Os Tipos de dados do JSON

Além de _objeto_ e _array_ serem considerados os tipos de dados principais.
O JSON também tem os tipos de dados primitivos que nós já falamos aqui no { Dicas de Programação }.
//LINK

Os tipos de dados básicos do JSON são:

1. **string** - separados por aspas (duplas ou simples). Ex. "Brasil" ou 'Brasil'
2. **número** - sem aspas e pode ser inteiro ou real, quando for do tipo real deve-se usar o caractere `.` (ponto) para separar a parte inteira das casas decimais . Ex. `1` (inteiro) ou `23.454` (real)
3. **booleano** - tipo lógico normal, pode assumir valores `true` ou `false`.
4. **nulo** - este é o valor nulo mesmo. Ex. `{ "nome" : null }`

Veja abaixo um exemplo de objeto JSON com todos estes tipos de dados.

```javascript
{
    "texto" : "Brasil",
    "numero" : 23,
    "numeroReal" : 54.87,
    "booleano": true,
    "nulo": null
}
```

## Como trabalar com JSON no Javascript

## Como trabalar com JSON no Python

## O que estudar depois de saber JSON
