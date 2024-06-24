# E-Commerce API

### :hammer_and_wrench: Techs
- [Poetry](https://python-poetry.org/docs/#installation)

### Bootstrap do projeto

#### :arrow_down: Instalação das dependências
```sh
poetry install
```

#### :gear: Configuração do banco de dados
1. Execução do *shell* no Flask
   ```sh
   poetry run flask shell
   ```
2. Criação da base de dados
   ```sh
   db.create_all()
   db.session.commit()
   exit()
   ```

#### :fire: Execução da API
```sh
poetry run dev
```
