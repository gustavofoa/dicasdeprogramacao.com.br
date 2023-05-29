---
title: Como criar uma classe em Javascript
date: 2019-09-06
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante
slug: como-criar-uma-classe-em-javascript
---

A partir da especificação ES2015, nós podemos criar uma classe em javascript de forma muito simples,
mais parecido com outras linguagens do paradigma de Orientação a Objetos,
utilizando a palavra-chave reservada `class`. Veja o exemplo abaixo:

```javascript
class Pessoa{

}
```

Para instanciar a classe usamos a palavra-chave `new`.

```javascript
let pessoa = new Pessoa();
```

## Atributos

Diferentemente de Java, C# e outras linguagens do paradigma OO,
em javascript precisamos especificar os atributos de uma classe dentro do seu construtor.
Veja o exemplo abaixo:

```javascript
class Pessoa{

    constructor(){
        this.nome = ''
    }
}
```

No exemplo acima a nossa classe `Pessoa` define o atributo `nome` que é inicializado com um texto vazio.

## Métodos

Métodos são "funções" que pertencem a uma classe.
E para declarar um método em javascript basta escrever o seu nome, sem a necessidade da palafra-chave `functions`. Veja o exemplo do método `calculaArea` da classe `Retangulo` abaixo.

```javascript
class Retangulo {
    constructor(altura, largura) {
      this.altura = altura;
      this.largura = largura;
    }

    calculaArea() {  
        return this.altura * this.largura;  
    }
}
```

Perceba também que estamos recebendo no construtor da classe, os valores iniciais dos atributos `altura` e `largura`.

Dá uma olhada na utilização desta classe no console do meu navegador.

![utilização de uma classe em javascript](/images/como-criar-uma-classe-em-javascript/classe-em-javascript.gif){:style="width:100%;padding:10px"}

Viu como é simples?

Qualquer dúvida fique à vontade para escrever aqui em baixo nos comentários!

## Referências

1. [Mozilla: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes){:target=\_blank}
2. [Especificação EcmaScript 6.0: Class Definitions](https://www.ecma-international.org/ecma-262/6.0/#sec-class-definitions){:target=\_blank}