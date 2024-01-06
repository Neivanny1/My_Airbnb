#!/usr/bin/python3
"""
Create a route '/status' on onject app_views
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status", methods=["GET"])
def status():
    """
    Returns JSON response for REST api health
    """
    status = {"status": "ok"}
    return jsonify(status)
