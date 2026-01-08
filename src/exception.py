
from typing import Any
from src.logger import logging

def error_message_detail(error: Exception, error_detail: Any):
    """Generate detailed error message with file name and line number."""
    _, _, exc_tb = error_detail.exc_info()
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    else:
        error_message = f"Error occurred: {str(error)}"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Any):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(self.error_message)
    
    def __str__(self) -> str:
        return self.error_message

