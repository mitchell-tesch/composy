"""
Composy - Compos API python wrapper
Module for the Compos Member object
"""
__all__ = ['Member']

# import Composy components
from composy.compos_api import compos_api
from composy.error_handle import ComposyError, ComposError
import composy.result_enums as results_enums
import composy.result_dataclasses as result


class Member():
    """Compos 8.6 Member"""

    def __init__(self, compos_auto: compos_api.Automation = None, index: int = None):
        # existing member will have an index
        self._compos_auto: compos_auto.Automation = compos_auto
        self._index: int = index
        self._name: str = self._get_member_name()
        self._section_desc: str = self._get_section_desc()
        self._analysis_run: bool = False
        self._design_run: bool = False
        self._results_available: bool = False
        self._code_status: results_enums.CodeStatus = results_enums.CodeStatus(4)
        self._num_stations: int = int()
        self._stations: list[float] = []
        self._num_trans_rebar: int = int()

    def __repr__(self):
        return f"ComposMember({self.index}: {self.name})"

    @property
    def index(self):
        """Index of Compos member."""
        return self._index

    @property
    def name(self):
        """Name of Compos member."""
        return self._name

    @property
    def section_desc(self):
        """Section of Compos member."""
        return self._section_desc

    @property
    def analysis_run(self):
        """Compos analysis run?"""
        return self._analysis_run

    @property
    def design_run(self):
        """Compos design run?"""
        return self._design_run

    @property
    def results_available(self):
        """Results available?"""
        return self._results_available

    @property
    def code_status(self):
        """Code status of Compos member."""
        return self._code_status

    @property
    def num_stations(self):
        """Number of stations."""
        return self._num_stations

    @property
    def stations(self):
        """Station positions from left end."""
        return self._stations

    @property
    def num_trans_rebar(self):
        """Number of transverse reinforcement bars."""
        return self._num_trans_rebar


    @classmethod
    def from_index(cls, compos_auto: compos_api.Automation, member_index: int):
        """Create Composy member from Compos index."""
        return cls(compos_auto, member_index)


    # Public methods
    def analyse_member(self):
        """Analyse member and retrieve code status, and station data.

        :raises ComposError: Analysis of member {} failed.
        """
        ret: int = self._compos_auto.Analyse(self._name)
        if ret != 0:
            raise ComposError(ret, f"Analysis of member {self._name} failed.")
        else:
            self._analysis_run = True
            self._get_code_status()
            self._get_number_stations()
            self._get_station_positions()
            if self._results_available:
                self._get_number_trans_rebar()

    def design_member(self):
        """Design member and retrieve code status, and station data.

        :raises ComposError: Design of member {} failed.
        """
        ret: int = self._compos_auto.Design(self._name)
        if ret != 0:
            raise ComposError(ret, f"Design of member {self._name} failed.")
        else:
            self._design_run = True
            self._get_code_status()
            self._get_number_stations()
            self._get_station_positions()
            if self._results_available:
                self._get_number_trans_rebar()

    def get_utilisation_factors(self) -> result.UtilisationFactors:
        """Retrieves member utilisation factors.

        :raises ComposyError: Member has no results available.
        :return: Member utilisation factors.
        :rtype: UtilisationFactors
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        utilisation_factors: list[float] = []
        for factor in [results_enums.UtilisationFactor.CONST_MOMENT,
                       results_enums.UtilisationFactor.CONST_SHEAR,
                       results_enums.UtilisationFactor.CONST_BUCK,
                       results_enums.UtilisationFactor.CONST_DEFL,
                       results_enums.UtilisationFactor.FINAL_MOMENT,
                       results_enums.UtilisationFactor.FINAL_SHEAR,
                       results_enums.UtilisationFactor.FINAL_DEFL,
                       results_enums.UtilisationFactor.TRANS_SHEAR,
                       results_enums.UtilisationFactor.WEB_OPEN,
                       results_enums.UtilisationFactor.NATURAL_FREQ]:
            utilisation_factors.append(self._compos_auto.UtilisationFactor(self._name, str(factor)))
        return result.UtilisationFactors(*utilisation_factors)

    def get_station_results(self,
                            result_type: results_enums.RESULT_TYPES) -> result.StationResults:
        """Retrieves result value for all member stations.

        :param result_type: result type StrEnum.
        :type result_type: results_enums.RESULT_TYPES
        :raises ComposyError: Member has no results available.
        :return: Results for all member stations.
        :rtype: StationResults
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_results: list[float] = []
        for station_index in range(0, self._num_stations):
            station_results.append(self._compos_auto.Result(self._name,
                                                            str(result_type),
                                                            station_index))
        return result.StationResults(result_type, station_results)

    def get_station_result(self,
                           result_type: results_enums.RESULT_TYPES,
                           station_index: int) -> result.StationResult:
        """Retrieves result value at specified member station.

        :param result_type: result type StrEnum.
        :type result_type: results_enums.RESULT_TYPES
        :param station_index: index of desired station.
        :type station_index: int
        :raises ComposyError: Member has no results available.
        :return: Result for requested member station.
        :rtype: StationResult
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_result: float = self._compos_auto.Result(self._name, str(result_type), station_index)
        return result.StationResult(result_type, station_index, station_result)

    def get_max_result(self, result_type: results_enums.RESULT_TYPES) -> result.MaxResult:
        """Retrieves result maximum value and corresponding station.

        :param result_type: result type StrEnum.
        :type result_type: results_enums.RESULT_TYPES
        :raises ComposyError: Member has no results available.
        :return: Maximum result and corresponding station.
        :rtype: MaxResult
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_index: int = int()
        max_result: float = float()
        max_result, station_index = self._compos_auto.MaxResult(self._name,
                                                                str(result_type),
                                                                station_index)
        return result.MaxResult(result_type, station_index, max_result)

    def get_min_result(self, result_type: results_enums.RESULT_TYPES) -> result.MinResult:
        """Retrieves result minimum value and corresponding station.

        :param result_type: result type StrEnum.
        :type result_type: results_enums.RESULT_TYPES
        :raises ComposyError: Member has no results available.
        :return: Minimum result and corresponding station.
        :rtype: MinResult
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_index: int = int()
        min_result: float = float()
        min_result, station_index = self._compos_auto.MinResult(self._name,
                                                                str(result_type),
                                                                station_index)
        return result.MinResult(result_type, station_index, min_result)

    def get_trans_rebar_properties(self,
                                   property_type: results_enums.TransRebarProp) -> result.TransRebarProperties:
        """Retrieves property values for all transverse rebars.

        :param property_type: transverse rebar property type
        :type property_type: results_enums.TransRebarProp
        :raises ComposyError: Member has no results available.
        :return: Property values for all transverse rebars.
        :rtype: result.TransRebarProperties
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        property_values: list[float] = []
        for rebar_index in range(0, self._num_trans_rebar):
            property_values.append(self._compos_auto.TranRebarProp(self._name,
                                                                   str(property_type),
                                                                   rebar_index))
        return result.TransRebarProperties(property_type, property_values)

    def get_trans_rebar_property(self,
                                 property_type: results_enums.TransRebarProp,
                                 rebar_index: int) -> result.TransRebarProperty:
        """Retrieves property value for specified transverse rebar.

        :param property_type: transverse rebar property type
        :type property_type: results_enums.TransRebarProp
        :param rebar_index: index of desired transverse rebar.
        :type rebar_index: int
        :raises ComposyError: Member has no results available.
        :return: Property value for specified transverse rebar.
        :rtype: result.TransRebarProperty
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        property_value: float = self._compos_auto.TranRebarProp(self._name,
                                                                str(property_type),
                                                                rebar_index)
        return result.TransRebarProperty(property_type, rebar_index, property_value)


    # Private methods
    def _get_member_name(self) -> str:
        return self._compos_auto.MemberName(self._index)

    def _get_section_desc(self) -> str:
        return self._compos_auto.BeamSectDesc(self._name)

    def _get_code_status(self):
        code_status_int: int = self._compos_auto.CodeSatisfied(self._name)
        if code_status_int == 3:
            raise ComposError(code_status_int, f"Member {self._name} does not exist.")
        self._code_status = results_enums.CodeStatus(code_status_int)
        if self._code_status == results_enums.CodeStatus.NO_RESULT:
            self._results_available = False
        else:
            self._results_available = True

    def _get_number_stations(self):
        num_stations: int = self._compos_auto.NumIntermediatePos(self._name)
        if num_stations == -1:
            raise ComposError(num_stations, f"Member {self._name} does not exist.")
        elif num_stations == 0:
            self._results_available = False
            self._num_stations = int()
        else:
            self._results_available = True
            self._num_stations = num_stations

    def _get_station_positions(self):
        if not self._results_available:
            self._stations = []
            return
        for station_index in range(0, self._num_stations):
            self._stations.append(self._compos_auto.Result(self._name,
                                                           str(results_enums.ResultStations.SECTION_DIST),
                                                           station_index))

    def _get_number_trans_rebar(self):
        num_trans_rebar = self._compos_auto.NumTranRebar(self._name)
        if num_trans_rebar == -1:
            raise ComposError(num_trans_rebar, f"Member {self._name} does not exist.")
        else:
            self._num_trans_rebar = num_trans_rebar
