# Comosy - Compos API python wrapper
# Results data classes
__all__ = ['UtilisationFactors', 
           'StationResults',
           'StationResult',
           'MaxResult',
           'MinResult']

from dataclasses import dataclass

# import Composy components
from composy.result_enums import *


@dataclass
class UtilisationFactors:
    construction_moment : float
    construction_shear : float
    construction_buckling : float
    construction_deflection : float
    final_moment : float
    final_shear : float
    final_deflection : float
    transverse_shear : float
    web_opening : float
    natural_frequency : float

@dataclass
class StationResults:
    """Results data class for results at all member stations.
    """
    result_type: RESULT_TYPES
    results: list[float]


@dataclass
class StationResult:
    """Results data class for result at specified station.
    """
    result_type: RESULT_TYPES
    station_index: int
    result: float


@dataclass
class MaxResult:
    """Results data class for result maximum and corresponding station.
    """
    result_type: RESULT_TYPES
    station_index: int
    result: float


@dataclass
class MinResult:
    """Results data class for result minimum and corresponding station.
    """
    result_type: RESULT_TYPES
    station_index: int
    result: float