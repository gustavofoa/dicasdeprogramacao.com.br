Title: Como desinstalar o Oracle completamente
Date: 2014-07-31 14:09
Author: gustavo.foa
Category: Bancos de dados, Oracle
Tags: banco de dados, oracle
Slug: como-desinstalar-o-oracle-completamente
Status: published

O
[SGBD](http://www.dicasdeprogramacao.com.br/o-que-e-um-sgbd/ "O que é um SGBD?")
Oracle, um dos melhores do mercado, é um software criado para ser
utilizados em servidores robustos de empresas com grandes bancos de
dados. Entretanto podemos instalá-lo em nosso computador pessoal,
obviamente para fins de desenvolvimento e estudo.

Já publiquei aqui no **{ Dicas de Programação }** um artigo ensinando
como instalar o Oracle no windows para criar um ambiente de estudos de
banco de dados, inclusive dou dicas de como desabilitar a execução do
oracle quando não estamos mais utilizando, isso ajuda muito o desempenho
do seu computador.

**[Veja como instalar o Oracle XE no Windows para estudar bancos de
dados e
SQL](http://www.dicasdeprogramacao.com.br/como-criar-um-ambiente-para-estudar-banco-de-dados-e-sql/ "Como criar um ambiente para estudar Banco de Dados e SQL")**

Mas quando não queremos mais o Oracle instalado no nosso computador,
talvez porque você não precise mais estudar banco de dados e SQL ou por
qualquer outro motivo, vem a questão: como desinstalar completamente o
Oracle? Adianto que não é uma desinstalação simples como você está
acostumado, não basta simplesmente abrir o "Adicionar e Remover
programas" do Windows e desinstalar o Oracle.

No passado eu tive problemas para desinstalar o Oracle do meu
computador. Vou mostrar como faço passo-a-passo para desinstalar
completamente o Oracle do Windows ...

**Importante!** Os passos apresentados aqui edita o registro do Windows
e desinstala todos os produtos do Oracle completamente. Isso pode ser
perigoso, um erro cometido na edição do registro pode causar danos
irreparáveis ao seu sistema operacional. <span
style="text-decoration: underline;">Portando seja muito cuidadoso ao
editar o registro do Windows.</span>

> Obs.: As imagens ilustradas representa os produtos Oracle instalados
> no meu computador, no seu caso pode ser diferente.

Passo-a-passo para desinstalar o Oracle completamente
-----------------------------------------------------

### 1. Desinstale os produtos Oracle através do OUI.

Acesse o Oracle Universal Installer no menu iniciar de desinstale todos
os componentes Oracle.

![Desinstalar Oracle Universal
Installer](http://www.dicasdeprogramacao.com.br/wp-content/uploads/Desinstalar-Oracle-Universal-Installer.png){.aligncenter
.wp-image-1881 .size-full width="656" height="519"}

### 2. Abra o Editor de Registro do Windows.

Para abrir o Editor de Registro do Windows clique no Menu
Iniciar-&gt;Executar (ou use a combinação de teclas "Windows"+R), digite
o comando "regedit" e tecle ENTER. ![executar
regedit](http://www.dicasdeprogramacao.com.br/wp-content/uploads/executar-regedit.png){.aligncenter
.wp-image-1878 .size-full width="413" height="217"}

> LEMBRANDO! Muito cuidado com o que você exclui no registro. Siga
> **cuidadosamente** os passos a seguir.

### 3. Exclua a chave de registro HKEY\_LOCAL\_MACHINE/SOFTWARE/Oracle.

Esta chave contém entradas de registro para todos os produtos Oracle.
![excluir chave de registro do
Oracle](http://www.dicasdeprogramacao.com.br/wp-content/uploads/excluir-chave-de-registro-do-Oracle.png){.aligncenter
.wp-image-1884 .size-full width="641" height="555"}

### 4. Se você estiver usando um Windows 64-bits, exclua também a chave de registro HKEY\_LOCAL\_MACHINE/SOFTWARE/Wow6432Node/Oracle.

![excluir chave de registro do Oracle
2](http://www.dicasdeprogramacao.com.br/wp-content/uploads/excluir-chave-de-registro-do-Oracle-2.png){.aligncenter
.wp-image-1885 .size-full width="1086" height="555"}

### 5. Exclua todas as referências para serviços Oracle dentro desta parte do registro: HKEY\_LOCAL\_MACHINE/SYSTEM/CurrentControlSet/Services/.

Deve ser fácil identificar os nomes dos serviços que começam com "Ora".
![excluir chave de registro dos serviços
Oracle](http://www.dicasdeprogramacao.com.br/wp-content/uploads/excluir-chave-de-registro-dos-serviços-Oracle.png){.aligncenter
.wp-image-1886 .size-full width="1107" height="555"}

### 6. Reinicie o seu computador.

### 7. Exclua a pasta "C:\\Oracle", ou a pasta configurada como ORACLE\_BASE.

No meu caso, o ORACLE\_BASE era a pasta "C:\\app\\oracle".

### 8. Exclua a pasta "C:\\Program Files\\Oracle".

Se vocês estiver usando um Windows 64-bits, exclua também a pasta
"C:\\Program Files (x86)\\Oracle".

### 9. Exclua a pasta do Oracle do menu iniciar.

Provavelmente seja a pasta "C:\\ProgramData\\Microsoft\\Windows\\Start
Menu\\Programs\\".

### 10. Esvazie a pasta "C:\\Temp".

### 11. Esvazie a Lixeira.

A partir de agora, sua máquina estará completamente sem o Oracle.

Não custa lembrar... Muito cuidado ao editar o registro do Windows. Um
erro pode causar danos irreversíveis ao seu Sistema Operacional.

Espero que isso ajude!
