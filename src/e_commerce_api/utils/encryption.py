import os
from bcrypt import gensalt, hashpw, checkpw


class Encryption:

    @classmethod
    def add_hash_password(cls, password: str):
        encoded_password = cls.__encode_password_to_bytes(password)

        salt_rounds = int(os.getenv("SALT_ROUNDS"))
        print(salt_rounds)
        salt = gensalt(salt_rounds)

        hashed_password = hashpw(encoded_password, salt)

        return cls.__decode_password_to_string(hashed_password)

    @classmethod
    def check_password(cls, password: str, password_hash: str):
        encoded_password = cls.__encode_password_to_bytes(password)
        encoded_password_hash = cls.__encode_password_to_bytes(password_hash)

        return checkpw(encoded_password, encoded_password_hash)

    @classmethod
    def __encode_password_to_bytes(cls, password: str):
        return password.encode("utf-8")

    @classmethod
    def __decode_password_to_string(cls, password: bytes):
        return password.decode("utf-8")
