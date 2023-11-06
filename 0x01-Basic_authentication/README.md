# Python - Basic authentication

## Description of the files inside this folder:


0. Download and start your project from this archive.zip. In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.
1. Add a new error handler for this status code 401. For testing this new error handler, add a new endpoint in api/v1/views/index.py. By calling abort(401), the error handler for 401 will be executed.
2. Add a new error handler for this status code 403. For testing this new error handler, add a new endpoint in api/v1/views/index.py. By calling abort(403), the error handler for 403 will be executed.
3. Create a class to manage the API authentication.
4. Update the method def require_auth(self, path: str, excluded_paths: List[str]) -> bool: in Auth that returns True if the path is not in the list of strings excluded_paths.
5. Update the method def authorization_header(self, request=None) -> str: in api/v1/auth/auth.py. Update the file api/v1/app.py.
6. Create a class BasicAuth that inherits from Auth. For the moment this class will be empty. Update api/v1/app.py for using BasicAuth class instead of Auth depending of the value of the environment variable AUTH_TYPE, If AUTH_TYPE is equal to basic_auth.
7. Add the method def extract_base64_authorization_header(self, authorization_header: str) -> str: in the class BasicAuth that returns the Base64 part of the Authorization header for a Basic Authentication.
8. Add the method def decode_base64_authorization_header(self, base64_authorization_header: str) -> str: in the class BasicAuth that returns the decoded value of a Base64 string base64_authorization_header.
9. Add the method def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str) in the class BasicAuth that returns the user email and password from the Base64 decoded value.
10. Add the method def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'): in the class BasicAuth that returns the User instance based on his email and password.
11. Add the method def current_user(self, request=None) -> TypeVar('User') in the class BasicAuth that overloads Auth and retrieves the User instance for a request. With this update, now your API is fully protected by a Basic Authentication. 
- Use authorization_header
- Use extract_base64_authorization_header
- Use decode_base64_authorization_header
- Use extract_user_credentials
- Use user_object_from_credentials


## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>