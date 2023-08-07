# Comosy - Compos API python wrapper
# Compos Member object
__all__ = ['Member']

# import Composy components
from composy.compos_api import *
from composy.error_handle import *
from composy.result_enums import *
from composy.result_dataclasses import *


class Member():
    """Compos 8.6 Member"""
    
    def __init__(self, compos_api : compos.Automation = None, index : int = None):
        # existing member will have an index
        self.compos_api : compos.Automation = compos_api
        self._index : int = index
        self._name : str = self._get_member_name()
        self._section_desc : str = self._get_section_desc()
        self._analysis_run : bool = False
        self._design_run : bool = False
        self._results_available : bool = False
        self._code_status : eCodeStatus = eCodeStatus(4)
        self._num_stations : int = int()
        self._stations : [float] = []

    def __repr__(self):
        return(f"ComposMember({self.index}: {self.name})")

    @property
    def index(self):
        return self._index

    @property
    def name(self):
        return self._name

    @property
    def section_desc(self):
        return self._section_desc

    @property
    def analysis_run(self):
        return self._analysis_run

    @property
    def design_run(self):
        return self._design_run
    
    @property
    def results_available(self):
        return self._results_available
    
    @property
    def code_status(self):
        return self._code_status
    
    @property
    def num_stations(self):
        return self._num_stations
    
    @property
    def stations(self):
        return self._stations


    @classmethod
    def from_index(cls, compos_api, member_index):
        return cls(compos_api, member_index)


    def analyse_member(self):
        """Analyse member and retrieve code status, and station data.

        :raises ComposError: Analysis of member {} failed.
        """
        iErr : int = self.compos_api.Analyse(self.name)
        if iErr != 0:
            raise ComposError(iErr, f"Analysis of member {self.name} failed.")
        else:
            self._analysis_run = True
            self._get_code_status()
            self._get_number_stations()
            self._get_station_positions()

    def design_member(self):
        """Design member and retrieve code status, and station data.

        :raises ComposError: Design of member {} failed.
        """
        iErr : int = self.compos_api.Design(self.name)
        if iErr != 0:
            raise ComposError(iErr, f"Design of member {self.name} failed.")
        else:
            self.design_run = True
            self._get_code_status()
            self._get_number_stations()
            self._get_station_positions()

    def get_utilisation_factors(self) -> UtilisationFactors:
        """Retrieves member utilisation factors.

        :raises ComposyError: Member has no results available.
        :return: Member utilisation factors.
        :rtype: UtilisationFactors
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        utilisation_factors = []
        for factor in [eUtilisationFactor.CONST_MOMENT, eUtilisationFactor.CONST_SHEAR,
                       eUtilisationFactor.CONST_BUCK, eUtilisationFactor.CONST_DEFL,
                       eUtilisationFactor.FINAL_MOMENT, eUtilisationFactor.FINAL_SHEAR,
                       eUtilisationFactor.FINAL_DEFL, eUtilisationFactor.TRANS_SHEAR,
                       eUtilisationFactor.WEB_OPEN, eUtilisationFactor.NATURAL_FREQ]:
            utilisation_factors.append(self.compos_api.UtilisationFactor(self.name, str(factor)))
        return UtilisationFactors(*utilisation_factors)

    def get_station_results(self, result_type : RESULT_TYPES) -> StationResults:
        """Retrieves result value for all member stations.

        :param result_type: result type StrEnum.
        :type result_type: RESULT_TYPES
        :raises ComposyError: Member has no results available.
        :return: Results for all member stations.
        :rtype: StationResults
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_results = []
        for station_index in range(0, self.num_stations):
            station_results.append(self.compos_api.Result(self.name, str(result_type), station_index))
        return StationResults(result_type, station_results)

    def get_station_result(self, result_type : RESULT_TYPES, station_index : int) -> StationResult:
        """Retrieves result value at specified member station.

        :param result_type: result type StrEnum.
        :type result_type: RESULT_TYPES
        :param station_index: index of desired station.
        :type station_index: int
        :raises ComposyError: Member has no results available.
        :return: Result for requested member station.
        :rtype: StationResult
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_result = self.compos_api.Result(self.name, str(result_type), station_index)
        return StationResult(result_type, station_index, station_result)

    def get_max_result(self, result_type : RESULT_TYPES) -> MaxResult:
        """Retrieves result maximum value and corresponding station.

        :param result_type: result type StrEnum.
        :type result_type: RESULT_TYPES
        :raises ComposyError: Member has no results available.
        :return: Maximum result and corresponding station.
        :rtype: MaxResult
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_index = int()
        max_result, station_index = self.compos_api.MaxResult(self.name, str(result_type), station_index)
        return MaxResult(result_type, station_index, max_result)

    def get_min_result(self, result_type : RESULT_TYPES) -> MinResult:
        """Retrieves result minimum value and corresponding station.

        :param result_type: result type StrEnum.
        :type result_type: RESULT_TYPES
        :raises ComposyError: Member has no results available.
        :return: Minimum result and corresponding station.
        :rtype: MinResult
        """
        if not self._results_available:
            raise ComposyError("Member has no results available.")
        station_index = int()
        min_result, station_index = self.compos_api.MinResult(self.name, str(result_type), station_index)
        return MinResult(result_type, station_index, min_result)


    def _get_member_name(self):
        return self.compos_api.MemberName(self.index)

    def _get_section_desc(self):
        return self.compos_api.BeamSectDesc(self.name)

    def _get_code_status(self):
        code_status_int = self.compos_api.CodeSatisfied(self.name)
        if code_status_int == 3:
            raise ComposError(code_status_int, f"Member {self.name} does not exist.")
        self._code_status = eCodeStatus(code_status_int)
        if self._code_status == eCodeStatus.NO_RESULT:
            self._results_available = False
        else:
            self._results_available = True

    def _get_number_stations(self):
        num_stations = self.compos_api.NumIntermediatePos(self.name)
        if num_stations == -1:
            raise ComposError(num_stations, f"Member {self.name} does not exist.")
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
        for station_index in range(0, self.num_stations):
            self._stations.append(self.compos_api.Result(self.name, str(eResultStations.SECTION_DIST), station_index))