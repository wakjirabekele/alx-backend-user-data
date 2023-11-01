#!/usr/bin/env python3
"""
This project module contains a logging module
"""
import re
import logging
import mysql.connector as connection
from typing import List
from os import environ


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log records using filter_datum.
            Returns: A log.
        """
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    This is a function that uses a regex to replace
    occurrences of certain field values.
    Returns:
        The log message obfuscated.
    """
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))


def get_logger() -> logging.Logger:
    """
    This is a function that returns a logging.Logger object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(streamHandler)
    return logger


def get_db() -> connection.MySQLConnection:
    """
    Connect to mysql server with environmental vars
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', "")
    db_host = environ.get('PERSONAL_DATA_DB_HOST', "localhost")
    db_name = environ.get('PERSONAL_DATA_DB_NAME')
    connector = connection.MySQLConnection(
        username=username,
        password=password,
        host=db_host,
        database=db_name)
    return connector


def main() -> None:
    """
    Obtains a database connection using get_db and retrieve all rows
    in the users table and display each row under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    logger = get_logger()

    fields = [x[0] for x in cursor.description]

    for row in records:
        msg = ''
        for i in range(len(fields)):
            msg += fields[i] + '=' + str(row[i]) + ';'
        logger.info(msg)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
