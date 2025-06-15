from flask import session
import csv
import os

USER_FILE = 'data/users.csv'
USER_FIELDS = ['id', 'name', 'role', 'password']

def is_user_authenticated():
    return session.get('user') is not None