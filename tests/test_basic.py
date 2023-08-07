from context import composy
from composy.compos import *

compos_app = ComposApp()

compos_app.open(r"D:\source\repos\composy\test_file\Compos.cob")

compos_app.members[0].analyse_member()

utilisation_factors = compos_app.members[0].get_utilisation_factors()

result = compos_app.members[0].get_station_results(compos_app.eResultActions.FINAL_LIVE_MOMENT)

min_result = compos_app.members[0].get_min_result(compos_app.eResultActions.FINAL_LIVE_MOMENT)