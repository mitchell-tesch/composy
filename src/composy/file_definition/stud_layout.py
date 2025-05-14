"""
Composy - Compos API python wrapper
Compos file definition - Stud Layout
"""

__all__ = ['StudLayout']

from enum import StrEnum


# Layout Type enumerations
class LayoutType(StrEnum):
    AUTO_FULL = 'AUTO_100'
    AUTO_MIN = 'AUTO_MINIMUM_STUD'
    AUTO_PERCENT = 'AUTO_PERCENT'
    USER_DEFINED = 'USER_DEFINED'


class StudLayout:
    _check_spacing = {True: 'CHECK_SPACE_YES', False: 'CHECK_SPACE_NO'}

    def __init__(
        self,
        member_name,
        layout_type: LayoutType = LayoutType.AUTO_FULL,
        target_percent_inter: float = 1.0,
        min_saving_multi_zone: float = 0.2,
        num_stud_zones: int = 0,
        stud_zone_index: int = 0,
        zone_start_pos: float = 0,
        num_stud_rows: int = 0,
        num_stud_lines: int = 0,
        row_spacing: float = 200,
        line_spacing: float = 0,
        check_user_spacing: bool = True,
    ):
        self.member_name = member_name
        self.layout_type = layout_type
        self.min_saving = min_saving_multi_zone
        if layout_type == LayoutType.AUTO_PERCENT:
            self.percent_inter = target_percent_inter
        else:
            self.percent_inter = 0.0
        if layout_type == LayoutType.USER_DEFINED:
            self.num_zones = num_stud_zones
            self.zone_index = stud_zone_index
            self.zone_start_pos = zone_start_pos
            self.num_stud_rows = num_stud_rows
            self.num_stud_lines = num_stud_lines
            self.row_spacing = row_spacing
            self.line_spacing = line_spacing
            self.check_spacing = self._check_spacing[check_user_spacing]
        else:
            self.num_zones = 0
            self.zone_index = 0
            self.zone_start_pos = 0.0
            self.num_stud_rows = 0
            self.num_stud_lines = 0
            self.row_spacing = 0.0
            self.line_spacing = 0.0
            self.check_spacing = self._check_spacing[False]

    def __repr__(self) -> str:
        match self.layout_type:
            case LayoutType.AUTO_FULL | LayoutType.AUTO_MIN:
                return f'STUD_LAYOUT({self.layout_type},{self.min_saving})'
            case LayoutType.AUTO_PERCENT:
                return f'STUD_LAYOUT({self.layout_type},{self.min_saving},{self.percent_inter})'
        return f'STUD_LAYOUT({self.layout_type},{self.num_zones},{self.zone_index},{self.zone_start_pos},{self.num_stud_rows},\
            {self.row_spacing},{self.line_spacing},{self.check_spacing})'

    def __str__(self) -> str:
        match self.layout_type:
            case LayoutType.AUTO_FULL | LayoutType.AUTO_MIN:
                return f'STUD_LAYOUT,{self.member_name},{self.layout_type},{self.min_saving}'
            case LayoutType.AUTO_PERCENT:
                return f'STUD_LAYOUT,{self.member_name},{self.layout_type},{self.min_saving},{self.percent_inter}'
        return (
            f'STUD_LAYOUT,{self.member_name},{self.layout_type},{self.num_zones},{self.zone_index},{self.zone_start_pos},\
            {self.num_stud_rows},{self.row_spacing},{self.line_spacing},{self.check_spacing})'
        )
