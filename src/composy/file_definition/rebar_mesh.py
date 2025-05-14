"""
Composy - Compos API python wrapper
Compos file definition - Rebar Longitudinal
"""

__all__ = ['RebarMesh']

from enum import StrEnum


# Mesh and mesh direction enumerations
class Mesh(StrEnum):
    A393 = 'A393'
    A252 = 'A252'
    A193 = 'A193'
    A142 = 'A142'
    A98 = 'A98'
    B1131 = 'B1131'
    B785 = 'B785'
    B503 = 'B503'
    B385 = 'B385'
    B283 = 'B283'
    B196 = 'B196'
    C785 = 'C785'
    C636 = 'C636'
    C503 = 'C503'
    C385 = 'C385'
    C283 = 'C283'


class MeshDirection(StrEnum):
    PARALLEL = 'PARALLEL'
    PERPENDICULAR = 'PERPENDICULAR'


class RebarMesh:
    _user_defined = {True: 'USER_DEFINED', False: 'PROGRAM_DESIGNED'}

    def __init__(self, member_name, mesh: Mesh, cover: float, direction: MeshDirection):
        self.member_name = member_name
        self.mesh = mesh
        self.cover = cover
        self.direction = direction

    def __repr__(self) -> str:
        return f'REBAR_WESH({self.mesh},{self.cover},{self.direction})'

    def __str__(self) -> str:
        return f'REBAR_WESH,{self.member_name},{self.mesh},{self.cover},{self.direction}'
