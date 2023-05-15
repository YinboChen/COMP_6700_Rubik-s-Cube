'''
    Created on Jan 26, 2023
    
    @auther: Yinbo Chen
'''
from rubik.model.cube import Cube
from rubik.model.constants import *

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    encodedCube = parms.get('cube')
    directions = parms.get('dir')
    theCube = Cube(encodedCube)
    theCube.rotate(directions)
    
    if len(list(parms))>2:
        result['status'] = 'error: extraneous key detected'
    elif theCube.getStatus() == 'ok':
        result['cube'] = theCube.get()
        result['status'] = theCube.getStatus()
    else:
        result['status'] = theCube.getStatus()
        
    return result

def checkCubeValidation(encodedCube):
 
    checkPointsResults = []
    if checkCubeExistAndTypeAndHas54Chars(encodedCube):
        checkPointsResults.append(checkCubeNaming(encodedCube))
        checkPointsResults.append(checkCubeHasUniqueCenterChars(encodedCube))
        checkPointsResults.append(checkCubeAdjacentEdgesAndCorners(encodedCube))
        checkPointsResults.append(checkOccurrencesOfLegalChar(encodedCube))
        if checkPointsResults.count(True)== len(checkPointsResults):
            return True
        else:
            return False
    else:
        return False
    print(checkPointsResults)


def checkDirValidation(directions):
    acceptableDirections = set('FfRrBbLlUu')
    if directions == None:   
            return True

    elif isinstance(directions, str):
        validationDirections = set(directions)
        if validationDirections.issubset(acceptableDirections):
            return True
        else:    
            return False
    else:
        return False
    
def checkCubeExistAndTypeAndHas54Chars(encodedCube):
    totalNumbeOfCubeElements = 54
    if encodedCube != None and isinstance(encodedCube, str) and len(encodedCube) == totalNumbeOfCubeElements:
        return True
    else:
        return False
def checkCubeNaming(encodedCube):
    acceptableCubeElement = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    validationCubeElement = set(encodedCube)
    if validationCubeElement.issubset(acceptableCubeElement):
        return True
    else:
        return False
    
def checkCubeHasUniqueCenterChars(encodedCube):
    totalFacesInCube = 6
    validationCubeElement = set(encodedCube)
    uniqueElementsFromCube = "".join(validationCubeElement)
    uniqueElementsFromCubeEachFaceCenter = "".join(encodedCube[FMM]+encodedCube[RMM]+encodedCube[BMM]+\
                                                   encodedCube[LMM]+encodedCube[UMM]+ encodedCube[DMM])
    if len(uniqueElementsFromCube) == totalFacesInCube and set(uniqueElementsFromCube)== set(uniqueElementsFromCubeEachFaceCenter):
        return True
    else:
        return False
    
def checkCubeAdjacentEdgesAndCorners(encodedCube):
    #Cube has 3 layers, each layer has 4 pairs. The total number is 4*2*3 =24
    sumOfEntireMiddleAdjcEdge = 24
    #Cube has 8 corners, each corner has 3 different colors. The total number is 8*3 = 24
    sumOfEntireCorners = 24
    sumOfLengthOfAdjcEdge = sumOfDiffAdjacentEdges(encodedCube)
    sumOfLengthOfCorners = sumOfDiffAllCorners(encodedCube)
    if sumOfLengthOfAdjcEdge == sumOfEntireMiddleAdjcEdge and sumOfLengthOfCorners ==sumOfEntireCorners:
        return True
    else:
        return False  
    
def checkOccurrencesOfLegalChar(encodedCube):
    theNumbleOfCharOnOneFace = 9
    validationCubeChar = set(encodedCube)
    result = False
    
    for char in validationCubeChar:
        if encodedCube.count(char)!=theNumbleOfCharOnOneFace:
            result = False
            break
        else:
            result = True
            continue
    return result   

def sumOfDiffAdjacentEdges(encodedCube):
    sumOfLengthOfAdjcEdge = len(set(encodedCube[RTM] + encodedCube[UMR])) + len(set(encodedCube[LTM] + encodedCube[UML])) +\
                            len(set(encodedCube[RBM] + encodedCube[DMR])) + len(set(encodedCube[LBM] + encodedCube[DML])) +\
                            len(set(encodedCube[RMR] + encodedCube[BML])) + len(set(encodedCube[LML] + encodedCube[BMR])) +\
                            len(set(encodedCube[BTM] + encodedCube[UTM])) + len(set(encodedCube[DBM] + encodedCube[BBM])) +\
                            len(set(encodedCube[FTM] + encodedCube[UBM])) + len(set(encodedCube[FMR] + encodedCube[RML])) +\
                            len(set(encodedCube[FBM] + encodedCube[DTM])) + len(set(encodedCube[FML] + encodedCube[LMR]))
    return sumOfLengthOfAdjcEdge

def sumOfDiffAllCorners(encodedCube):
    sumOfLengthOfCorners = len(set(encodedCube[FTL] + encodedCube[LTR] + encodedCube[UBL])) +\
                           len(set(encodedCube[UBR] + encodedCube[RTL] + encodedCube[FTR])) +\
                           len(set(encodedCube[FBR] + encodedCube[RBL] + encodedCube[DTR])) +\
                           len(set(encodedCube[FBL] + encodedCube[LBR] + encodedCube[DTL])) +\
                           len(set(encodedCube[UTR] + encodedCube[RTR] + encodedCube[BTL])) +\
                           len(set(encodedCube[DBR] + encodedCube[RBR] + encodedCube[BBL])) +\
                           len(set(encodedCube[UTL] + encodedCube[LTL] + encodedCube[BTR])) +\
                           len(set(encodedCube[LBL] + encodedCube[DBL] + encodedCube[BBR]))
    return sumOfLengthOfCorners


    

