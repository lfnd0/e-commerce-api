from abc import ABC, abstractmethod
from ...models import User


class UserRepository(ABC):

    @abstractmethod
    def create_user(self, user_data: User) -> None:
        pass

    @abstractmethod
    def fetch_user_by_username(self, username: str) -> User:
        pass
