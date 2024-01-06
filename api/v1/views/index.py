#!/usr/bin/python3
"""
Create a route '/status' on onject app_views
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Returns JSON response for REST api health
    """
    status = {"status": "ok"}
    return jsonify(status)


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def count():
    """
    Returns numbe rof each object type
    """
    return jsonify(
        amenities=storage.count('Amenity'),
        cities=storage.count('City'),
        places=storage.count('Place'),
        reviews=storage.count('Review'),
        states=storage.count('State'),
        users=storage.count('User')
    )
