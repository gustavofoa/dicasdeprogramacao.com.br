title: A primeira fase de um projeto de banco de dados
date: 2015-03-18
author: Gustavo Furtado de Oliveira Alves
category: Banco de dados
slug: a-primeira-fase-de-um-projeto-de-banco-de-dados

O projeto de banco de dados é, geralmente, uma das partes mais
importantes no desenvolvimento de um novo software. Claro que existem
softwares que nem usam bancos de dados, mas a grande maioria dos
sistemas de informação consulta ou mantém dados armazenados em um banco
de dados, por este motivo entender como um banco de dados é projetado e
também saber criar um projeto de banco de dados é essencial na carreira
de qualquer desenvolvedor de software.

[Já dei uma visão geral sobre projetos de bancos de
dados](http://www.dicasdeprogramacao.com.br/como-criar-um-projeto-de-banco-de-dados/ "Como criar um projeto de banco de dados"){:target=\_blank}
em um artigo anterior. Neste artigo vamos ver, com exemplos
práticos, como executar a primeira fase de um projeto de banco de dados:
**A análise de requisitos**.

##Primeiro passo

A primeira coisa que se deve fazer é reunir dados relevantes para o novo
projeto através de documentos existentes, realização de entrevistas com
especialistas no negócio, etc. Esta etapa é muito importante, pois
quando o projetista entende errado os requisitos, o projeto pode ser um
fracasso. Nesta etapa deve-se gerar uma documentação descritiva, de
forma breve, sem ambiguidades e que descreva bem como as coisas
funcionam na realidade, uma **descrição textual das regras de negócio**.

Este texto sucinto que compila o entendimento das regras de negócio é
conhecido como **mini-mundo**. E é mesmo um mini-mundo, pois é a partir
da descrição das regras de negócio que desenvolvemos os modelos externos
(que são representações gráficas do mini-mundo e devem ser entendíveis
pelo usuário) e estes modelos não devem fugir da realidade descrita nas
regras de negócio.

![projeo de banco de
dados](/images/a-primeira-fase-de-um-projeto-de-banco-de-dados/modelagem-de-banco-de-dados.jpg){.aligncenter}

##Exemplo de um mini-mundo

Vejamos um exemplo de dessa primeira etapa e uma descrição de regras de
negócios para um caso fictício. Vamos tomar por exemplo um consultório
odontológico básico. Para simplificar consideremos que este consultório
é mantido por uma entidade social e não cobra diretamente dos pacientes,
ou seja, no momento do atendimento este consultório apenas atende os
pacientes sem se preocupar com pagamentos.

Primeiro eu me reuni com os dentistas, a secretária e o dono do
consultório, realizei entrevistas onde fiz algumas perguntas sobre como
é o trabalho deles e o fluxo de trabalho no dia-a-dia do consultório e
fiz cópias de fichas de pacientes e alguns relatórios que a secretária
faz para o dono do consultório semanal e mensalmente. Agora vou redigir
a descrição do mini-mundo deste consultório para entendermos como as
coisas funcionam no atendimento dos pacientes.

> No consultório odontológico ‘Dentibão’, situado na rua ‘X’, nº ‘1’ na
> cidade ‘Y’, estado de MG (‘Dentibão’ só poderia ser de MG né? rsrs),
> as consultas funcionam por ordem de chegada dos pacientes da seguinte
> maneira: O paciente, ao chegar no consultório, obtém do atendente uma
> senha numérica de ordem crescente e aguarda até o momento de ser
> chamado.\
> O atendente chama os pacientes pela ordem das senhas. Inicialmente o
> atendente solicita o nome do paciente e procura a ficha dele no
> arquivo de pacientes (que está em ordem alfabética). Se o paciente
> ainda não tiver ficha no consultório, então o atendente solicita os
> dados básicos do paciente para criar uma ficha para ele, estes dados
> são: CPF, Nome, Data de nascimento, endereço e telefones.\
> Com a ficha do paciente em mãos, o atendente pergunta ao paciente o
> motivo da consulta, que geralmente é *consulta de rotina* ou *dor de
> dente*. Então o atendente cria uma <span
> style="text-decoration: underline;">ficha de atendimento</span> com as
> informações de motivo da consulta, anexa à ficha do paciente e coloca
> em baixo da pilha de fichas para atendimentos do dentista. Neste
> momento o atendente diz ao paciente que espere que o dentista o chame,
> e finaliza o atendimento.\
> O dentista chama os pacientes pela ordem que o atendente organizou a
> pilha de fichas, mas antes de chamar cada paciente, o dentista analisa
> o histórico de atendimentos do paciente e o motivo que ele (paciente)
> descreveu para a consulta atual. Após atender o paciente, o dentista
> descreve detalhes do atendimento na ficha de atendimento, como
> diagnóstico, receita de remédios, solicitação de retorno, etc.
> Finaliza-se a consulta e paciente é liberado.

##Modelos Externos

Descrevi acima um exemplo básico de descrição de regras de negócio.
Agora vamos criar os primeiros modelos com as entidades e os
relacionamentos desta descrição de mini-mundo. Estes primeiros modelos
são conhecidos como **modelos externos**, pois devem ser de fácil
entendimento por todos os envolvidos, não apenas os técnicos, ou seja,
no nosso caso o dentista, o atendente, a secretária devem ser capazes de
entender esses modelos e opinar o que condiz ou não com a realidade e o
objetivo do novo banco de dados que está sendo projetado.

Para criar esses modelos iniciais podemos seguir uma dica simples:
identificar **substantivos** e **verbos** potenciais no texto. Os
substantivos podem ser Entidades e os verbos podem ser Relacionamentos.

Alguns substantivos potenciais para entidades: Paciente, Atendente,
Dentista, Atendimento, Histórico de atendimento, Senha…\
Alguns verbos potenciais para relacionamentos: Obter (Senha), Atender
(atendente atender paciente), Atender (dentista atender paciente),
Analisar (Atendimentos)…

Nestes modelos vamos adotar a notação mais utilizada para este fim, a
“[Notação de
Chen](http://pt.wikipedia.org/wiki/Modelo_de_entidade_e_relacionamento "Modelo de Entidades e Relacionamentos"){:target=\_blank}”,
também conhecida como MER (Modelo de Entidades e Relacionamentos) ou DER
(Diagrama de Entidades e Relacionamentos). Nesta notação as entidades
são representadas como retângulos e os relacionamentos como
losangos. Vamos criar então, os primeiros modelos baseados na descrição
acima.

Retorne ao texto do mini-mundo e leia o primeiro parágrafo.

![modelo-paciente-senha](/images/a-primeira-fase-de-um-projeto-de-banco-de-dados/modelo-paciente-senha.png){.aligncenter}

Acho que esse primeiro modelo tá entendível para uma pessoa leiga, né?
Esse é o objetivo do modelo externo! Dá pra lê-lo como “O atendente
fornece uma senha ao paciente”. Observe onde estão os substantivos e os
verbos. Este modelo representa a primeira etapa do atendimento, quando o
paciente chega ao consultório.

É importante notar que a ordem do atendimento não é importante para o
modelo desta etapa, pois isso não diz respeito a dados e sim a
lógica. Lembrando que o objetivo aqui é um projeto de banco de dados,
não os requisitos de "funcionamento" de um sistema.

Vamos fazer mais um modelo para o nosso mini-mundo:

![modelo-atendente-paciente](/images/a-primeira-fase-de-um-projeto-de-banco-de-dados/modelo-atendente-paciente.png){.aligncenter}

Deu pra perceber que um atendente “atende” um paciente e inicia a “Ficha
de atendimento”? Beleza, então vamos ao próximo modelo:

![modelo-dentista-paciente](/images/a-primeira-fase-de-um-projeto-de-banco-de-dados/modelo-dentista-paciente.png){.aligncenter}

Neste modelo dá pra ler que o Dentista “atende” o paciente. Certo?
Também dá pra ler que o dentista “conclui” o Atendimento atual (iniciado
pelo atendente). Além disso dá pra ler que o Dentista analisa os
atendimentos anteriores, com essa última leitura do modelo, percebemos
que a entidade “Atendimento” não representa só o atual, mas também os
anteriores. Com essa interpretação, podemos concluir que para os
atendimentos anteriores do paciente e o próprio atendimento atual, nem
sempre era o mesmo atendente e nem o mesmo dentista. Captou a ideia?

Vamos juntar tudo?

![modelo-entidade-relacionamento](/images/a-primeira-fase-de-um-projeto-de-banco-de-dados/modelo-entidade-relacionamento.png){.aligncenter}

Apareceu um relacionamento interessante quando juntamos tudo, um
“paciente recebe atendimento”. Após montar o modelo completo eu senti
falta desse relacionamento. Acho que agora qualquer um que olhar o
modelo vai entender o processo inteiro. E se não estiver claro, o modelo
deve ser melhorado! O modelo externo deve ser entendido “externamente”
ao profissional de desenvolvimento de software, ou seja, deve ser
entendido por qualquer um. O seu objetivo é ajudar todas as pessoas que
estão participando do projeto do banco de dados entenderem a mesma
coisa. Se você já tem um conhecimento de banco de dados, não pense em
tabelas agora, o importante é todo mundo entender o cenário.

##Conclusão

Vimos neste post como se inicia um projeto de banco de dados, desde
a captação e organização de dados junto aos <span
style="text-decoration: underline;">especialistas do domínio</span>, até
a análise e a criação de um documento e modelos externos que representam
diferentes visões do mini-mundo.

Repare que criamos vários modelos, cada um representa uma determinada
visão, visão do atendente, visão do dentista, visão geral, etc... Essa é
a ideia, na fase seguinte do projeto nós começamos a aprofundar nestes
modelos acrescentando informações

Espero que esse exemplo ajude a entender como os modelos podem ajudar na
transferência de conhecimento entre o profissional que entende do
negócio (no caso o dono do consultório), e os profissionais que
trabalham no desenvolvimento de softwares. Acredite, esses modelos são
de fundamental importância para o sucesso do banco de dados, pois uma
falha na comunicação aqui, resulta em um banco de dados ruim lá na
frente.

Pronto para iniciar um projeto de banco de dados? Qualquer dúvida, post
aqui em baixo nos comentários!
