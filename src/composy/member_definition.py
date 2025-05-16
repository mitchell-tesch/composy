"""
Composy - Compos API python wrapper
Compos file definition - Member interface
"""

__all__ = ['MemberDefinition']

import composy.file_definition.design_option as design_option
import composy.file_definition.criteria_def_limit as criteria_def_limit
import composy.file_definition.criteria_beam_size_limit as criteria_beam_size_limit
import composy.file_definition.criteria_optimise_option as criteria_optimise_option
import composy.file_definition.criteria_section_type as criteria_section_type
import composy.file_definition.beam_steel_material_std as beam_material_std
import composy.file_definition.beam_steel_material_user as beam_material_user
import composy.file_definition.beam_welding_material as beam_weld_material
import composy.file_definition.beam_section_at_x as beam_section

from composy.file_definition.member_title import MemberTitle
from composy.file_definition.beam_span_length import BeamSpanLength


class MemberDefinition:
    DesignCode = design_option.DesignCode
    ConstructionType = design_option.ConstructionType
    DefScenario = criteria_def_limit.DefScenario
    DefLimitType = criteria_def_limit.DefLimitType
    OptimiseOption = criteria_optimise_option.OptimiseOption
    SectionType = criteria_section_type.SectionType
    StdSteelGrade = beam_material_std.StdSteelGrade
    StdWeldGrade = beam_weld_material.StdSWeldingGrade

    def __init__(
        self,
        name: str,
        grid_ref: str,
        note: str,
        beam_span: float,
        design_code: DesignCode,
        construction_type: ConstructionType,
        include_beam_weight: bool = True,
        include_slab_weight: bool = True,
        include_shear_deform: bool = False,
        include_thin_flange: bool = False,
    ):
        self._member_name = name
        self._member_title = MemberTitle(name, grid_ref, note)
        self._beam_span = BeamSpanLength(name, 1, beam_span)
        self._design_option = design_option.DesignOption(
            name,
            design_code,
            construction_type,
            include_beam_weight,
            include_slab_weight,
            include_shear_deform,
            include_thin_flange,
        )
        self._criteria_def_limits: list[criteria_def_limit.CriteriaDefLimit] = []
        self._criteria_beam_size_limit: None | criteria_beam_size_limit.CriteriaBeamSizeLimit = None
        self._criteria_optimise_option: None | criteria_optimise_option.OptimiseOption = None
        self._criteria_section_type: None | criteria_section_type.CriteriaSectionType = None
        # TODO
        # criteria_frequency
        # safety_factor_load
        # safety_factor_material
        self._beam_steel_material: (
            None | beam_material_std.BeamSteelMaterialStd | beam_material_user.BeamSteelMaterialUser
        ) = None
        self._beam_weld_material: None | beam_weld_material.StdSWeldingGrade = None
        self._beam_section: list[beam_section.BeamSectionAtX]
        # TODO
        # restraint_point
        # restraint_top_flange
        # restraint_secondary_beam
        # end_flange_free_rotate
        # final_restraint_point
        # final_restraint_no_stud
        # final_restraint_secondary_beam
        # final_end_flange_free_rotate
        # slab_concrete_material
        # slab_dimension
        # rebar_mesh
        # rebar_material
        # rebar_longitudinal
        # rebar_transverse
        # decking_user and decking_catalogue
        # stud_definition
        # stud_layout
        # stud_no_stud_zone
        # stud_ec4_apply
        # stud_ncci_limit_apply
        # stud_rft_position
        # web_opening
        # load
        # floor_response
        # ec_design_option
        # ec_load_comb_factors

    @property
    def member_name(self):
        return self._member_name

    @property
    def member_title(self):
        return self._member_title

    @property
    def beam_span(self):
        return self._beam_span

    @property
    def design_option(self):
        return self._design_option

    @property
    def criteria_def_limits(self):
        return self._criteria_def_limits

    @property
    def criteria_beam_size_limit(self):
        return self._criteria_beam_size_limit

    @property
    def criteria_optimise_option(self):
        return self._criteria_optimise_option

    @property
    def criteria_section_type(self):
        return self._criteria_section_type

    @property
    def beam_steel_material(self):
        return self._beam_steel_material

    @property
    def beam_weld_material(self):
        return self._beam_weld_material

    def add_criteria_deflection(self, scenario: DefScenario, limit_type: DefLimitType, limit: float):
        self._criteria_def_limits.append(
            criteria_def_limit.CriteriaDefLimit(self._member_name, scenario, limit_type, limit)
        )

    def set_beam_size_limit(self, min_depth: float, max_depth: float, min_width: float, max_width: float):
        self._criteria_beam_size_limit = criteria_beam_size_limit.CriteriaBeamSizeLimit(
            self._member_name, min_depth, max_depth, min_width, max_width
        )

    def set_optimise_option(self, optimise_option: OptimiseOption):
        self._criteria_optimise_option = criteria_optimise_option.CriteriaOptimiseOption(
            self._member_name, optimise_option
        )

    def set_section_type(self, section_types: list[SectionType]):
        self._criteria_section_type = criteria_section_type.CriteriaSectionType(self._member_name, section_types)

    def set_beam_material(
        self,
        std_grade: None | StdSteelGrade = StdSteelGrade.AS_300,
        fy: float = 300,
        elastic_mod: float = 200000,
        density: float = 7.85,
        reduced_en_pmc: bool = False,
    ):
        if std_grade:
            self._beam_steel_material = beam_material_std.BeamSteelMaterialStd(self._member_name, std_grade)
        else:
            self._beam_steel_material = beam_material_user.BeamSteelMaterialUser(
                self._member_name, fy, elastic_mod, density, reduced_en_pmc
            )

    def set_beam_weld_material(self, std_weld_grade: StdWeldGrade):
        self._beam_weld_material = beam_weld_material.BeamWeldingMaterial(self._member_name, std_weld_grade)

    def generate_definition(self):
        member_contents: list[str] = []
        member_contents.append(str(self._member_title))
        member_contents.append(str(self._design_option))
        return member_contents
