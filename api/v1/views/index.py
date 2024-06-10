#!/usr/bin/python3
"""
for index
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API"""
    data = jsonify({"status": "OK"})
    data.status_code = 200
    return data


@app_views.route("/stats", methods=['GET'])
def stats():
    """
    route to return stats of all objects
    """
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }

    res = jsonify(data)
    res.status_code = 200

    return res
