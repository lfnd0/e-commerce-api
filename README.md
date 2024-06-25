# E-Commerce API

### Techs
- [Poetry](https://python-poetry.org/docs/#installation)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart)
- [Flask-Marshmallow](https://pypi.org/project/flask-marshmallow/#description)
- [SQLite](https://www.sqlite.org/index.html)

### Bootstrap do projeto

#### :construction: Instalação das dependências
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

### Autor
[Luiz Fernando](https://github.com/lfnd0)
