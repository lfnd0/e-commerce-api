from dotenv import load_dotenv

load_dotenv()

from e_commerce_api import app_module, app


def run():
    app_module.run()


if __name__ == "__main__":
    app_module.run()
