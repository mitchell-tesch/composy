"""
Composy - Compos API python wrapper
Compos file definition - Criteria Frequency
"""

__all__ = ['CriteriaFrequency']


class CriteriaFrequency:
    _check_status = {True: 'CHECK_NATURAL_FREQUENCY', False: 'IGNORE_NATURAL_FREQUENCY'}

    def __init__(
        self,
        member_name,
        check_status: bool,
        min_frequency: float = 5.0,
        dead_load_percent: float = 1.0,
        live_load_percent: float = 0.1,
    ):
        self.member_name = member_name
        if check_status:
            self.check_status = self._check_status[check_status]
            self.min_frequency = str(min_frequency)
            self.dead_load_percent = str(dead_load_percent)
            self.live_load_percent = str(live_load_percent)
        else:
            self.check_status = self._check_status[check_status]
            self.min_frequency = ''
            self.min_frequency = ''
            self.min_frequency = ''

    def __repr__(self) -> str:
        return f'CRITERIA_DEF_LIMIT({self.check_status},{self.dead_load_percent},{self.live_load_percent})'

    def __str__(self) -> str:
        return f'CRITERIA_DEF_LIMIT,{self.member_name},{self.check_status},\
            {self.dead_load_percent},{self.live_load_percent}'
