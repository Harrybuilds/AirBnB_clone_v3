#!/usr/bin/python3
"""
State objects that handles all default RESTFul API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.state import State


METHODS = ['GET', 'POST', 'PUT', 'DELETE']


@app_views.route('/states', methods=METHODS, strict_slashes=False)
@app_views.route("/states/<state_id>", methods=METHODS, strict_slashes=False)
def state_handler(state_id=None):
    """ handles all states API endpoints """
    req_methods_handler = {
        "GET": get_states,
        "POST": create_state,
        "PUT": update_state,
        "DELETE": delete_state_by_id
    }
    if request.method in req_methods_handler:
        return req_methods_handler[request.method](state_id)


def get_states(state_id=None):
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    if state_id:
        fetched_obj = storage.get(State, str(state_id))

        if fetched_obj is None:
            abort(404)

        return jsonify(fetched_obj.to_dict())
    return jsonify([state.to_dict() for state in states]), 200


def create_state(state_id=None):
    """
    returns newly created state obj
    """
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, 'Not a JSON')
    if "name" not in state_json:
        abort(400, 'Missing name')

    new_state = State(**state_json)
    new_state.save()
    resp = jsonify(new_state.to_dict())

    return resp, 201


def update_state(state_id=None):
    """
    updates specific State object by ID
    :param state_id: state object ID
    :return: state object and 200 on success, or 400 or 404 on failure
    """
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, 'Not a JSON')

    fetched_obj = storage.get(State, str(state_id))

    if fetched_obj is None:
        abort(404)
    for key, val in state_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(fetched_obj, key, val)
    fetched_obj.save()
    return jsonify(fetched_obj.to_dict()), 200


def delete_state_by_id(state_id=None):
    """
    deletes State by id
    :param state_id: state object id
    :return: empty dict with 200 or 404 if not found
    """

    fetched_obj = storage.get(State, str(state_id))

    if fetched_obj is None:
        abort(404)

    storage.delete(fetched_obj)
    storage.save()

    return jsonify({}), 200
