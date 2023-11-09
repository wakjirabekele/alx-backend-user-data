#!/usr/bin/env python3
"""
Class BasicAuth
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import Union, TypeVar


class BasicAuth(Auth):
    """flask authorization BasicAuth Class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that takes the authorization header and
        returns the Base64 part of the Authorization header
        for a Basic Authentication.
        """

        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Method that takes the base64_authorization header and
        returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            string_bytes = base64.b64decode(base64_bytes)
            return string_bytes.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Union[str, str]:
        """ Method that takes the decoded_base64_authorization header and
        returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return (None, None)
        arr = [':']
        for i in arr:
            if i not in decoded_base64_authorization_header:
                return (None, None)
            return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Method that takes user_email and user_pwd and
        returns the User instance based on his email and password.
        """
        if user_email is None or user_pwd is None or not isinstance(
                user_email, str) or not isinstance(user_pwd, str):
            return None
        user_credentials = {'email': user_email, }
        user = User()
        result = user.search(user_credentials)
        if not result:
            return None
        user = result[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that overloads Auth and retrieves the User instance
        for a request.
        """

        # Retrieve auth header from the request using Auth method
        auth_header = self.authorization_header(request)

        # Decode auth header value, get user data using Basic Auth methods
        b64_header = self.extract_base64_authorization_header(auth_header)
        decoded_header = self.decode_base64_authorization_header(b64_header)
        user_creds = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(*user_creds)
