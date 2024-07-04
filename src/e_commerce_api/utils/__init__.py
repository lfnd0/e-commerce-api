def encode_password(password: str):
    return password.encode("utf-8")

def decode_password(password: bytes):
    return password.decode("utf-8")
