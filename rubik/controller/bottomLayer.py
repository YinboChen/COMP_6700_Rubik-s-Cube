'''
    Created on Feb 27, 2023
    
    @auther: Yinbo Chen
'''

from rubik.model.constants import *
from rubik.model.cube import Cube
import time


def solveBottomLayer(theCube: Cube) -> str:
    
    rotateResult = []
    rotateResult.append('')
    timeout = time.time()+2
    while _isBottomLayerSolved(theCube)!= True:
        if time.time()> timeout:
            break   
        _findOnTopsidesPatternLocations(theCube,rotateResult) 
        _findOnLeftsidesPatternLocations(theCube,rotateResult)
        _findOnRightsidesPatternLocations(theCube,rotateResult)
        _findOnDownsidesPatternLocations(theCube,rotateResult)
           
    return _stringReplace("".join(rotateResult))

def _isBottomLayerSolved(theCube):   
    cubeList = list(theCube.get())
    eachFaceShouldUique = 5
    sumFCount = len(set(cubeList[FMM]+cubeList[FBL]+cubeList[FBM]+cubeList[FBR]))
    sumRCount = len(set(cubeList[RMM]+cubeList[RBL]+cubeList[RBM]+cubeList[RBR]))
    sumBCount = len(set(cubeList[BMM]+cubeList[BBL]+cubeList[BBM]+cubeList[BBR]))
    sumLCount = len(set(cubeList[LMM]+cubeList[LBL]+cubeList[LBM]+cubeList[LBR]))
    sumDCount = len(set(cubeList[DTL]+cubeList[DTM]+cubeList[DTR]+cubeList[DML]+\
                        cubeList[DMM]+cubeList[DMR]+cubeList[DBL]+cubeList[DBM]+\
                        cubeList[DBR]))
    totalSumFiveFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount
    if totalSumFiveFacesCount == eachFaceShouldUique:
        return True
    else:
        return False
    

def _findOnLeftsidesUpdateCube(theCube):
    cubeList = list(theCube.get())
    checkLeftSingleCharList = [cubeList[LTR], cubeList[FTR], cubeList[RTR], cubeList[BTR]]
    checkCharOnLeftSidesList = [[cubeList[LTR], cubeList[FTL], cubeList[FMM]], 
                                [cubeList[FTR], cubeList[RTL], cubeList[RMM]], 
                                [cubeList[RTR], cubeList[BTL], cubeList[BMM]], 
                                [cubeList[BTR], cubeList[LTL], cubeList[LMM]]]
    return cubeList, checkLeftSingleCharList, checkCharOnLeftSidesList

def _findOnLeftsidesPatternLocations(theCube,rotateResult):
    allSideLeftSlotsAreEmpty = 4  
    cubeList, checkLeftSingleCharList, checkCharOnLeftSidesList = _findOnLeftsidesUpdateCube(theCube)
    while cubeList[DMM] in checkLeftSingleCharList:
        while True:
            emptyLeftCheck = 0
            for checkIndex in range(len(checkCharOnLeftSidesList)):
                if cubeList[DMM] == checkCharOnLeftSidesList[checkIndex][0] and \
                    checkCharOnLeftSidesList[checkIndex][1] == checkCharOnLeftSidesList[checkIndex][2]:
                    if checkCharOnLeftSidesList[checkIndex][2] == cubeList[FMM]:
                        rotateResult.append('luL')
                        theCube.rotate('luL')
                    elif checkCharOnLeftSidesList[checkIndex][2] == cubeList[RMM]:
                        rotateResult.append('fuF')
                        theCube.rotate('fuF')
                    elif checkCharOnLeftSidesList[checkIndex][2] == cubeList[BMM]:
                        rotateResult.append('ruR')
                        theCube.rotate('ruR')
                    elif checkCharOnLeftSidesList[checkIndex][2] == cubeList[LMM]:
                        rotateResult.append('buB')
                        theCube.rotate('buB')                      
                else:
                    emptyLeftCheck +=1
                cubeList, checkLeftSingleCharList, checkCharOnLeftSidesList = _findOnLeftsidesUpdateCube(theCube)
            if emptyLeftCheck == allSideLeftSlotsAreEmpty :
                break
        if cubeList[DMM] in checkLeftSingleCharList:
            rotateResult.append('U')
            theCube.rotate('U')
            cubeList, checkLeftSingleCharList, checkCharOnLeftSidesList = _findOnLeftsidesUpdateCube(theCube)
    

def _findOnRightsidesUpdateCube(theCube):
    cubeList = list(theCube.get())
    checkRightSingleCharList = [cubeList[FTL], cubeList[RTL], cubeList[BTL], cubeList[LTL]]
    checkCharOnRightSidesList = [[cubeList[FTL], cubeList[LTR], cubeList[LMM]], 
                                 [cubeList[RTL], cubeList[FTR], cubeList[FMM]], 
                                 [cubeList[BTL], cubeList[RTR], cubeList[RMM]], 
                                 [cubeList[LTL], cubeList[BTR], cubeList[BMM]]]
    return cubeList, checkRightSingleCharList, checkCharOnRightSidesList

def _findOnRightsidesPatternLocations(theCube,rotateResult):  
    allSideRightSlotsAreEmpty = 4
    cubeList, checkRightSingleCharList, checkCharOnRightSidesList = _findOnRightsidesUpdateCube(theCube)
    while cubeList[DMM] in checkRightSingleCharList:
        while True:
            emptyRightCheck = 0
            for checkIndex in range(len(checkCharOnRightSidesList)):
                if cubeList[DMM] == checkCharOnRightSidesList[checkIndex][0] and \
                    checkCharOnRightSidesList[checkIndex][1] == checkCharOnRightSidesList[checkIndex][2]:
                    if checkCharOnRightSidesList[checkIndex][2] == cubeList[LMM]:
                        rotateResult.append('FUf')
                        theCube.rotate('FUf')
                    elif checkCharOnRightSidesList[checkIndex][2] == cubeList[FMM]:
                        rotateResult.append('RUr')
                        theCube.rotate('RUr')
                    elif checkCharOnRightSidesList[checkIndex][2] == cubeList[RMM]:
                        rotateResult.append('BUb')
                        theCube.rotate('BUb')
                    elif checkCharOnRightSidesList[checkIndex][2] == cubeList[BMM]:
                        rotateResult.append('LUl')
                        theCube.rotate('LUl') 
                         
                else:
                    emptyRightCheck +=1
                    # print(emptyRightCheck)
            
                cubeList, checkRightSingleCharList, checkCharOnRightSidesList = _findOnRightsidesUpdateCube(theCube)
            if emptyRightCheck == allSideRightSlotsAreEmpty :
                break
        if cubeList[DMM] in checkRightSingleCharList:
            rotateResult.append('U')
            theCube.rotate('U')
            cubeList, checkRightSingleCharList, checkCharOnRightSidesList = _findOnRightsidesUpdateCube(theCube)

def _findOnTopsidesUpdateCube(theCube):
    cubeList = list(theCube.get())
    checkTopSingleCharList = [cubeList[UBR], cubeList[UTR], cubeList[UTL], cubeList[UBL]]
    checkBottomGroupCharsList = [[cubeList[DTR], cubeList[FBR], cubeList[RBL], cubeList[FMM], cubeList[RMM]], 
                                 [cubeList[DBR], cubeList[RBR], cubeList[BBL], cubeList[RMM], cubeList[BMM]], 
                                 [cubeList[DBL], cubeList[BBR], cubeList[LBL], cubeList[BMM], cubeList[LMM]], 
                                 [cubeList[DTL], cubeList[LBR], cubeList[FBL], cubeList[LMM], cubeList[FMM]]]
    return cubeList, checkTopSingleCharList, checkBottomGroupCharsList

def _findOnTopsidesPatternLocations(theCube,rotateResult):
    positionUBR = 0
    positionUTR = 1
    positionUTL = 2
    positionUBL = 3
    timeoutTop = time.time()+1
    cubeList, checkTopSingleCharList,checkBottomGroupCharsList= _findOnTopsidesUpdateCube(theCube)   
    while cubeList[DMM] in checkTopSingleCharList:
        if time.time()> timeoutTop:
                break
        for checkTopIndex in range(len(checkTopSingleCharList)):
            if checkTopSingleCharList[checkTopIndex]==cubeList[DMM]:
                if checkBottomGroupCharsList[checkTopIndex][0]!= cubeList[DMM] or\
                        (checkBottomGroupCharsList[checkTopIndex][1]!=checkBottomGroupCharsList[checkTopIndex][3] and\
                         checkBottomGroupCharsList[checkTopIndex][2]!=checkBottomGroupCharsList[checkTopIndex][4]):
                    if checkTopIndex == positionUBR:
                        rotateResult.append('RUUr')
                        theCube.rotate('RUUr')
                    elif checkTopIndex == positionUTR:
                        rotateResult.append('BUUb')
                        theCube.rotate('BUUb')
                    elif checkTopIndex == positionUTL:
                        rotateResult.append('LUUl')
                        theCube.rotate('LUUl')
                    elif checkTopIndex == positionUBL:
                        rotateResult.append('FUUf')
                        theCube.rotate('FUUf')
                else:
                    pass
                    # rotateResult.append('U')
                    # theCube.rotate('U')  
        cubeList, checkTopSingleCharList, checkBottomGroupCharsList= _findOnTopsidesUpdateCube(theCube)
        _findOnLeftsidesPatternLocations(theCube,rotateResult)
        _findOnRightsidesPatternLocations(theCube,rotateResult)
        rotateResult.append('U')
        theCube.rotate('U')
        cubeList, checkTopSingleCharList, checkBottomGroupCharsList= _findOnTopsidesUpdateCube(theCube)
        # findOnDownsidesPatternLocations(theCube,rotateResult)
        
def _findOnDownsidesUpdateCube(theCube):
    cubeList = list(theCube.get())
    bottomCornerList = [[cubeList[DTR], cubeList[FBR], cubeList[RBL]], 
                        [cubeList[DBR], cubeList[RBR], cubeList[BBL]], 
                        [cubeList[DBL], cubeList[BBR], cubeList[LBL]], 
                        [cubeList[DTL], cubeList[LBR], cubeList[FBL]]]
    topCornerList = [[cubeList[UBR], cubeList[FTR], cubeList[RTL]], 
                     [cubeList[UTR], cubeList[RTR], cubeList[BTL]], 
                     [cubeList[UTL], cubeList[BTR], cubeList[LTL]], 
                     [cubeList[UBL], cubeList[LTR], cubeList[FTL]]]
    adjacentSidesList = [[cubeList[FMM], cubeList[RMM]], 
                         [cubeList[RMM], cubeList[BMM]], 
                         [cubeList[BMM], cubeList[LMM]], 
                         [cubeList[LMM], cubeList[FMM]]]
    return bottomCornerList, cubeList, topCornerList, adjacentSidesList
    
def _findOnDownsidesPatternLocations(theCube,rotateResult):
    positionDTR = 0
    positionDBR = 1
    positionDBL = 2
    positionDTL = 3
    noIncorrectDMMInBottomCorners = 4 
    bottomCornerList, cubeList, topCornerList, adjacentSidesList = _findOnDownsidesUpdateCube(theCube)
    while True:   
        fourBottomCornersCheck = 0
        for bottomCheckIndex in range(len(bottomCornerList)):
            if (bottomCornerList[bottomCheckIndex][0]== cubeList[DMM] and \
                bottomCornerList[bottomCheckIndex][1]== adjacentSidesList[bottomCheckIndex][0] and \
                bottomCornerList[bottomCheckIndex][2]== adjacentSidesList[bottomCheckIndex][1]) or \
                (cubeList[DMM] not in bottomCornerList[bottomCheckIndex]):
                fourBottomCornersCheck+=1
            else:
                if cubeList[DMM] not in topCornerList[bottomCheckIndex]:
                    if bottomCheckIndex == positionDTR:
                        rotateResult.append('RUr')
                        theCube.rotate('RUr')
                    elif bottomCheckIndex == positionDBR:
                        rotateResult.append('BUb')
                        theCube.rotate('BUb')
                    elif bottomCheckIndex == positionDBL:
                        rotateResult.append('LUl')
                        theCube.rotate('LUl')
                    elif bottomCheckIndex == positionDTL:
                        rotateResult.append('FUf')
                        theCube.rotate('FUf')               
                else:
                    rotateResult.append('U')
                    theCube.rotate('U')
            bottomCornerList, cubeList, topCornerList, adjacentSidesList = _findOnDownsidesUpdateCube(theCube)
        if fourBottomCornersCheck == noIncorrectDMMInBottomCorners:
            break
                          
def _stringReplace(joinedString):
    replaceDict ={'UUU':'u','Uu':'','uuu':'U'}
    for key, value in replaceDict.items():
        joinedString = joinedString.replace(key,value)
    return joinedString



    