"""
Composy - Compos API python wrapper
Compos file definition - Restraint Point
"""

__all__ = ['RestraintPoint']

from enum import StrEnum


# Final restraint points enumerations
class RestraintType(StrEnum):
    STANDARD = 'STANDARD'
    USER_DEFINED = 'USER_DEFINED'


class RestraintPoint:
    def __init__(
        self,
        member_name,
        restraint_type: RestraintType,
        num_restraints: int,
        rest_index: int = 0,
        rest_pos_left: float = 0.0,
    ):
        self.member_name = member_name
        self.restraint_type = restraint_type
        self.num_restraints = num_restraints
        self.index = rest_index
        self.position = rest_pos_left

    def __repr__(self) -> str:
        if self.restraint_type == RestraintType.STANDARD:
            return f'RESTRAINT_POINT({self.restraint_type},{self.num_restraints})'
        return f'RESTRAINT_POINT({self.restraint_type},{self.num_restraints},{self.num_restraints},{self.index},{self.position})'

    def __str__(self) -> str:
        if self.restraint_type == RestraintType.STANDARD:
            return f'RESTRAINT_POINT,{self.member_name},{self.restraint_type},{self.num_restraints})'
        return f'RESTRAINT_POINT,{self.member_name},{self.restraint_type},{self.num_restraints},{self.num_restraints},\
            {self.index},{self.position}'
