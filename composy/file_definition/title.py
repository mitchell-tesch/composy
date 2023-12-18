"""
Composy - Compos API python wrapper
Compos file definition - Unit Data
"""
__all__ = ['Title']


class Title():
    def __init__(self,
                 job_title: str,
                 sub_title: str,
                 calc_header: str,
                 job_number: str,
                 initials: str):
        self.title = job_title
        self.sub_title = sub_title
        self.calc = calc_header
        self.job = job_number
        self.initials = initials
    
    def __repr__(self) -> str:
        return f"TITLE({self.title},{self.sub_title},{self.calc},{self.job},{self.initials})"
    
    def __str__(self) -> str:
        return f"TITLE,{self.title},{self.sub_title},{self.calc},{self.job},{self.initials}"
