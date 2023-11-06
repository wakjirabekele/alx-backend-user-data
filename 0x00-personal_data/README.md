# Python - Personal data

## Description of the files inside this folder:


0. This project module contains a function called filter_datum that returns the log message obfuscated. The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.
1.  This project module contains a format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered. The format method should be less than 5 lines long.
2.  This project module contains a get_logger function that takes no arguments and returns a logging.Logger object. he logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.
Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter.
3. Connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”). The database name is stored in PERSONAL_DATA_DB_NAME. Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object). Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database.
4. This project module contains a main function that takes no arguments and returns nothing. The function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format. Only the main function should run when the module is executed. 
Filtered fields:
- name
- email
- phone
- ssn
- password
5. This project module contains a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string. Use the bcrypt package to perform the hashing (with hashpw).
6. This project module contains a is_valid function that expects 2 arguments and returns a boolean. Use bcrypt to validate that the provided password matches the hashed password.
Arguments:
- hashed_password: bytes type
- password: string type


## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
