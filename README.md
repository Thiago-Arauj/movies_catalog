# Movies Catalog

## Descrição

O **Movies Catalog** é um projeto que permite catalogar filmes de forma prática e organizada. Ele oferece funcionalidades para listar, adicionar, editar e remover filmes, facilitando o gerenciamento de um acervo pessoal ou profissional de filmes.

Este projeto é ideal para quem deseja ter um controle simples e eficiente sobre seus filmes favoritos, podendo ser utilizado como base para projetos maiores ou como ferramenta independente.

## Funcionalidades

- Listagem de filmes cadastrados
- Adição de novos filmes ao catálogo
- Edição dos dados dos filmes existentes
- Remoção de filmes do catálogo
- Interface simples e intuitiva para facilitar o uso

## Tecnologias Utilizadas

- Python
- Django
- PostgreSQL

## Como Rodar o Projeto

### Pré-requisitos

- Ter instalado [Python](https://www.python.org/)
- Ter instalado [Pgadmin](https://www.pgadmin.org/download/)

### Passos para instalação

1. Clone o repositório:
```
git clone https://github.com/Thiago-Arauj/movies_catalog.git
```

2. Acesse a pasta do projeto:
```
cd movies_catalog
```

3. Crie sua venv:
   - No windows:
      ```
      py -m venv venv
      ```
      ou
      ```
      python -m venv venv
      ```
    - No linux:
      ```
      python3 -m venv venv
      ```
4. Ative sua venv:
   - No windows:
      ```
      venv\Scripts\activate
      ```
   - No linux:
     ```
      source venv\bin\activate
     ```

5. Instale as dependências:
   - No windows:
      ```
      pip install -r requirements.txt
      ```
   - No linux:
     ```
     pip3 install -r requirements.txt
     ```
6. Prepare o projeto:
```
py manage.py makemigrations
```
```
py manage.py migrate
```
7. Execute o projeto:
```
py manage.py runserver
```

## Como Contribuir

Contribuições são bem-vindas! Para contribuir com o projeto, siga os passos abaixo:

- Faça um fork deste repositório
- Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`)
- Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
- Faça push para a branch (`git push origin feature/nome-da-feature`)
- Abra um Pull Request descrevendo suas alterações
