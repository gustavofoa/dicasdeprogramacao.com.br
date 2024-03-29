---
title: Como criar um arquivo CSV no Python
date: 2021-11-28
author: Marcelo Santos de Oliveira
category: : Dicas de Python :
tags: csv, criar arquivo csv
slug: como-criar-um-arquivo-csv-no-python
---

CSV é um tipo que arquivos onde os dados são separados por vígula, daí vem a sigla da extenção CSV(comma-separated values, valores separados por virgula na tradução).

Apesar de na programação existir outros tipos de arquivos que também são úteis para se trabalhar, como arquivos JSON ou XML, que já possuem funções em quase todas as linguagens para manipular esses tipos de dados, para um usuário que precisa baixar dados de um sistema esses tipos de arquivos podem acabar não sendo a melhor escolha quando é necessario colocar esses dados em suas planilhas feitas em excel, que é muito utilizado nas empresas.

Dessa forma o arquivo CSV se torna a melhor escolha para essa situação onde é necessário disponibilizar uma quantidade de dados para que o usuário baixe e coloque em planilhas.

Então vamos mostrar como podemos criar, ler e adicionar itens em um arquivo CSV com python.

O **python** já possui o módulo csv em suas bibliotecas *build-in*, dessa forma tudo que precisamos é importar o módulo no início do código.

```python
import csv
```

Agora já temos o módulo csv para usarmos mais a frente.

Vamos iniciar com o código onde criaremos o arquivo CSV, para isso iremos usar a função `open()` que é utilizada para abrir arquivos. Essa função pode receber alguns parâmetros, daremos atenção apenas nos necessários para atingirmos nosso objetivo.

Os parâmetros que vamos utilizar da função `open()` são: `file, mode`. File é o path do arquivo, ou seja, o caminho onde ele está ou será criado.O `mode` é o modo como o arquivo será aberto, os dois principais modos são 'r' para read(leitura) e 'w' para writer(escrita).

Antes de utilizarmos a função `open()` vamos colocar a palavra `with` que irá nos auxiliar fechando o arquivo depois da execução desta tarefa.

Dessa forma nosso código está dessa maneira:

```python
import csv
with open('./teste.csv, 'w') as csvfile:
```

Assim estamos abrindo o arquivo `teste.csv`, na raiz do script e atribuindo a ele uma variável `csvfile`, que vamos usar para manipular o arquivo.

Um detalhe a se observar é que se o arquivo não existir, ele será criado, pois o parâmetro de escrita ('w'), tanto abre um arquivo exitente, como cria o arquivo se ele não existir.

Agora vamos utilizar algumas funções que o modulo CSV nos disponibiliza, a função `writer()` e a função `writerow()`.

A primera está relacionada a configuração da forma como vamos compor o arquivo CSV, estamos configurando o nosso `writer`, ou seja, o nosso objeto **escritor**, que vai nos permitir escrever no arquivo que acabamos de criar e irá receber dois paramêtros a variável que aponta para o arquivo, no nosso caso ***csvfile*** e o **delimiter** que é o delimitador do arquivo, ou seja, que define o caracter que irá separar os dados no arquivo, nesse caso usaremos a vírgula. Nosso código está assim:

```python
import csv
with open('./teste.csv, 'w') as csvfile:
  csv.writer(csvfile, delimiter=',')
```

Então vamos a outra função que precisamos para conseguir escrever no arquivo CSV a `writerow()`, que é a função que escreve uma linha, essa função deve ser escrita na frente da `writer()` e é dentro dela que vamos escrever os dados, em forma de listas, ficando dessa forma:

```python
import csv
with open('./teste.csv, 'w') as csvfile:
    csv.writer(csvfile, delimiter=',').writerow(['João', '30' ])
    csv.writer(csvfile, delimiter=',').writerow(['José', '27'])
    csv.writer(csvfile, delimiter=',').writerow(['Pedro', '20'])
```

Pronto em nosso código já criamos o arquivo e escrevemos dados nesse arquivo.

![Dados no arquivo criado](/images/como-criar-um-arquivo-csv-no-python/dados-salvos-no-arquivo.png "Dados no arquivo que criamos"){:width=100%}

## Como ler um arquivo CSV em python

Então vamos ver agora como ler um arquivo CSV. É muito parecido com o processo que fizemos anteriormente para criar o arquivo,  porem com uma pequena mudança, o parâmetro que usamos anteriormente era 'w', porem agora vamos usar o 'r' de read, ou se preferir não precisa nem colocar o parâmetro pois a função open() por padrão já abre o arquivo em modo de leitura, então temos o seguinte:

```python
import csv
with open('./teste.csv) as csvfile:
```

E vamos utilizar a função `reader()` para ler o arquivo que criamos, porem com um detalhe, para termos uma saída estruturada em nosso terminal vamos usar um loop pra iteramos todas as linhas do arquivo, ficando dessa forma:

```python
import csv
with open('./teste.csv) as csvfile:
    for x in csv.reader(csvfile):
      print(x)
```

Assim teremos esta saída no terminal:

![Saida do terminal](/images/como-criar-um-arquivo-csv-no-python/saida-do-terminal.png "Saida do terminal"){:width=100%}

Pronto já criamos o arquivo e salvamos dados, agora o arquivo pode ser aberto em um editor de planilhas que estará separado de forma correta.

![Arquivo aberto editor de planilhas](/images/como-criar-um-arquivo-csv-no-python/arquivo-aberto-editor-planilhas.png "Arquivo aberto no editor de planilhas"){:width=100%}

## Melhorando nosso código

Até o momento com os passos anteriores já atingimos nosso objetivo, mas sempre podemos melhorar o nosso código. Certo?.

Vamos analizar alguns detalhes do código escrito. Quando escrevemos os dados no arquivo CSV, nós criamos o objeto "escritor", passamos para ele a variável
que aponta para o arquivo, configuramos o delimitador e depois escrevemos os dados. Tudo junto dessa forma:

```python
csv.writer(csvfile, delimiter=',').writerow(['João', '30' ])
csv.writer(csvfile, delimiter=',').writerow(['José', '27'])
csv.writer(csvfile, delimiter=',').writerow(['Pedro', '20'])
```

Notamos que em cada linha repetimos `csv.writer(csvfile, delimiter=',')`, isso faz com que em cada linha estamos criando este objeto, para 3 linhas de dados pode não fazer diferença,
mas quando estamos pensando em arquivos CVS, são arquivos que podem conter algumas centenas de dados, ou talvez milhares.

Dessa forma um arquivo irá criar centenas ou milhares de objetos. Isso irá consumir recursos de processamento, que se traduz em gastos, se criarmos algumas dezenas de arquivos por dia, porque não por hora, começamos a notar que isso pode crescer de forma a gerar gastos consideraveis.

 Pensando nisso, ao invés de executar a função que cria o objeto escritor milhares de vezes, vamos executar esta função apenas uma vez e armazenar em uma variável (chamada writer, por exemplo) o objeto que ela retorna.

Refatorando nosso código fica assim:

```python
import csv
with open('./teste.csv, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['João', '30' ])
    writer.writerow(['José', '27'])
    writer.writerow(['Pedro', '20'])
```

Seguindo essa linha de pensamento, também podemos melhorar nosso cógigo de escrita, passando o objeto de escrita que está sendo criado a cada iteração do loop `for` para uma variável e apenas usar no loop.

Ficando dessa forma:

```python
import csv
with open('./teste.csv) as csvfile:
    reader = csv.reader(csvfile)
    for x in reader:
      print(x)
```

Pronto! Agora temos nosso código otimimizado para criar arquivos CSVs e consumir menos de memória e processamento!

E aí, o que achou deste post? Gostou de aprender a trabalhar com arquivos CSVs no python?
Deixe aí nos comentários se este post foi útil pra você!
