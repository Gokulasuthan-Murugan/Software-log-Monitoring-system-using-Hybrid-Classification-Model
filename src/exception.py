import sys 
from src.logger import logging

def error_message_details(error,error_details:sys): 
    _,_,exc_tb=error_details.exc_info() # type,value,trace_back=sys.exc_info() # type==>type of the exception /value==>the actual error object / trace_back==>Holds the info about where the error occurred (filename, line no., etc.)
    file_name=exc_tb.tb_frame.f_code.co_filename  #tb_fram==>it gives the current function frame where the exception occurred.
    # f_code==>It holds metadata about the function like function name,filename 
    # co_filenam==>returns the filename where the code cause error lives in  

    error_message='error occured in python script name [{0}] line number [{1}] error message[{2}]'.format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details)

    def  __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        10/0
    except Exception as e:
        logging.info('Divide by Zero')
        raise CustomException(e,sys)