# E-Commerce API

### Techs
- [Poetry](https://python-poetry.org/docs/#installation)

### Bootstrap do projeto

#### Instalação das dependências
```sh
poetry install
```

#### Configuração do banco de dados
##### Execuçao do *shell* no Flask
```sh
poetry run flask shell
```
##### Criação da base de dados
```sh
db.create_all()
db.session.commit()
exit()
```

#### Execução da API
```sh
poetry run dev
```
