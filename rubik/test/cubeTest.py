'''
Created on Jan 26, 2023

@author: yinbo
'''
import unittest
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):
    
#Analysis of Cube
#
#    Cube: class, instance of a state machine, maintain internal state
#    Method:    __init__    constructs cube from a serialized string, 54 characters, 
#                           6unique characters from[a-zA-Z0-9],(5th,14th,23rd,32nd,41st,50th)must be unique
#                get        yields serialized string of internal representation
#                rotate     performs rotations on the cube per 'dir' key
#
#    Analysis:    Cube.rotate
#        inputs:
#            directions:    string, len .GE. 0, [FfRrBbLlUu]; optional, defaulting to F if missing; invalidated
#        outputs:
#            side-effects:    no external effects; internal state change
#            nominal:
#                return serialized rotated cube
#            abnormal:
#                raise DirException
#
#        happy path:
#            test 010:    F rotation
#            test 020:    f rotation
#            test 030:    R rotation
#            test 040:    r rotation
#            test 050:    B rotation
#            test 060:    b rotation
#            test 070:    L rotation
#            test 080:    l rotation
#            test 090:    U rotation
#            test 100:    u rotation
            
#            ...
#            test 110:    missing direction
#            test 120:    empty direction, meaning ""
#            test 130:    multi-string rotation
#
#        sad path
#            test 910:    invalid direction
#
#        evil path
#            none



    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_020_ShouldRotateCubeInfDirection(self):
        cubeToRotate = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube, 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo')
        
    def test_rotate_030_ShouldRotateCubeInRDirection(self):
        cubeToRotate = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube, 'byoyowobygbbobogworbrbroyyrbwwggggrywwygyyoowgrrgwrwrb')
        
    def test_rotate_040_ShouldRotateCubeInrDirection(self):
        cubeToRotate = 'byoyowobygbbobogworbrbroyyrbwwggggrywwygyyoowgrrgwrwrb'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
        
    def test_rotate_050_ShouldRotateCubeInBDirection(self):
        cubeToRotate = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'byyyoyobwboybbrgowrrbyrbrorywwwggwryowggyboorgrogwwbgg')
        
    def test_rotate_060_ShouldRotateCubeInbDirection(self):
        cubeToRotate = 'byyyoyobwboybbrgowrrbyrbrorywwwggwryowggyboorgrogwwbgg'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
        
    def test_rotate_070_ShouldRotateCubeInLDirection(self):
        cubeToRotate = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        self.assertEqual(rotatedCube, 'wyygoyobwboobbwgogbbwrrgrygggbrgwygwrwyoybrorbroywwory')
    
    def test_rotate_080_ShouldRotateCubeInlDirection(self):
        cubeToRotate = 'wyygoyobwboobbwgogbbwrrgrygggbrgwygwrwyoybrorbroywwory'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
    
    def test_rotate_090_ShouldRotateCubeInUDirection(self):
        cubeToRotate = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        self.assertEqual(rotatedCube, 'booyoyobwbbrbbwgogbwwrroryrbyyggggryogwoywrbygrogwwwry')
    
    def test_rotate_100_ShouldRotateCubeInuDirection(self):
        cubeToRotate = 'booyoyobwbbrbbwgogbwwrroryrbyyggggryogwoywrbygrogwwwry'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
        
    def test_rotate_110_ShouldRotateCubeInFDirectionWhenCantFindKey(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate(None)
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
    
    def test_rotate_120_ShouldRotateCubeInFDirectionWhenDirIsEmpty(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('')
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_130_ShouldRotateCubeInMultipleDirectionInput(self):
        cubeToRotate = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('FRBLUfrblu')
        #rotatedCube = theCube.rotate('FfRrBbLlUu')
        self.assertEqual(rotatedCube, 'oyyboooggbwrbbbrbrbrwwrggrobgyygrwgyoywryoborgwyowygww')
        #self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
        
    #Those tests come from the prof's customer tests of increment1(tests review) 
    def test_rotate_111_ShouldRotateCubeInFDirectionInput(self):
        cubeToRotate = 'rrgfrtttRfrrgRRVVfRfgVggVgfRffRfVrVRVrtttRtttgRrgVrVfg'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        #rotatedCube = theCube.rotate('FfRrBbLlUu')
        self.assertEqual(rotatedCube, 'tfrtrrRtgtrrtRRtVfRfgVggVgfRfgRfRrVrVrtttRRVfVgfgVrVfg')
        #self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
        
    def test_rotate_112_ShouldRotateCubeInbDirectionInput(self):
        cubeToRotate = '4MPqXP4PMXM1q44P44q1411MqPqqXX4P4Pq11qPMM1MPMM11XqXXXX'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        #rotatedCube = theCube.rotate('FfRrBbLlUu')
        self.assertEqual(rotatedCube, '4MPqXP4PMXM1q4qP4P4Mq11Pq1qXXXXP4Xq1P4qMM1MPMM11XqX441')
        #self.assertEqual(rotatedCube, 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry')
        

    

