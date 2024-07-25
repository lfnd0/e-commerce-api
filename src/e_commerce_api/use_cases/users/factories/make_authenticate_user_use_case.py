from ....repositories import SQLiteUserRepository
from .. import AuthenticateUserUseCase


def make_authenticate_user_use_case():
    sqlite_user_repository = SQLiteUserRepository()
    authenticate_user_use_case = AuthenticateUserUseCase(sqlite_user_repository)

    return authenticate_user_use_case
