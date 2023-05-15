from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import *
import hashlib
import secrets

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    itemToTokenizeList = []
    itemToTokenizeList.append(encodedCube)  
    if len(list(parms))>1:
        result['status'] = 'error: extraneous key detected'
    elif theCube.getStatus() == 'ok':
        rotations = ""
        rotations += solveBottomCross(theCube)      #iteration 2
        rotations += solveBottomLayer(theCube)      #iteration 3
        rotations += solveMiddleLayer(theCube)      #iteration 4
        rotations += solveUpCross(theCube)          #iteration 5
        if _isCubeSolvable(theCube) == True:
            rotations += solveUpSurface(theCube)        #iteration 5
            rotations += solveUpperLayer(theCube)       #iteration 6   
            subFullToken = calRandomHashToken(itemToTokenizeList, rotations)
            result['solution'] = rotations
            result['status'] = 'ok'    
            result['integrity'] = ''.join(subFullToken) #iteration 3
        else:
            result['status'] = 'error: unsolvable cube'      
    else:
        result['status'] = theCube.getStatus()              
    return result

def calRandomHashToken(itemToTokenizeList, rotations):
    itemToTokenizeList.append(rotations)
    itemToTokenizeList.append('yzc0129')
    stringToHash = ''.join(itemToTokenizeList)
    sha256Hash = hashlib.sha256()
    sha256Hash.update(stringToHash.encode())
    fullToken = sha256Hash.hexdigest()
    secretsGenerator = secrets.SystemRandom()
    startIndex = secretsGenerator.randint(0,len(fullToken)-8)
    subFullToken = fullToken[startIndex:startIndex+8]
    return subFullToken

def _isCubeSolvable(theCube):
    cubeList = list(theCube.get())
    leftCountList = [cubeList[FTR],cubeList[RTR],cubeList[BTR],cubeList[LTR]]
    rightCountList = [cubeList[FTL],cubeList[RTL],cubeList[BTL],cubeList[LTL]]
    totalNumber = 2*(leftCountList.count(cubeList[UMM])) + 1*(rightCountList.count(cubeList[UMM]))
    if totalNumber%3 !=0:
        return  False
    else:
        return True
                     

