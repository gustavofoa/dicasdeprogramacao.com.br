title: 5 funções curingas em PHP que todo iniciante em programação deve saber
date: 2013-12-11
author: Gustavo Furtado de Oliveira Alves
category: Programação
tags: PHP
slug: 5-funcoes-curingas-em-php-que-todo-iniciante-em-programacao-deve-saber

Este é um *Guest Post* escrito pela equipe da
[FastCom](http://fastcom.com.br/ "FastCom Marketing Digital e Performance")
para o **{ Dicas de Programação }**, se você também tem interesse em
escrever um Guest Post para o nosso blog basta entrar em
[contato](http://www.dicasdeprogramacao.com.br/contato/ "Contato"). A
FastCom é uma empresa que presta serviços orientados de marketing
digital, criação de sites com foco em SEO para e-commerces, ads e mídias
sociais.

É fato. Mesmo quem está dando os primeiros passos na área de
desenvolvimento web sabe que é necessário ter sempre à mão pequenos
truques da programação para otimizar o tempo de trabalho. Por isso, na
postagem de hoje, trouxemos uma série de funções úteis para você que
está começando a desenvolver em PHP - com certeza a linguagem de
programação mais utilizada atualmente para desenvolvimento web -, onde
você poderá ter uma espécie de ‘canivete suíço’ inicial, para utilizar
em seus futuros projetos.

![funções
php](/images/5-funcoes-curingas-em-php-que-todo-iniciante-em-programacao-deve-saber/php.jpg){.size-full .aligncenter}

O Hypertext Preprocessor (PHP) é muito versátil e com linhas de códigos
podemos fazer muitas coisas quando o assunto é o meio digital. Ele,
inclusive, pode ser usado na maioria dos sistemas operacionais e, aqui,
elencamos algumas funções básicas e mostramos de forma prática situações
nas quais você pode usar os scripts. Na internet, você encontra muitos
outros, porém, sem os exemplos mostrados a seguir:

##1. Como mostrar dados de uma string XML?

O Twitter, Facebook e alguns serviços do Google passam informações por
meio de suas APIs. Utilizando XML e JSON, podemos mostrar as informações
de um XML através da seguinte função:

```html
<!DOCTYPE html>
<?php

$string_xml="<?xml version='1.0'?>
<users>
   <user id='398'>
      <name>Joao</name>
      <email>joao@ninguem.com</email>
   </user>
   <user id='867'>
      <name>Fulano</name>
      <email>fulano@detal.com</email>
   </user>
</users>";

//carrega a string xml usando a função
$xml =simplexml_load_string($string_xml);

//faz um look para cada ocorrência de "user"
foreach ($xml->user as $user)
{
   //acessa atributo
   echo $user['id'], '  ';
   //ocorrencias internas acessadas através do operador ->
   echo $user->name, '  ';
   echo $user->email, '<br />';
}

?>
<html>
<head>
</head>
<body>

<?php
    // imprime o resultado
    echo $xml;

?>

</body>
</html>
```

O resultado desse código PHP você pode ver aqui:

![Resultado a função mostra xml](/images/5-funcoes-curingas-em-php-que-todo-iniciante-em-programacao-deve-saber/mostra-xml.png "Exemplo que mostra as informações de um XML").

##2. Como imprimir resultados de uma string JSON sem loop?

APIs como Flickr, Twitter e outros serviços populares utilizam esse
formato. Você pode utilizar, por exemplo, para mostrar os tweets que
contém uma determinada hashtag, pois você pode desenvolver uma aplicação
que guarda as ocorrências de determinada hashtag durante um ano, e
depois monta um gráfico para saber quando elas ocorrem mais. Ou comparar
a semelhança dos trending topics cada vez que eles mudam, ou um gráfico
pra ver quais países digitam a hashtag \#justinbieber nos dias de
semana, após as 20h.

```html
<?php

    $json_string='{"id":1,"nome":"joao","email":"joao@ninguem.com","interesses":["wordpress","php"]} ';
    $obj = json_decode($json_string);
    echo $obj->nome; //imprime o nome
    echo "<br />";
    echo $obj->interesses[1]; //improme o segundo interesse = php

?>
```

O resultado desse código PHP você pode
ver aqui:

![Resultado da função Mostra Json](/images/5-funcoes-curingas-em-php-que-todo-iniciante-em-programacao-deve-saber/mostra-json.png "Exemplo que mostra as informações de um JSON sem loop").

##3. Como listar o conteúdo de uma pasta?

Você pode utilizar essa função em uma aplicação onde você gostaria de
listar o conteúdo de uma pasta onde estão seus relatórios e imagens de
uma determinada pasta. Listar os arquivos sempre é o primeiro passo para
você começar a mensurar seus gastos com servidor (CPU, memória, banda e
disco);

```html
<?php

    //declara a função
    function list_files($dir)
    {
        // verifica se a é um diretório
        if(is_dir($dir))
        {

            //abre o diretorio
            if($handle = opendir($dir))
            {

                // percorre os registros do diretorio
                while(($file = readdir($handle)) !== false)
                {

                    if($file != "." && $file != ".." && $file != "Thumbs.db")
                    {
                        //monta um link com o nome do arquivo
                        echo '<a target="_blank" href="'.$dir.$file.'">'.$file.'</a><br>'."n";
                    }
                }
                closedir($handle);
            }
        }
    }

?>

<?

    $root = '.';

    list_files($root);

?>
```

##4. Como mostrar o IP real do visitante?

Você pode utilizar essa informação para mostrar dados personalizados
baseados no IP do visitante. Vale ressaltar que tal script não
funcionará em casos nos quais o usuário usa navegadores anônimos, como o
TOR.

```html
<?php

    //declara função
    function pegaip()
    {
        //verifica se não é vazio
        if (!empty($_SERVER['HTTP_CLIENT_IP']))
        {
            $ip=$_SERVER['HTTP_CLIENT_IP'];
        }
        //verifica se vem de um proxy
        elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
        {
            $ip=$_SERVER['HTTP_X_FORWARDED_FOR'];
        }
        else
        {
            $ip=$_SERVER['REMOTE_ADDR'];
        }
        //retorna ip
        return $ip;
    }

?>

<?php

    echo pegaip();

?>
```

O resultado desse código PHP você pode
ver aqui:

![Exemplo que mostra como obter o IP real de um visitante do site.](/images/5-funcoes-curingas-em-php-que-todo-iniciante-em-programacao-deve-saber/php-ip-real.png)

##5. Como comparar duas strings?

Este PHP é usado para muitas finalidades, como, por exemplo, verificar
se as tags ‘title’ do seu site são iguais, ou efetuar qualquer tipo de
comparativo entre páginas do seu site.

```html
<?php

    //atribui valor a string 1
    $string1 = "Programar usando php é muito legal";
    //atribui valor a string 2
    $string2 = "Programar usando php é muito chato";
    //compara 2 strings
    similar_text($string1, $string2, $quanto);
    //$quanto mostrará quantos % as 2 strings são iguais

    //imprime os resultados
    echo "As Strings:";
    echo "<br />";
    echo $string1;
    echo "<br />";
    echo "e<br />";
    echo $string2;
    echo "<br />";
    echo "são ".$quanto." % parecidas";

?>
```

O resultado desse código PHP você pode
ver 

![Exemplo que mostra como comparar duas strings](/images/5-funcoes-curingas-em-php-que-todo-iniciante-em-programacao-deve-saber/verifica-parecidas.png).

Estas funções são básicas e servem como base para seus projetos em
desenvolvimento e [criação de
sites](http://fastcom.com.br/servicos/criacao-de-sites/){:target=\_blank}. Em caso de
dúvidas, entre em contato com a gente!

*Fonte:* [*FastCom*](http://fastcom.com.br/)*.*
*Imagem: Getty Images*
