from e_commerce_api import app
from ..controllers import read_root

@app.route("/api")
def get_root():
    return read_root()
