"""
Composy - Compos API python wrapper
Compos File Test
Creation of a Compos .coa file
"""
import composy

compos_file = composy.ComposDefinition('test_job',
                                       'test_subtitle',
                                       'test_header',
                                       'test_job_number',
                                       'test_initials',
                                       composy.ComposDefinition.ForceUnit.kN,
                                       composy.ComposDefinition.LengthUnit.m,
                                       composy.ComposDefinition.LengthUnit.m,
                                       composy.ComposDefinition.LengthUnit.mm,
                                       composy.ComposDefinition.StressUnit.kPa,
                                       composy.ComposDefinition.MassUnit.kg)


compos_member = composy.MemberDefinition('test_member',
                                         'test_grid_ref',
                                         'test_note',
                                         composy.MemberDefinition.DesignCode.ASNZS2327_2017,
                                         composy.MemberDefinition.ConstructionType.UNPROPPED)

compos_file.add_member(compos_member)

file = compos_file.generate_coa()

print(file)
