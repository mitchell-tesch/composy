"""
Composy - Compos API python wrapper
Compos file definition - Group
"""

__all__ = ['Group']


class Group:
    def __init__(self, name: str, note: str, members: [str]):
        self.name = name
        self.note = note
        self.num_members = len(members)
        self.members = members

    def __repr__(self) -> str:
        return f'GROUP({self.name},{self.note},{self.num_members},{",".join(self.members)})'

    def __str__(self) -> str:
        return f'GROUP,{self.name},{self.note},{self.num_members},{",".join(self.members)}'
