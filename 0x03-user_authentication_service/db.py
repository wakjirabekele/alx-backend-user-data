#!/usr/bin/env python3
"""
Contains DB class to handle data.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """
    DB class to handle data
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Set and Return the user session.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Method that takes two arguments to save the user to the database.
            Returns: A User object.
        """
        if email is None or not isinstance(email, str):
            return None
        if hashed_password is None or not isinstance(hashed_password, str):
            return None
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Method that takes in arbitrary keyword arguments.
            Returns: The first row found in the users table as filtered
        by the passed arguments.
        """
        valid_arguments = [
            'id', 'email', 'hashed_password', 'session_id', 'reset_token'
        ]
        input_keys = kwargs.keys()
        for k in input_keys:
            if k not in valid_arguments:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Method that takes as argument a required user_id integer
        and arbitrary keyword arguments.
            Returns: None.
        """
        valid_arguments = [
            'id', 'email', 'hashed_password', 'session_id', 'reset_token'
        ]

        user_located = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in valid_arguments:
                raise ValueError
        setattr(user_located, key, value)
        self._session.commit()
        return None
