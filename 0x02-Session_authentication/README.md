# Python - Session authentication

## Description of the files inside this folder:


0. Add a new endpoint: GET /users/me to retrieve the authenticated User object. 
1. Create a class SessionAuth that inherits from Auth. Update api/v1/app.py for using SessionAuth instance for the variable auth depending of the value of the environment variable AUTH_TYPE.
2. Update SessionAuth class. Create a class attribute user_id_by_session_id initialized by an empty dictionary. Create an instance method def create_session(self, user_id: str = None) -> str: that creates a Session ID for a user_id.
3. Update SessionAuth class. Create an instance method def user_id_for_session_id(self, session_id: str = None) -> str: that returns a User ID based on a Session ID. There are 2 methods (create_session and user_id_for_session_id) for storing and retrieving a link between a User ID and a Session ID.
4. Update api/v1/auth/auth.py by adding the method def session_cookie(self, request=None): that returns a cookie value from a request.
5. Update the @app.before_request method in api/v1/app.py. Add the URL path /api/v1/auth_session/login/ in the list of excluded paths of the method require_auth.
6. Update SessionAuth class. Create an instance method def current_user(self, request=None): (overload) that returns a User instance based on a cookie value. Use self.session_cookie(...) and self.user_id_for_session_id(...) to return the User ID based on the cookie _my_session_id
By using this User ID, you will be able to retrieve a User instance from the database - you can use User.get(...) for retrieving a User from the database.
7. Flask view that handles all routes for the Session authentication. In the file api/v1/views/session_auth.py, create a route POST /auth_session/login (= POST /api/v1/auth_session/login).
8. Update the class SessionAuth by adding a new method def destroy_session(self, request=None): that deletes the user session / logout. Update the file api/v1/views/session_auth.py, by adding a new route DELETE /api/v1/auth_session/logout.

## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
