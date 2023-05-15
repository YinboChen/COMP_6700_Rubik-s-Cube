'''
Created on Feb 14, 2023

@author: yinbo
'''

from unittest import TestCase
from rubik.view.solve import solve
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.controller import bottomCross


# Create unittest for checking the output solution from the bottomCross
# Rotate the cube based on the solution and checking the rotated cube whether has the bottomCross

#happy path:
#    test    001    test function (isSolvedBottomCross)
#    test    002    test function (haveDaisyOnU)
#    test    003    test function (makeDaisyOnU)

#    test    190    test bottomCross return correct solution
#    test    191    test bottomCross return correct solution(special scenario )

#sad path
#    Test    200    missing cube object 
#    Test    210    empty cube
#    Test    220    invalid cube
#    Test    230    invalid key
#

class BottomCrossTest(TestCase):
    

    def _checkBottomCrossComparison(self, result, cubeToRotate, groundTrue):
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate(result.get('solution'))
        #print(result.get('solution'))
        checkRotatedCube = "".join(
            rotatedCube[FMM] + rotatedCube[FBM] + rotatedCube[RMM] + rotatedCube[RBM] + rotatedCube[BMM] +\
            rotatedCube[BBM] + rotatedCube[LMM] + rotatedCube[LBM] + rotatedCube[DTM] + rotatedCube[DML] +\
            rotatedCube[DMM] + rotatedCube[DMR] + rotatedCube[DBM])
        checkGroundTrueCube = "".join(
            groundTrue[FMM] + groundTrue[FBM] + groundTrue[RMM] + groundTrue[RBM] + groundTrue[BMM] +\
            groundTrue[BBM] + groundTrue[LMM] + groundTrue[LBM] + groundTrue[DTM] + groundTrue[DML] +\
            groundTrue[DMM] + groundTrue[DMR] + groundTrue[DBM])
        return checkRotatedCube, checkGroundTrueCube
    
    def _checkBottomCrossDaisy(self, strResult, cubeToRotate, groundTrue):
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate(strResult)
        checkRotatedCube = "".join([rotatedCube[UBM]+rotatedCube[UMR]+rotatedCube[UTM]+rotatedCube[UML]])

        checkGroundTrueCube = "".join(groundTrue[UBM] + groundTrue[UMR] + groundTrue[UTM] + groundTrue[UML])
        return checkRotatedCube, checkGroundTrueCube

    def test001_funcTest_bottomCross_isSolvedBottomCross(self):
        encodedCube= 'ybobogoorwyyrbrbbrooryrogrgbogggryggwybbygrybwwywwwoww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = bottomCross.isSolvedBottomCross(theCube)
        self.assertEqual(groundTrue, testResult)
        
    def test002_funcTest_bottomCross_haveDaisyOnU(self):
        encodedCube= 'ooryoogbgbbggbryygyrobrgoorwgyrgrborbwrwywbwwwyobwgyyw'
        groundTrue = []
        groundTrue.append('FFRRBBLL')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        bottomCross.haveDaisyOnU(theCube,rotateResult)
        self.assertEqual("".join(groundTrue), "".join(rotateResult))
        
    def test003_funcTest_bottomCross_makeDaisyOnU(self):
        encodedCube= 'oroyoyygrwgoobbggrboboryyrgwbgrgborbrwywywygbrywwwowbg'
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        bottomCross.makeDaisyOnU(theCube,rotateResult)
        cubeToRotate ='oroyoyygrwgoobbggrboboryyrgwbgrgborbrwywywygbrywwwowbg' 
        groundTrue = 'ooryoogbgbbggbryygyrobrgoorwgyrgrborbwrwywbwwwyobwgyyw'
        resutCheck= "".join(rotateResult)
        checkRotatedCube, checkGroundTrueCube = self._checkBottomCrossDaisy(resutCheck, cubeToRotate, groundTrue)
        self.assertEqual(checkRotatedCube, checkGroundTrueCube )
         
    def test190_solve_returnBottomCrossedSolution(self):
        
        parms = {}
        parms['cube'] = 'boyooborrbyrobbybrwggrrywbgogwrgworbyogwygoyryggwwywwb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)    
        cubeToRotate = 'boyooborrbyrobbybrwggrrywbgogwrgworbyogwygoyryggwwywwb'
        groundTrue = 'obbrorwooobrgbygbgyyroryorgwgyrgbrgrggboyybowbwywwwyww'
        checkRotatedCube, checkGroundTrueCube = self._checkBottomCrossComparison(result, cubeToRotate, groundTrue)

        self.assertEqual(checkRotatedCube, checkGroundTrueCube )
        
        
    def test191_solve_returnBottomCrossedSolution(self):
        
        parms = {}
        parms['cube'] = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        
        cubeToRotate = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        groundTrue =   'bboobggbbyoorrrrrbggbygboggobyooyrorwywrygrygwwwwwwywy'
        checkRotatedCube, checkGroundTrueCube = self._checkBottomCrossComparison(result, cubeToRotate, groundTrue)
        self.assertEqual(checkRotatedCube, checkGroundTrueCube )     
    
    def test200_missingCubeObject(self):
        parms = {}
        parms['cube'] = None
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test210_emptyCube(self):
        parms = {}
        parms['cube'] = ''
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test220_invalidCubeInput(self):
        parms = {}
        parms['cube'] = 'oroyoyygrwgoobbgg'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test230_invalidKeyInput(self):
        parms = {}
        parms['cube'] = 'wgboogowrrryobrybgoygyrgwwowrbygbgbwoobwybrrybggywwyor'
        parms['rotate'] = 'LLBBRR'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])
        
        #test
    def test301_solve_returnBottomCrossedSolution(self):
        
        parms = {}
        parms['cube'] = '5RABdJBdRJBBB5555JAAdJBJBBBRdJAAA555AdRRRRdAdJJddJRR5A'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        
        cubeToRotate = '5RABdJBdRJBBB5555JAAdJBJBBBRdJAAA555AdRRRRdAdJJddJRR5A'
        groundTrue =   'ddddddddd555555555BBBBBBBBBAAAAAAAAARRRRRRRRRJJJJJJJJJ'
        checkRotatedCube, checkGroundTrueCube = self._checkBottomCrossComparison(result, cubeToRotate, groundTrue)
        self.assertEqual(checkRotatedCube, checkGroundTrueCube )
        
    def test302_solve_returnBottomCrossedSolution(self):
        
        parms = {}
        parms['cube'] = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        
        cubeToRotate = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        groundTrue =   'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        checkRotatedCube, checkGroundTrueCube = self._checkBottomCrossComparison(result, cubeToRotate, groundTrue)
        self.assertEqual(checkRotatedCube, checkGroundTrueCube )

        




