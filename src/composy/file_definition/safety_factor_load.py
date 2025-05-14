"""
Composy - Compos API python wrapper
Compos file definition - Safety Factor Load
"""

__all__ = ['SafetyFactorLoad']


class SafetyFactorLoad:
    def __init__(self, member_name, const_dead: float, const_live: float, final_dead: float, final_live: float):
        self.member_name = member_name
        self.const_dead = const_dead
        self.const_live = const_live
        self.final_dead = final_dead
        self.final_live = final_live

    def __repr__(self) -> str:
        return f'SAFETY_FACTOR_LOAD({self.const_dead},{self.const_live},{self.final_dead},{self.final_live})'

    def __str__(self) -> str:
        return f'SAFETY_FACTOR_LOAD,{self.member_name},{self.const_dead},{self.const_live},\
            {self.final_dead},{self.final_live}'
