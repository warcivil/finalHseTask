from os import error
from flask import jsonify


def get_money_name(old, new, symbol="_"):
    return old+symbol+new


def catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify(dict(status="BAD",
                                error=str(e)
                                ))
    wrapper.__name__ = func.__name__                 
    return wrapper
