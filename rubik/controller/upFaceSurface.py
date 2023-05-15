'''
Created on Apr 4, 2023

@author: yinbo Chen
'''
from rubik.model.constants import *
from rubik.model.cube import Cube
import time

def solveUpSurface(theCube: Cube) -> str:
    rotateResult = []
    rotateResult.append('')
    timeout = time.time()+0.5
    while _isUpFaceSurfaceSolved(theCube) != True:
        # print(theCube.get())
        # print(rotateResult)
        if time.time()> timeout:
            break
        else:
            if _checkTopHeavyExist(theCube,rotateResult) == True:
                _doRUrURUUr(theCube,rotateResult)
            elif _doesCleanCrossExist(theCube, rotateResult) ==True:
                _doRUrURUUr(theCube,rotateResult)
                if _doesAFishExist(theCube,rotateResult) == True:
                    _doRUrURUUr(theCube,rotateResult)
            elif _doesAFishExist(theCube,rotateResult) == True:
                _doRUrURUUr(theCube,rotateResult)
            else:
                _doRUrURUUr(theCube,rotateResult)
            
    return "".join(rotateResult)

def _isUpFaceSurfaceSolved(theCube):
    cubeList = list(theCube.get())
    eachFaceShouldUique = 6
    sumFCount = len(set(cubeList[FML]+cubeList[FMM]+cubeList[FMR]+cubeList[FBL]+cubeList[FBM]+cubeList[FBR]))
    sumRCount = len(set(cubeList[RML]+cubeList[RMM]+cubeList[RMR]+cubeList[RBL]+cubeList[RBM]+cubeList[RBR]))
    sumBCount = len(set(cubeList[BML]+cubeList[BMM]+cubeList[BMR]+cubeList[BBL]+cubeList[BBM]+cubeList[BBR]))
    sumLCount = len(set(cubeList[LML]+cubeList[LMM]+cubeList[LMR]+cubeList[LBL]+cubeList[LBM]+cubeList[LBR]))
    sumDCount = len(set(cubeList[DTL]+cubeList[DTM]+cubeList[DTR]+cubeList[DML]+cubeList[DMM]+cubeList[DMR]+\
                        cubeList[DBL]+cubeList[DBM]+cubeList[DBR]))
    sumUCrossCount = len(set(cubeList[UTM]+cubeList[UML]+cubeList[UMM]+cubeList[UMR]+cubeList[UBM]+\
                             cubeList[UTL]+cubeList[UTR]+cubeList[UBL]+cubeList[UBR]))
    totalSumSixFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount +sumUCrossCount
    if totalSumSixFacesCount == eachFaceShouldUique:
        return True
    else:
        return False
    
def _doesCleanCrossExist(theCube, rotateResult):
    cubeList = list(theCube.get())
    cleanCrossList = [cubeList[UTM],cubeList[UML],cubeList[UMM],cubeList[UMR],cubeList[UBM]]
    fourUpSurfaceCornersList = [cubeList[UTL],cubeList[UTR],cubeList[UBL],cubeList[UBR]]
    checkTopLeftSideCornerList = [cubeList[LTR],cubeList[FTR],cubeList[RTR],cubeList[BTR]]
    if set(cleanCrossList)==set(cubeList[UMM]) and (cubeList[UMM] not in fourUpSurfaceCornersList):
        if checkTopLeftSideCornerList[0]==cubeList[UMM]:
            return True
        elif checkTopLeftSideCornerList[1] == cubeList[UMM]:
            rotateResult.append('U')
            theCube.rotate('U')
            return True
        elif checkTopLeftSideCornerList[2] == cubeList[UMM]:
            rotateResult.append('UU')
            theCube.rotate('UU')
            return True
        elif checkTopLeftSideCornerList[3] == cubeList[UMM]:
            rotateResult.append('u')
            theCube.rotate('u')
            return True
        else:
            return False   
    else:
            return False  
        
def _doRUrURUUr(theCube,rotateResult):
    rotateResult.append('RUrURUUr')
    theCube.rotate('RUrURUUr')
    
def _doesAFishExist(theCube,rotateResult):
    cubeList = list(theCube.get())
    cleanCrossrishList = [cubeList[UTM],cubeList[UML],cubeList[UMM],cubeList[UMR],cubeList[UBM]]
    restThreeCornersList =[[cubeList[UTL],cubeList[UTR],cubeList[UBR]],[cubeList[UTR],cubeList[UBR],cubeList[UBL]],
                           [cubeList[UBR],cubeList[UBL],cubeList[UTL]],[cubeList[UBL],cubeList[UTL],cubeList[UTR]]]
    #fourUpSurfaceCornersList = [cubeList[UTL],cubeList[UTR],cubeList[UBL],cubeList[UBR]]
    if (set(cleanCrossrishList)==set(cubeList[UMM])) and\
        (cubeList[UMM] == cubeList[UBL]) and\
        (cubeList[UMM] not in restThreeCornersList[0]):
        # and (cubeList[FTR] == cubeList[UMM]):
        return True
    elif (set(cleanCrossrishList)==set(cubeList[UMM])) and\
         (cubeList[UMM] == cubeList[UTL]) and\
         (cubeList[UMM] not in restThreeCornersList[1]):# and (cubeList[LTR] == cubeList[UMM]):
        rotateResult.append('u')
        theCube.rotate('u')
        return True
    elif (set(cleanCrossrishList)==set(cubeList[UMM])) and\
        (cubeList[UMM] == cubeList[UTR]) and\
        (cubeList[UMM] not in restThreeCornersList[2]):# and (cubeList[BTR] == cubeList[UMM]):
        rotateResult.append('UU')
        theCube.rotate('UU')
        return True
    elif (set(cleanCrossrishList)==set(cubeList[UMM])) and\
        (cubeList[UMM] == cubeList[UBR]) and\
        (cubeList[UMM] not in restThreeCornersList[3]):# and (cubeList[RTR] == cubeList[UMM]):
        rotateResult.append('U')
        theCube.rotate('U')
        return True  
    else:
        return False

def _checkTopHeavyExist(theCube,rotateResult):
    cubeList = list(theCube.get())
    heavyList = [[cubeList[UTL],cubeList[UTM],cubeList[UTR],cubeList[UML],cubeList[UMM],cubeList[UMR],cubeList[UBM]],
                 [cubeList[UTM],cubeList[UTR],cubeList[UML],cubeList[UMM],cubeList[UMR],cubeList[UBM],cubeList[UBR]],
                 [cubeList[UTM],cubeList[UML],cubeList[UMM],cubeList[UMR],cubeList[UBL],cubeList[UBM],cubeList[UBR]],
                 [cubeList[UTL],cubeList[UTM],cubeList[UML],cubeList[UMM],cubeList[UMR],cubeList[UBL],cubeList[UBM]]]
    if set(cubeList[UMM])==set(heavyList[0]):
        return True
    elif set(cubeList[UMM])==set(heavyList[1]):
        rotateResult.append('u')
        theCube.rotate('u')
        return True
    elif set(cubeList[UMM])==set(heavyList[2]):
        rotateResult.append('UU')
        theCube.rotate('UU')
        return True
    elif set(cubeList[UMM])==set(heavyList[3]):
        rotateResult.append('U')
        theCube.rotate('U')
        return True
    
    
    
    
    
    
    
    
    
    
    