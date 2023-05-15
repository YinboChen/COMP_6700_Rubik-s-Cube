'''
    Created on Jan 26, 2023
    
    @auther: Yinbo Chen
'''
from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    test 100 dir = F
#    test 110 dir = f
#    test 120 dir = R
#    test 130 dir = r
#    test 140 dir = B
#    test 150 dir = b
#    test 160 dir = L
#    test 170 dir = l
#    test 180 dir = U
#    test 190 dir = u
#    test 200 dir is missing
#    test 210 dir = ''
#    test 220 dir = 'FRBLUfrblu'


# Sad path
#    test 230 dir = d 
#    test 240 dir = D
#    test 250 dir = d or/and D inside a multiple strings dir
#    test 260 dir include other value which not in FRBLUfrblu'
#    test 270 dir is string
#    test 280 cube is string
#    test 290 dir and cube both are invalid
#    test 310 cube is missing
#    test 320 length of cube = 0
#    test 330 length of cube !=54
#    test 340 cube elements don't exist in [a-zA-Z0-9]
#    test 350 cube each side elements !=9
#    test 390 cube parms >2
#
#
# Evil path
#    test 360 cube (5th,14th,23rd,32nd,41st,50th) are not unique
#    test 370 cube middle edge are not unique
#            index[...]10/41,28/39,16/50,34/49,14/21,30/23/,19/37,52/25,1/43,5/12,7/46,3/32 
#    test 380 cube 4 corners 3 sides are not unique
#             index[...]0/29/42,44/9/2,8/15/47,6/35/45,38/11/18,53/17/24,36/27/20,33/51/26
#
#    
#    Test that the stubbed rotate returns the correct result
    def test100_rotate_returnFSolution(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        rotatedCube = 'bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test110_rotate_returnfSolution(self):
        encodedCube = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        rotatedCube = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test120_rotate_returnRSolution(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        rotatedCube = 'byoyowobygbbobogworbrbroyyrbwwggggrywwygyyoowgrrgwrwrb'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'R'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test130_rotate_returnrSolution(self):
        encodedCube = 'byoyowobygbbobogworbrbroyyrbwwggggrywwygyyoowgrrgwrwrb'
        rotatedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'r'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test140_rotate_returnBSolution(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        rotatedCube = 'byyyoyobwboybbrgowrrbyrbrorywwwggwryowggyboorgrogwwbgg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'B'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test150_rotate_returnbSolution(self):
        encodedCube = 'byyyoyobwboybbrgowrrbyrbrorywwwggwryowggyboorgrogwwbgg'
        rotatedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'b'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test160_rotate_returnLSolution(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        rotatedCube = 'wyygoyobwboobbwgogbbwrrgrygggbrgwygwrwyoybrorbroywwory'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'L'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test170_rotate_returnlSolution(self):
        encodedCube = 'wyygoyobwboobbwgogbbwrrgrygggbrgwygwrwyoybrorbroywwory'
        rotatedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'l'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test180_rotate_returnUSolution(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        rotatedCube = 'booyoyobwbbrbbwgogbwwrroryrbyyggggryogwoywrbygrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'U'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test190_rotate_returnuSolution(self):
        encodedCube = 'booyoyobwbbrbbwgogbwwrroryrbyyggggryogwoywrbygrogwwwry'
        rotatedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'u'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test200_rotate_returnFSolutionWhenDirIsMissing(self):
        encodedCube = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        rotatedCube = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = None
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test210_rotate_returnFSolutionWhenDirIsEmpty(self):
        encodedCube = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        rotatedCube = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test220_rotate_returnMultipleStringSolution(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        rotatedCube = 'oyyboooggbwrbbbrbrbrwwrggrobgyygrwgyoywryoborgwyowygww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrblu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
    
    def test230_rotate_returnErrorInvalidRotationWhenDRotation(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'D'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
    
    def test240_rotate_returnErrorInvalidRotationWhendRotation(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'd'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
    
    def test250_rotate_returnErrorInvalidRotationWhenDOrdInMultipleRotateDic(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBDLUfrbldu'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
    
    def test260_rotate_returnErrorInvalidRotationWhenInputInvailedDir(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLSN'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
    
    def test270_rotate_returnErrorInvalidRotationWhenInputDirIsNotString(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 123456
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation', result['status'])
    
    def test280_rotate_returnErrorInvalidCubeWhenInputDirIsNotString(self):
        encodedCube = 1234567
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test290_rotate_returnErrorInvalidDirAndCubeWhenInputBothInvalid(self):
        encodedCube = 1234567
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'ddddddDDDDDff'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid rotation and cube', result['status'])
    
    def test310_rotate_returnErrorInvalidCubeWhenCubeIsMissing(self):
        encodedCube = None
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test320_rotate_returnErrorInvalidCubeWhenCubeIsEmpty(self):
        encodedCube = ''
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test330_rotate_returnErrorInvalidCubeWhenCubeIsNoEqual54(self):
        encodedCube = 'byyyoyobwboobbwgogbbrrroryrbwwggggrywwygyboorgrogwwwr'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test340_rotate_returnErrorInvalidCubeWhenCubeElementNotInList(self):
        encodedCube = 'byyyoyobwbo%bbwgogbbrrror-rbww*gggrywwygyboorgrogwwwr9'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test350_rotate_returnErrorInvalidCubeWhenCubeDuplicatedElementNotEq6(self):
        encodedCube = 'byyyoyo1wbbobbwgogbbrrr9ryrbwwggggrywwygyboorgrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test360_rotate_returnErrorInvalidCubeWhenCubeEachSideCenterElementEq(self):
        encodedCube = 'booyryobwbbrbbwgogbwwrroryrbyygggyryogwogwrbygrogwwwry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test370_rotate_returnErrorInvalidCubeWhenCubeEdgeOfIntrSurfsEqu(self):
        encodedCube = 'ooogooowbybrobbbbwrrgbrrrrwgyorggwgggyyyybyyyowwgwbwrw'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test380_rotate_returnErrorInvalidCubeWhenCubeAllCornersLengthSetNoEqu24(self):
        encodedCube = 'boogowwobgorbbbogwgrrrrbrgwyroygywrggyygybyyyowwbwbwro'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test390_rotate_returnErrorExtraneousKeyDetectedWhenParmsLargerThanTwo(self):
        encodedCube = 'boogowwobgorbbbogwgrrrrbrgwyroygywrggyygybyyyowwbwbwro'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrbl'
        parms['anotherkey']= 'anothervalue'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])
      
    #The tests below come from the customer tests(increment1 feedback) which I didn't pass at the first time.  
    def test101_rotate_returnFSolution(self):
        encodedCube = 'rrgfrtttRfrrgRRVVfRfgVggVgfRffRfVrVRVrtttRtttgRrgVrVfg'
        rotatedCube = 'tfrtrrRtgtrrtRRtVfRfgVggVgfRfgRfRrVrVrtttRRVfVgfgVrVfg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(rotatedCube, result.get('cube'))
        
    def test102_rotate_returnError9OccurrencesOfLegalChar(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'L'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    
