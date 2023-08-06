# Comosy - Compos API python wrapper
# Results data classes

from dataclasses import dataclass

# import Composy components
from composy.result_enums import *


@dataclass
class StationResults:
    result_type: RESULT_OPTIONS
    results: list[float]


@dataclass
class StationResult:
    result_type: RESULT_OPTIONS
    station_index: int
    result: float


@dataclass
class MaxResult:
    result_type: RESULT_OPTIONS
    station_index: int
    result: float


@dataclass
class MinResult:
    result_type: RESULT_OPTIONS
    station_index: int
    result: float