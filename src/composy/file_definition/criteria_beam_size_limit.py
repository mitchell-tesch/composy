"""
Composy - Compos API python wrapper
Compos file definition - Criteria Beam Size Limit
"""

__all__ = ['CriteriaBeamSizeLimit']


class CriteriaBeamSizeLimit:
    def __init__(self, member_name, min_depth: float, max_depth: float, min_width: float, max_width: float):
        self.member_name = member_name
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.min_width = min_width
        self.max_width = max_width

    def __repr__(self) -> str:
        return f'CRITERIA_BEAM_SIZE_LIMIT({self.min_depth},{self.max_depth},{self.min_width},\
            {self.max_width})'

    def __str__(self) -> str:
        return f'CRITERIA_BEAM_SIZE_LIMIT,{self.member_name},{self.min_depth},{self.max_depth},\
            {self.min_width},{self.max_width}'
