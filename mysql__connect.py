# Python Example
import mysql.connector

config = {
    'user': 'khurana',
    'password': 'Aroundtheworld@7',
    'host': 'MariaDB',
    'database': 'frenchwithkunal',
    'port': 3306
}

connection = mysql.connector.connect(**config)