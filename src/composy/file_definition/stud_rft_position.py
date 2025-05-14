"""
Composy - Compos API python wrapper
Compos file definition - Stud Reinforcement Position
"""

__all__ = ['StudReoPosition']


class StudReoPosition:
    def __init__(self, member_name, depth: float):
        self.member_name = member_name
        self.depth = depth

    def __repr__(self) -> str:
        return f'STUD_RFT_POSITON({self.depth})'

    def __str__(self) -> str:
        return f'STUD_RFT_POSITON,{self.member_name},{self.depth}'
