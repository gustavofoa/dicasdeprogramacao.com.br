title: Migração do blog para Site Estático
date: 2018-01-05
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Programação }
tags: blogs
slug: migracao-do-blog-para-site-estatico

Já faz um tempo que não publico nada aqui no **{ Dicas de Programação }**,
o último post foi publicado em [maio de 2016](https://dicasdeprogramacao.com.br/ingles-tecnico-para-programadores/).
Infelizmente eu fiquei bastante tempo sem escrever aqui para me dedicar a outros
[projetos](https://gustavofurtado.com.br/projetos).
Mas recebo e-mails todos os dias de pessoas agradecendo pelos meus posts,
dizendo que minha forma de explicar as ajudaram a entender conceitos básicos de programação.
O [minicurso gratuito por e-mail de lógica de programação](https://mclp.dicasdeprogramacao.com.br/)
recebe novos inscritos todos os dias e também recebo muitos e-mails de alunos agradecendo
pelo minicurso.

Esse carinho dos alunos e leitores do blog me insentivaram a voltar a escrever.
Mas antes eu precisava refleti um pouco sobre o motivo de eu ter ficado tanto tempo sem escrever aqui.
Percebi que o processo de abrir a área administrativa do wordpress para escrever um post
era uma barreira para mim.
Eu não sou um escritor, pra mim não é natural abrir o word ou o wordpress para escrever.
Pra mim é natural abrir uma IDE para programar, escrever códigos.

## Escrever posts como se estivesse programando

Então eu descobri os **geradores de site estático** (_Static Site Generators_ - SSGs),
comecei a pesquisar sobre o assunto e descobri várias vantagens de se ter um blog estático.
Mas a principal vantagem pra mim era que eu iria escrever posts como se estivesse programando,
armazenando meu blog como um código no [github](https://github.com/gustavofoa/dicasdeprogramacao.com.br/),
criando _branches_, fazendo _commits_, _merge_, _push_, etc.

Agora eu estou escrevendo este post em um lugar sem internet e
utilizando a IDE que trabalho diariamente [IntelliJ IDEA](TODO URL PARA intellij), veja:

![Escrevendo post com uma IDE](/images/migracao-do-blog-para-site-estatico/escrevendo-post-com-uma-ide.png)

Existem muitas vantagens de se ter um blog como um site estático,
mas não vou falar disso neste post, prefiro escrever um post dedicado a isso.
Mas só o fato de poder escrever posts sem precisar abrir a área administrativa do Wordpress
já me conquistou e eu decidi migrar o **{ Dicas de Programação }** para esta tecnologia.

## A migração de Wordpress para Pelican

Dentre os vários geradores de site estático (**SSGs**), eu escolhi o [Pelican](TODO URL PARA PELICAN)
e comecei a entender o seu funcionamento para fazer a migração.

Não tive grandes dificuldades para fazer a migração.
Basicamente é necessário entender como um blog é estruturado em qualquer plataforma.
Um blog sem tem _posts, páginas, categorias, tags, temas, plugins_, etc.
Tanto o Wordpress o Blogger, quanto outras tecnologias de blog têm os mesmos conceitos,
com poucas diferenças entre elas. Para SSGs não é diferente.

A coisa mais importante que se tem que ter em mente ao migrar um blog para SSG é
a identificação do que tem que ser dinâmico no blog, ou seja, o que tem que ser gerado
no servidor no momento da requisição de uma página do blog.
Se as páginas do blog serão geradas apenas uma vez ao invés de serem geradas no momento
em que um usuário abre uma página, as partes necessariamente dinâmicas não
podem ficar sob responsabilidade do blog mais, para isso usamos outros serviços.

Por exemplo, **os comentários** de todas os posts são diâmicos.
Quando alguém faz um comentário, este deve aparecer na página do post daquele momento em diante,
mas o blog não é gerado novamente toda vez que alguém comenta no blog.
Para isso nós podemos usar alguns serviços terceirizados.
Aqui no **{ Dicas de Programação }** estou utilizando o [Disqus](TODO LINK PARA DISQUS),
para gerenciar os comentários e mostrá-los dinâmicamente nos posts.
O [Facebook](TODO LINK PARA FACEBOOK DEVELOPERS) também tem o mesmo serviço.

![Utilizando o Disqus para o serviço de comentários](TODO IMAGEM DO DISQUS)

Outra parte dinâmica do blog é o formulário de contatos,
para este serviço eu utilizei o [Formspree](TODO LINK PARA O FORMSPREE).

Além da parte dinâmica, se você deseja utilizar o mesmo tema do seu blog wordpress,
será necessário migrá-lo para a tecnologia de template do SSG.
Este foi o principal motivo de eu ter escolhido utilizar o Pelican,
pois este utiliza [Jinja2](TODO LINK PARA JINJA2) para template.

Fiz a migração do tema wordpress para pelican sem grandes dificuldades,
mas tenho que reconhecer que essa parte não é trivial,
é necessário ter conhecimento de programação, além de HTML, CSS e Javascript.
Mas a maioria dos SSGs tem boa documentação para ajudar nesta tarefa.

Por fim sobraram os plugins. A quantidade de plugins disponível depende do SSG
e evidentemente a maioria dos plugins do wordpress não existem nos SSGs, pois
Infelizmente grande parte deles precisam necessariamente ser dinâmicos,
ou seja, precisam ser executados no momento da requisição da página do blog.
O que os impede de serem utilizados com um SSG.
Os SSGs mais famosos como Jekyll, Pelican, Hugo, têm bastante plugins.
Mas é necessário ter em mente que eles serão executados no momento da geração do blog,
não no momento em que alguém faz a requisição para uma página.

## De volta à ativa

Infelizmente o **{ Dicas de Programação }** ficou um pouco abandonado nos últimos tempos.
Há tempos eu queria voltar a publicar por aqui, mas ficava adiando.

Final de ano é sempre um tempo para fazer uma retrospectiva e corrigir o trajeto da caminhada.
Em 2018 pretendo voltar à ativa aqui no blog e essa migração para _site estático_,
foi uma ação para evitar um bloqueio mental que eu sempre tive de **não escritor**.

Agora, escrevendo posts em arquivos, fazendo commits
e utilizando a mesma IDE que utilizo diariamente,
acredito que terei mais ânimo para escrever.

Na próxima semana vou postar um artigo com as vantagens de se utilizar um SSG,
ao invés de um CMS como o Wordpress.