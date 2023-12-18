"""
Composy - Compos API python wrapper
Basic Tests of Compos App
Using Compos Sample file - refer compos_sample.py
"""
from pathlib import Path
import pytest
import composy
import composy.compos_member # imported for testing only
import composy.result_dataclasses as result_dc # imported for testing only
import tests.compos_sample as compos_sample



def test_compos_open_close():
    """Test Compos application open and close."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file testing
    compos.open(compos_sample.FILE_PATH)
    assert compos.file_open is True
    assert compos.file_path == Path(compos_sample.FILE_PATH)
    # close file testing
    compos.close()
    assert compos.file_open is False
    assert compos.file_path == Path("")


def test_member_population():
    """Test load of Compos members from file."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # check number of members loaded
    assert compos.num_members == compos_sample.NUM_MEMBERS
    # check population of member names list
    assert len(compos.member_names) == compos_sample.NUM_MEMBERS
    assert all([a == e for a, e in zip(compos.member_names, compos_sample.MEMBER_NAMES)])
    # check member object collection
    member_names = []
    member_sections = []
    for member in compos.members:
        # check instance of member
        assert isinstance(member, composy.compos_member.ComposMember)
        member_names.append(member.name)
        member_sections.append(member.section_desc)
    # check qty and name of member objects
    assert len(member_names) == compos_sample.NUM_MEMBERS
    assert all([a == e for a, e in zip(member_names, compos_sample.MEMBER_NAMES)])
    # check qty and name of section description
    assert len(member_sections) == compos_sample.NUM_MEMBERS
    assert all([a == e for a, e in zip(member_sections, compos_sample.MEMBER_SECTIONS)])
    # close file
    compos.close()


def test_member_analyse_all():
    """Test analysis of all Compos members."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse all members
    compos.analyse_all_members()
    # check member analysis and results status
    for member in compos.members:
        assert member.analysis_run is True
        # check results unavailable for those where analysis is invalid
        if member.index in compos_sample.ANALYSIS_INVALID:
            assert member.results_available is False
            continue
        assert member.results_available is True
        assert min(member.stations) == pytest.approx(0.0)
        assert max(member.stations) == pytest.approx(compos_sample.MEMBER_LENGTHS[member.index])
    # close file
    compos.close()


def test_member_analyse():
    """Test analysis of singgle Compos member."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse specific member
    test_member = compos.members[compos_sample.MEMBER_INDEX]
    test_member.analyse_member()
    # check analysis and results status
    assert test_member.analysis_run is True
    assert test_member.results_available is True
    # check result stations
    assert test_member.stations == pytest.approx(compos_sample.MEMBER_STATIONS, abs=1e-3)
    # close file
    compos.close()


def test_member_utilisation():
    """Test utilisation result retrieval of specific member."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse specific member
    test_member = compos.members[compos_sample.MEMBER_INDEX]
    test_member.analyse_member()
    # check utilisation factors
    utlisation_factors = test_member.get_utilisation_factors()
    expected_factors = (pytest.approx(f, abs=0.001) for f in compos_sample.MEMBER_UTILISATIONS)
    expected_factors = result_dc.UtilisationFactors(*expected_factors)
    assert utlisation_factors == expected_factors
    # close file
    compos.close()


def test_member_station_results():
    """Test member stations results retrieval for specific member."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse specific member
    test_member = compos.members[compos_sample.MEMBER_INDEX]
    test_member.analyse_member()
    # check ULS final moment
    result_type = compos.ResultActions.ULS_FINAL_MOMENT
    station_moments = test_member.get_station_results(result_type)
    assert station_moments.result_type == str(result_type )
    assert station_moments.result_values == pytest.approx(compos_sample.MEMBER_ULS_FINAL_MOMENT,
                                                          abs=1)
    # close file
    compos.close()


def test_member_station_result():
    """Test member station result retrieval for specific member."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse specific member
    test_member = compos.members[compos_sample.MEMBER_INDEX]
    test_member.analyse_member()
    # check ULS final moment at each station
    result_type = compos.ResultActions.ULS_FINAL_MOMENT
    for station_index in range(0, test_member.num_stations):
        station_moment = test_member.get_station_result(result_type, station_index)
        assert station_moment.result_type == str(result_type)
        assert station_moment.station_index == station_index
        assert station_moment.result_value == pytest.approx(compos_sample.MEMBER_ULS_FINAL_MOMENT[station_index],
                                                            abs=1)
    # close file
    compos.close()


def test_member_min_result():
    """Test member min result retrieval for specific member."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse specific member
    test_member = compos.members[compos_sample.MEMBER_INDEX]
    test_member.analyse_member()
    # check ULS final moment min
    result_type = compos.ResultActions.ULS_FINAL_MOMENT
    min_result = test_member.get_min_result(result_type)
    expected_min = min(compos_sample.MEMBER_ULS_FINAL_MOMENT)
    assert min_result.result_type == str(result_type)
    assert min_result.result_value == pytest.approx(expected_min, abs=1)
    assert min_result.station_index == compos_sample.MEMBER_ULS_FINAL_MOMENT.index(expected_min)
    # close file
    compos.close()


def test_member_max_result():
    """Test member max result retrieval for specific member."""
    # create composy Compos app
    compos = composy.ComposApp()
    # open compos file
    compos.open(compos_sample.FILE_PATH)
    # analyse specific member
    test_member = compos.members[compos_sample.MEMBER_INDEX]
    test_member.analyse_member()
    # check ULS final shear max
    result_type = compos.ResultActions.ULS_FINAL_SHEAR
    max_result = test_member.get_max_result(result_type)
    expected_max = max(compos_sample.MEMBER_ULS_FINAL_SHEAR)
    assert max_result.result_type == str(result_type)
    assert max_result.result_value == pytest.approx(expected_max, abs=1)
    assert max_result.station_index == compos_sample.MEMBER_ULS_FINAL_SHEAR.index(expected_max)
    # close file
    compos.close()
