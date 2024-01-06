#!/usr/bin/python3
"""
Returning json
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status")
def status():
    """
    Returns status
    """
    status = {"status": "ok"}
    return jsonify(status)
