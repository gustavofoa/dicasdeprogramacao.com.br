---
title: NodeJs: Como ler variável de ambiente
date: 2018-08-23
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: process, nodejs
slug: nodejs-como-ler-variavel-de-ambiente
---

Ler uma variável de ambiente é muito simples com Javascript.
As variáveis de ambiente dos seu SO são carregadas como atributos do objeto `process.env`.

Ou seja, você só precisa adicionar ponto (.) e o nome da variável de ambiente.

Por exemplo, pra acessar o valor da variável de ambiente `OS` faça assim:

```javascript
process.env.OS
```

Uma outra forma é informando o nome da variável entre colchetes.

```javascript
process.env['OS']
```

## Exemplo de execução

![Como ler variável de ambiente com Javascript](/images/nodejs-como-ler-variavel-de-ambiente/ler-variavel-de-ambiente.gif){:style="width:100%;padding:10px;"}

Assim você pode consultar o valor de qualquer variável de ambiente do seu sistema operacional.

## Referência

1. [Doc: process.env](https://nodejs.org/dist/latest-v10.x/docs/api/process.html#process_process_env){:target=\_blank}
