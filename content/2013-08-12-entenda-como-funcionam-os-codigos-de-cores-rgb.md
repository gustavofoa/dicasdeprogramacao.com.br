title: Entenda como funciona o código de cores RGB
date: 2013-08-12
author: Gustavo Furtado de Oliveira Alves
category: Iniciante
slug: entenda-como-funcionam-os-codigos-de-cores-rgb

Em muitas áreas de aplicação nós precisamos trabalhar com cores, mesmo
que não seja programando, por exemplo, configurar a cor de um site ou
editar uma imagem com o Photoshop, o Corel draw, paint, etc. Geralmente
essas cores são representadas por um código de 6 caracteres hexadecimais
(de 0 a F) precedido do caracter "**\#**", por exemplo: '**\#68B46D**'.

Dado um código, você sabe descobrir que cor é essa? E o contrário? Dada
uma cor, você sabe descobrir o código? Neste artigo vou explicar como
funciona esse código e, de forma simples, como descobrir o código de uma
cor e vice-versa.

##Como as cores são formadas?

![cores
rgb](/images/entenda-como-funcionam-os-codigos-de-cores-rgb/cores-rgb.jpg){.alignleft}

Existem duas maneiras de se formar cor, uma é através de pigmentação e
outra é através da luz. A primeira é muito utilizada em artes plásticas,
onde se mistura cores para formar uma outra. Mas a forma utilizada na
tecnologia é a formação por luz.

Na formação de cores por luz, as cores são formadas a partir de três
cores primarias. As três cores primárias mais conhecidas são: Vermelho,
Verde e Azul, ou RGB (do inglês, Red-Green-Blue). A partir delas pode-se
criar as demais cores.

As cores são criadas na computação com a combinação de valores de RGB.
Cada uma dessas cores primárias recebe um valor de intensidade que varia
de 0 a 255. O branco é quando se tem o maior valor para as 3 cores, ou
seja, 255 e o preto é formado quando se tem o valor 0 para essas 3
cores.

##A formação do código RGB

Um código RGB é uma representação dos valores das cores primárias
juntas, só que em Hexadecimal. Podemos perceber que os códigos são
sempre formados com 6 dígitos, o que dá 2 dígitos para cada cor. Se em 2
dígitos hexadecimais conseguimos valores de 00 a FF, então conseguimos
representar valores de 0 a 255 da base decimal.

**[As 10 conversões numéricas mais utilizadas na
computação.](http://www.dicasdeprogramacao.com.br/as-10-conversoes-numericas-mais-utilizadas-na-computacao/ "As 10 conversões numéricas mais utilizadas na computação"){:target=\_blank}**

Pensemos, se branco é formado com a combinação dos maiores valores, o
código RGB do branco é: \#FFFFFF. O preto seria \#000000. Certo? Agora
olhando pra figura apresentada acima que mostra a combinação de cores
primárias para formar outras cores, como seria a representação da cor
amarela em código RGB?

Bom, percebemos que o amarelo é formado com a combinação do Verde e do
Vermelho. Então o código RGB do amarelo é \#FFFF00. Ou seja, valores
máximos para R (Red) e G (Green) e 0 para o B (Blue).

Deu pra entender né...

##Como descobrir a cor de um código RGB

Existem vários sites que fazem isso. Mas pra facilitar a sua vida eu
implementei aqui neste artigo um campo pra você ver a cor de um
código. Basta digitar o código no campo abaixo. Por exemplo \#2C76D0.

**Digite o código RGB aqui:**
<input id="txtCor" type="text" value="#2C76D0" oninput="changeColor()"></input>
<div id="representacaoDaCor" style="background-color: #2c76d0; height:50px; width:300px;">
</div>
<br/>

##Como descobrir o código de uma cor

Agora que você já entendeu o conceito do código RGB, fica fácil
descobrir o código de uma cor. Você pode usar o próprio paint do windows
pra isso. Vou descrever quais os passos para descobrir o código RGB de
uma cor a partir do seu computador.

1.  Coloque a cor visível na tela do seu computador e pressione a
    tecla **PRINT SCREEN**. (Pra copiar a tela do seu computador)
2.  Abra o **paint** e pressione **Ctrl+V** pra colar a imagem da
    sua tela.
3.  Clique na ferramenta **Selecionador de cores** do paint. (É esse
    ícone: ![selecionador de
    cores](/images/entenda-como-funcionam-os-codigos-de-cores-rgb/selecionador-de-cores.png))
4.  Clique em cima da cor que deseja identificar.
5.  Clique no botão **Editar cores.** (É esse ícone: ![editar cores no
    paint](/images/entenda-como-funcionam-os-codigos-de-cores-rgb/editar-cores.png))
6.  Identifique os valores de Vermelho, Verde e Azul. Conforme
    apresentado na tela abaixo.

![Vermelho Verde e Azul de uma
cor](/images/entenda-como-funcionam-os-codigos-de-cores-rgb/tela-que-identifica-os-valores-de-rgb.png){.aligncenter}

Esses números estão na base decimal. Pra gerar o código RGB é necessário
convertê-los para a base **Hexadecimal**.

**[As 10 conversões numéricas mais utilizadas na
computação.](http://www.dicasdeprogramacao.com.br/as-10-conversoes-numericas-mais-utilizadas-na-computacao/ "As 10 conversões numéricas mais utilizadas na computação"){:target=\_blank}**

Pra facilitar a sua vida, eu também implementei neste artigo três campos
pra você digitar os números em decimal e obter o código RGB da cor.

R =
<input id="txtR" style="width: 30px;" type="text" value="27" oninput="changeRGB()"></input>
G =
<input id="txtG" style="width: 30px;" type="text" value="139" oninput="changeRGB()"></input>
B =
<input id="txtB" style="width: 30px;" type="text" value="61" oninput="changeRGB()"></input>

<div id="codigoRGB">
<b>Código RGB:</b> \#1b8b3d
<div style="background-color:#1b8b3d; height:50px; width:300px;"></div>
</div>
<br/>

##Curiosidade sobre o código RGB

Agora você já sabe que o código \#FFFFFF é a cor branca e o código
\#000000 é a cor preta. Uma curiosidade sobre o código RGB é que quando
os valores são iguais para as três cores primárias, nós temos cores em
escala de cinza. Por exemplo, o código \#5A5A5A é um cinza escuro, pois
está próximo do preto \#000000. Já o código \#B7B7B7 é um cinza mais
claro, pois está mais próximo do branco \#FFFFFF.

Espero que tenha gostado dessa dica. Entender como é formado o código
RGB é importante para fazer muitas coisas, principalmente se você
trabalhar com desenvolvimento Web.

<script type="text/javascript" src="/images/entenda-como-funcionam-os-codigos-de-cores-rgb/rgbscript.js"></script>
