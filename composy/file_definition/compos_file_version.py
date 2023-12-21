"""
Composy - Compos API python wrapper
Compos file definition - Compos File Version
"""
__all__ = ['ComposFileVersion']


class ComposFileVersion():
    def __init__(self,
                 version_num: int):
        self.version_num = version_num
    
    def __repr__(self) -> str:
        return f"COMPOS_FILE_VERSION({self.version_num})"
    
    def __str__(self) -> str:
        return f"COMPOS_FILE_VERSION,{self.version_num}"