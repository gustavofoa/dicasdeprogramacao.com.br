---
title: Como fazer uma requisicao HTTP GET com javascript puro
date: 2018-08-10
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante, request, http, javascript
slug: como-fazer-uma-requisicao-http-get-com-javascript-puro
---

Este post mostra como fazer uma requisição HTTP com javascript puro, ou seja sem usar frameworks como jQuery.
Para isso basta utilizar a API **XMLHttpRequest** nativa do javascript.

> Disponibilizei um arquivo texto para utilizarmos como exemplo no endereço:
<https://dicasdeprogramacao.com.br/images/como-fazer-uma-requisicao-http-get-com-javascript-puro/exemplo.txt>

O código abaixo mostra a forma mais simples, embora não indicada, de fazer uma requisição GET com javascript.

```javascript
var url = "https://dicasdeprogramacao.com.br/images/como-fazer-uma-requisicao-http-get-com-javascript-puro/exemplo.txt";//Sua URL

var xhttp = new XMLHttpRequest();
xhttp.open("GET", url, false);
xhttp.send();//A execução do script pára aqui até a requisição retornar do servidor

console.log(xhttp.responseText);
```

O código acima faz uma requisição **síncrona** (pois o terceiro parâmetro da função ```open``` é ```false```).
Ou seja, a execução do código pára no método ```send()``` enquanto a requisição não retorna do servidor.

**Importante!** O suporte à requisições síncronas com XMLHttpRequest será removido em versões futuras do javascript.
Por isso é mais **indicado fazer requisições assíncronas**! Embora esse processo de remoção possa demorar anos.

Com requisições assíncronas, o código continua sendo executado mesmo que o servidor não tenha respondido à requisição ainda.

O código abaixo mostra como fazer uma requisição HTTP **assíncrona** com ```XMLHttpRequest```.

```javascript
var url = "https://dicasdeprogramacao.com.br/images/como-fazer-uma-requisicao-http-get-com-javascript-puro/exemplo.txt";//Sua URL

var xhttp = new XMLHttpRequest();
xhttp.open("GET", url, true);

xhttp.onreadystatechange = function(){//Função a ser chamada quando a requisição retornar do servidor
    if ( xhttp.readyState == 4 && xhttp.status == 200 ) {//Verifica se o retorno do servidor deu certo
        console.log(xhttp.responseText);
    }
}

xhttp.send();//A execução do script CONTINUARÁ mesmo que a requisição não tenha retornado do servidor
```

Repare que a execução do código principal não vai parar agora que o terceiro parâmetro da função ```open``` é ```true```.

O retorno da requisição é recuperado pela função configurada no atributo ```onreadystatechange``` do seu objeto ```XMLHttpRequest```.

## Exemplo completo

O código abaixo mostra um exemplo completo de código javascript que implementa o exemplo acima, embutido em uma página HTML simples.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Exemplo de requisição HTTP GET com javascript puro</title>
</head>
<body>

    <input type="text" id="url" style="width:300px;" value="https://dicasdeprogramacao.com.br/images/como-fazer-uma-requisicao-http-get-com-javascript-puro/exemplo.txt">
    <button onclick="fazerRequisicao();">Fazer requisição</button>
    <hr />
    <div id="resposta"></div>
    
    <script>
        function fazerRequisicao(){

            var url = document.getElementById('url').value;

            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", url, false);
            
            xhttp.send();//A execução do script pára aqui até a requisição retornar do servidor

            document.getElementById("resposta").innerHTML = xhttp.responseText;
        }
    </script>
</body>
</html>
```

Veja abaixo o resultado deste código.

![execução de uma requisição http get com javascript puro](/images/como-fazer-uma-requisicao-http-get-com-javascript-puro/resultado.gif){:style="width:100%;padding:10px;"}

Qualquer dúvidas, fique a vontade para postar nos comentários.

## Referências

1. [Mozila: XMLHttpRequest](https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHTTPRequest){:target=\_blank}
2. [Código-fonte](https://github.com/gustavofoa/dicasdejavascript.com.br/tree/master/content/examples/exemplo-http-get-request/){:target=\_blank}
