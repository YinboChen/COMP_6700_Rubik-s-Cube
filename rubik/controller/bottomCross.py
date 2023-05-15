'''
    Created on Feb 10, 2023
    
    @auther: Yinbo Chen
'''

from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    rotateResult = []
    rotateResult.append('')
    if isSolvedBottomCross(theCube)!= True: 
        makeDaisyOnU(theCube, rotateResult)
        haveDaisyOnU(theCube,rotateResult)
    return stringReplace("".join(rotateResult))

def isSolvedBottomCross(theCube):
    cubeList = list(theCube.cube)
    eachFaceShouldUique = 5
    sumFCount = len(set(cubeList[FMM]+cubeList[FBM]))
    sumLCount = len(set(cubeList[LMM]+cubeList[LBM]))
    sumRCount = len(set(cubeList[RMM]+cubeList[RBM]))
    sumBCount = len(set(cubeList[BMM]+cubeList[BBM]))
    sumDCount = len(set(cubeList[DMM]+cubeList[DTM]+cubeList[DBM]+cubeList[DML]+cubeList[DMR]))
    totalSumFiveFacesCount = sumFCount+sumLCount+sumRCount+sumBCount+sumDCount
    if totalSumFiveFacesCount == eachFaceShouldUique:
        return True
    else:
        return False
    
def haveDaisyOnU(theCube,rotateResult):
    while(isSolvedBottomCross(theCube)!= True):
        cubeList = list(theCube.cube)
        
        if cubeList[FTM]== cubeList[FMM] and cubeList[UBM]== cubeList[DMM]:
            theCube.rotate('FF')
            rotateResult.append('FF')
        elif cubeList[RTM]== cubeList[RMM] and cubeList[UMR]== cubeList[DMM]:
            theCube.rotate('RR')
            rotateResult.append('RR')
        elif cubeList[BTM]== cubeList[BMM] and cubeList[UTM]== cubeList[DMM]:
            theCube.rotate('BB')
            rotateResult.append('BB')
        elif cubeList[LTM]== cubeList[LMM] and cubeList[UML]== cubeList[DMM]:
            theCube.rotate('LL')
            rotateResult.append('LL')
        else:
            
            while cubeList[UBM]!= cubeList[DMM] and (cubeList[DMM] in[cubeList[UBM],cubeList[UMR],cubeList[UTM],cubeList[UML]]):
                theCube.rotate('U')
                rotateResult.append('U')
                cubeList = list(theCube.cube)
    
            if cubeList[FTM]== cubeList[FMM]:
                theCube.rotate('FF')
                rotateResult.append('FF')
            elif cubeList[FTM]== cubeList[RMM]:
                theCube.rotate('uRR')
                rotateResult.append('uRR')
            elif cubeList[FTM]== cubeList[BMM]:
                theCube.rotate('uuBB')
                rotateResult.append('uuBB')
            elif cubeList[FTM]== cubeList[LMM]:
                theCube.rotate('ULL')
                rotateResult.append('ULL')
            

def makeDaisyOnUUpdateCube(theCube):
    cubeList = list(theCube.cube)
    daisyPattern = [cubeList[UBM], cubeList[UMR], cubeList[UTM], cubeList[UML]]
    outerCharsList = [[cubeList[UBM], cubeList[RML], cubeList[DTM], cubeList[LMR]], 
                      [cubeList[UMR], cubeList[BML], cubeList[DMR], cubeList[FMR]], 
                      [cubeList[UTM], cubeList[LML], cubeList[DBM], cubeList[RMR]], 
                      [cubeList[UML], cubeList[FML], cubeList[DML], cubeList[BMR]]]
    innerCharsList = [[cubeList[FTM], cubeList[FMR], cubeList[FBM], cubeList[FML]], 
                      [cubeList[RTM], cubeList[RMR], cubeList[RBM], cubeList[RML]], 
                      [cubeList[BTM], cubeList[BMR], cubeList[BBM], cubeList[BML]], 
                      [cubeList[LTM], cubeList[LMR], cubeList[LBM], cubeList[LML]]]
    return cubeList, outerCharsList, daisyPattern, innerCharsList


def makeDaisyOnUCheckOuterFaces(theCube, rotateResult, cubeFacesIndex, rotateOuterFacesList, cubeList, outerCharsList):
    if cubeList[DMM] == outerCharsList[cubeFacesIndex][0]:
        theCube.rotate(rotateOuterFacesList[cubeFacesIndex][0])
        rotateResult.append(rotateOuterFacesList[cubeFacesIndex][0])
    elif cubeList[DMM] == outerCharsList[cubeFacesIndex][1]:
        theCube.rotate(rotateOuterFacesList[cubeFacesIndex][1])
        rotateResult.append(rotateOuterFacesList[cubeFacesIndex][1])
    elif cubeList[DMM] == outerCharsList[cubeFacesIndex][2]:
        theCube.rotate(rotateOuterFacesList[cubeFacesIndex][2])
        rotateResult.append(rotateOuterFacesList[cubeFacesIndex][2])
    elif cubeList[DMM] == outerCharsList[cubeFacesIndex][3]:
        theCube.rotate(rotateOuterFacesList[cubeFacesIndex][3])
        rotateResult.append(rotateOuterFacesList[cubeFacesIndex][3])


def makeDaisyOnUCheckInnerFaces(theCube, rotateResult, cubeFacesIndex, rotateInnerFacesList, cubeList, innerCharsList):
    if cubeList[DMM] == innerCharsList[cubeFacesIndex][3]:
        theCube.rotate(rotateInnerFacesList[cubeFacesIndex][0])
        rotateResult.append(rotateInnerFacesList[cubeFacesIndex][0])
    elif cubeList[DMM] == innerCharsList[cubeFacesIndex][0]:
        theCube.rotate(rotateInnerFacesList[cubeFacesIndex][1])
        rotateResult.append(rotateInnerFacesList[cubeFacesIndex][1])
    elif cubeList[DMM] == innerCharsList[cubeFacesIndex][1]:
        theCube.rotate(rotateInnerFacesList[cubeFacesIndex][2])
        rotateResult.append(rotateInnerFacesList[cubeFacesIndex][2])
    elif cubeList[DMM] == innerCharsList[cubeFacesIndex][2]:
        theCube.rotate(rotateInnerFacesList[cubeFacesIndex][3])
        rotateResult.append(rotateInnerFacesList[cubeFacesIndex][3])

def makeDaisyOnU(theCube,rotateResult):
    # F = 0
    cubeFacesIndex = 0
    rotateOuterFacesList = [['U','fU','FFU','FU'],['U','rU','RRU','RU'],
                            ['U','bU','BBU','BU'],['U','lU','LLU','LU']]
    rotateInnerFacesList = [['Ul','fUl','ffUl','FUl'],['Uf','rUf','rrUf','RUf'],
                            ['Ur','bUr','bbUr','BUr'],['Ub','lUb','llUb','LUb']]
    
    while True:
        cubeList, outerCharsList, daisyPattern, innerCharsList = makeDaisyOnUUpdateCube(theCube)
        if set(cubeList[DMM])== set(daisyPattern):
            break
        elif cubeList[DMM] in outerCharsList[cubeFacesIndex]:
            makeDaisyOnUCheckOuterFaces(theCube, rotateResult, cubeFacesIndex, rotateOuterFacesList, cubeList, outerCharsList)
        elif cubeList[DMM] in innerCharsList[cubeFacesIndex]:
            
            makeDaisyOnUCheckInnerFaces(theCube, rotateResult, cubeFacesIndex, rotateInnerFacesList, cubeList, innerCharsList)
        else:
            theCube.rotate('u')
            rotateResult.append('u')
            cubeList = list(theCube.cube)
            cubeFacesIndex+=1
            if cubeFacesIndex >3:
                    # F = 0
                    # R = 1
                    # B = 2
                    # L = 3
                cubeFacesIndex = 0
            continue     
        cubeList, outerCharsList, daisyPattern, innerCharsList = makeDaisyOnUUpdateCube(theCube)

def stringReplace(joinedString):
    # replaceDict ={'UUU':'u','Uu':'','uuu':'U'}
    replaceDict ={'UUU':'u','Uu':'','uuu':'U'}
    for key, value in replaceDict.items():
        joinedString = joinedString.replace(key,value)
        
    return joinedString
    
    
            