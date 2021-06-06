from src.constant import (ERROR_CODE, ERROR_MSG)

class ErrorObject():
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def get_message(self):
        return self.message
    
    def get_as_dict(self):
        return {
            ERROR_CODE: self.code,
            ERROR_MSG: self.message
        }