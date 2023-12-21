"""
Composy - Compos API python wrapper
Compos file definition - Beam Span Length
"""
__all__ = ['BeamSpanLength']


class BeamSpanLength():
    def __init__(self,
                 member_name,
                 span_number: int,
                 span_length: float):
        self.member_name = member_name
        self.span_number = span_number
        self.span_length = span_length

    def __repr__(self) -> str:
        return f"BEAM_STEEL_MATERIAL_USER({self.span_number},{self.span_length})"

    def __str__(self) -> str:
        return f"BEAM_STEEL_MATERIAL_USER,{self.member_name},{self.span_number},{self.span_length}"
