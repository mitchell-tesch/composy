"""
Composy - Compos API python wrapper
Compos file definition - Criteria Def Limit
"""

__all__ = ['CriteriaDefLimit']

from enum import StrEnum


# Deflection Scenario and Deflection Limit type enumerations
class DefScenario(StrEnum):
    CONST_DEAD_LOAD = 'CONSTRUCTION_DEAD_LOAD'
    ADD_DEAD_LOAD = 'ADDITIONAL_DEAD_LOAD'
    FINAL_LIVE_LOAD = 'FINAL_LIVE_LOAD'
    TOTAL = 'TOTAL'
    POST_CONSTRUCTION = 'POST_CONSTRUCTION'


class DefLimitType(StrEnum):
    ABSOLUTE = 'ABSOLUTE'
    RELATIVE = 'RELATIVE'


class CriteriaDefLimit:
    def __init__(self, member_name, scenario: DefScenario, limit_type: DefLimitType, limit: float):
        self.member_name = member_name
        self.scenario = scenario
        self.limit_type = limit_type
        self.limit = limit

    def __repr__(self) -> str:
        return f'CRITERIA_DEF_LIMIT({self.scenario},{self.limit_type},{self.limit})'

    def __str__(self) -> str:
        return f'CRITERIA_DEF_LIMIT,{self.member_name},{self.scenario},{self.limit_type},{self.limit}'
