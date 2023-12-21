"""
Composy - Compos API python wrapper
Compos file definition - Beam Steel Material User
"""
__all__ = ['BeamSteelMaterialUser']


class BeamSteelMaterialUser():
    _reduce_factor = {True: 'TRUE',
                      False: 'FALSE'}
    
    def __init__(self,
                 member_name,
                 fy: float,
                 elastic_mod: float,
                 density: float,
                 reduce_en_pmc: bool = False):
        self.member_name = member_name
        self.fy = fy
        self.elastic_mod = elastic_mod
        self.density = density
        if reduce_en_pmc:
            self.reduce = self._reduce_factor[reduce_en_pmc]
        else:
            self.reduce = self._reduce_factor[reduce_en_pmc]

    def __repr__(self) -> str:
        return f"BEAM_STEEL_MATERIAL_USER({self.fy},{self.elastic_mod},{self.density},{self.reduce})"

    def __str__(self) -> str:
        return f"BEAM_STEEL_MATERIAL_USER,{self.member_name},{self.fy},{self.elastic_mod},\
            {self.density},{self.reduce}"
