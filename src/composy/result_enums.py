"""
Composy - Compos API python wrapper
Module providing results option enumerations
"""

from enum import IntEnum, StrEnum


class CodeStatus(IntEnum):
    """Enumeration for Compos Beam code status"""

    ALL_SATISFIED = 0
    EXCEPT_NATURAL_FREQ = 1
    UNSATISFIED = 2
    NO_RESULT = 4


class UtilisationFactor(StrEnum):
    """Enumeration for Compor beam utilisation options."""

    FINAL_MOMENT = 'FinalMoment'
    FINAL_SHEAR = 'FinalShear'
    FINAL_DEFL = 'FinalDeflection'
    CONST_MOMENT = 'ConstructionMoment'
    CONST_SHEAR = 'ConstructionShear'
    CONST_BUCK = 'ConstructionBuckling'
    CONST_DEFL = 'ConstructionDeflection'
    TRANS_SHEAR = 'TransverseShear'
    WEB_OPEN = 'WebOpening'
    NATURAL_FREQ = 'NaturalFrequency'


class ResultStations(StrEnum):
    """Enumeration for Compos beam result types relating to beam stations."""

    SECTION_DIST = 'CRITI_SECT_DIST'
    """Current position/distance from left end of the member"""
    SECTION_ATTR = 'CRITI_SECT_ATTRI'
    """Position attributes (max shear, moment and etc.,)"""


class ResultProperties(StrEnum):
    """Enumeration for Compos beam result types relating to properties."""

    WELD_SIZE_TOP = 'GIRDER_WELD_THICK_T'
    """Welding thickness at top"""
    WELD_SIZE_BTM = 'GIRDER_WELD_THICK_B'
    """Welding thickness at bottom"""

    CONST_FLANGE_CLASS = 'CLAS_CONS_FLAN_CLASS'
    """Flange class in Construction stage"""
    CONST_WEB_CLASS = 'CLAS_CONS_WEB_CLASS'
    """web class in Construction stage"""
    CONST_SECTION_CLASS = 'CLAS_CONS_SECTION'
    """Section class in Construction stage"""

    STEEL_A = 'AREA_STEEL_BEAM'
    """Area of steel beam"""
    STEEL_I = 'I_STEEL_BEAM'
    """Moment of Inertia of steel beam"""
    STEEL_NA_DEPTH = 'X_STEEL_BEAM'
    """Neutral axis depth of steel beam"""

    EFF_SLAB_WIDTH_LHS = 'SLAB_WIDTH_L_EFFECT'
    """Effective slab width on left side"""
    EFF_SLAB_WIDTH_RHS = 'SLAB_WIDTH_R_EFFECT'
    """Effective slab width on right side"""

    FINAL_FLANGE_CLASS = 'CLAS_FINA_FLAN_CLASS'
    """Flange class in Final stage"""
    FINAL_WEB_CLASS = 'CLAS_FINA_WEB_CLASS'
    """web class in Final stage"""
    FINAL_SECT_CLASS = 'CLAS_FINA_SECTION'
    """Section class in Final stage"""

    SHORT_TERM_A = 'AREA_SHORT_TERM'
    """ Area of beam for short term loading"""
    SHORT_TERM_I = 'I_SHORT_TERM'
    """Moment of Inertia of beam for short term loading"""
    SHORT_TERM_NA_DEPTH = 'X_SHORT_TERM'
    """Neutral axis depth of beam for short term loading"""

    LONG_TERM_A = 'AREA_LONG_TERM'
    """Area of beam for long term loading"""
    LONG_TERM_I = 'I_LONG_TERM'
    """Moment of Inertia of beam for long term loading"""
    LONG_TERM_NA_DEPTH = 'X_LONG_TERM'
    """Neutral axis depth of beam for long term loading"""

    SHRINK_A = 'AREA_SHRINK'
    """Area of beam for shrinkage"""
    SHRINK_I = 'I_SHRINK'
    """Moment of Inertia of beam for shrinkage"""
    SHRINK_NA_DEPTH = 'X_SHRINK'
    """Neutral axis depth of beam for shrinkage"""

    EFFECTIVE_A = 'AREA_EFFECT'
    """Effective Area of beam"""
    EFFECTIVE_I = 'I_EFFECTIVE'
    """Effective moment of Inertia of beam"""
    EFFECTIVE_NA_DEPTH = 'X_EFFECTIVE'
    """Neutral axis depth of beam under combined loading"""


class ResultActions(StrEnum):
    """Enumeration for Compos beam result types relating to actions."""

    ULS_CONST_MOMENT = 'ULTI_MOM_CONS'
    """Construction stage ultimate moment"""
    ULS_CONST_SHEAR = 'ULTI_SHE_CONS'
    """Construction stage ultimate shear"""
    ULS_CONST_AXIAL = 'ULTI_AXIAL_CONS'
    """Construction stage ultimate axial force"""
    ULS_FINAL_MOMENT = 'ULTI_MOM_FINA'
    """Final stage ultimate moment"""
    ULS_FINAL_SHEAR = 'ULTI_SHE_FINA'
    """Final stage ultimate shear"""
    ULS_FINAL_AXIAL = 'ULTI_AXIAL_FINA'
    """Final stage ultimate axial force"""

    CONST_DEAD_MOMENT = 'WORK_MOM_CONS_DEAD'
    """Construction stage working dead load moment"""
    CONST_DEAD_SHEAR = 'WORK_SHE_CONS_DEAD'
    """ Construction stage working dead load shear"""
    CONST_DEAD_AXIAL = 'WORK_AXIAL_CONS_DEAD'
    """Construction stage working dead load axial"""
    CONST_LIVE_MOMENT = 'WORK_MOM_CONS_LIVE'
    """Construction stage working live load moment"""
    CONST_LIVE_SHEAR = 'WORK_SHE_CONS_LIVE'
    """Construction stage working live load shear"""
    CONST_LIVE_AXIAL = 'WORK_AXIAL_CONS_LIVE'
    """Construction stage working live load axial"""

    FINAL_ADD_DEAD_MOMENT = 'WORK_MOM_FINA_ADDI'
    """Final stage working additional dead load shear"""
    FINAL_ADD_DEAD_SHEAR = 'WORK_SHE_FINA_ADDI'
    """Final stage working additional dead load shear"""
    FINAL_ADD_DEAD_AXIAL = 'WORK_AXIAL_FINA_ADDI'
    """Final stage working additional dead load axial"""
    FINAL_LIVE_MOMENT = 'WORK_MOM_FINA_LIVE'
    """Final stage working live load moment"""
    FINAL_LIVE_SHEAR = 'WORK_SHE_FINA_LIVE'
    """Final stage working live load shear"""
    FINAL_LIVE_AXIAL = 'WORK_AXIAL_FINA_LIVE'
    """Final stage working live load axial"""
    FINAL_SHRINK_MOMENT = 'WORK_MOM_FINA_SHRI'
    """Final stage working shrinkage moment"""


class ResultCapacity(StrEnum):
    """Enumeration for Compos beam result types relating to capacity."""

    CAPACITY_CONST_HOG_MOMENT = 'CAPA_MOM_ULTI_CONS_HOG'
    """Hogging moment capacity in Construction stage"""
    CAPACITY_CONST_PLAST_HOG_MOMENT = 'CAPA_MOM_BEAM_PLAS_HOG'
    """Assumed plastic Hogging moment capacity in Construction stage"""
    CAPACITY_CONST_SAG_MOMENT = 'CAPA_MOM_ULTI_CONS_SAG'
    """Sagging moment capacity in Construction stage"""
    CAPACITY_CONST_PLAST_SAG_MOMENT = 'CAPA_MOM_BEAM_PLAS_SAG'
    """Assumed plastic Sagging moment capacity in Construction stage"""

    CAPACITY_FINAL_HOG_MOMENT = 'CAPA_MOM_ULTI_FINA_HOG'
    """Hogging moment capacity in Final stage"""
    CAPACITY_FINAL_100INT_HOG_MOMENT = 'CAPA_MOM_100_INTER_HOG'
    """Assumed 100% shear interaction hogging moment capacity in final stage"""
    CAPACITY_FINAL_SAG_MOMENT = 'CAPA_MOM_ULTI_FINA_SAG'
    """Sagging moment capacity in Final stage"""
    CAPACITY_FINAL_100INT_SAG_MOMENT = 'CAPA_MOM_100_INTER_SAG'
    """Assumed 100% shear interaction sagging moment capacity in final stage"""

    CAPACITY_SHEAR_YIELD = 'CAPA_SHE_SHEAR'
    """Shear capacity"""
    CAPACITY_SHEAR_BUCKLE = 'CAPA_SHE_BUCLE'
    """Shear capacity with web buckling"""
    CAPACITY_SHEAR_USED = 'CAPA_SHE_PV'
    """Used shear capacity"""


class ResultNeutralAxis(StrEnum):
    """Enumeration for Compos beam result types relating to neutral axis."""

    NA_DEPTH_CONS_HOG = 'NEUTRAL_X_ULTI_CONS_HOG'
    """Neutral axis depth under Hogging moment in Construction stage"""
    NA_DEPTH_CONS_PLAS_HOG = 'NEUTRAL_X_BEAM_PLAS_HOG'
    """Neutral axis depth under Assumed plastic Hogging moment in Construction stage"""
    NA_DEPTH_CONS_SAG = 'NEUTRAL_X_ULTI_CONS_SAG'
    """Neutral axis depth under Sagging moment in Construction stage"""
    NA_DEPTH_CONS_PLAS_SAG = 'NEUTRAL_X_BEAM_PLAS_SAG'
    """Neutral axis depth under Assumed plastic Sagging moment in Construction stage"""

    NA_DEPTH_FINAL_HOG = 'NEUTRAL_X_ULTI_FINA_HOG'
    """Neutral axis depth under Hogging moment in Final stage"""
    NA_DEPTH_FINAL_100INT_HOG = 'NEUTRAL_X_100_INTER_HOG'
    """Neutral axis depth under assumed 100% interaction hogging moment in final stage"""
    NA_DEPTH_FINAL_SAG = 'NEUTRAL_X_ULTI_FINA_SAG'
    """Neutral axis depth under Sagging moment in Final stage"""
    NA_DEPTH_FINAL_100INT_SAG = 'NEUTRAL_X_100_INTER_SAG'
    """Neutral axis depth under assumed 100% interaction sagging moment in final stage"""


class ResultDeflection(StrEnum):
    """Enumeration for Compos beam result types relating to deflection."""

    CONST_DEAD_DELTA = 'DEFL_CONS_DEAD_LOAD'
    """Deflection due to Construction dead loads"""
    ADD_DEAD_DELTA = 'DEFL_ADDI_DEAD_LOAD'
    """Deflection due to additional dead loads"""
    FINAL_LIVE_DELTA = 'DEFL_FINA_LIVE_LOAD'
    """Deflection due to Final stage live loads"""
    SHRINK_DELTA = 'DEFL_SHRINK'
    """Deflection due to shrinkage of concrete"""
    POST_CONST_DELTA = 'DEFL_POST_CONS'
    """Deflection due to post Construction loads"""
    FINAL_TOTAL_DELTA = 'DEFL_FINA_TOTAL'
    """Total Deflection"""


class ResultStress(StrEnum):
    """Enumeration for Compos beam result types relating to stress."""

    CONST_STEEL_BTM_FLANGE = 'STRESS_CONS_BEAM_BOT'
    """Maximum stress in steel beam bottom Flange due to Construction loads"""
    CONST_STEEL_WEB = 'STRESS_CONS_BEAM_WEB'
    """Maximum stress in steel beam web due to Construction loads"""
    CONST_STEEL_TOP_FLANGE = 'STRESS_CONS_BEAM_TOP'
    """Maximum stress in steel beam top Flange due to Construction loads"""

    ADD_DEAD_STEEL_BTM_FLANGE = 'STRESS_ADDI_BEAM_BOT'
    """Maximum stress in steel beam bottom Flange due to additional dead loads"""
    ADD_DEAD_STEEL_WEB = 'STRESS_ADDI_BEAM_WEB'
    """Maximum stress in steel beam web due to additional dead loads"""
    ADD_DEAD_STEEL_TOP_FLANGE = 'STRESS_ADDI_BEAM_TOP'
    """Maximum stress in steel beam top Flange due to additional dead loads"""
    ADD_DEAD_CONC_MAX = 'STRESS_ADDI_CONC_STRESS'
    """Maximum stress in concrete slab due to additional dead loads"""

    FINAL_LIVE_STEEL_BTM_FLANGE = 'STRESS_FINA_LIVE_BEAM_BOT'
    """Maximum stress in steel beam bottom Flange due to Final stage live loads"""
    FINAL_LIVE_STEEL_WEB = 'STRESS_FINA_LIVE_BEAM_WEB'
    """Maximum stress in steel beam web due to Final stage live loads"""
    FINAL_LIVE_STEEL_TOP_FLANGE = 'STRESS_FINA_LIVE_BEAM_TOP'
    """Maximum stress in steel beam top Flange due to Final stage live loads"""
    FINAL_LIVE_CONC_MAX = 'STRESS_FINA_LIVE_CONC_STRESS'
    """Maximum stress in concrete slab due to Final stage live loads"""

    SHRINK_STEEL_BTM_FLANGE = 'STRESS_SHRINK_BEAM_BOT'
    """Maximum stress in steel beam bottom Flange due to shrinkage"""
    SHRINK_STEEL_WEB = 'STRESS_SHRINK_BEAM_WEB'
    """Maximum stress in steel beam web due to shrinkage"""
    SHRINK_STEEL_TOP_FLANGE = 'STRESS_SHRINK_BEAM_TOP'
    """Maximum stress in steel beam top Flange due to shrinkage"""
    SHRINK_CONC_MAX = 'STRESS_SHRINK_CONC_STRESS'
    """Maximum stress in concrete slab due to shrinkage"""

    FINAL_TOTAL_STEEL_BTM_FLANGE = 'STRESS_FINA_TOTL_BEAM_BOT'
    """Maximum stress in steel beam bottom Flange in Final stage"""
    FINAL_TOTAL_STEEL_WEB = 'STRESS_FINA_TOTL_BEAM_WEB'
    """Maximum stress in steel beam web in Final stage"""
    FINAL_TOTAL_STEEL_TOP_FLANGE = 'STRESS_FINA_TOTL_BEAM_TOP'
    """Maximum stress in steel beam top Flange in Final stage"""
    FINAL_TOTAL_CONC_MAX = 'STRESS_FINA_TOTL_CONC_STRESS'
    """Maximum stress in concrete slab in Final stage"""


class ResultStrain(StrEnum):
    """Enumeration for Compos beam result types relating to strain."""

    ADD_DEAD_CONC_MAX = 'STRESS_ADDI_CONC_STRAIN'
    """Maximum strain in concrete slab due to additional dea[d loads"""
    FINAL_LIVE_CONC_MAX = 'STRESS_FINA_LIVE_CONC_STRAIN'
    """Maximum strain in concrete slab due to Final stage live loads"""
    SHRINK_CONC_MAX = 'STRESS_SHRINK_CONC_STRAIN'
    """Maximum strain in concrete slab due to shrinkage"""
    FINAL_TOTAL_CONC_MAX = 'STRESS_FINA_TOTL_CONC_STRAIN'
    """Maximum strain in concrete slab in Final stage"""


class ResultVibration(StrEnum):
    """Enumeration for Compos beam result types relating to vibration."""

    MODAL_SHAPE = 'MODAL_SHAPE'
    """Mode shape"""
    VIBRATION_A = 'AREA_VIBRATION'
    """Area of beam for vibration"""
    VIBRATION_I = 'I_VIBRATION'
    """Moment of Inertia of beam for vibration"""
    VIBRATION_DEPTH_NA = 'X_VIBRATION'
    """Neutral axis depth of beam for vibration"""


class ResultStuds(StrEnum):
    """Enumeration for Compos beam result types relating to studs."""

    PROVIDED_STUDS_LEFT = 'STUD_NUM_LEFT_PROV'
    """Actual number of studs provided from left end"""
    PROVIDED_STUDS_RIGHT = 'STUD_NUM_RIGHT_PROV'
    """Actual number of studs provided from right end"""

    USED_STUDS_LEFT = 'STUD_NUM_LEFT_USED'
    """Used number of studs provided from left end"""
    USED_STUDS_RIGHT = 'STUD_NUM_RIGHT_USED'
    """Used number of studs provided from right end"""

    STUD_INT = 'STUD_PERCENT_INTERACTION'
    """Actual shear interaction"""
    SINGLE_STUD_CAPACITY = 'STUD_ONE_CAPACITY'
    """One shear stud capacity"""
    STUD_CAPACITY = 'STUD_CONCRTE_FORCE'
    """Actual stud capacity"""
    STUD_CAPACITY_LEFT = 'STUD_CAPACITY_LEFT'
    """Actual shear capacity from left end"""
    STUD_CAPACITY_RIGHT = 'STUD_CAPACITY_RIGHT'
    """Actual shear capacity from right end"""

    REQ_STUD_CAPACITY_100INT = 'STUD_CONCRTE_FORCE_100'
    """Required stud capacity for 100% shear interaction"""
    REQ_STUD_CAPACITY_MOMENT = 'STUD_CONCRTE_FORCE_REQ'
    """Required stud capacity for given moment"""
    REQ_INT_MOMENT = 'STUD_INTERACT_REQ'
    """Required shear interaction for given moment"""


# Type Alias for Results Enums
RESULT_TYPES = (
    ResultStations
    | ResultProperties
    | ResultActions
    | ResultCapacity
    | ResultNeutralAxis
    | ResultDeflection
    | ResultStress
    | ResultStrain
    | ResultVibration
    | ResultStuds
)


class TransRebarProp(StrEnum):
    """Enumeration for Compos transverse reinforcement property types."""

    EXTENT_LHS = 'REBAR_DIST_LEFT_SIDE'
    """Rebar starting position"""
    EXTENT_RHS = 'REBAR_DIST_RIGHT_SIDE'
    """Rebar ending position"""
    DIAMETER = 'REBAR_DIAMETER'
    """Rebar diameter"""
    SPACING = 'REBAR_INTERVAL'
    """Rebar interval"""
    COVER = 'REBAR_COVER'
    """Rebar cover"""
    AREA_PER_M = 'REBAR_AREA'
    """Rebar area per meter"""
    CRITICAL_POSITION = 'REBAR_CRITI_DIST'
    """Critical transverse shear position"""
    CRITICAL_FAILURE_SURFACE = 'REBAR_CRITI_SURFACE'
    """Failure surface, 1: a-a section; 2:b-b section; 5: e-e section"""
    EFFECTIVE_PERIMETER = 'REBAR_CRITI_PERI'
    """Effective perimeter"""
    TRANSVERSE_SHEAR = 'REBAR_CRITI_ACTUAL_SHEAR'
    """Transverse shear force"""
    CONC_SHEAR_RESIST = 'REBAR_CRITI_SHEAR_CONC'
    """Concrete shear resistance"""
    DECK_SHEAR_RESIST = 'REBAR_CRITI_SHEAR_DECK'
    """Decking shear resistance"""
    MESH_SHEAR_RESIST = 'REBAR_CRITI_SHEAR_MESH'
    """Mesh bar shear resistance"""
    BAR_SHEAR_RESIST = 'REBAR_CRITI_SHEAR_REBAR'
    """Rebar shear resistance"""
    MAX_ALLOW_SHEAR_RESIST = 'REBAR_CRITI_SHEAR_MAX_ALLOW'
    """Maximum allowable shear resistance"""
