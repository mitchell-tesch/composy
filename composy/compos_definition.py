"""
Composy - Compos API python wrapper
Interface to create a Compos file via Compos text
"""
__all__ = ["ComposDefinition"]

import composy.file_definition.title as title
import composy.file_definition.unit_data as unit_data
from composy.member_definition import *

class ComposDefinition():
    ForceUnit = unit_data.ForceUnit
    LengthUnit = unit_data.LengthUnit
    StressUnit = unit_data.StressUnit
    MassUnit = unit_data.MassUnit
    
    def __init__(self,
                 job_title: str,
                 sub_title: str,
                 calc_header: str,
                 job_number: str,
                 initials: str,
                 force_unit: ForceUnit = ForceUnit.kN,
                 length_unit: LengthUnit = LengthUnit.m,
                 disp_unit: LengthUnit = LengthUnit.m,
                 section_unit: LengthUnit = LengthUnit.mm,
                 stress_unit: StressUnit = StressUnit.kPa,
                 mass_unit: MassUnit = MassUnit.kg):
        self._title = title.Title(job_title, sub_title, calc_header, job_number, initials)
        
        self._unit_data = unit_data.UnitData(force_unit, length_unit, disp_unit,
                                             section_unit, stress_unit, mass_unit)
        self.member_definitions: list[MemberDefinition] = []
        
    @property
    def title(self):
        return self._title
    
    @property
    def unit_data(self):
        return self._unit_data
    
    def add_member(self, member_definition: MemberDefinition):
        self.member_definitions.append(member_definition)
        
    def generate_coa(self, file_path = ''):
        file_contents: list[str] = []
        file_contents.append(str(self._title))
        file_contents.extend(self._unit_data.get_unit_strings())
        for member in self.member_definitions:
            file_contents.extend(member.generate_definition())
        return file_contents