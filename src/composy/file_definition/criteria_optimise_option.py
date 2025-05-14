"""
Composy - Compos API python wrapper
Compos file definition - Criteria Optimise Option
"""

__all__ = ['CriteriaOptimiseOption']

from enum import StrEnum


# Optimise Method type enumerations
class OptimiseOption(StrEnum):
    MIN_WEIGHT = 'MINIMUM_WEIGHT'
    MIN_DEPTH = 'MINIMUM_DEPTH'


class CriteriaOptimiseOption:
    def __init__(self, member_name, objective: OptimiseOption):
        self.member_name = member_name
        self.objective = objective

    def __repr__(self) -> str:
        return f'CRITERIA_OPTIMISE_OPTION({self.objective})'

    def __str__(self) -> str:
        return f'CRITERIA_OPTIMISE_OPTION,{self.member_name},{self.objective}'
