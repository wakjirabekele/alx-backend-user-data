# Python - User authentication service

## Description of the files inside this folder:


0. Create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy). The model will have the following attributes:
- id, the integer primary key
- email, a non-nullable string
- hashed_password, a non-nullable string
- session_id, a nullable string
- reset_token, a nullable string

1. Create a DB class. Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database.
2. Implement the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point. Make sure that SQLAlchemy’s NoResultFound and InvalidRequestError are raised when no results are found, or when wrong query arguments are passed, respectively. Import NoResultFound from sqlalchemy.orm.exc.
3. Implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None. The method will use find_user_by to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database. 
If an argument that does not correspond to a user attribute is passed, raise a ValueError.
4. Define a _hash_password method that takes in a password string arguments and returns bytes. The returned bytes is a salted hash of the input password, hashed with bcrypt.hashpw.
5. Create class Auth and implement the method Auth.register_user. This method should take mandatory email and password string arguments and return a User object. If a user already exist with the passed email, raise a ValueError with the message User already exists. If not, hash the password with _hash_password, save the user to the database using self._db and return the User object.
6. Set up a basic Flask app. Create a Flask app that has a single GET route ("/") and use flask.jsonify to return a JSON payload.
7. Implement the end-point to register a user. Define a users function that implements the POST /users route. Import the Auth object and instantiate it at the root of the module. The end-point should expect two form data fields: "email" and "password". If the user does not exist, the end-point should register it and respond with a JSON payload. If the user is already registered, catch the exception and return a JSON payload of the form and return a 400 status code. Remember that you should only use AUTH in this app. DB is a lower abstraction that is proxied by Auth. 
8. Implement the Auth.valid_login method. It should expect email and password required arguments and return a boolean. Try locating the user by email. If it exists, check the password with bcrypt.checkpw. If it matches return True. In any other case, return False.
9. Implement a _generate_uuid function in the auth module. The function should return a string representation of a new UUID. Use the uuid module. Note that the method is private to the auth module and should NOT be used outside of it.
10. Implement the Auth.create_session method. It takes an email string argument and returns the session ID as a string. The method should find the user corresponding to the email, generate a new UUID and store it in the database as the user’s session_id, then return the session ID. Remember that only public methods of self._db can be used.
11. Implement a login function to respond to the POST /sessions route. The request is expected to contain form data with "email" and a "password" fields. If the login information is incorrect, use flask.abort to respond with a 401 HTTP status. Otherwise, create a new session for the user, store it the session ID as a cookie with key "session_id" on the response and return a JSON payload.
12. Implement the Auth.get_user_from_session_id method. It takes a single session_id string argument and returns the corresponding User or None. If the session ID is None or no user is found, return None. Otherwise return the corresponding user. Remember to only use public methods of self._db.
13. Implement Auth.destroy_session. The method takes a single user_id integer argument and returns None.
The method updates the corresponding user’s session ID to None. Remember to only use public methods of self._db.
14. Implement a logout function to respond to the DELETE /sessions route. The request is expected to contain the session ID as a cookie with key "session_id". Find the user with the requested session ID. If the user exists destroy the session and redirect the user to GET /. If the user does not exist, respond with a 403 HTTP status.
15. In this task, you will implement a profile function to respond to the GET /profile route. The request is expected to contain a session_id cookie. Use it to find the user. If the user exist, respond with a 200 HTTP status and a JSON payload. If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.
16. Implement the Auth.get_reset_password_token method. It take an email string argument and returns a string. Find the user corresponding to the email. If the user does not exist, raise a ValueError exception. If it exists, generate a UUID and update the user’s reset_token database field. Return the token.
17. Implement a get_reset_password_token function to respond to the POST /reset_password route. The request is expected to contain form data with the "email" field. If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and a JSON payload.
18. Implement the Auth.update_password method. It takes reset_token string argument and a password string argument and returns None. Use the reset_token to find the corresponding user. If it does not exist, raise a ValueError exception. Otherwise, hash the password and update the user’s hashed_password field with the new hashed password and the reset_token field to None.
19. Implement the update_password function in the app module to respond to the PUT /reset_password route. The request is expected to contain form data with fields "email", "reset_token" and "new_password". Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code. If the token is valid, respond with a 200 HTTP code and the following JSON payload.
20. Create a new module called main.py. Create one function for each of the following tasks. Use the requests module to query your web server for the corresponding end-point. Use assert to validate the response’s expected status code and payload (if any) for each task.

- register_user(email: str, password: str) -> None
- log_in_wrong_password(email: str, password: str) -> None
- log_in(email: str, password: str) -> str
- profile_unlogged() -> None
- profile_logged(session_id: str) -> None
- log_out(session_id: str) -> None
- reset_password_token(email: str) -> str
- update_password(email: str, reset_token: str, new_password: str) -> None

Copy the following code at the end of the main module:

```
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
```

Run python main.py. If everything is correct, you should see no output.

## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
