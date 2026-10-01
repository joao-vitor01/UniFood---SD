# UniFood

Sistema de gestão de pedidos e estoque para cantinas universitárias da UNIVASF.

## Comandos para rodar localmente

Este projeto utiliza uma Maquina Virtual para garantir que toda a equipe desenvolva no mesmo ambiente (Ubuntu 20.04).

## Pré-requisitos

* VirtualBox
* Vagrant

## Passo a Passo

1. Clone o repositório:
    git clone 
    cd unifood

2. Inicie a Máquina Virtual:

    vagrant up

3. Acesse a Máquina Virtual:

    vagrant ssh

4. Inicie o servidor:

    source ~/venv/bin/activate
    cd /vagrant/web-folder/unifood
    python manage.py runserver 0:8000

5. Acesse no navegador:

    http://localhost:8000

 Aviso obre a Rede: Para o acesso via localhost:8000 funcione, o arquivo .Vagrantfile da sua maquina virtual precisa ter esta linha de redirecionamento configurada:
    
    config.vm.network "forwarded_port", guest: 8000, host: 8000

