# Composy - Compos API python wrapper
# Error handler - for Compos API exceptions
__all__ = ['ComposError', 'ComposyError', 'ErrorCodes']


class Error(Exception):
    """Error base class for non-exit exceptions"""
    pass

class ComposError(Error):
    """General Compos Error Class"""
    def __init__(self, ret_value : int, message : str):
        self.ret_value : int = ret_value
        self.message : str = message

class ComposyError(Error):
    """General Composy Error Class"""
    def __init__(self, message : str):
        self.message : str = message


class ErrorCodes():
    SAVE = {1: "No Compos file open.",
            2: "No default path is available, use save_as().",
            3: "Failed to save Compos file."}
    
    SAVE_AS = {1: "No Compos file open.",
               2: "Invalid Compos file extension.",
               3: "Failed to save Compos file."}