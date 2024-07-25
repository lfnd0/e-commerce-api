from .. import CreateUserUseCase
from ....repositories import SQLiteUserRepository

def make_create_user_use_case():
    sqlite_user_repository = SQLiteUserRepository()
    create_user_use_case = CreateUserUseCase(sqlite_user_repository)

    return create_user_use_case
