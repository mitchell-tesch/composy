"""
Composy - Compos API python wrapper
Compos File Test
Creation of a Compos .coa file
"""

from composy import ComposDefinition, MemberDefinition

compos_file = ComposDefinition(
    'test_job',
    'test_subtitle',
    'test_header',
    'test_job_number',
    'test_initials',
    1,
    ComposDefinition.ForceUnit.kN,
    ComposDefinition.LengthUnit.m,
    ComposDefinition.LengthUnit.m,
    ComposDefinition.LengthUnit.mm,
    ComposDefinition.StressUnit.kPa,
    ComposDefinition.MassUnit.kg,
)


compos_member = MemberDefinition(
    'test_member',
    'test_grid_ref',
    'test_note',
    11,
    MemberDefinition.DesignCode.ASNZS2327_2017,
    MemberDefinition.ConstructionType.UNPROPPED,
)

compos_member.add_criteria_deflection(
    MemberDefinition.DefScenario.CONST_DEAD_LOAD, MemberDefinition.DefLimitType.RELATIVE, 360.0
)
compos_member.add_criteria_deflection(
    MemberDefinition.DefScenario.FINAL_LIVE_LOAD, MemberDefinition.DefLimitType.RELATIVE, 360.0
)
compos_member.add_criteria_deflection(MemberDefinition.DefScenario.TOTAL, MemberDefinition.DefLimitType.RELATIVE, 250.0)

compos_member.set_beam_size_limit(200.0, 900.0, 0.0, 1000)
compos_member.set_optimise_option(MemberDefinition.OptimiseOption.MIN_WEIGHT)
compos_member.set_section_type([MemberDefinition.SectionType.AUS_UB])
compos_member.set_beam_material(MemberDefinition.StdSteelGrade.AS_300)
compos_file.add_member(compos_member)

file = compos_file.generate_csv()

print(file)
