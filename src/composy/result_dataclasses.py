"""
Composy - Compos API python wrapper
Module providing results data classes for result returns
"""

__all__ = ['UtilisationFactors', 'StationResults', 'StationResult', 'MaxResult', 'MinResult']

from dataclasses import dataclass

# import Composy components
import composy.result_enums as results_enums


@dataclass
class UtilisationFactors:
    """Results data class for utilisation factors"""

    construction_moment: float
    construction_shear: float
    construction_buckling: float
    construction_deflection: float
    final_moment: float
    final_shear: float
    final_deflection: float
    transverse_shear: float
    web_opening: float
    natural_frequency: float


@dataclass
class StationResults:
    """Results data class for results at all member stations."""

    result_type: results_enums.RESULT_TYPES
    result_values: list[float]


@dataclass
class StationResult:
    """Results data class for result at specified station."""

    result_type: results_enums.RESULT_TYPES
    station_index: int
    result_value: float


@dataclass
class MaxResult:
    """Results data class for result maximum and corresponding station."""

    result_type: results_enums.RESULT_TYPES
    station_index: int
    result_value: float


@dataclass
class MinResult:
    """Results data class for result minimum and corresponding station."""

    result_type: results_enums.RESULT_TYPES
    station_index: int
    result_value: float


@dataclass
class TransRebarProperties:
    """Results data class for properties of all transverse rebars."""

    property_type: results_enums.TransRebarProp
    property_values: list[float]


@dataclass
class TransRebarProperty:
    """Results data class for property of specified transverse rebar."""

    property_type: results_enums.TransRebarProp
    rebar_index: int
    property_value: float
