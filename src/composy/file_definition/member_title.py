"""
Composy - Compos API python wrapper
Compos file definition - Member Title
"""

__all__ = ['MemberTitle']


class MemberTitle:
    def __init__(self, name: str, grid_ref: str, note: str):
        self.name = name
        self.grid_ref = grid_ref
        self.note = note

    def __repr__(self) -> str:
        return f'MEMBER_TITLE({self.name},{self.grid_ref},{self.note})'

    def __str__(self) -> str:
        return f'MEMBER_TITLE,{self.name},{self.grid_ref},{self.note}'
