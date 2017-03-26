title: Como descobrir o primeiro e o último dia do mês em C#
date: 2015-03-26
author: Gustavo Furtado de Oliveira Alves
category: { Dicas Rápidas }
slug: como-descobrir-o-primeiro-e-o-ultimo-dia-do-mes-em-c

Criar uma data em C\# com o primeiro dia do mês é simples, mas muita
gente tem dúvida na hora de criar uma data com o último dia do mês, pois
depende do mês. Logo pensam em toda uma lógica, com Switch-case, etc.
Mas em C\# isso é bem fácil. Vejamos ...

Se você tem uma data e deseja criar uma outra data para o <span
style="text-decoration: underline;">primeiro dia do mês</span>, basta
criar um novo DateTime com o dia 1 usando o mês e o ano da primeira
data. Veja no código abaixo.

```
//Vamos considerar que a data seja o dia de hoje, mas pode ser qualquer data.
DateTime data = DateTime.Today;

//DateTime com o primeiro dia do mês
DateTime primeiroDiaDoMes = new DateTime(data.Year, data.Month, 1);
```

Já pra criar um DateTime com o último dia do mês em C\# temos que saber
quantos dias tem no mês, para isso existe um método estático da struct
DateTime que resolve esse problema.

<span class="wrap:true lang:default decode:true crayon-inline">public
static int DaysInMonth(int year, int month);</span>

Perceba que este método recebe o ano e mês como parâmetros e retorna a
quantidade de dias daquele mês.

Considerando a mesma variável *data* do código anterior, o código abaixo
mostra como criar o DateTime com o <span
style="text-decoration: underline;">último dia do mês</span> corrente.

```
//DateTime com o último dia do mês
DateTime ultimoDiaDoMes = new DateTime(data.Year, data.Month, DateTime.DaysInMonth(data.Year, data.Month));
```

Essa é uma dica rápida do **{ Dicas de Programação }**. Se ficou com
dúvida, pode perguntar nos comentários aí em baixo.
