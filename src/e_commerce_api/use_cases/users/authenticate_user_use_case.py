from typing import Dict
from ...repositories import UserRepository
from ...utils import Encryption


class AuthenticateUserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_data: Dict):
        username = user_data["username"]

        user = self.user_repository.fetch_user_by_username(username)
        if not user:
            raise ValueError("invalid credentials")

        password = user_data["password"]
        password_hash = user.password_hash

        is_valid_password = Encryption.check_password(password, password_hash)
        if not is_valid_password:
            raise ValueError("invalid credentials")

        return user
