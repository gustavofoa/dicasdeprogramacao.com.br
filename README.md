# { Dicas de Programação}

Blog com dicas para quem quer aprender desenvolvimento de softwares

## Dependências do projeto

É preciso ter o node e o python3 instalado na maquina para que seja possa rodar o sistema.

## Rodando o projeto

Após ter feito com clone do projeto com para a maquina local
com o comando `git clone git@github.com:gustavofoa/dicasdepython.com.br.git` 
será necessário instalar o gulp globalmente utilizando 
o comando `npm install -g gulp`.

Instalado o gulp globalmente acessa a pasta do projeto rode 
o comando `npm install` para ser instalado as dependências do node, 
crie uma virtualenv para rodar o sistema em python com 
o comando `python3 -m  venv venv`, 
ative a virtualenv como o comando `source venv/bin/activate`, 
agora instale as dependências do python 
usando `pip3 install -r requirements.txt`.

Após todas as dependências instaladas podemos rodar projeto com 
o comando `gulp serve` esse comando irá gerar os arquivos 
e subir um servidor no enderço **<http://localhost:1337>**

## Como criar um novo post

1. Crie um arquivo `.md` na pasta da categoria corresponde
dentro da pasta `/content/posts`.
2. Especifique o cabeçalho do post como no exemplo abaixo:

```
---
title: Primeiro programa em Javascript
date: '2018-08-01'
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Javascript }
tags: iniciante
image: /images/logo-javascript.png
slug: primeiro-programa-em-javascript
---
```

3. Na pasta `/content/images` crie uma pasta com o nome igual ao slug do post.
Exemplo `primeiro-programa-em-javascript`. Coloque todas as imagens do post nesta pasta
4. Crie uma imagem chamada `destaque.png` na pasta de imagens do post.
5. Execute o script para corte da imagem destaque. 
   1. Abra o terminal e entre na pasta `/content/images`
   2. Execute o programa cut_images.py passando o slug como argumento.
   Exemplo: `python cut_images.py primeiro-programa-em-javascript`
   3. Confirme que as imagens cortadas foram geradas na pasta.