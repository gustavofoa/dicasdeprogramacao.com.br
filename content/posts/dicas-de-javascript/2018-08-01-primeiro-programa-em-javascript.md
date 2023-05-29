---
title: Primeiro programa em Javascript
date: '2018-08-01'
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante
image: /images/logo-javascript.png
slug: primeiro-programa-em-javascript
---

A forma mais simples de criar um programa com javascript é através de páginas HTML.
Isso porque os browsers interpretam javascript nativamente.

Isso significa que você não precisa instalar nada em seu computador para rodar um programa 
escrito javascript, basta ter um browser.

Vejamos então como criar o seu primeiro código javascript com HTML.

crie um arquivo com a extensão `.html`, por exemplo `hello-world.html`
e escreva o conteúdo abaixo nele. Para isso abra o arquivo em algum editor de texto.

```html
<html>
  <head>
    <title>Título</title>
  </head>
  <body>
  <script type="text/javascript">
    alert('Meu primeiro programa javascript.');
  </script>
  </body>
</html>
```

Ao executar o arquivo (dois cliques), a página HTML será carregada em um browser,
o código javascript que está dentro da tag `<script>` será executado,
apresando a mensagem na tela.

Se tiver alguma dúvida, poste aí nos comentários.