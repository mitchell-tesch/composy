# Comosy - Compos API python wrapper
# Results option enumerations

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
    '''Effective slab width on left side'''
    EFF_SLAB_WIDTH_LHS = "SLAB_WIDTH_L_EFFECT"
    '''Effective slab width on right side'''
    EFF_SLAB_WIDTH_RHS = "SLAB_WIDTH_R_EFFECT"

    # '''Welding thickness at top'''
    # "GIRDER_WELD_THICK_T"
    # '''Welding thickness at bottom'''
    # "GIRDER_WELD_THICK_B"
    
    # '''moment of Inertia of steel beam'''
    # "I_STEEL_BEAM"
    
    # '''Neutral axis depth of steel beam'''
    # 'X_STEEL_BEAM'
    
    # '''Area of steel beam'''
    # "AREA_STEEL_BEAM"
    
    # '''moment of Inertia of beam for long term loading'''
    # "I_LONG_TERM"
    
    # '''Neutral axis depth of beam for long term loading'''
    # "X_LONG_TERM"
    
    # '''Area of beam for long term loading'''
    # "AREA_LONG_TERM"
    
    # '''moment of Inertia of beam for short term loading'''
    # "I_SHORT_TERM"
    
    # '''Neutral axis depth of beam for short term loading'''
    # 'X_SHORT_TERM'

    # ''' Area of beam for short term loading'''
    # "AREA_SHORT_TERM"
    
    # '''moment of Inertia of beam for shrinkage'''
    # "I_SHRINK"
    
    # '''Neutral axis depth of beam for shrinkage'''
    # "X_SHRINK"
    
    # '''Area of beam for shrinkage'''
    # "AREA_SHRINK"
    
    # '''Effective moment of Inertia of beam'''
    # "I_EFFECTIVE"
    
    # '''Neutral axis depth of beam under combined loading'''
    # "X_EFFECTIVE"
    
    # '''Effective Area of beam'''
    # "AREA_EFFECT"
    
    # '''Flange class in Construction stage'''
    # "CLAS_CONS_FLAN_CLASS"

    # '''web class in Construction stage'''
    # "CLAS_CONS_WEB_CLASS"
    
    # '''Section class in Construction stage'''
    # "CLAS_CONS_SECTION"
    
    # '''Flange class in Final stage'''
    # "CLAS_FINA_FLAN_CLASS"
    
    # '''web class in Final stage'''
    # "CLAS_FINA_WEB_CLASS"
    
    # '''Section class in Final stage'''
    # "CLAS_FINA_SECTION"


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


# class eResultDeflection(StrEnum):
    # '''Deflection due to Construction dead loads'''
    # "DEFL_CONS_DEAD_LOAD"
    
    # '''Deflection due to additional dead loads'''
    # "DEFL_ADDI_DEAD_LOAD"
    
    # '''Deflection due to Final stage live loads'''
    # "DEFL_FINA_LIVE_LOAD"
    
    # '''Deflection due to shrinkage of concrete'''
    # "DEFL_SHRINK"
    
    # '''Deflection due to post Construction loads'''
    # "DEFL_POST_CONS"
    
    # '''Total Deflection'''
    # "DEFL_FINA_TOTAL"


# class eResultStress(StrEnum):
    # '''Maximum stress in steel beam bottom Flange due to Construction loads'''
    # "STRESS_CONS_BEAM_BOT"
    
    # '''Maximum stress in steel beam web due to Construction loads'''
    # "STRESS_CONS_BEAM_WEB"
    
    # '''Maximum stress in steel beam top Flange due to Construction loads'''
    # "STRESS_CONS_BEAM_TOP"
    
    # '''Maximum stress in steel beam bottom Flange due to additional dead loads'''
    # "STRESS_ADDI_BEAM_BOT"
    
    # '''Maximum stress in steel beam web due to additional dead loads'''
    # "STRESS_ADDI_BEAM_WEB"
    
    # '''Maximum stress in steel beam top Flange  due to additional dead loads'''
    # "STRESS_ADDI_BEAM_TOP"
    
    # '''Maximum stress in concrete slab due to additional dead loads'''
    # "STRESS_ADDI_CONC_STRESS"
    
    # '''Maximum strain in concrete slab due to additional dead loads'''
    # "STRESS_ADDI_CONC_STRAIN"
    
    # '''Maximum stress in steel beam bottom Flange due to Final stage live dead loads'''
    # "STRESS_FINA_LIVE_BEAM_BOT"
    
    # '''Maximum stress in steel beam web due to Final stage live dead loads'''
    # "STRESS_FINA_LIVE_BEAM_WEB"
    
    # '''Maximum stress in steel beam top Flange  due to Final stage live dead loads'''
    # "STRESS_FINA_LIVE_BEAM_TOP"
    
    # '''Maximum stress in concrete slab due to Final stage live loads'''
    # "STRESS_FINA_LIVE_CONC_STRESS"
    
    # '''Maximum strain in concrete slab due to Final stage live loads'''
    # "STRESS_FINA_LIVE_CONC_STRAIN"
    
    # '''Maximum stress in steel beam bottom Flange due to shrinkage'''
    # "STRESS_SHRINK_BEAM_BOT"
    
    # '''Maximum stress in steel beam web due to shrinkage'''
    # "STRESS_SHRINK_BEAM_WEB"
    
    # '''Maximum stress in steel beam top Flange due to shrinkage'''
    # "STRESS_SHRINK_BEAM_TOP"
    
    # '''Maximum stress in concrete slab due to shrinkage'''
    # "STRESS_SHRINK_CONC_STRESS"
    
    # '''Maximum strain in concrete slab due to shrinkage'''
    # "STRESS_SHRINK_CONC_STRAIN"
    
    # '''Maximum stress in steel beam bottom Flange in Final stage'''
    # "STRESS_FINA_TOTL_BEAM_BOT"
    
    # '''Maximum stress in steel beam web in Final stage'''
    # "STRESS_FINA_TOTL_BEAM_WEB"
    
    # '''Maximum stress in steel beam top Flange in Final stage'''
    # "STRESS_FINA_TOTL_BEAM_TOP"
    
    # '''Maximum stress in concrete slab in Final stage'''
    # "STRESS_FINA_TOTL_CONC_STRESS"
    
    # '''Maximum strain in concrete slab in Final stage'''
    # "STRESS_FINA_TOTL_CONC_STRAIN"


# class eResultVibration(StrEnum):
    # '''Mode shape'''
    # "MODAL_SHAPE"
    
    # '''moment of Inertia of beam for vibration'''
    # "I_VIBRATION"
    
    # '''Neutral axis depth of beam for vibration'''
    # "X_VIBRATION"
    
    # '''Area of beam for vibration'''
    # "AREA_VIBRATION"


# class eResultStuds(StrEnum):
    # '''Actual stud capacity'''
    # "STUD_CONCRTE_FORCE"
    
    # '''Actual number of studs provided from left end'''
    # "STUD_NUM_LEFT_PROV"
    
    # '''Actual number of studs provided from right end'''
    # "STUD_NUM_RIGHT_PROV"
    
    # '''Used number of studs provided from left end'''
    # "STUD_NUM_LEFT_USED"
    
    # '''Used number of studs provided from right end'''
    # "STUD_NUM_RIGHT_USED"
    
    # '''Required stud capacity for 100% shear interaction'''
    # "STUD_CONCRTE_FORCE_100"
    
    # '''Required stud capacity for given moment'''
    # "STUD_CONCRTE_FORCE_REQ"
    
    # '''Required shear interaction for given moment'''
    # "STUD_INTERACT_REQ"
    
    # '''One shear stud capacity'''
    # "STUD_ONE_CAPACITY"
    
    # '''Actual shear interaction'''
    # "STUD_PERCENT_INTERACTION"
    
    # '''Actual shear capacity from left end'''
    # "STUD_CAPACITY_LEFT"
    
    # '''Actual shear capacity from right end'''
    # "STUD_CAPACITY_RIGHT"

RESULT_OPTIONS = eResultStations | \
                 eResultProperties | \
                 eResultActions | \
                 eResultCapacity | \
                 eResultNeutralAxis