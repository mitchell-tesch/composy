from context import composy

from composy.compos import *
from composy.result_enums import *


from pathlib import Path

ComposFile = Compos()

ComposFile.open(r"D:\source\repos\composy\test_file\Compos.cob")

ComposFile.members[0].analyse_member()

result = ComposFile.members[0].get_station_results(eResultActions.FINAL_LIVE_MOMENT)

min_result = ComposFile.members[0].get_min_result(eResultActions.FINAL_LIVE_MOMENT)

print(ComposFile._member_names)

