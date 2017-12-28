title: Padronizando ambiente de desenvolvimento com Vagrant
date: 2016-01-12
author: Gustavo Furtado de Oliveira Alves
category: { Dicas de Programação }
tags: Ferramentas
slug: padronizando-ambiente-de-desenvolvimento-com-vagrant

Com a evolução do desenvolvimento de um projeto de software é normal a
necessidade de adicionar novos pacotes, configurações de ambiente, etc.
Também no inicio de um projeto, geralmente é necessário adicionar todas
as dependências do projeto nas máquinas de todos os desenvolvedores.

É comum ouvir aqueles clássicos "Na minha máquina funciona" ou "Adiciona
o XPTO.jar no seu classpath" ou "instala o pacote ABC" e por aí vai.

Uma das melhores formas de resolver este problema é usando o
**[Vagrant](https://www.vagrantup.com/){:target=\_blank}**, que colocar a configuração do
ambiente de desenvolvimento no próprio repositório do código.

Neste post você vai entender como funciona e como utilizar essa
ferramenta fantástica e cada vez mais utilizada por grandes times de
desenvolvimento de softwares, impulsionado pela filosofia **DevOps**.

![vagrant](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/vagrant.jpg){:width=100%}

##Como funciona o Vagrant

Através de poucos arquivos de configuração (um ou dois), o Vagrant cria
uma máquina virtual (com VirtualBox ou VMWare) e instala todas as
configurações necessárias. Deixando o ambiente de desenvolvimento pronto
para trabalhar, em qualquer máquina que você esteja.

Uma das coisas mais interessantes é que as configurações do ambiente são
aplicadas apenas à máquina virtual e não no seu sistema operacional
hospedeiro.

Outro grande benefício é poder trabalhar em vários projetos com
ambientes completamente diferentes. Por exemplo, é possível trabalhar
num projeto com Python 3.0 e em outro projeto com o Python 2.5. Sem nem
precisar instalar o Python no seu computador.

Para criar o ambiente do projeto que você vai trabalhar, basta acessar a
pasta do projeto pelo prompt de comando e digitar "vagrant up". Pronto,
o Vagrant vai baixar a imagem do repositório, inicia a máquina
virtual e, caso configurado) instala todos os pacotes necessários para o
desenvolvimento do projeto.

A máquina virtual é criada apenas na primeira vez, nas próximas
execuções de "vagrant up" o vagrant só verifica se tem algum novo pacote
a ser instalado.

##Instalação do Vagrant

Antes de instalar o Vagrant é preciso instalar o VirtualBox que vai ser
o responsável por executar as máquinas virtuais do vagrant. Baixe o
instalador do VirtualBox em
<https://www.virtualbox.org/wiki/Downloads> e instale-o no seu sistema
operacional. A instalação é simples. Veja abaixo algumas imagens da
instalação do VirtualBox no Windows. O VirtalBox também é suportado
pelo Mac e Linux.

<span style="text-decoration: underline;">**\*\*Off
topic**</span>: Atualmente eu trabalho no Linux Mint, mas instalei o
Virtualbox e o vagrant num Windows 10 para testar e funcionou
normalmente. Só o acesso ssh que é um pouco diferente no windows, mas
vou dar uma superdica mais abaixo.

![Wizard-VirtualBox-1](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-1.png){.aligncenter}

![Wizard-VirtualBox-2](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-2.png){.aligncenter}

![Wizard-VirtualBox-3](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-3.png){.aligncenter}

![Wizard-VirtualBox-4](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-4.png){.aligncenter}

![Wizard-VirtualBox-5](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-5.png){.aligncenter}

![Wizard-VirtualBox-6](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-6.png){.aligncenter}

![Wizard-VirtualBox-7](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-VirtualBox-7.png){.aligncenter}

Para instalar o Vagrant você só precisa acessar a página de download do
Vagrant <https://www.vagrantup.com/downloads.html>, baixar o instalador
apropriado para o seu sistema operacional e seguir o passo a passo da
instalação. Abaixo eu mostro algumas imagens das telas da instalação do
Vagrant no Windows. No Linux e no Mac é tão simples quanto no Windows.

![Wizard-Vagrant-1](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-Vagrant-1.png){.aligncenter}

![Wizard-Vagrant-2](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-Vagrant-2.png){.aligncenter}

![Wizard-Vagrant-3](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-Vagrant-3.png){.aligncenter}

![Wizard-Vagrant-4](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-Vagrant-4.png){.aligncenter}

![Wizard-Vagrant-5](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-Vagrant-5.png){.aligncenter}

![Wizard-Vagrant-6](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Wizard-Vagrant-6.png){.aligncenter}

O instalador acrescentará os comandos do Vagrant no Path do seu sistema
operacional. Isso significa que você poderá executar os <span
style="text-decoration: underline;">comandos do vagrant</span> via linha
de comando em qualquer pasta que você estiver. Veremos mais sobre os
comandos do vagrant mais adiante neste post. Caso os comandos não
funcionem, reinicie o sistema operacional.

##Configuração do ambiente de desenvolvimento

A primeira coisa que você precisa saber é que quando você inicia a
máquina virtual do Vagrant para o seu projeto pela primeira vez ele
vai baixar uma imagem e iniciar a VM. Essas imagens de máquinas
virtuais ficam armazenadas em repositórios online e são chamadas
de **Boxes** ("Box" no singular).

Existem boxes que já vem com várias coisas instaladas prontas para
desenvolver. Eu, particularmente, prefiro pegar um ubuntu limpo e criar
um script para instalar as dependências que vou precisar para o meu
projeto. Para visualizar as boxes disponíveis no repositório do Vagrant
acesse: <https://atlas.hashicorp.com/boxes/search>.

Entendido o que são boxes (imagens de sistemas operacionais), vamos
criar a nossa configuração do Vagrant. Para isto basta criar um arquivo
chamado **Vagrantfile** na raiz do seu projeto com o conteúdo abaixo:

```
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
end
```

O **Vagrantfile** é o principal arquivo de configuração do Vagrant. Ele
define qual a <span style="text-decoration: underline;">box</span> que
será instalada na VM.

Para que o Vagrant crie o **Vagrantfile** para você, basta acessar
a pasta do seu projeto via prompt de comando e execute "**vagrant init
ubuntu/trusty64**".

Esse comando apenas cria o **Vagrantfile** já configurado com a box
"ubuntu/trusty64" e um monte de comentários (em inglês) para mais opções
configurações.

"ubuntu/trusty64" é uma box básica com o **Ubuntu 14.04 LTS
64-bit**, mas você pode configurar qualquer box que esteja no
repositório do Vagrant, você pode encontrar novas boxes
acessando <https://atlas.hashicorp.com/boxes/search>.

Com o arquivo **Vagrantfile **criado, agora você pode iniciar a sua VM
com o comando **vagrant up**. O Vagrant vai baixar a box configurada,
inicializar a VM e pronto, sua VM já está rodando.

##Acessar a máquina virtual

O Vagrant usa SSH para acessar suas VMs. Se você usa linux, para acessar
a máquina virtual do seu projeto basta digitar o comando **vagrant ssh**
e você já estará conectado à VM. Mas se você usa Windows é um pouquinho
diferente.

O Windows não possui um cliente SSH nativo. Então você deve usar um
client SSH como o [Putty](http://www.putty.org/){:target=\_blank}. Mas tem uma forma
melhor ... [Instalar o git](https://git-scm.com/){:target=\_blank}! O git adiciona um
client ssh no Path do Windows e como resultado o comando **vagrant ssh**
funciona no Windows. Basta instalar o git e selecionar a opção **"Use
Git and optional Unix tools from the Windows Command Prompt"** conforme
a imagem abaixo.

![Git-SSH-Windows](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/Git-SSH-Windows.png){.aligncenter}

Com o git instalado e selecionada a opção de usar ferramentas opcionais
do Unix no prompt de comando do Windows, o comando **vagrant ssh**
funciona como no Linux.

Após executar **vagrant ssh** você estará conectado à máquina virtual.

A pasta do seu projeto com o seus arquivos são acessíveis dentro da VM
na pasta /vagrant. Se você quiser acessar os arquivos do seu projeto de
dentro da VM basta acessar a VM com o **vagrant ssh** e abrir a pasta
/vagrant através do comando **cd /vagrant**.

##Scripts de instalação de dependências

Se tudo correu bem até aqui, você já tem uma máquina virtual funcionando
e acessível. Agora vamos ver como automatizar a instalação de
dependências através de scripts. Para isso você deve criar um
script *bash* com os comandos a serem executados ao iniciar a sua VM
através do vagrant up e configurar o *Vagrantfile* para identificá-lo.

Vamos supor que você deseja instalar o *nginx* para servir o seu projeto
como um site. Para isso crie um arquivo chamado **nginx.sh** com o
script abaixo.

```bash
#!/usr/bin/env bash

apt-get update
apt-get install -y nginx
if ! [ -L /usr/share/nginx/html ]; then
 rm -rf /usr/share/nginx/html
 ln -fs /vagrant /usr/share/nginx/html
fi
```

No *Vagrantfile* você deve apontar esse script com a configuração de
um provision conforme abaixo.

```
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, path: "nginx.sh"
end
```

Pronto, agora quando você iniciar o seu ambiente de desenvolvimento
com **vagrant up** o nginx será instalado na sua máquina e a pasta do
seu projeto **/vagrant** será configurada como raiz do seu site.

Você pode configurar outros scripts no *Vagrantfile*.

Se a sua VM já estiver rodando, você pode forçar a execução dos scripts
com o comando **vagrant provision**.

##Compartilhamento de portas

Agora que você já sabe configurar o vagrant para instalar
automaticamente todas as dependências do seu projeto através de scripts
*bash*. Como você acessaria o seu site para teste a partir da sua
máquina host? É possível configurar o vagrant para mapear portas entre a
máquina host e a VM. Alterei o nosso *Vagrantfile* para mapear a porta
80 da VM (porta padrão do apache) para a porta 8000 da máquina host.

```
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, path: "nginx.sh"
  config.vm.network :forwarded_port, guest: 80, host: 8000
end
```

Para atualizar a VM com o mapeamento da porta, basta executar **vagrant
reload**.

##Testando o novo ambiente de desenvolvimento

Para testar se a nossa configuração do Vagrant funcionou, vamos criar um
arquivo index.html na pasta do projeto com uma página de exemplo.

```
<html>
<head><title>Testando o Vagrant</title></head>
<body>
<h1>O Vagrant funcionou!</h1>
</body>
</html>
```

Na máquina host podemos acessar o endereço http://localhost:8000 e a
nossa página de exemplo está funcionando.

![teste do
vagrant](/images/padronizando-ambiente-de-desenvolvimento-com-vagrant/teste-do-vagrant-e1452366196423.png){.aligncenter}

##Comandos

Abaixo listo alguns comando do vagrant para referência.

-   **vagrant init**: Este comando cria o arquivo **Vagrantfile** na
    pasta em que o comando foi executado. O parâmetro seguinte ao
    comando é o nome da Box que será utilizada. Por exemplo ****vagrant
    init ubuntu/trusty64**** configura no Vagrantfile a box que tem um
    Linux Ubuntu 14.04 LTS. O arquivo Vagrantfile criado pelo
    comando **vagrant init** é cheio de comentários de possíveis
    configurações do Vagrant, é interessante lê e tentar entender
    estas configurações.
-   **vagrant up**: Este comando inicia a máquina virtual e instala
    todas as dependências configuradas no **Vagrantfile**. Quando este
    comando é executado a primeira vez, a **box** é baixada, a máquina
    virtual é instalada e todasas dependências configuradas são
    instaladas na VM. Nas execuções seguintes de vagrant up, apenas as
    novas dependências são instaladas.
-   **vagrant suspend**: Este comando suspende a execução da máquina
    virtual, liberando memória. É como se desligasse a VM, mas mantendo
    o estado da máquina.
-   **vagrant resumo**: Este comando restaura a execução de uma
    VM suspensa.
-   **vagrant halt**: Este comando desliga a VM.
-   **vagrant reload**: Este comando reinicia a VM e reavalia o
    Vagrantfile para instalação de novas dependências. É o mesmo
    que **vagrant halt + vagrant up**.
-   **vagrant ssh**: Este comando faz uma conexão via ssh com a
    máquina virtual. Funciona nativamente no Linux e no Mac, para o
    funcionar no Windows, siga as instruções da Sessão "ACESSAR A
    MÁQUINA VIRTUAL" deste artigo para verificar como fazer este
    comando funcionar.
-   **vagrant box add**: Este comando baixa e instala uma box para
    o seu computador. Dessa forma quando quando você executar uma vm
    pela primeira vez a box não precisará ser baixada da internet.
-   **vagrant destroy**: Este comando remove a vm do seu computador. Ou
    seja, quando você executar **vagrant up** novamente a VM será
    instalada do zero novamente.
-   **vagrant provision**: Força a execução dos scripts

Existem muitos outros comandos do Vagrant, para obter uma lista de todos
os comandos, basta digitar **vagrant** no prompt de comando e todas as
opções são apresentadas.

##Conclusão

Meu objetivo com este post é mostrar como utilizar o vagrant para
automatizar a criação de ambiente de desenvolvimento. Isso é muito útil
para equipes de desenvolvimento de softwares pois elimina configurações
manuais na máquina de cada integrante da equipe e simplifica o trabalho.
Basta baixar o código do repositório, digitar **vagrant up** e pronto, o
seu ambiente de trabalho está funcional. Com o vagrant a configuração do
ambiente de desenvolvimento fica junto com o código do projeto no
repositório de código.

É interessante notar que cada desenvolvedor pode usar a IDE que desejar
na máquina host.

Há muitas opções de configuração do vagrant. Mostrei aqui uma
configuração básica, mas o vagrant pode ser usado junto com Docker,
Chef, muitas opções de provisioning, muitas boxes já configuradas, etc.
Acesse <https://docs.vagrantup.com/> para ver a documentação.

Eu uso o Vagrant em vários projetos, e você? Você já conhecia o Vagrant?
Deixe aí em baixo o seu comentário!
