"""
Composy - Compos API python wrapper
Module providing results option enumerations
"""
from enum import IntEnum, StrEnum


class eCodeStatus(IntEnum):
    ALL_SATISFIED = 0
    EXCEPT_NATURAL_FREQ = 1
    UNSATISFIED = 2
    NO_RESULT = 4


class eUtilisationFactor(StrEnum):
    FINAL_MOMENT = "FinalMoment"
    FINAL_SHEAR = "FinalShear"
    FINAL_DEFL = "FinalDeflection"
    CONST_MOMENT = "ConstructionMoment"
    CONST_SHEAR = "ConstructionShear"
    CONST_BUCK = "ConstructionBuckling"
    CONST_DEFL = "ConstructionDeflection"
    TRANS_SHEAR = "TransverseShear"
    WEB_OPEN = "WebOpening"
    NATURAL_FREQ = "NaturalFrequency"


class eResultStations(StrEnum):
    '''Current position/distance from left end of the member'''
    SECTION_DIST = "CRITI_SECT_DIST"
    '''Position attributes (max shear, moment and etc.,)'''
    SECTION_ATTR = "CRITI_SECT_ATTRI"


class eResultProperties(StrEnum):
    '''Welding thickness at top'''
    WELD_SIZE_TOP = "GIRDER_WELD_THICK_T"
    '''Welding thickness at bottom'''
    WELD_SIZE_BTM = "GIRDER_WELD_THICK_B"

    '''Flange class in Construction stage'''
    CONST_FLANGE_CLASS = "CLAS_CONS_FLAN_CLASS"
    '''web class in Construction stage'''
    CONST_WEB_CLASS = "CLAS_CONS_WEB_CLASS"
    '''Section class in Construction stage'''
    CONST_SECTION_CLASS = "CLAS_CONS_SECTION"

    '''Area of steel beam'''
    STEEL_A = "AREA_STEEL_BEAM"
    '''Moment of Inertia of steel beam'''
    STEEL_I = "I_STEEL_BEAM"
    '''Neutral axis depth of steel beam'''
    STEEL_NA_DEPTH = "X_STEEL_BEAM"

    '''Effective slab width on left side'''
    EFF_SLAB_WIDTH_LHS = "SLAB_WIDTH_L_EFFECT"
    '''Effective slab width on right side'''
    EFF_SLAB_WIDTH_RHS = "SLAB_WIDTH_R_EFFECT"

    '''Flange class in Final stage'''
    FINAL_FLANGE_CLASS = "CLAS_FINA_FLAN_CLASS"
    '''web class in Final stage'''
    FINAL_WEB_CLASS = "CLAS_FINA_WEB_CLASS"
    '''Section class in Final stage'''
    FINAL_SECT_CLASS = "CLAS_FINA_SECTION"

    ''' Area of beam for short term loading'''
    SHORT_TERM_A = "AREA_SHORT_TERM"
    '''Moment of Inertia of beam for short term loading'''
    SHORT_TERM_I = "I_SHORT_TERM"
    '''Neutral axis depth of beam for short term loading'''
    SHORT_TERM_NA_DEPTH = "X_SHORT_TERM"

    '''Area of beam for long term loading'''
    LONG_TERM_A = "AREA_LONG_TERM"
    '''Moment of Inertia of beam for long term loading'''
    LONG_TERM_I = "I_LONG_TERM"
    '''Neutral axis depth of beam for long term loading'''
    LONG_TERM_NA_DEPTH = "X_LONG_TERM"

    '''Area of beam for shrinkage'''
    SHRINK_A = "AREA_SHRINK"
    '''Moment of Inertia of beam for shrinkage'''
    SHRINK_I = "I_SHRINK"
    '''Neutral axis depth of beam for shrinkage'''
    SHRINK_NA_DEPTH = "X_SHRINK"
    
    '''Effective Area of beam'''
    EFFECTIVE_A = "AREA_EFFECT"
    '''Effective moment of Inertia of beam'''
    EFFECTIVE_I = "I_EFFECTIVE"
    '''Neutral axis depth of beam under combined loading'''
    EFFECTIVE_NA_DEPTH = "X_EFFECTIVE"


class eResultActions(StrEnum):
    '''Construction stage ultimate moment'''
    ULS_CONST_MOMENT = "ULTI_MOM_CONS"
    '''Construction stage ultimate shear'''
    ULS_CONST_SHEAR = "ULTI_SHE_CONS"
    '''Construction stage ultimate axial force'''
    ULS_CONST_AXIAL = "ULTI_AXIAL_CONS"
    '''Final stage ultimate moment'''
    ULS_FINAL_MOMENT = "ULTI_MOM_FINA"
    '''Final stage ultimate shear'''
    ULS_FINAL_SHEAR = "ULTI_SHE_FINA"
    '''Final stage ultimate axial force'''
    ULS_FINAL_AXIAL = "ULTI_AXIAL_FINA"
    
    '''Construction stage working dead load moment'''
    CONST_DEAD_MOMENT = "WORK_MOM_CONS_DEAD"
    ''' Construction stage working dead load shear'''
    CONST_DEAD_SHEAR = "WORK_SHE_CONS_DEAD"
    '''Construction stage working dead load axial'''
    CONST_DEAD_AXIAL = "WORK_AXIAL_CONS_DEAD"
    '''Construction stage working live load moment'''
    CONST_LIVE_MOMENT = "WORK_MOM_CONS_LIVE"
    '''Construction stage working live load shear'''
    CONST_LIVE_SHEAR = "WORK_SHE_CONS_LIVE"
    '''Construction stage working live load axial'''
    CONST_LIVE_AXIAL = "WORK_AXIAL_CONS_LIVE"
    
    '''Final stage working additional dead load shear'''
    FINAL_ADD_DEAD_MOMENT = "WORK_MOM_FINA_ADDI"
    '''Final stage working additional dead load shear'''
    FINAL_ADD_DEAD_SHEAR = "WORK_SHE_FINA_ADDI"
    '''Final stage working additional dead load axial'''
    FINAL_ADD_DEAD_AXIAL = "WORK_AXIAL_FINA_ADDI"
    '''Final stage working live load moment'''
    FINAL_LIVE_MOMENT = "WORK_MOM_FINA_LIVE"
    '''Final stage working live load shear'''
    FINAL_LIVE_SHEAR = "WORK_SHE_FINA_LIVE"
    '''Final stage working live load axial'''
    FINAL_LIVE_AXIAL = "WORK_AXIAL_FINA_LIVE"
    '''Final stage working shrinkage moment'''
    FINAL_SHRINK_MOMENT = "WORK_MOM_FINA_SHRI"


class eResultCapacity(StrEnum):
    '''Hogging moment capacity in Construction stage'''
    CAPACITY_CONS_HOG_MOMENT = "CAPA_MOM_ULTI_CONS_HOG"
    '''Assumed plastic Hogging moment capacity in Construction stage'''
    CAPACITY_CONS_PLAST_HOG_MOMENT = "CAPA_MOM_BEAM_PLAS_HOG"
    '''Sagging moment capacity in Construction stage'''
    CAPACITY_CONS_SAG_MOMENT = "CAPA_MOM_ULTI_CONS_SAG"
    '''Assumed plastic Sagging moment capacity in Construction stage'''
    CAPACITY_CONS_PLAST_SAG_MOMENT = "CAPA_MOM_BEAM_PLAS_SAG"

    '''Hogging moment capacity in Final stage'''
    CAPACITY_FINAL_HOG_MOMENT = "CAPA_MOM_ULTI_FINA_HOG"
    '''Assumed 100% shear interaction hogging moment capacity in final stage'''
    CAPACITY_FINAL_100INT_HOG_MOMENT = "CAPA_MOM_100_INTER_HOG"
    '''Sagging moment capacity in Final stage'''
    CAPACITY_FINAL_SAG_MOMENT = "CAPA_MOM_ULTI_FINA_SAG"
    '''Assumed 100% shear interaction sagging moment capacity in final stage'''
    CAPACITY_FINAL_100INT_SAG_MOMENT = "CAPA_MOM_100_INTER_SAG"
    
    '''Shear capacity'''
    CAPACITY_SHEAR_YIELD = "CAPA_SHE_SHEAR"
    '''Shear capacity with web buckling'''
    CAPACITY_SHEAR_BUCKLE = "CAPA_SHE_BUCLE"
    '''Used shear capacity'''
    CAPACITY_SHEAR_USED ="CAPA_SHE_PV"


class eResultNeutralAxis(StrEnum):
    '''Neutral axis depth under Hogging moment in Construction stage'''
    NA_DEPTH_CONS_HOG = "NEUTRAL_X_ULTI_CONS_HOG"
    '''Neutral axis depth under Assumed plastic Hogging moment in Construction stage'''
    NA_DEPTH_CONS_PLAS_HOG = "NEUTRAL_X_BEAM_PLAS_HOG"
    '''Neutral axis depth under Sagging moment in Construction stage'''
    NA_DEPTH_CONS_SAG = "NEUTRAL_X_ULTI_CONS_SAG"
    '''Neutral axis depth under Assumed plastic Sagging moment in Construction stage'''
    NA_DEPTH_CONS_PLAS_SAG = "NEUTRAL_X_BEAM_PLAS_SAG"
    
    '''Neutral axis depth under Hogging moment in Final stage'''
    NA_DEPTH_FINAL_HOG = "NEUTRAL_X_ULTI_FINA_HOG"
    '''Neutral axis depth under assumed 100% interaction hogging moment in final stage'''
    NA_DEPTH_FINAL_100INT_HOG = "NEUTRAL_X_100_INTER_HOG"
    '''Neutral axis depth under Sagging moment in Final stage'''
    NA_DEPTH_FINAL_SAG = "NEUTRAL_X_ULTI_FINA_SAG"
    '''Neutral axis depth under assumed 100% interaction sagging moment in final stage'''
    NA_DEPTH_FINAL_100INT_SAG= "NEUTRAL_X_100_INTER_SAG"


class eResultDeflection(StrEnum):
    '''Deflection due to Construction dead loads'''
    CONST_DEAD_DELTA = "DEFL_CONS_DEAD_LOAD"
    '''Deflection due to additional dead loads'''
    ADD_DEAD_DELTA = "DEFL_ADDI_DEAD_LOAD"
    '''Deflection due to Final stage live loads'''
    FINAL_LIVE_DELTA = "DEFL_FINA_LIVE_LOAD"
    '''Deflection due to shrinkage of concrete'''
    SHRINK_DELTA = "DEFL_SHRINK"
    '''Deflection due to post Construction loads'''
    POST_CONST_DELTA = "DEFL_POST_CONS"
    '''Total Deflection'''
    FINAL_TOTAL_DELTA = "DEFL_FINA_TOTAL"


class eResultStress(StrEnum):
    '''Maximum stress in steel beam bottom Flange due to Construction loads'''
    CONST_STEEL_BTM_FLANGE = "STRESS_CONS_BEAM_BOT"
    '''Maximum stress in steel beam web due to Construction loads'''
    CONST_STEEL_WEB = "STRESS_CONS_BEAM_WEB"
    '''Maximum stress in steel beam top Flange due to Construction loads'''
    CONST_STEEL_TOP_FLANGE = "STRESS_CONS_BEAM_TOP"
    
    '''Maximum stress in steel beam bottom Flange due to additional dead loads'''
    ADD_DEAD_STEEL_BTM_FLANGE = "STRESS_ADDI_BEAM_BOT"
    '''Maximum stress in steel beam web due to additional dead loads'''
    ADD_DEAD_STEEL_WEB = "STRESS_ADDI_BEAM_WEB"
    '''Maximum stress in steel beam top Flange due to additional dead loads'''
    ADD_DEAD_STEEL_TOP_FLANGE = "STRESS_ADDI_BEAM_TOP"
    '''Maximum stress in concrete slab due to additional dead loads'''
    ADD_DEAD_CONC_MAX = "STRESS_ADDI_CONC_STRESS"
    
    '''Maximum stress in steel beam bottom Flange due to Final stage live loads'''
    FINAL_LIVE_STEEL_BTM_FLANGE = "STRESS_FINA_LIVE_BEAM_BOT"
    '''Maximum stress in steel beam web due to Final stage live loads'''
    FINAL_LIVE_STEEL_WEB = "STRESS_FINA_LIVE_BEAM_WEB"
    '''Maximum stress in steel beam top Flange due to Final stage live loads'''
    FINAL_LIVE_STEEL_TOP_FLANGE = "STRESS_FINA_LIVE_BEAM_TOP"
    '''Maximum stress in concrete slab due to Final stage live loads'''
    FINAL_LIVE_CONC_MAX = "STRESS_FINA_LIVE_CONC_STRESS"
    
    '''Maximum stress in steel beam bottom Flange due to shrinkage'''
    SHRINK_STEEL_BTM_FLANGE = "STRESS_SHRINK_BEAM_BOT"
    '''Maximum stress in steel beam web due to shrinkage'''
    SHRINK_STEEL_WEB = "STRESS_SHRINK_BEAM_WEB"
    '''Maximum stress in steel beam top Flange due to shrinkage'''
    SHRINK_STEEL_TOP_FLANGE = "STRESS_SHRINK_BEAM_TOP"
    '''Maximum stress in concrete slab due to shrinkage'''
    SHRINK_CONC_MAX = "STRESS_SHRINK_CONC_STRESS"
    
    '''Maximum stress in steel beam bottom Flange in Final stage'''
    FINAL_TOTAL_STEEL_BTM_FLANGE = "STRESS_FINA_TOTL_BEAM_BOT"
    '''Maximum stress in steel beam web in Final stage'''
    FINAL_TOTAL_STEEL_WEB = "STRESS_FINA_TOTL_BEAM_WEB"
    '''Maximum stress in steel beam top Flange in Final stage'''
    FINAL_TOTAL_STEEL_TOP_FLANGE = "STRESS_FINA_TOTL_BEAM_TOP"
    '''Maximum stress in concrete slab in Final stage'''
    FINAL_TOTAL_CONC_MAX = "STRESS_FINA_TOTL_CONC_STRESS"


class eResultStrain(StrEnum):
    '''Maximum strain in concrete slab due to additional dead loads'''
    ADD_DEAD_CONC_MAX = "STRESS_ADDI_CONC_STRAIN"
    '''Maximum strain in concrete slab due to Final stage live loads'''
    FINAL_LIVE_CONC_MAX = "STRESS_FINA_LIVE_CONC_STRAIN"
    '''Maximum strain in concrete slab due to shrinkage'''
    SHRINK_CONC_MAX = "STRESS_SHRINK_CONC_STRAIN"
    '''Maximum strain in concrete slab in Final stage'''
    FINAL_TOTAL_CONC_MAX = "STRESS_FINA_TOTL_CONC_STRAIN"


class eResultVibration(StrEnum):
    '''Mode shape'''
    MODAL_SHAPE = "MODAL_SHAPE"
    '''Area of beam for vibration'''
    VIBRATION_A = "AREA_VIBRATION"
    '''moment of Inertia of beam for vibration'''
    VIBRATION_I = "I_VIBRATION"
    '''Neutral axis depth of beam for vibration'''
    VIBRATION_DEPTH_NA = "X_VIBRATION"
    

class eResultStuds(StrEnum):
    '''Actual number of studs provided from left end'''
    PROVIDED_STUDS_LEFT = "STUD_NUM_LEFT_PROV"
    '''Actual number of studs provided from right end'''
    PROVIDED_STUDS_RIGHT = "STUD_NUM_RIGHT_PROV"
    
    '''Used number of studs provided from left end'''
    USED_STUDS_LEFT = "STUD_NUM_LEFT_USED"
    '''Used number of studs provided from right end'''
    USED_STUDS_RIGHT = "STUD_NUM_RIGHT_USED"
    
    '''Actual shear interaction'''
    STUD_INT = "STUD_PERCENT_INTERACTION"
    '''One shear stud capacity'''
    SINGLE_STUD_CAPACITY = "STUD_ONE_CAPACITY"
    '''Actual stud capacity'''
    STUD_CAPACITY = "STUD_CONCRTE_FORCE"
    '''Actual shear capacity from left end'''
    STUD_CAPACITY_LEFT = "STUD_CAPACITY_LEFT"
    '''Actual shear capacity from right end'''
    STUD_CAPACITY_RIGHT = "STUD_CAPACITY_RIGHT"
    
    '''Required stud capacity for 100% shear interaction'''
    REQ_STUD_CAPACITY_100INT = "STUD_CONCRTE_FORCE_100"
    '''Required stud capacity for given moment'''
    REQ_STUD_CAPACITY_MOMENT = "STUD_CONCRTE_FORCE_REQ"
    '''Required shear interaction for given moment'''
    REQ_INT_MOMENT = "STUD_INTERACT_REQ"


# Type Alias for Results Enums
RESULT_TYPES = eResultStations | eResultProperties | eResultActions | \
                eResultCapacity | eResultNeutralAxis | eResultDeflection | \
                eResultStress | eResultStrain | eResultVibration | \
                eResultStuds