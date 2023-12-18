"""
Composy - Compos API python wrapper
Compos file definition - Member interface
"""
__all__ = ["MemberDefinition"]

import composy.file_definition.design_option as design_option
from composy.file_definition.member_title import *
import composy.file_definition.criteria_def_limit as criteria_def_limit

class MemberDefinition():
    DesignCode = design_option.DesignCode
    ConstructionType = design_option.ConstructionType
    DefScenario = criteria_def_limit.DefScenario
    DefLimitType = criteria_def_limit.DefLimitType
    
    def __init__(self,
                 name: str, grid_ref: str, note: str,
                 design_code: DesignCode,
                 construction_type: ConstructionType,
                 include_beam_weight: bool = True,
                 include_slab_weight: bool = True,
                 include_shear_deform: bool = False,
                 include_thin_flange: bool = False):
        self._member_name = name
        self._member_title = MemberTitle(name, grid_ref, note)
        self._design_option = design_option.DesignOption(name,
                                                         design_code,
                                                         construction_type,
                                                         include_beam_weight,
                                                         include_slab_weight,
                                                         include_shear_deform,
                                                         include_thin_flange)
        self._criteria_def_limit: list[criteria_def_limit.CriteriaDefLimit] = []
    
    @property
    def member_name(self):
        return self._member_name
    
    @property
    def member_title(self):
        return self._member_title
    
    @property
    def design_option(self):
        return self._design_option

    def add_criteria_deflection(self,
                                scenario: DefScenario,
                                limit_type: DefLimitType,
                                limit: float):
        self._criteria_def_limit.append(criteria_def_limit.CriteriaDefLimit(self._member_name,
                                                                            scenario,
                                                                            limit_type,
                                                                            limit))

    def generate_definition(self):
        member_contents: list[str] = []
        member_contents.append(str(self._member_title))
        member_contents.append(str(self._design_option))
        return member_contents
            
