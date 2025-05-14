"""
Composy - Compos API python wrapper
Compos file definition - Beam Section at X
"""

__all__ = ['BeamSectionAtX']


class BeamSectionAtX:
    _tapered = {True: 'TAPERED_YES', False: 'TAPERED_NO'}

    def __init__(
        self,
        member_name,
        number_sections: int,
        index_of_section: int,
        section_description: str,
        distance_left: float,
        is_distance_relative: bool = False,
        is_tapered: bool = False,
    ):
        self.member_name = member_name
        self.number_sections = number_sections
        self.index_of_section = index_of_section
        self.section_description = section_description
        if is_distance_relative:
            self.distance_left = -distance_left
        else:
            self.distance_left = distance_left
        if is_tapered:
            self.is_tapered = self._tapered[is_tapered]

    def __repr__(self) -> str:
        return f'BEAM_STEEL_MATERIAL_STD({self.number_sections},{self.index_of_section},\
            {self.distance_left},{self.is_tapered})'

    def __str__(self) -> str:
        return f'BEAM_STEEL_MATERIAL_STD,{self.member_name},{self.number_sections},{self.index_of_section},\
            {self.distance_left},{self.is_tapered}'
