#!/usr/bin/env python3
"""
This project module contains a function to encrypt passwords
and other to check valid password.

"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    This is a function that expects one string argument name password.
    Returns:
        A salted, hashed password, which is a byte string.
    """
    bytePwd = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    return bcrypt.hashpw(bytePwd, mySalt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This is a function that expects 2 arguments. The plain text password
    (Must be bytes) and the hashed password.
    Returns:
        A boolean.
    """
    bytePwd = password.encode('utf-8')
    return bcrypt.checkpw(bytePwd, hashed_password)
