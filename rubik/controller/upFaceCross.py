'''
    Created on Apr 03, 2023
    
    @auther: Yinbo Chen
'''

from rubik.model.constants import *
from rubik.model.cube import Cube
import time

def solveUpCross(theCube: Cube) -> str:
    rotateResult = []
    rotateResult.append('')
    timeout = time.time()+0.1
    
    while _isUpFaceCrossSolved(theCube) != True:
        if time.time()> timeout:
            break
        else:
            if (_doesVerticalExist(theCube, rotateResult) == False) and (_doesTargetOnNineAndTwelv(theCube, rotateResult) == False):
                _doFURurfRotation(theCube, rotateResult)
            elif (_doesVerticalExist(theCube, rotateResult) == True) and (_doesTargetOnNineAndTwelv(theCube, rotateResult)== False):
                _doFURurfRotation(theCube, rotateResult)
            elif _doesTargetOnNineAndTwelv(theCube, rotateResult)== True:
                _doFURurfRotation(theCube, rotateResult)      
            
    return "".join(rotateResult)     

def _isUpFaceCrossSolved(theCube):
    cubeList = list(theCube.get())
    eachFaceShouldUique = 6
    sumFCount = len(set(cubeList[FML]+cubeList[FMM]+cubeList[FMR]+cubeList[FBL]+cubeList[FBM]+cubeList[FBR]))
    sumRCount = len(set(cubeList[RML]+cubeList[RMM]+cubeList[RMR]+cubeList[RBL]+cubeList[RBM]+cubeList[RBR]))
    sumBCount = len(set(cubeList[BML]+cubeList[BMM]+cubeList[BMR]+cubeList[BBL]+cubeList[BBM]+cubeList[BBR]))
    sumLCount = len(set(cubeList[LML]+cubeList[LMM]+cubeList[LMR]+cubeList[LBL]+cubeList[LBM]+cubeList[LBR]))
    sumDCount = len(set(cubeList[DTL]+cubeList[DTM]+cubeList[DTR]+cubeList[DML]+cubeList[DMM]+cubeList[DMR]+\
                        cubeList[DBL]+cubeList[DBM]+cubeList[DBR]))
    sumUCrossCount = len(set(cubeList[UTM]+cubeList[UML]+cubeList[UMM]+cubeList[UMR]+cubeList[UBM]))
    totalSumSixFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount +sumUCrossCount
    if totalSumSixFacesCount == eachFaceShouldUique:
        return True
    else:
        return False
    
def _doesVerticalExist(theCube, rotateResult):
    cubeList = list(theCube.get())
    topDownVerticalList = [cubeList[UTM],cubeList[UMM],cubeList[UBM]]
    leftRighVerticalList = [cubeList[UML],cubeList[UMM],cubeList[UMR]]
    if set(topDownVerticalList) == set(cubeList[UMM]):
        return True
    elif set(leftRighVerticalList) == set(cubeList[UMM]):
        rotateResult.append('U')
        theCube.rotate('U')
        return True
    else:
        return False
    
def _doesTargetOnNineAndTwelv(theCube, rotateResult):
    cubeList = list(theCube.get())
    nineTwelvCrossList = [[cubeList[UML],cubeList[UTM]],[cubeList[UTM],cubeList[UMR]],
                          [cubeList[UMR],cubeList[UBM]],[cubeList[UBM],cubeList[UML]]]
    if set(nineTwelvCrossList[0])==set(cubeList[UMM]):
        return True
    elif set(nineTwelvCrossList[1])==set(cubeList[UMM]):
        rotateResult.append('u')
        theCube.rotate('u')
        return True
    elif set(nineTwelvCrossList[2])==set(cubeList[UMM]):
        rotateResult.append('UU')
        theCube.rotate('UU')
        return True
    elif set(nineTwelvCrossList[3])==set(cubeList[UMM]):
        rotateResult.append('U')
        theCube.rotate('U')
        return True
    else:
        return False

def _doFURurfRotation(theCube, rotateResult):
        rotateResult.append('FURurf')
        theCube.rotate('FURurf')


        
    
    
    