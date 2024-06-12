#!/usr/bin/python3
"""
routea for index
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.user import User


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Returns the status of the API"""
    data = jsonify({"status": "OK"})
    data.status_code = 200
    return data


@app_views.route("/stats", strict_slashes=False)
def get_stats():
    """
    route to return stats of all objects
    """
    data = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
        }

    res = jsonify(data)
    res.status_code = 200

    return res
