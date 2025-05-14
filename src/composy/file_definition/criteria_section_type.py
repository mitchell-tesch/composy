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

    # TODO - library indexing...


class CriteriaSectionType:
    def __init__(self, member_name, section_type: SectionType):
        self.member_name = member_name
        self.section_type = section_type

    def __repr__(self) -> str:
        return f'CRITERIA_SECTION_TYPE({self.section_type})'

    def __str__(self) -> str:
        return f'CRITERIA_SECTION_TYPE,{self.member_name},{self.section_type}'
