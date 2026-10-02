# UniFood

Sistema de gestão de pedidos e estoque para cantinas universitárias da UNIVASF.

## Comandos para rodar localmente

Este projeto utiliza uma Máquina Virtual para garantir que toda a equipe desenvolva no mesmo ambiente (Ubuntu 20.04).

## Pré-requisitos

* VirtualBox
* Vagrant
* Git

## Passo a Passo de Configuração

### 1. Clonar no local correto (Windows)

O projeto **deve obrigatoriamente** ser clonado dentro da pasta que o seu Vagrant compartilha com a máquina virtual (pasta `web-folder`). 

Abra o terminal do Windows (CMD ou PowerShell), entre na sua `web-folder` e clone o repositório:

```bash
cd caminho\para\sua\web-folder
git clone https://github.com/joao-vitor01/UniFood-SD.git 
```

### 2. Inicie a Máquina Virtual:

    vagrant up

### 3. Acesse a Máquina Virtual:

    vagrant ssh

### 4. Preparar o ambiente e instalar Dependências:

    source ~/venv/bin/activate

    cd /vagrant/web-folder/projeto-SD
    
    pip install django faker

### 5. Popular o Banco de Dados:
    python manage.py migrate
    python popular_bd.py

### 6. Iniciar o Servidor:

    python manage.py runserver 0:8000

## 7. Acessar o Sistema:

    http://localhost:8000

    Painel Administrativo: http://localhost:8000/admin

 Aviso obre a Rede: Para o acesso via localhost:8000 funcione, o arquivo .Vagrantfile da sua maquina virtual precisa ter esta linha de redirecionamento configurada:
    
    config.vm.network "forwarded_port", guest: 8000, host: 8000

