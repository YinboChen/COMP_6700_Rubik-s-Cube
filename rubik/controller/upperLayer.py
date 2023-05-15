'''
Created on Apr 15, 2023

@author: yinbo
'''
from rubik.model.constants import *
from rubik.model.cube import Cube
import time

def solveUpperLayer(theCube: Cube) -> str:
    rotateResult = []
    rotateResult.append('')
    _controllerMakerCornerSolved(theCube,rotateResult)
    _controllerAfterCornerSolved(theCube,rotateResult)
   
    return "".join(rotateResult)


def _isUpperLayerSolved(theCube):
    cubeList = list(theCube.get())
    eachFaceShouldUique = 6
    sumFCount = len(set(cubeList[FTL] + cubeList[FTM] + cubeList[FTR] + cubeList[FML] + cubeList[FMM] +\
                        cubeList[FMR] + cubeList[FBL] + cubeList[FBM] + cubeList[FBR]))
    sumRCount = len(set(cubeList[RTL] + cubeList[RTM] + cubeList[RTR] + cubeList[RML] + cubeList[RMM] +\
                        cubeList[RMR] + cubeList[RBL] + cubeList[RBM] + cubeList[RBR]))
    sumBCount = len(set(cubeList[BTL] + cubeList[BTM] + cubeList[BTR] + cubeList[BML] + cubeList[BMM] +\
                        cubeList[BMR] + cubeList[BBL] + cubeList[BBM] + cubeList[BBR]))
    sumLCount = len(set(cubeList[LTL] + cubeList[LTM] + cubeList[LTR] + cubeList[LML] + cubeList[LMM] +\
                        cubeList[LMR] + cubeList[LBL] + cubeList[LBM] + cubeList[LBR]))
    sumDCount = len(set(cubeList[DTL] + cubeList[DTM] + cubeList[DTR] + cubeList[DML] + cubeList[DMM] +\
                        cubeList[DMR] + cubeList[DBL] + cubeList[DBM] + cubeList[DBR]))
    sumUCount = len(set(cubeList[UTL] + cubeList[UTM] + cubeList[UTR] + cubeList[UML] + cubeList[UMM] +\
                        cubeList[UMR] + cubeList[UBL] + cubeList[UBM] + cubeList[UBR]))
    totalSumSixFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount +sumUCount
    if totalSumSixFacesCount == eachFaceShouldUique:
        return True
    else:
        return False

def _doesHaveTwoSamePieces(theCube):
    cubeList = list(theCube.get())
    checkTwoCornersList = [[cubeList[FTL],cubeList[FTR]],[cubeList[RTL],cubeList[RTR]],
                           [cubeList[BTL],cubeList[BTR]],[cubeList[LTL],cubeList[LTR]]]
    returnResult = []
    theLastIndex = 3
    for checkTwoCornersIndex in range(len(checkTwoCornersList)):
        if checkTwoCornersList[checkTwoCornersIndex][0]==checkTwoCornersList[checkTwoCornersIndex][1]:
            if checkTwoCornersList[checkTwoCornersIndex][0] == cubeList[FMM]:
                returnResult.append(cubeList[FMM])
                returnResult.append(str(checkTwoCornersIndex))
                return returnResult        
            elif checkTwoCornersList[checkTwoCornersIndex][0] == cubeList[RMM]:
                returnResult.append(cubeList[RMM])
                returnResult.append(str(checkTwoCornersIndex))
                return returnResult
            elif checkTwoCornersList[checkTwoCornersIndex][0] == cubeList[BMM]:
                returnResult.append(cubeList[BMM])
                returnResult.append(str(checkTwoCornersIndex))
                return returnResult 
            elif checkTwoCornersList[checkTwoCornersIndex][0] == cubeList[LMM]:
                returnResult.append(cubeList[LMM])
                returnResult.append(str(checkTwoCornersIndex))
                return returnResult 
        else:
            if checkTwoCornersIndex == theLastIndex:
                returnResult.append('')
                returnResult.append('')
                return returnResult
        
def _performAlignment(theCube,rotateResult,startLocation):
    cubeList = list(theCube.get())
    locationOnFRBL =[['','u','UU','U'],['U','','u','UU'],['UU','U','','u'],['u','UU','U','']]
    indexOnFRBL = ['0','1','2','3']
    checkLocationList = [cubeList[FMM],cubeList[RMM],cubeList[BMM],cubeList[LMM]]
    for checkLocationIndex in range(len(checkLocationList)):
        if startLocation[0]== checkLocationList[checkLocationIndex]:
            for checkMatchedIndex in range(len(indexOnFRBL)):
                if startLocation[1] == indexOnFRBL[checkMatchedIndex]:
                    rotateResult.append(locationOnFRBL[checkMatchedIndex][checkLocationIndex])
                    if locationOnFRBL[checkMatchedIndex][checkLocationIndex] =='':
                        break
                    else:
                        theCube.rotate(locationOnFRBL[checkMatchedIndex][checkLocationIndex])
            return checkLocationList[checkLocationIndex]
            
def _isUpperFourCornerSolved(theCube):
    cubeList = list(theCube.get())
    eachFaceShouldUique = 6
    sumFCount = len(set(cubeList[FTL] + cubeList[FTR] + cubeList[FML] + cubeList[FMM] +\
                        cubeList[FMR] + cubeList[FBL] + cubeList[FBM] + cubeList[FBR]))
    sumRCount = len(set(cubeList[RTL] + cubeList[RTR] + cubeList[RML] + cubeList[RMM] +\
                        cubeList[RMR] + cubeList[RBL] + cubeList[RBM] + cubeList[RBR]))
    sumBCount = len(set(cubeList[BTL] + cubeList[BTR] + cubeList[BML] + cubeList[BMM] +\
                        cubeList[BMR] + cubeList[BBL] + cubeList[BBM] + cubeList[BBR]))
    sumLCount = len(set(cubeList[LTL] + cubeList[LTR] + cubeList[LML] + cubeList[LMM] +\
                        cubeList[LMR] + cubeList[LBL] + cubeList[LBM] + cubeList[LBR]))
    sumDCount = len(set(cubeList[DTL] + cubeList[DTM] + cubeList[DTR] + cubeList[DML] + cubeList[DMM] +\
                        cubeList[DMR] + cubeList[DBL] + cubeList[DBM] + cubeList[DBR]))
    sumUCount = len(set(cubeList[UTL] + cubeList[UTM] + cubeList[UTR] + cubeList[UML] + cubeList[UMM] +\
                        cubeList[UMR] + cubeList[UBL] + cubeList[UBM] + cubeList[UBR]))
    totalSumSixFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount +sumUCount
    if totalSumSixFacesCount == eachFaceShouldUique:
        return True
    else:
        return False
            
def _performCornerSwith(theCube,rotateResult,twoSamePiecesResult):
    cubeList = list(theCube.get())
    alignmentInfo = twoSamePiecesResult[0]
    if alignmentInfo == '':
        rotateResult.append('lURuLUrRUrURUUr')
        theCube.rotate('lURuLUrRUrURUUr')
    elif alignmentInfo == cubeList[LMM]:
        rotateResult.append('lURuLUrRUrURUUr')
        theCube.rotate('lURuLUrRUrURUUr')
    elif alignmentInfo == cubeList[FMM]:
        rotateResult.append('fUBuFUbBUbUBUUb')
        theCube.rotate('fUBuFUbBUbUBUUb')
    elif alignmentInfo == cubeList[RMM]:
        rotateResult.append('rULuRUlLUlULUUl')
        theCube.rotate('rULuRUlLUlULUUl')
    elif alignmentInfo == cubeList[BMM]:
        rotateResult.append('bUFuBUfFUfUFuuf')
        theCube.rotate('bUFuBUfFUfUFuuf')

def _performMiddlePiecesSwitch(theCube,rotateResult):
    cubeList = list(theCube.get())
    if cubeList[BTM]==cubeList[BMM]:
        rotateResult.append('FFUrLFFlRUFF')
        theCube.rotate('FFUrLFFlRUFF')
    elif cubeList[LTM]==cubeList[LMM]:
        rotateResult.append('RRUbFRRfBURR')
        theCube.rotate('RRUbFRRfBURR')
    elif cubeList[FTM]==cubeList[FMM]:
        rotateResult.append('BBUlRBBrLUBB')
        theCube.rotate('BBUlRBBrLUBB')
    elif cubeList[RTM]==cubeList[RMM]:
        rotateResult.append('LLUfBLLbFULL')
        theCube.rotate('LLUfBLLbFULL')
    else:
        rotateResult.append('FFUrLFFlRUFF')
        theCube.rotate('FFUrLFFlRUFF')
        
def _controllerAfterCornerSolved(theCube,rotateResult):
    timeoutControllerAfter = time.time()+0.5
    while True:
        if _isUpperLayerSolved(theCube) == True:
            break
        elif time.time()>timeoutControllerAfter :
            break
        else:
            _performMiddlePiecesSwitch(theCube, rotateResult)

      
def _controllerMakerCornerSolved(theCube,rotateResult):
    theSideHasTwoSamePieces = 0
    timeoutControllerMaker= time.time()+0.5
    while True:
        if _isUpperFourCornerSolved(theCube) == True:
            break
        elif time.time()>timeoutControllerMaker:
            break
        else:
            startSideLocation = _doesHaveTwoSamePieces(theCube)
            if startSideLocation[theSideHasTwoSamePieces] != '':
                _performAlignment(theCube,rotateResult,startSideLocation)
                while True:
                    if _isUpperFourCornerSolved(theCube) == True:
                        break
                    else:
                        _performCornerSwith(theCube,rotateResult,startSideLocation)
            else:
                _performCornerSwith(theCube,rotateResult,startSideLocation)
                
    
    
    