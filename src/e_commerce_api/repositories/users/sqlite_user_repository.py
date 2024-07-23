from . import UserRepository
from ...models import User
from e_commerce_api import db


class SQLiteUserRepository(UserRepository):

    def create_user(self, user_data: User):
        db.session.add(user_data)
        db.session.commit()

    def fetch_user_by_username(self, username: str) -> User:
        user = User.query.filter_by(username=username).first()
        return user
