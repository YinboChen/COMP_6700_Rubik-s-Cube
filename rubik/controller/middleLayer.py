'''
    Created on Mar 21, 2023
    
    @auther: Yinbo Chen
'''

from rubik.model.constants import *
from rubik.model.cube import Cube
import time

def solveMiddleLayer(theCube: Cube) -> str:
    rotateResult = []
    rotateResult.append('')
    timeout = time.time()+0.1
    while _isMiddleLayerSolved(theCube)!= True:
        if time.time()> timeout:
            break
        _matchAndLRTrigger(theCube, rotateResult)   
    return _stringReplace("".join(rotateResult))

def _isMiddleLayerSolved(theCube):
    cubeList = list(theCube.get())
    eachFaceShouldUique = 5
    sumFCount = len(set(cubeList[FML]+cubeList[FMM]+cubeList[FMR]+cubeList[FBL]+cubeList[FBM]+cubeList[FBR]))
    sumRCount = len(set(cubeList[RML]+cubeList[RMM]+cubeList[RMR]+cubeList[RBL]+cubeList[RBM]+cubeList[RBR]))
    sumBCount = len(set(cubeList[BML]+cubeList[BMM]+cubeList[BMR]+cubeList[BBL]+cubeList[BBM]+cubeList[BBR]))
    sumLCount = len(set(cubeList[LML]+cubeList[LMM]+cubeList[LMR]+cubeList[LBL]+cubeList[LBM]+cubeList[LBR]))
    sumDCount = len(set(cubeList[DTL]+cubeList[DTM]+cubeList[DTR]+cubeList[DML]+cubeList[DMM]+cubeList[DMR]+\
                        cubeList[DBL]+cubeList[DBM]+cubeList[DBR]))
    totalSumFiveFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount
    if totalSumFiveFacesCount == eachFaceShouldUique:
        return True
    else:
        return False

def _doesTopCenterInTopEdgeCross(theCube):
    inAll = 4
    cubeList = list(theCube.get())
    topCrossList = [[cubeList[UBM],cubeList[FTM]],[cubeList[UMR],cubeList[RTM]],
                    [cubeList[UTM],cubeList[BTM]],[cubeList[UML],cubeList[LTM]]]
    countNum = 0
    for topCrossListIndex in range(len(topCrossList)):
        if cubeList[UMM] in topCrossList[topCrossListIndex]:
            countNum +=1
            if countNum == inAll:
                return True
        else:
            return False
       
def _updateSwitchMiddleLayerCorner(theCube):
    cubeList = list(theCube.get())
    middelCornerList = [[cubeList[FMR], cubeList[RML], cubeList[FMM], cubeList[RMM]], 
                        [cubeList[RMR], cubeList[BML], cubeList[RMM], cubeList[BMM]], 
                        [cubeList[BMR], cubeList[LML], cubeList[BMM], cubeList[LMM]], 
                        [cubeList[LMR], cubeList[FML], cubeList[LMM], cubeList[FMM]]]
    return middelCornerList, cubeList

def _switchMiddleLayerCorner(theCube,rotateResult):
    middelCornerList, cubeList = _updateSwitchMiddleLayerCorner(theCube)
    facingFMM = 0
    facingRMM = 1
    facingBMM = 2
    facingLMM = 3
    for middleCornerIndex in range(len(middelCornerList)):
        if (middelCornerList[middleCornerIndex][0]==middelCornerList[middleCornerIndex][2]) and\
            (middelCornerList[middleCornerIndex][1]==middelCornerList[middleCornerIndex][3]):
            pass
        else:
            if  middleCornerIndex == facingFMM:
                rotateResult.append('RUrufuF')
                theCube.rotate('RUrufuF')
            elif middleCornerIndex == facingRMM:
                rotateResult.append('BUburuR')
                theCube.rotate('BUburuR')
            elif middleCornerIndex == facingBMM:
                rotateResult.append('LUlubuB')
                theCube.rotate('LUlubuB')
            elif middleCornerIndex == facingLMM:
                rotateResult.append('FUfuluL')
                theCube.rotate('FUfuluL')
            middelCornerList, cubeList = _updateSwitchMiddleLayerCorner(theCube)  
            _matchAndLRTrigger(theCube, rotateResult)

def _updateMatchAndLRTrigger(theCube):
    cubeList = list(theCube.get())
    topEdgeCheckList = [[cubeList[UBM], cubeList[FTM], cubeList[FMM]], [cubeList[UMR], cubeList[RTM], cubeList[RMM]], 
                        [cubeList[UTM], cubeList[BTM], cubeList[BMM]], [cubeList[UML], cubeList[LTM], cubeList[LMM]]]
    return topEdgeCheckList, cubeList

def _performLRTrigger(theCube, rotateResult, topEdgeCheckList, cubeList, topListCheckIndex):
    if topEdgeCheckList[topListCheckIndex][2] == cubeList[FMM]:
        if topEdgeCheckList[topListCheckIndex][0] == cubeList[LMM]:
            rotateResult.append('uluLUFUf')
            theCube.rotate('uluLUFUf')
        elif topEdgeCheckList[topListCheckIndex][0] == cubeList[RMM]:
            rotateResult.append('URUrufuF')
            theCube.rotate('URUrufuF')
    elif topEdgeCheckList[topListCheckIndex][2] == cubeList[RMM]:
        if topEdgeCheckList[topListCheckIndex][0] == cubeList[FMM]:
            rotateResult.append('ufuFURUr')
            theCube.rotate('ufuFURUr')
        elif topEdgeCheckList[topListCheckIndex][0] == cubeList[BMM]:
            rotateResult.append('UBUburuR')
            theCube.rotate('UBUburuR')
    elif topEdgeCheckList[topListCheckIndex][2] == cubeList[BMM]:
        if topEdgeCheckList[topListCheckIndex][0] == cubeList[RMM]:
            rotateResult.append('uruRUBUb')
            theCube.rotate('uruRUBUb')
        elif topEdgeCheckList[topListCheckIndex][0] == cubeList[LMM]:
            rotateResult.append('ULUlubuB')
            theCube.rotate('ULUlubuB')
    elif topEdgeCheckList[topListCheckIndex][2] == cubeList[LMM]:
        if topEdgeCheckList[topListCheckIndex][0] == cubeList[BMM]:
            rotateResult.append('ubuBULUl')
            theCube.rotate('ubuBULUl')
        elif topEdgeCheckList[topListCheckIndex][0] == cubeList[FMM]:
            rotateResult.append('UFUfuluL')
            theCube.rotate('UFUfuluL')

def _matchAndLRTrigger(theCube,rotateResult): 
    topEdgeCheckList, cubeList = _updateMatchAndLRTrigger(theCube)
    if _doesTopCenterInTopEdgeCross(theCube)!= True:
        for topListCheckIndex in range(len(topEdgeCheckList)):          
            if cubeList[UMM] in set(topEdgeCheckList[topListCheckIndex][0]+ topEdgeCheckList[topListCheckIndex][1]):
                pass
            elif topEdgeCheckList[topListCheckIndex][1] == topEdgeCheckList[topListCheckIndex][2]:
                _performLRTrigger(theCube, rotateResult, topEdgeCheckList, cubeList, topListCheckIndex)
                topEdgeCheckList, cubeList = _updateMatchAndLRTrigger(theCube)
                break
        rotateResult.append('U')
        theCube.rotate('U')
        topEdgeCheckList, cubeList = _updateMatchAndLRTrigger(theCube)
    else:
        if _isMiddleLayerSolved(theCube) == False:
            _switchMiddleLayerCorner(theCube,rotateResult)
        
def _stringReplace(joinedString):
    replaceDict ={'UUU':'u','Uu':'','uuu':'U'}
    for key, value in replaceDict.items():
        joinedString = joinedString.replace(key,value)
    return joinedString     
            
    
    
    
    
    
    
    
    
    
    
    