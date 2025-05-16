"""
Composy - Compos API python wrapper
Compos file definition - Criteria Section Type
"""

__all__ = ['CriteriaSectionType']

from enum import StrEnum


# Optimise Section type enumerations
class SectionType(StrEnum):
    EURO_IPE = '26'
    BRITISH_UB = '70'
    BRITISH_UC = '71'
    AUS_UB = '242'

    # TODO - library indexing...


class CriteriaSectionType:
    def __init__(self, member_name, section_types: list[SectionType]):
        self.member_name = member_name
        self.section_types = section_types

    def __repr__(self) -> str:
        return f'CRITERIA_SECTION_TYPE({",".join(self.section_types)})'

    def __str__(self) -> str:
        return f'CRITERIA_SECTION_TYPE,{self.member_name},{",".join(self.section_types)}'
