import sys               ##It is a built-in module in Python that provides access to some variables and functions that interact with the Python interpreter. It is often used for system-related tasks.

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured in python script {{0}} line number {{1}} error message {{2}} ".format(
        file_name,exc_tb.tb_lineno,str(error))
    

    return error_message



class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)           ##inherit exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message