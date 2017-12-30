title: Porque utilizar SSG para criação de blogs
date: 2018-01-12
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Programação }
tags: Blogs
slug: porque-utilizar-ssg-para-criacao-de-blogs

Você decidiu criar um blog e o primeiro passo é fazer uma pesquisa no google sobre:
**qual a melhor tecnologia para criar o próximo blog de sucesso da internet**.
Blogger? Wordpress?
Ao identificar as características de cada opção, percebemos que
nem sempre é mais indicado seguir o que a maior parte das pessoas está fazendo.

Neste post vou explicar porque na maioria dos casos
é mais indicado criar um blog utilizando um
**Gerador de Site Estático** ou **Static Site Generator** (SSG) em inglês,
 ao invés de um **Sistema de Gerenciamento de Conteúdo** ou **Content Management System** (CMS).

# Desvantagens dos Sistemas de Gerencimento de Conteúdo

Geralmente os sistemas de gerenciamento de conteúdo (CMS) são sites dinâmicos.
Ou seja, são construídos com uma linguagem para WEB (como PHP, Java, Ruby, etc.),
utilizam um banco de dados (MySQL, Postgress, Oracle, SqlServer etc.)
e funcionam sobre um servidor de aplicações (Apache, Nginx, Tomcat, etc.).

Provavelmente você já ouviu falar de **Workpress**,
o CMS mais utilizado no mundo para criação de blogs.
Ele é construído em PHP com MySQL.

O _Stack_ _PHP+MySQL_ utilizado pelo Wordpress é indicado para muitas situações simples,
principalmente quando você **precisa** gerar as páginas web dinamicamente,
ou responder a um evento em tempo real.
Mas para a criação de um blog nem sempre há essa necessidade.

![Wordpress](/images/porque-utilizar-ssg-para-criacao-de-blogs/wordpress.png){.aligncenter}

No passado era bastante justificável a utilização de CMSs para blogs,
um blog geralmente precisa de um controle de acesso para o gerenciamento do conteúdo,
um formulário de contatos, gestão de comentários, etc.
E para implementar isso era necessário ter as soluções no próprio sistema de gestão do blog.
Mas hoje em dia todas essas necessidades podem ser atendidas por sistemas terceiros.

Por exemplo, para gestão de comentários nós podemos utilizar o [Disqus](https://disqus.com/),
ou até mesmo o [Facebook](https://developers.facebook.com/).
Para formulário de contatos também existem vários serviços como [Formspree](https://formspree.io) ou
[Formbucket](https://www.formbucket.com/).
Para controle de acesso de gestão de conteúdo, podemos utilizar o próprio [Github](https://github.com/),
com o processo de aprovação via _Pull Requests_ que a maioria dos programadores já está acostumada.

Além de podermos utilizar sistemas terceiros para as partes dinâmicas do nosso blog,
CMSs como o Workdpress têm algumas desvantagens que já me deram algumas dores de cabeça no passado,
tanto aqui no **{ Dicas de Programação }**, quanto em outro site meu chamado [**Músicas para Missa**](https://musicasparamissa.com.br).

## Segurança

A principal desvantagem é que por ser o CMS mais utilizado no mundo,
o Wordpress sofre ataques harckers constantemente.
É frequente a descoberta de uma ou outra [brecha de segurança no Wordpress](https://www.google.com.br/search?q=falha+de+segurança+no+wordpress).
Eu mesmo já tive blog invadido por causa de uma dessas brechas de segurança.

Não que o Wordpress seja ruim na parte de segurança, na verdade é um problema dos sistemas de sucesso, como o próprio Windows.
Por ser o mais utilizado, quando nós instalamos um wordpress é como se estivéssemos pintando um alvo na nossa testa (ou no nosso servidor).

Também já perdi as contas de quantas vezes o meu servidor MySQL caiu quando este e outros blogs sofreram ataques DDOS.

## Banco de dados

Uma outra desvantagem forte dos CMSs na minha opinião,
é que o histórico de alterações de conteúdo fica no banco de dados.
Eu sou totalmente contra essa característica dos CMS
por causa do fator "gestão de banco de dados" que isso implica.
É necessário ter um processo rígido de backup e também de um bom conhecimento
sobre a forma como o CMS faz esse gerenciamento de versões.

Sabemos que todo programador curte os sistemas de gerenciamento de versões como GIT, SVN, etc.
Por que não utilizar esses sistemas para gerenciar o blog inteiro, principalmente o seu conteúdo?
Agora que o **{ Dicas de Programação }** é um blog estático eu escrevo post na minha IDE preferida. ;)

## Custo

Ah como é bom pagar menos!
Com um site dinâmico nós precisamos nos preocupar com hospedagens, servidores, bancos de dados, escalabilidade, etc.
O custo para manter servidores para nosso blog vai lá nas alturas.

Além disso, aplicações dinâmicas trazem uma série de preocupações para manter o site no ar.
Cache, persistência, segurança, infra-estrutura web, etc.
Por isso, manter um blog com um CMS pode ficar caro ao longo do tempo, com o aumento das visitas.

Criando o seu blog como um **site estático** você não precisa se preocupar com nada disso.
Pois no final das contas nós teremos apenas arquivos HTML, CSS e Javascript para hospedar em qualquer servidor barato.
Você poderá utilizar um [S3 da Amazon Web Service](TODO)
com custo baixíssimo, ou mesmo hospedar o seu blog de graça no [Github Pages](TODO).

# Geradores de Sites Estáticos

Apresentados os problemas para se manter um blog diâmico,
os _Geradores de Sites Estáticos_ vem se mostrando a melhor solução para a maioria dos blogs.

Os **Static Site Generators** (SSG) são programas processadores que unem conteúdo,
algumas configurações, tema e plugins para criar as páginas do site.
O resultado é uma pasta que contém os arquivos estáticos que compõem o site.
Depois do site gerado você pode hospedá-lo em qualquer servidor básico de conteúdo estático.

O próprio Github tem um projeto chamado [Github Pages](https://pages.github.com/)
que hospeda o site estático gratuitamente com alguns [limites de uso](https://help.github.com/articles/what-is-github-pages/#usage-limits).

![Static Site Generator](/images/porque-utilizar-ssg-para-criacao-de-blogs/ssg.png){.aligncenter}

Existem SSGs em diferentes linguagens como você pode conferir [neste link](https://www.staticgen.com/).

O mais famoso é o [Jekyll](https://jekyllrb.com/), feito em Ruby.
Mas eu uso e gosto bastante do [Pelican](https://blog.getpelican.com/),
que é feito em Python e inclusive utilizo para gerar este blog.
Não sou um defensor do Pelican. O que me atraiu mais para utilizá-lo
é a tecnologia de templates (Jinja2) que é mesma tecnologia do django.

## Vantagens de se utilizar um SSG

Com os SSGs obtemos algumas vantagens em relação aos CMSs para blogs.

- Controle de versão para o conteúdo do blog (histórico e gestão de conteúdo);
- Escalabilidade para acesso em massa do blog (inclusive ataques DDOS);
- Proteção contra ataques (eles não tem o quê invadir);
- Escrever conteúdos para o blog como se estivesse programando
(Abre o código do blog na sua IDE favorita e divirta-se);
- É mais barato! Qualquer servidorzinho de site estático é mais barato
que uma hospedagem de site dinâmico.
- Estabilidade. Por exemplo eu armazeno meus blogs no S3 da Amazon (barato).
O dia em que a Amazon cair você não poderá ver suas séries favoritas da Netflix.
- Preview offline.
  No momento em que escrevo este post eu estou em um lugar sem internet ;)
  e visualizando como ficará o post no blog.

Além disso, é possível utilizar ferramentas de integração contínua (como Travis-CI, Cicle-CI, Jenkins, etc),
para fazer o deploy do blog direto no seu servidor de site estático.

Eu, particularmente, armazeno os códigos-fonte dos meus blogs no meu [github](https://github.com/gustavofoa)
e uso o [Travis-CI](https://travis-ci.org/) para fazer deploy automaticamente deles no S3 da Amazon
a cada commit/push que eu faço no _master_ do meu repositório remoto.
Ou seja, não preciso nem me preocupar com a publicação do post,
só enviar o código fonte para o github!

![Travis-CI](/images/porque-utilizar-ssg-para-criacao-de-blogs/travis-ci-gustavo.png){.aligncenter}


Concluindo ...
--------------

Muita gente tem preconceito de SSGs por exigir um pouco mais de conhecimento técnico
em comparação aos CMSs como Wordpress.
Temos que concordar, criar um blog com Wordpress é muito simples e
tem várias hospedagens que fornecem um serviço de instalação do Wordpress
com apenas 1 clique. O dono do blog não precisa se preocupar (por enquanto) com PHP, MySQL, Apache, etc.

Mas ao mesmo tempo que a barreira de entrada do Wordpress é muito pequena,
todo mundo que cria um blog, quer que ele cresça, e isso significa que
será necessário se preocupar com questões técnicas para mantê-lo no ar no futuro.
Com um site estático você está apenas antecipando esta preocupação.

Além disso, configurar e personalizar temas e plugins deixa de ser tão trivial quanto instalar o Wordpress,
sendo necessário contratar programadores e designers para deixar o blog como o blogueiro quer.

Os SSGs antecipam essa parte para a criação do blog, mas depois que ele já está criado,
configurado e personalizado, não tem mais preocupação nenhuma. Só criar conteúdo!

E aí, já conhecia os SSGs? Gostou?
Algo a compartilhar sobre o assunto?
Escreva aqui abaixo, no serviço de comentários (disqus) que eu não criei por ser diâmico
... ;)
