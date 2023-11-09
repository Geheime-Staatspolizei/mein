from ..Record import Record
from functools import wraps
from flask import request

class AccessRecord():
    def passes(roles):
        def engine(func):
            wraps(func)
            def _engine(*args, **kwargs):
                token = request.headers.get('authorization')
                record = Record().verify(token)
                if(record.payload["role"] in roles):
                    return func(kwargs)
            return _engine
        return engine
    