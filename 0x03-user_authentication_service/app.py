#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from flask import url_for
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return:
      - Welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
    Function to create user
    Return:
    - User object JSON represented
    - 400 if the user is already registered
    """
    try:
        form = request.form
        email = form['email']
        password = form['password']
        new_user = AUTH.register_user(email, password)
        if new_user:
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions
    Function to log in a session
    Return:
    - A JSON payload of the form
    - 401 if the login information is incorrect
    """

    form = request.form
    email = form['email']
    password = form['password']
    valid_user = AUTH.valid_login(email, password)
    if valid_user:
        session_id = AUTH.create_session(email)
        message = jsonify({"email": email, "message": "logged in"})
        response = make_response(message)
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /sessions
    Function to respond to the DELETE /sessions route.
    Return:
    - If the user exists,  destroy the session and redirect the user to '/'.
    - If the user does not exist, respond with a 403 HTTP status.
    """
    user_cookie = request.cookies.get('session_id', None)
    valid_user = AUTH.get_user_from_session_id(user_cookie)
    if valid_user is None or user_cookie is None:
        abort(403)
    else:
        AUTH.destroy_session(valid_user.id)
        return redirect(url_for('index'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ GET /profile
    Function to respond to the GET /profile route.
    Return:
    - If the user exists, respond with a 200 HTTP status and
    a JSON payload.
    - If the session ID is invalid or the user does not exist,
    respond with a 403 HTTP status.
    """
    user_cookie = request.cookies.get('session_id', None)
    valid_user = AUTH.get_user_from_session_id(user_cookie)
    if valid_user is None or user_cookie is None:
        abort(403)
    else:
        return jsonify({"email": valid_user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ POST /reset_password'
    Function to respond to the POST /reset_password route.
    Return:
    - If the email is registered, generate a token, respond with
    a 200 HTTP status and a JSON payload.
    - If the email is not registered, respond with a 403 HTTP status.
    """
    form = request.form
    email = form.get('email', '')
    session_id = AUTH.create_session(email)
    if email is None or session_id is None:
        abort(403)
    else:
        new_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": new_token}), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ PUT /reset_password'
    Function to respond to the PUT /reset_password route.
    Return:
    - If the token is valid, respond with a 200 HTTP status
    and a JSON payload.
    - If the token is not registered, respond with a 403 HTTP status.
    """
    form = request.form
    email = form.get('email', '')
    reset_token = form.get('reset_token', '')
    new_password = form.get('new_password', '')
    if email is None or reset_token is None or new_password is None:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
        message = {"email": email, "message": "Password updated"}
        return jsonify(message), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
