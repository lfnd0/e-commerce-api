from typing import Dict
from ...repositories import UserRepository
from ...utils import Encryption
from ...models import User


class CreateUserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_data: Dict):
        username = user_data["username"]
        user = self.user_repository.fetch_user_by_username(username)

        if user:
            raise ValueError("user already exists")

        password = user_data["password"]
        hashed_password = Encryption.add_hash_password(password)
        new_user = User(username=username, password_hash=hashed_password)

        self.user_repository.create_user(new_user)
