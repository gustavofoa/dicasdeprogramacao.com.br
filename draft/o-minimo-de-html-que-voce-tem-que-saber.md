Title: O mínimo de HTML que você TEM que saber!
Date: 2015-05-25 12:13
Author: gustavo.foa
Category: HTML, Iniciante
Slug: o-minimo-de-html-que-voce-tem-que-saber
Status: published

O mundo está cada vez mais tecnológico e entender as coisas básicas de
tecnologia que usamos é uma questão de alfabetização. Sim, a nova
alfabetização!

As pessoas usam a internet, mas muitos não fazem ideia de como as coisas
funcionam para ela poderem consumir este conteúdo na rede. Conhecer os
conceitos básicos da tecnologia é dar os primeiros passos num novo mundo
cheio de oportunidades!

Neste post quero te apresentar o HTML! A linguagem responsável por te
entregar este texto que você está lendo neste exato momento. E todas as
páginas de internet que você acessa todos os dias.

O que é HTML?
-------------

Quando vemos uma página de internet no navegador, a vemos toda bonitinha
com cores, imagens, textos, links, etc. Mas na verdade, o seu navegador
interpreta um código e apresenta a página para você. Esse código é o
HTML, que significa *Linguagem de Marcação de Hiper-Textos* (tradução de
*hypertext markup language*).

Ao contrário do que muita gente pensa, HTML NÃO é uma linguagem de
programação, o nome já diz: **Linguagem de Marcação**.

Mas o que isso significa? Significa que não criamos programas com HTML.

O HTML é uma linguagem que usa apenas marcadores (ou *tags*), para
"configurar" uma página. Por exemplo, podemos dizer que um texto deve
estar em negrito marcando ele com a tag **&lt;b&gt;**
ou **&lt;strong&gt;**.

Se você clicar nesta página com o botão direito do mouse e selecionar
"Exibir código fonte", você verá o código HTML desta página. E se
procurar pelo texto **Linguagem de Marcação** que está em negrito, verá
que ele estará entre as *tags* **&lt;strong&gt;&lt;/strong&gt;**. Veja
na imagem abaixo.

![exemplo de código
html](http://dicasdeprogramacao.com.br/wp-content/uploads/strong.png){.aligncenter
.size-full .wp-image-2168 width="522" height="165"}

Acho que você notou outras *tags* no código-fonte acima. Certo? Uma
tag **&lt;p&gt;&lt;/p&gt;** que marca um *parágrafo* e outra
tag **&lt;em&gt;&lt;/em&gt;** que marca um texto a ser *enfatizado*. O
HTML é formado por estas *tags*, que *marcam* o texto.

Vamos avançar um pouquinho mais? Vamos criar uma página web ...

Criando uma página HTML simples
-------------------------------

Um código simples ajudará a gente entender os conceitos básicos de HTML,
acho mais fácil entender na prática. Abaixo eu apresento um código HTML.
Você pode copiar esse código, salvar em um arquivo com a extensão
".html" e abri-lo num navegador.

``` {.lang:xhtml .decode:true}
<html>
   <head>
      <title>Título da página</title>
   </head>
   <body bgcolor='gray'>
      Primeira página HTML
      
      <br>
      <br />
      
      <img "cores rgb" alt="cores rgb" src="http://www.dicasdeprogramacao.com.br/wp-content/uploads/cores-rgb.jpg" />

      <a href="http://www.dicasdeprogramacao.com.br/">Clique aqui para acessar o blog <strong>{ Dicas de Programação }</a>

   </body>
</html>
```

Agora vamos entender este código e aprender os conceitos básicos de HTML
...

1.  Podemos ver no código HTML acima que ele é formado por *tags* (o
    texto entre os sinais de menor e maior "&lt; e &gt;"). Essas tags,
    abrem um "bloco" que deve ser fechado. Para fechar uma tag,
    utiliza-se a barra logo depois do símbolo de menor. Por exemplo,
    abrimos a tag &lt;title&gt; e fechamos ela dessa
    forma: &lt;/title&gt;.
2.  O texto que fica dentro da tag &lt;title&gt; é o texto que aparece
    na barra de títulos do navegador.
3.  O texto que fica entre a *tag* de abertura e a *tag* de fechamento é
    conhecido como "valor de corpo da tag"
4.  As tags HTML pode ser aninhadas, ou seja, uma dentro da outra
    (Perceba que a tag &lt;title&gt; está dentro da tag &lt;head&gt;,
    que por sua vez está dentro da tag &lt;html&gt;).
5.  Um HTML básico é formado pela tag &lt;html&gt; e dentro desta, as
    tags &lt;head&gt; (cabeçalho) e &lt;body&gt; (corpo).
6.  Tudo que fica dentro da tag &lt;body&gt; é o corpo da sua página.
7.  As tags podem ter atributos, por exemplo o atributo bgcolor da tag
    &lt;body&gt; define a cor de fundo da página. No exemplo definimos
    as cor de fundo como 'gray' (cinza). Pode-se também utilizar
    **[códigos
    RGB](http://www.dicasdeprogramacao.com.br/entenda-como-funcionam-os-codigos-de-cores-rgb/)**.
8.  Algumas tags não precisam de *valor de corpo* e em HTML puro, não
    precisam ser fechadas, como a tag &lt;br&gt; (quebra de linha). Mas
    para compatibilizar com XML, é correto fechar todas as tags. Nesse
    caso, você não precisa fechar a tag do modo convencional (por
    exemplo **&lt;br&gt;&lt;/br&gt;**). Pode simplesmente fechar com uma
    barra ao final da tag de abertura. Assim: **&lt;br /&gt;**. O mesmo
    pode ser observado na tag &lt;img&gt;.
9.  As imagens que vemos em uma página web são definidas pela tag
    &lt;img&gt; do HTML. Os atributos que mais utilizamos desta tag são
    src (que determina o endereço da imagem a ser exibida), *title* e
    *alt* (que definem o texto exibido quando colocamos o cursor do
    mouse em cima da imagem). Dica: Os atributos *title* e *alt* são
    muito importantes para o SEO (Otimização para mecanismos de busca)
    da sua página. ;)\
    Exemplo do código de uma imagem HTML: &lt;img title="cores rgb"
    alt="cores rgb"
    src="<http://www.dicasdeprogramacao.com.br/wp-content/uploads/cores-rgb.jpg>" /&gt;
10. Os links das páginas web são criados pela tag &lt;a&gt;. O atributo
    mais importante dos links é o href que é o endereço do link. O texto
    que aparece dentro da tag de link (entre a abertura &lt;a&gt; e o
    fechamento &lt;/a&gt;) é conhecido como "texto âncora". Este texto
    também é muito importante para o SEO.

Não dá pra falar tudo sobre HTML em um único post, mas pra começar a
entender como funcionam as páginas da internet. Os conceitos básicos de
HTML apresentados acima é o mínimo que qualquer um deve saber sobre as
páginas Web que você acessa todos os dias. Se você em ter um blog por
exemplo, saber um pouquinho de HTML te ajudará muito!

Claro que tem muito mais. Criação de tabelas, divs, formatação com CSS,
adição de javascript, páginas dinâmicas, etc. HTML é só o começo. Não
pare por aqui!
