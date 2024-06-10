
#!/usr/bin/python3

from models import storage
from flask import Flask

app = Flask("__name__")


@app.route("/api/v1/stats", strict_slashes=False)
def stat():
    return storage.count()
