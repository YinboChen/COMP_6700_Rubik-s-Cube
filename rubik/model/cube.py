'''
    Created on Jan 26, 2023
    
    @auther: Yinbo Chen
'''
from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        
        if self.checkCubeValidation(encodedCube):
            self.cube = encodedCube
            self.cubeStatus = 'ok'
        else:
            self.cube = None
            self.cubeStatus = 'error: invalid cube'
            
        
    def rotate(self, directions):
        
        if self.checkDirValidation(directions) and self.cube != None:
            self.cubeStatus = 'ok'
            cubeList = list(self.cube)
            self._selectRotateCondition(directions, cubeList)
            return self.cube
        elif self.checkDirValidation(directions) and self.cube == None:
            self.cubeStatus = 'error: invalid cube'
        elif self.checkDirValidation(directions)==False and self.cube == None:
            self.cubeStatus = 'error: invalid rotation and cube'
        else:    
            self.cubeStatus = 'error: invalid rotation'
        
    
    def get(self):
        return self.cube
    
    def getStatus(self):
        return self.cubeStatus
           
    def checkCubeValidation(self,encodedCube):
     
        checkPointsResults = []
        if self._checkCubeExistAndTypeAndHas54Chars(encodedCube):
            checkPointsResults.append(self._checkCubeNaming(encodedCube))
            checkPointsResults.append(self._checkCubeHasUniqueCenterChars(encodedCube))
            checkPointsResults.append(self._checkCubeAdjacentEdgesAndCorners(encodedCube))
            checkPointsResults.append(self._checkOccurrencesOfLegalChar(encodedCube))
            if checkPointsResults.count(True)== len(checkPointsResults):
                return True
            else:
                return False
        else:
            return False
    
    
    def checkDirValidation(self,directions):
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
        
    def _checkCubeExistAndTypeAndHas54Chars(self,encodedCube):
        totalNumbeOfCubeElements = 54
        if encodedCube != None and isinstance(encodedCube, str) and len(encodedCube) == totalNumbeOfCubeElements:
            return True
        else:
            return False
    def _checkCubeNaming(self,encodedCube):
        acceptableCubeElement = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        validationCubeElement = set(encodedCube)
        if validationCubeElement.issubset(acceptableCubeElement):
            return True
        else:
            return False
        
    def _checkCubeHasUniqueCenterChars(self,encodedCube):
        totalFacesInCube = 6
        validationCubeElement = set(encodedCube)
        uniqueElementsFromCube = "".join(validationCubeElement)
        uniqueElementsFromCubeEachFaceCenter = "".join(encodedCube[FMM]+encodedCube[RMM]+encodedCube[BMM]+\
                                                       encodedCube[LMM]+encodedCube[UMM]+ encodedCube[DMM])
        if len(uniqueElementsFromCube) == totalFacesInCube and set(uniqueElementsFromCube)== set(uniqueElementsFromCubeEachFaceCenter):
            return True
        else:
            return False
        
    def _checkCubeAdjacentEdgesAndCorners(self,encodedCube):
        #Cube has 3 layers, each layer has 4 pairs. The total number is 4*2*3 =24
        sumOfEntireMiddleAdjcEdge = 24
        #Cube has 8 corners, each corner has 3 different colors. The total number is 8*3 = 24
        sumOfEntireCorners = 24
        sumOfLengthOfAdjcEdge = self._sumOfDiffAdjacentEdges(encodedCube)
        sumOfLengthOfCorners = self._sumOfDiffAllCorners(encodedCube)
        if sumOfLengthOfAdjcEdge == sumOfEntireMiddleAdjcEdge and sumOfLengthOfCorners ==sumOfEntireCorners:
            return True
        else:
            return False  
        
    def _checkOccurrencesOfLegalChar(self,encodedCube):
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
    
    def _sumOfDiffAdjacentEdges(self,encodedCube):
        sumOfLengthOfAdjcEdge = len(set(encodedCube[RTM] + encodedCube[UMR])) + len(set(encodedCube[LTM] + encodedCube[UML])) +\
                                len(set(encodedCube[RBM] + encodedCube[DMR])) + len(set(encodedCube[LBM] + encodedCube[DML])) +\
                                len(set(encodedCube[RMR] + encodedCube[BML])) + len(set(encodedCube[LML] + encodedCube[BMR])) +\
                                len(set(encodedCube[BTM] + encodedCube[UTM])) + len(set(encodedCube[DBM] + encodedCube[BBM])) +\
                                len(set(encodedCube[FTM] + encodedCube[UBM])) + len(set(encodedCube[FMR] + encodedCube[RML])) +\
                                len(set(encodedCube[FBM] + encodedCube[DTM])) + len(set(encodedCube[FML] + encodedCube[LMR]))
        return sumOfLengthOfAdjcEdge
    
    def _sumOfDiffAllCorners(self,encodedCube):
        sumOfLengthOfCorners = len(set(encodedCube[FTL] + encodedCube[LTR] + encodedCube[UBL])) +\
                               len(set(encodedCube[UBR] + encodedCube[RTL] + encodedCube[FTR])) +\
                               len(set(encodedCube[FBR] + encodedCube[RBL] + encodedCube[DTR])) +\
                               len(set(encodedCube[FBL] + encodedCube[LBR] + encodedCube[DTL])) +\
                               len(set(encodedCube[UTR] + encodedCube[RTR] + encodedCube[BTL])) +\
                               len(set(encodedCube[DBR] + encodedCube[RBR] + encodedCube[BBL])) +\
                               len(set(encodedCube[UTL] + encodedCube[LTL] + encodedCube[BTR])) +\
                               len(set(encodedCube[LBL] + encodedCube[DBL] + encodedCube[BBR]))
        return sumOfLengthOfCorners


    def _rotateF(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate front face
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
        #rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
        #rotate right to bottom
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
        #rotate bottom to left
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
        #rotate left to up
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        self.cube = "".join(rotatedCubeList)
        
    def _rotatef(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate front face
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FTR] = cubeList[FBR]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FBR] = cubeList[FBL]
        
        #rotate right to up
        rotatedCubeList[UBL] = cubeList[RTL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBR] = cubeList[RBL]
        
        #rotate bottom to right
        rotatedCubeList[RTL] = cubeList[DTR]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RBL] = cubeList[DTL]
        
        #rotate left to bottom
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
        
        #rotate up to left
        rotatedCubeList[LTR] = cubeList[UBR]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LBR] = cubeList[UBL]
     
        self.cube = "".join(rotatedCubeList)

    def _rotateR(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate right face
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
       
        
        #rotate TOP to BACK
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
        
        #rotate back to bottom
        rotatedCubeList[DBR] = cubeList[BTL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DTR] = cubeList[BBL]
        
        #rotate bottom to front
        rotatedCubeList[FTR] = cubeList[DTR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FBR] = cubeList[DBR]
        
        #rotate front to top
        rotatedCubeList[UTR] = cubeList[FTR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UBR] = cubeList[FBR]
        self.cube = "".join(rotatedCubeList)
        
    def _rotater(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate right face
        rotatedCubeList[RTL] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RMR]
        rotatedCubeList[RTR] = cubeList[RBR]
        rotatedCubeList[RML] = cubeList[RTM]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RMR] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RTL]
        rotatedCubeList[RBM] = cubeList[RML]
        rotatedCubeList[RBR] = cubeList[RBL]   
        
        #rotate top to front
        rotatedCubeList[FTR] = cubeList[UTR]
        rotatedCubeList[FMR] = cubeList[UMR]
        rotatedCubeList[FBR] = cubeList[UBR]
        
        #rotate front to bottom
        rotatedCubeList[DTR] = cubeList[FTR]
        rotatedCubeList[DMR] = cubeList[FMR]
        rotatedCubeList[DBR] = cubeList[FBR]
        
        #rotate bottom to back
        rotatedCubeList[BBL] = cubeList[DTR]
        rotatedCubeList[BML] = cubeList[DMR]
        rotatedCubeList[BTL] = cubeList[DBR]
        
        #rotate back to top
        rotatedCubeList[UBR] = cubeList[BTL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UTR] = cubeList[BBL]
     
        self.cube = "".join(rotatedCubeList)
        
    def _rotateB(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate back face
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBR] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BBR]
          
        
        #rotate top to left
        rotatedCubeList[LBL] = cubeList[UTL]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LTL] = cubeList[UTR]
       
        
        #rotate left to bottom
        rotatedCubeList[DBL] = cubeList[LTL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBR] = cubeList[LBL]
      
        
        #rotate bottom to right
        rotatedCubeList[RBR] = cubeList[DBL]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RTR] = cubeList[DBR]
       
        
        #rotate right to top
        rotatedCubeList[UTL] = cubeList[RTR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTR] = cubeList[RBR]
      
     
        self.cube = "".join(rotatedCubeList)
        
    def _rotateb(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate back face
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BTR] = cubeList[BBR]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BBR] = cubeList[BBL]     
        
        #rotate  left to top
        rotatedCubeList[UTL] = cubeList[LBL]
        rotatedCubeList[UTM] = cubeList[LML]
        rotatedCubeList[UTR] = cubeList[LTL]  
        
        #rotate bottom to left
        rotatedCubeList[LTL] = cubeList[DBL]
        rotatedCubeList[LML] = cubeList[DBM]
        rotatedCubeList[LBL] = cubeList[DBR]
      
        
        #rotate right to bottom
        rotatedCubeList[DBL] = cubeList[RBR]
        rotatedCubeList[DBM] = cubeList[RMR]
        rotatedCubeList[DBR] = cubeList[RTR]
      
        #rotate right to top
        rotatedCubeList[RTR] = cubeList[UTL]
        rotatedCubeList[RMR] = cubeList[UTM]
        rotatedCubeList[RBR] = cubeList[UTR]
     
        self.cube = "".join(rotatedCubeList)
        
    def _rotateL(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate left face
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
    
        #rotate  top to front
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
              
        #rotate bottom to back
        rotatedCubeList[BBR] = cubeList[DTL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BTR] = cubeList[DBL]
              
        #rotate front to bottom
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
       
        #rotate back to top
        rotatedCubeList[UBL] = cubeList[BTR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UTL] = cubeList[BBR]

        self.cube = "".join(rotatedCubeList)
    
    def _rotatel(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate left face
        rotatedCubeList[LBL] = cubeList[LTL]
        rotatedCubeList[LML] = cubeList[LTM]
        rotatedCubeList[LTL] = cubeList[LTR]
        rotatedCubeList[LBM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LTM] = cubeList[LMR]
        rotatedCubeList[LBR] = cubeList[LBL]
        rotatedCubeList[LMR] = cubeList[LBM]
        rotatedCubeList[LTR] = cubeList[LBR]
        
        #rotate top to back
        rotatedCubeList[BBR] = cubeList[UTL]
        rotatedCubeList[BMR] = cubeList[UML]
        rotatedCubeList[BTR] = cubeList[UBL]
        
        #rotate back to bottom
        rotatedCubeList[DBL] = cubeList[BTR]
        rotatedCubeList[DML] = cubeList[BMR]
        rotatedCubeList[DTL] = cubeList[BBR]
        
        #rotate bottom to front
        rotatedCubeList[FTL] = cubeList[DTL]
        rotatedCubeList[FML] = cubeList[DML]
        rotatedCubeList[FBL] = cubeList[DBL]
        
        #rotate front to top
        rotatedCubeList[UTL] = cubeList[FTL]
        rotatedCubeList[UML] = cubeList[FML]
        rotatedCubeList[UBL] = cubeList[FBL]
        self.cube = "".join(rotatedCubeList)
        
    def _rotateU(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate left face
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
        
        #rotate front to left
        rotatedCubeList[LTL] = cubeList[FTL]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTR] = cubeList[FTR]
        
        #rotate left to back
        rotatedCubeList[BTL] = cubeList[LTL]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTR] = cubeList[LTR]
       
        #rotate back to right
        rotatedCubeList[RTL] = cubeList[BTL]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTR] = cubeList[BTR]
              
        #rotate right to front
        rotatedCubeList[FTL] = cubeList[RTL]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTR] = cubeList[RTR]
        
        self.cube = "".join(rotatedCubeList)
        
    def _rotateu(self, cubeList):
        rotatedCubeList = cubeList[:]
        #rotate left face
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UBR] = cubeList[UBL]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UTR] = cubeList[UBR]
        
        #rotate front to right
        rotatedCubeList[RTL] = cubeList[FTL]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTR] = cubeList[FTR]
        
        #rotate right to back
        rotatedCubeList[BTL] = cubeList[RTL]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTR] = cubeList[RTR]
       
        #rotate back to left
        rotatedCubeList[LTL] = cubeList[BTL]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTR] = cubeList[BTR]
        
        #rotate left to front
        rotatedCubeList[FTL] = cubeList[LTL]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTR] = cubeList[LTR]
        
        self.cube = "".join(rotatedCubeList)

    def _selectRotateCondition(self, directions, cubeList):
        if directions == None or directions == '':
            self._rotateF(cubeList)
        else:
            for singleDirection in directions:
                cubeList = list(self.cube)
                if singleDirection == 'F':
                    self._rotateF(cubeList)
                elif singleDirection == 'f':
                    self._rotatef(cubeList)
                elif singleDirection == 'R':
                    self._rotateR(cubeList)
                elif singleDirection == 'r':
                    self._rotater(cubeList)
                elif singleDirection == 'B':
                    self._rotateB(cubeList)
                elif singleDirection == 'b':
                    self._rotateb(cubeList)
                elif singleDirection == 'L':
                    self._rotateL(cubeList)
                elif singleDirection == 'l':
                    self._rotatel(cubeList)
                elif singleDirection == 'U':
                    self._rotateU(cubeList)
                elif singleDirection == 'u':
                    self._rotateu(cubeList)

        
    