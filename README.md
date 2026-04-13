# Job Tracker RPA

Projeto de automação web desenvolvido com **Python, Django e
SeleniumBase** para coletar e visualizar vagas de emprego em uma
interface web simples.

O sistema executa um processo de **web scraping automatizado**, armazena
os dados em banco e disponibiliza um **painel para consulta e
atualização das vagas**.

------------------------------------------------------------------------

# Objetivo do Projeto

Este projeto demonstra conceitos importantes utilizados em **RPA
(Robotic Process Automation)**:

-   navegação automatizada em páginas web
-   extração estruturada de dados
-   persistência em banco de dados
-   interface para consulta dos dados coletados
-   execução manual da automação via interface ou terminal

------------------------------------------------------------------------

# Tecnologias Utilizadas

-   Python
-   Django
-   SeleniumBase
-   SQLite
-   HTML / CSS

------------------------------------------------------------------------

# Funcionalidades

-   Web scraping automatizado de vagas
-   Armazenamento dos dados em banco de dados
-   Listagem web das vagas coletadas
-   Busca por título da vaga
-   Painel administrativo com Django Admin
-   Atualização manual das vagas pela interface
-   Comando CLI para executar scraping

------------------------------------------------------------------------

# Estrutura do Projeto

    Job_Tracker
    │
    ├── core/                      # Configurações principais do Django
    │   ├── settings.py
    │   ├── urls.py
    │
    ├── jobs/                      # App principal do projeto
    │   ├── management/
    │   │   └── commands/
    │   │       └── scrape_jobs.py
    │   │
    │   ├── templates/
    │   │   └── jobs/
    │   │       └── job_list.html
    │   │
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── scraper.py
    │
    ├── manage.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# Como Executar o Projeto

## 1. Clonar o repositório

``` bash
git clone https://github.com/SEU_USUARIO/job-tracker-rpa.git
cd job-tracker-rpa
```

------------------------------------------------------------------------

## 2. Criar ambiente virtual (recomendado)

Linux / Mac:

``` bash
python -m venv venv
source venv/bin/activate
```

Windows:

``` bash
venv\Scripts\activate
```

------------------------------------------------------------------------

## 3. Instalar dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 4. Rodar migrações

``` bash
python manage.py migrate
```

------------------------------------------------------------------------

## 5. Executar scraping inicial

``` bash
python manage.py scrape_jobs
```

------------------------------------------------------------------------

## 6. Iniciar o servidor

``` bash
python manage.py runserver
```

------------------------------------------------------------------------

## 7. Acessar o sistema

Painel de vagas:

http://127.0.0.1:8000/jobs/

Admin Django:

http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

# Executando o Scraper

O scraper pode ser executado de duas formas.

### Via terminal

``` bash
python manage.py scrape_jobs
```

### Via interface

No painel web existe um botão **"Atualizar vagas"** que executa a
coleta.

------------------------------------------------------------------------

# Como Funciona o Scraper

O scraper utiliza **SeleniumBase** para:

1.  abrir a página de vagas
2.  localizar os cards de vagas
3.  extrair:
    -   título
    -   empresa
    -   localização
    -   URL
4.  retornar os dados estruturados
5.  salvar no banco via Django ORM

Para evitar duplicação de registros, o sistema utiliza uma constraint
baseada em:

(title, company, location)

------------------------------------------------------------------------

# Possíveis Melhorias Futuras

-   paginação das vagas
-   filtros por empresa e localização
-   agendamento automático do scraper
-   exportação de dados para CSV
-   integração com APIs de vagas

------------------------------------------------------------------------

# Autor

Lucas Cruz

Projeto desenvolvido para fins de estudo e demonstração de automação web
com Python.

------------------------------------------------------------------------

# Licença

MIT
