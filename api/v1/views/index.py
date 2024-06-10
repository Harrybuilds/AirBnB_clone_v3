#!/usr/bin/python3

from flask import jsonify
from api.v1.views import app_views
from models import storage

print(storage.all())


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

