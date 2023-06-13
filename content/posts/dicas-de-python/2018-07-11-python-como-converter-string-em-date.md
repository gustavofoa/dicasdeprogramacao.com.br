---
title: Python: Como converter string em date
date: 2018-07-11
author: Gustavo Furtado de Oliveira Alves
category: : Dicas de Python :
tags: String, date, datetime
slug: python-como-converter-string-em-date
---

Para converter uma string em date em python, basta usar a função `strptime` da classe datetime, para obter um objeto datetime e em seguida, obter o objeto date através da função `date()`.

O código abaixo exemplifica a conversão de duas strings em formatos diferentes em objetos `date`.

```python
from datetime import datetime

str_date = '11/07/2018'

date = datetime.strptime(str_date, '%d/%m/%Y').date()

print(date, type(date))

str_date = '2018-07-11'

date = datetime.strptime(str_date, '%Y-%m-%d').date()

print(date, type(date))
```

Saída:

```
2018-07-11 <class 'datetime.date'>
2018-07-11 <class 'datetime.date'>
```

Referências:

1. [Documentação: datetime](https://docs.python.org/3/library/datetime.html){:target=\_blank}
