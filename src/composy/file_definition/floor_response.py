"""
Composy - Compos API python wrapper
Compos file definition - Floor Response
"""

__all__ = ['FloorResponse']


class FloorResponse:
    _response_analysis = {True: 'FLOOR_RESPONSE_ANALYSIS_YES', False: 'FLOOR_RESPONSE_ANALYSIS_NO'}

    _apply_damping = {True: 'WITH_DAMPING_LAYER', False: 'WITHOUT_DAMPING_LAYER'}

    def __init__(
        self,
        member_name,
        response_analysis: bool,
        trans_floor_length: float,
        total_beams: int,
        critical_damping: float,
        person_mass: float,
        max_walking_frq: float,
        apply_damping: bool,
        damping_e_mod: float,
        damping_g_mod: float,
        damping_lost_fact: float,
        damping_thick: float,
        damping_width: float,
    ):
        self.member_name = member_name
        self.do_response = response_analysis
        self.response_analysis = self._response_analysis[response_analysis]
        if response_analysis:
            self.trans_floor_length = trans_floor_length
            self.total_beams = total_beams
            self.critical_damping = critical_damping
            self.person_mass = person_mass
            self.max_walking_frq = max_walking_frq
            self.apply_damping = apply_damping
            self.damping_layer = self._apply_damping[apply_damping]
            if apply_damping:
                self.damping_e_mod = damping_e_mod
                self.damping_g_mod = damping_g_mod
                self.damping_lost_fact = damping_lost_fact
                self.damping_thick = damping_thick
                self.damping_width = damping_width
            else:
                self.damping_e_mod = 0.0
                self.damping_g_mod = 0.0
                self.damping_lost_fact = 0.0
                self.damping_thick = 0.0
                self.damping_width = 0.0

    def __repr__(self) -> str:
        if self.do_response:
            if self.apply_damping:
                return f'FLOOR_RESPONSE({self.response_analysis},{self.trans_floor_length},{self.total_beams},\
                    {self.critical_damping},{self.max_walking_frq},{self.damping_layer},{self.damping_e_mod},\
                        {self.damping_g_mod},{self.damping_lost_fact},{self.damping_thick},{self.damping_width})'
            else:
                return f'FLOOR_RESPONSE({self.response_analysis},{self.trans_floor_length},{self.total_beams},\
                    {self.critical_damping},{self.max_walking_frq},{self.damping_layer})'
        return f'FLOOR_RESPONSE({self.response_analysis})'

    def __str__(self) -> str:
        if self.do_response:
            if self.apply_damping:
                return f'FLOOR_RESPONSE,{self.member_name},{self.response_analysis},{self.trans_floor_length},\
                    {self.total_beams},{self.critical_damping},{self.max_walking_frq},{self.damping_layer},\
                        {self.damping_e_mod},{self.damping_g_mod},{self.damping_lost_fact},{self.damping_thick},\
                            {self.damping_width}'
            else:
                return f'FLOOR_RESPONSE,{self.member_name},{self.response_analysis},{self.trans_floor_length},\
                    {self.total_beams},{self.critical_damping},{self.max_walking_frq},{self.damping_layer},'
        return f'FLOOR_RESPONSE,{self.member_name},{self.response_analysis}'
