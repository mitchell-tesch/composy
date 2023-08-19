from context import composy
from composy.compos import *

compos_app = ComposApp()

compos_app.open(r"C:\Users\mitchell.tesch\dev\projects\composy\test_file\Compos.cob")

compos_app.members[0].analyse_member()

utilisation_factors = compos_app.members[0].get_utilisation_factors()

result = compos_app.members[0].get_station_results(compos_app.ResultActions.FINAL_LIVE_MOMENT)

trans_rebar_area = compos_app.members[0].get_trans_rebar_properties(compos_app.TransRebarProp.AREA_PER_M)

min_result = compos_app.members[0].get_min_result(compos_app.ResultActions.FINAL_LIVE_MOMENT)
