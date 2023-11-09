#!/usr/bin/env python3
""" Module Flask view that handles all routes for the Session authentication.
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    Return:
      - Access to user. Otherwise, create a Session ID for the User ID.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email == '':
        return jsonify({"error": "email missing"}), 400
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password == '':
        return jsonify({"error": "password missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    user_credentials = {'email': email, }
    user = User()
    result = user.search(user_credentials)
    if not result:
        return jsonify({"error": "no user found for this email"}), 404
    user = result[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie_name = os.getenv('SESSION_NAME')
    result = jsonify(user.to_json())
    result.set_cookie(cookie_name, session_id)
    return result


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ DELETE /auth_session/logout
    Return:
      - An empty JSON dictionary with the status code 200.
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        return abort(404)
    return jsonify({}), 200
