# UniFood

Sistema de gestão de pedidos e estoque para cantinas universitárias da UNIVASF.

## Como Rodar o Projeto com Docker (Recomendado)

A forma mais rápida de executar o projeto localmente é utilizando o Docker.

### Pré-requisitos
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução (com backend WSL 2 no Windows)
* Git

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/joao-vitor01/UniFood-SD.git](https://github.com/joao-vitor01/UniFood-SD.git)
   cd UniFood-SD
    ```

2. **Construir a imagem e iniciar o container:**
    ```bash
    docker compose up --build
    ```

3. **Acessar o sistema:**
    ```bash
    http://localhost:8000/admin
    ```
## Comando úteis do Docker

* Parar o container:
    ```bash
    docker compose down
    ```

* Executar migrações do banco(caso altere models):

    ```bash
        docker compose exec web python manage.py makemigrations
        docker compose exec web python manage.py migrate
    ```

* Criar um novo superusuário:

    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

* Rodar script de povoamento:

    ```bash
    docker compose exec web python popular_bd.py
    ```

### Como rodar após a primeira instalação

Depois que a imagem já foi construída e o banco configurado, você não precisa rodar --build nem recriar usuário:

* Iniciar o servidor:

    ```bash
    docker compose up
    ```

* Parar o servidor:
    Pressione Control + c no terminal ou execute: 
    ```bash
    docker compose down
    ```
## Fluxo de Trabalho (Git)

Para mantermos o site no ar sem interrupções e facilitar o desenvolvimento de todos, utilizaremos apenas **duas branches**:

- **`develop`**: Onde **todo mundo trabalha diretamente**. Todas as telas, correções e alterações devem ser feitas e enviadas aqui.
- **`main`**: Branch de **produção** (conectada ao deploy automático no Render). **Ninguém commita diretamente na `main`**.

---

### Como trabalhar no dia a dia (Passo a Passo)

Sempre que for começar a programar ou adicionar uma funcionalidade:

#### 1. Garantir que está na `develop` e atualizado
Antes de alterar qualquer código, puxe as últimas alterações feitas pelo grupo:

```bash
git checkout develop
git pull origin develop
```

## Comandos para rodar com a VM

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

    cd /vagrant/web-folder/UniFood-SD
    
    pip install django faker

### 5. Popular o Banco de Dados:
    python manage.py migrate
    python popular_bd.py

### 6. Iniciar o Servidor:

    python manage.py runserver 0:8000

## 7. Acessar o Sistema:

    http://localhost:8000

    Painel Administrativo: http://localhost:8000/admin

 Aviso sobre a Rede: Para o acesso via localhost:8000 funcione, o arquivo .Vagrantfile da sua maquina virtual precisa ter esta linha de redirecionamento configurada:
    
    config.vm.network "forwarded_port", guest: 8000, host: 8000

