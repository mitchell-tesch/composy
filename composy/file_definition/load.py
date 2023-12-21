"""
Composy - Compos API python wrapper
Compos file definition - Load
"""
__all__ = ['Load']

from enum import StrEnum

# Mesh and mesh direction enumerations
class LoadType(StrEnum):
    POINT = 'Point'
    UNIFORM = 'Uniform'
    LINEAR = 'Linear'
    TRI_LINEAR = 'Tri-Linear'
    PATCH = 'Patch'
    MEMBER = 'Member load'
    AXIAL = 'Axial'
    MOMENT = 'Moment'
    
class LoadDistribution(StrEnum):
    LINE = 'Line'
    AREA = 'Area Load'

class MemberEnd(StrEnum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


class Load():
    def __init__(self,
                 member_name,
                 load_type: LoadType,
                 distribution: LoadDistribution,
                 position_left: float,
                 const_dead_left: float,
                 const_live_left: float,
                 final_dead_left: float,
                 final_live_left: float,
                 position_right: float = 0.0,
                 const_dead_right: float = 0.0,
                 const_live_right: float = 0.0,
                 final_dead_right: float = 0.0,
                 final_live_right: float = 0.0,
                 axial_depth_left: float = 0.0,
                 axial_depth_right: float = 0.0,
                 loading_member_name: str = '',
                 loading_member_end: MemberEnd = MemberEnd.LEFT,
                 loading_member_pos_left: float = 0.0):
        self.member_name = member_name
        self.load_type = load_type
        match load_type:
            case LoadType.POINT:
                self.const_dead_1 = const_dead_left
                self.const_live_1 = const_live_left
                self.final_dead_1 = final_dead_left
                self.final_live_1 = final_live_left
                self.dist_1 = position_left
            case LoadType.UNIFORM:
                self.distribution = distribution
                self.const_dead_1 = const_dead_left
                self.const_live_1 = const_live_left
                self.final_dead_1 = final_dead_left
                self.final_live_1 = final_live_left
            case LoadType.LINEAR:
                self.distribution = distribution
                self.const_dead_1 = const_dead_left
                self.const_live_1 = const_live_left
                self.final_dead_1 = final_dead_left
                self.final_live_1 = final_live_left
                self.const_dead_2 = const_dead_right
                self.const_live_2 = const_live_right
                self.final_dead_2 = final_dead_right
                self.final_live_2 = final_live_right
            case LoadType.TRI_LINEAR | LoadType.PATCH:
                self.distribution = distribution
                self.const_dead_1 = const_dead_left
                self.const_live_1 = const_live_left
                self.final_dead_1 = final_dead_left
                self.final_live_1 = final_live_left
                self.dist_1 = position_left
                self.const_dead_2 = const_dead_right
                self.const_live_2 = const_live_right
                self.final_dead_2 = final_dead_right
                self.final_live_2 = final_live_right
                self.dist_2 = position_right
            case LoadType.MOMENT:
                self.const_dead_1 = const_dead_left
                self.const_live_1 = const_live_left
                self.final_dead_1 = final_dead_left
                self.final_live_1 = final_live_left
                self.const_dead_2 = const_dead_right
                self.const_live_2 = const_live_right
                self.final_dead_2 = final_dead_right
                self.final_live_2 = final_live_right
            case LoadType.AXIAL:
                self.const_dead_1 = const_dead_left
                self.const_live_1 = const_live_left
                self.final_dead_1 = final_dead_left
                self.final_live_1 = final_live_left
                self.dist_from_top_1 = axial_depth_left
                self.const_dead_2 = const_dead_right
                self.const_live_2 = const_live_right
                self.final_dead_2 = final_dead_right
                self.final_live_2 = final_live_right
                self.dist_from_top_2 = axial_depth_right
            case LoadType.MEMBER:
                self.member_name = loading_member_name
                self.member_end = loading_member_end
                self.member_pos = loading_member_pos_left

    def __repr__(self) -> str:
        match self.load_type:
            case LoadType.POINT:
                return f"LOAD({self.load_type},{self.load_type},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},{self.dist_1})"
            case LoadType.UNIFORM:
                return f"LOAD({self.load_type},{self.load_type},{self.distribution},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1})"
            case LoadType.LINEAR:
                return f"LOAD({self.load_type},{self.load_type},{self.distribution},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2})"
            case LoadType.TRI_LINEAR | LoadType.PATCH:
                return f"LOAD({self.load_type},{self.load_type},{self.distribution},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},{self.dist_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2},{self.dist_2})"
            case LoadType.MOMENT:
                return f"LOAD({self.load_type},{self.load_type},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2})"
            case LoadType.AXIAL:
                return f"LOAD({self.load_type},{self.load_type},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},{self.dist_from_top_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2},{self.dist_from_top_2})"
            case LoadType.MEMBER:
                return f"LOAD({self.load_type},{self.load_type},{self.member_name},{self.member_end},{self.member_pos})"

    def __str__(self) -> str:
        match self.load_type:
            case LoadType.POINT:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},{self.dist_1}"
            case LoadType.UNIFORM:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},{self.distribution},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1}"
            case LoadType.LINEAR:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},{self.distribution},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2}"
            case LoadType.TRI_LINEAR | LoadType.PATCH:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},{self.distribution},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},{self.dist_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2},{self.dist_2}"
            case LoadType.MOMENT:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2}"
            case LoadType.AXIAL:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},\
                    {self.const_dead_1},{self.const_live_1},{self.final_dead_1},{self.final_live_1},{self.dist_from_top_1},\
                        {self.const_dead_2},{self.const_live_2},{self.final_dead_2},{self.final_live_2},{self.dist_from_top_2}"
            case LoadType.MEMBER:
                return f"LOAD,{self.member_name},{self.load_type},{self.load_type},{self.member_name},{self.member_end},{self.member_pos}"
