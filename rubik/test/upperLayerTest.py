'''
Created on Apr 15, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view.solve import solve
from rubik.controller import upperLayer
import rubik.model.cube as cube
from rubik.model.constants import *

# Create unittest for checking the output solution from the upperLayer
# Rotate the cube based on the solution and checking the rotated cube whether has the entire cube been solved
#happy path: 
#            test010 test func (_isUpperLayerSolved)

#           
#            test801 - 840  normal test cases

class upperLayerTest(TestCase):
    
    def _checkComparison(self,cubeToRotate, groundTrue, result):
        theCube = cube.Cube(cubeToRotate)
        #print(result.get('solution'))
        if result.get('solution') == '':
            checkRotatedCube = "".join(
                cubeToRotate[FML] + cubeToRotate[FMM] + cubeToRotate[FMR] + cubeToRotate[FBL] + cubeToRotate[FBM] + cubeToRotate[FBR] +\
                cubeToRotate[RML] + cubeToRotate[RMM] + cubeToRotate[RMR] + cubeToRotate[RBL] + cubeToRotate[RBM] + cubeToRotate[RBR] +\
                cubeToRotate[BML] + cubeToRotate[BMM] + cubeToRotate[BMR] + cubeToRotate[BBL] + cubeToRotate[BBM] + cubeToRotate[BBR] +\
                cubeToRotate[LML] + cubeToRotate[LMM] + cubeToRotate[LMR] + cubeToRotate[LBL] + cubeToRotate[LBM] + cubeToRotate[LBR] +\
                cubeToRotate[DTL] + cubeToRotate[DTM] + cubeToRotate[DTR] + cubeToRotate[DML] + cubeToRotate[DMM] + cubeToRotate[DMR] +\
                cubeToRotate[DBL] + cubeToRotate[DBM] + cubeToRotate[DBR] + cubeToRotate[UTM] + cubeToRotate[UML] + cubeToRotate[UMM] +\
                cubeToRotate[UMR] + cubeToRotate[UBM] + cubeToRotate[UTL] + cubeToRotate[UTR] + cubeToRotate[UBL] + cubeToRotate[UBR] +\
                cubeToRotate[FTL] + cubeToRotate[FTM] + cubeToRotate[FTR] + cubeToRotate[RTL] + cubeToRotate[RTM] + cubeToRotate[RTR] +\
                cubeToRotate[BTL] + cubeToRotate[BTM] + cubeToRotate[BTR] + cubeToRotate[LTL] + cubeToRotate[LTM] + cubeToRotate[LTR])
        else:
            rotatedCube = theCube.rotate(result.get('solution'))
            checkRotatedCube = "".join(
                rotatedCube[FML] + rotatedCube[FMM] + rotatedCube[FMR] + rotatedCube[FBL] + rotatedCube[FBM] + rotatedCube[FBR] +\
                rotatedCube[RML] + rotatedCube[RMM] + rotatedCube[RMR] + rotatedCube[RBL] + rotatedCube[RBM] + rotatedCube[RBR] +\
                rotatedCube[BML] + rotatedCube[BMM] + rotatedCube[BMR] + rotatedCube[BBL] + rotatedCube[BBM] + rotatedCube[BBR] +\
                rotatedCube[LML] + rotatedCube[LMM] + rotatedCube[LMR] + rotatedCube[LBL] + rotatedCube[LBM] + rotatedCube[LBR] +\
                rotatedCube[DTL] + rotatedCube[DTM] + rotatedCube[DTR] + rotatedCube[DML] + rotatedCube[DMM] + rotatedCube[DMR] +\
                rotatedCube[DBL] + rotatedCube[DBM] + rotatedCube[DBR] + rotatedCube[UTM] + rotatedCube[UML] + rotatedCube[UMM] +\
                rotatedCube[UMR] + rotatedCube[UBM] + rotatedCube[UTL] + rotatedCube[UTR] + rotatedCube[UBL] + rotatedCube[UBR] +\
                rotatedCube[FTL] + rotatedCube[FTM] + rotatedCube[FTR] + rotatedCube[RTL] + rotatedCube[RTM] + rotatedCube[RTR] +\
                rotatedCube[BTL] + rotatedCube[BTM] + rotatedCube[BTR] + rotatedCube[LTL] + rotatedCube[LTM] + rotatedCube[LTR])
        checkGroundTrueCube = "".join(
                groundTrue[FML] + groundTrue[FMM] + groundTrue[FMR] + groundTrue[FBL] + groundTrue[FBM] + groundTrue[FBR] +\
                groundTrue[RML] + groundTrue[RMM] + groundTrue[RMR] + groundTrue[RBL] + groundTrue[RBM] + groundTrue[RBR] +\
                groundTrue[BML] + groundTrue[BMM] + groundTrue[BMR] + groundTrue[BBL] + groundTrue[BBM] + groundTrue[BBR] +\
                groundTrue[LML] + groundTrue[LMM] + groundTrue[LMR] + groundTrue[LBL] + groundTrue[LBM] + groundTrue[LBR] +\
                groundTrue[DTL] + groundTrue[DTM] + groundTrue[DTR] + groundTrue[DML] + groundTrue[DMM] + groundTrue[DMR] +\
                groundTrue[DBL] + groundTrue[DBM] + groundTrue[DBR] + groundTrue[UTM] + groundTrue[UML] + groundTrue[UMM] +\
                groundTrue[UMR] + groundTrue[UBM] + groundTrue[UTL] + groundTrue[UTR] + groundTrue[UBL] + groundTrue[UBR] +\
                groundTrue[FTL] + groundTrue[FTM] + groundTrue[FTR] + groundTrue[RTL] + groundTrue[RTM] + groundTrue[RTR] +\
                groundTrue[BTL] + groundTrue[BTM] + groundTrue[BTR] + groundTrue[LTL] + groundTrue[LTM] + groundTrue[LTR])
        
        self.assertEqual(checkRotatedCube, checkGroundTrueCube)
        
    def test010_funcTest_upperLayer_isUpperLayerSolved(self):
        encodedCube= 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upperLayer._isUpperLayerSolved(theCube)
        self.assertEqual(groundTrue, testResult) 
        
    def test020_funcTest_upperLayer_doesHaveTwoSamePieces(self):
        encodedCube= 'brrooooooggbbbbbbbrogrrrrrroboggggggyyyyyyyyywwwwwwwww'
        groundTrue = []
        groundTrue.append('o')
        theCube = cube.Cube(encodedCube)
        testResult = upperLayer._doesHaveTwoSamePieces(theCube)
        self.assertEqual(groundTrue[0], testResult[0])
        
    def test021_funcTest_upperLayer_doesHaveTwoSamePieces(self):
        encodedCube= 'obroooooogrbbbbbbbrgorrrrrrbogggggggyyyyyyyyywwwwwwwww'
        groundTrue = []
        groundTrue.append('')
        theCube = cube.Cube(encodedCube)
        testResult = upperLayer._doesHaveTwoSamePieces(theCube)
        self.assertEqual(groundTrue[0], testResult[0])
        
    def test030_funcTest_upperLayer_performAlignment(self):
        encodedCube= 'brrooooooggbbbbbbbrogrrrrrroboggggggyyyyyyyyywwwwwwwww'
        groundTrue = []
        rotateResult = []
        groundTrue.append('u')
        theCube = cube.Cube(encodedCube)   
        startLocation = ['o','3']
        upperLayer._performAlignment(theCube,rotateResult,startLocation)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test031_funcTest_upperLayer_performAlignment(self):
        encodedCube= 'brrooooooggbbbbbbbrogrrrrrroboggggggyyyyyyyyywwwwwwwww'
        groundTrue = 'o'
        rotateResult = []
        theCube = cube.Cube(encodedCube)   
        startLocation = ['o','3']
        alignmentResult = upperLayer._performAlignment(theCube,rotateResult,startLocation)
        self.assertEqual(groundTrue, alignmentResult)
        
    def test040_funcTest_upperLayer_isUpperFourCornerSolved(self):
        encodedCube= 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upperLayer._isUpperFourCornerSolved(theCube)
        self.assertEqual(groundTrue, testResult) 
        
    def test050_funcTest_upperLayer_performCornerSwitch(self):
        encodedCube= 'ogboooooorbobbbbbbbrrrrrrrrgogggggggyyyyyyyyywwwwwwwww'
        rotateResult = []
        groundTrue = []
        alignmentResult = ['g','1']
        groundResult = True
        groundTrue.append('lURuLUr')
        groundTrue.append('RUrURUUr')
        theCube = cube.Cube(encodedCube)
        upperLayer._performCornerSwith(theCube,rotateResult,alignmentResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test060_funcTest_upperLayer_performMiddlePieceSwitch(self):
        encodedCube= 'orooooooobgbbbbbbbrorrrrrrrgbgggggggyyyyyyyyywwwwwwwww'
        rotateResult = []
        groundTrue = []
        groundTrue.append('FFUrLFFlRUFF')
        theCube = cube.Cube(encodedCube)
        upperLayer._performMiddlePiecesSwitch(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test070_funcTest_upperLayer_controllerAfterCornerSolved(self):
        encodedCube= 'orooooooobgbbbbbbbrorrrrrrrgbgggggggyyyyyyyyywwwwwwwww'
        rotateResult = []
        groundTrue = []
        groundTrue.append('FFUrLFFlRUFF')
        groundTrue.append('LLUfBLLbFULL')
        theCube = cube.Cube(encodedCube)
        upperLayer._controllerAfterCornerSolved(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test080_funcTest_upperLayer_controllerMakerCornerSolved(self):
        encodedCube= 'obroooooogrbbbbbbbrgorrrrrrbogggggggyyyyyyyyywwwwwwwww'
        rotateResult = []
        groundTrue = []
        groundTrue.append('lURuLUrRUrURUUrubUFuBUfFUfUFuuf')
        theCube = cube.Cube(encodedCube)
        upperLayer._controllerMakerCornerSolved(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
    
    def test801_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        cubeToRotate = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test802_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        cubeToRotate = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test803_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test804_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        cubeToRotate = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test805_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        cubeToRotate = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test806_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        cubeToRotate = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test807_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        cubeToRotate = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test808_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        cubeToRotate = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test809_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        cubeToRotate = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test810_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        cubeToRotate = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test811_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        cubeToRotate = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test812_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        cubeToRotate = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test813_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        cubeToRotate = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test814_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        cubeToRotate = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test816_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        cubeToRotate = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test817_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        cubeToRotate = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test818_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        cubeToRotate = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test819_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        cubeToRotate = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)

    def test821_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        cubeToRotate = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test822_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        cubeToRotate = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test823_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        cubeToRotate = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
     
    def test825_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        cubeToRotate = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
 
    def test827_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        cubeToRotate = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test828_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        cubeToRotate = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test829_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        cubeToRotate = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)   
    
    def test831_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        cubeToRotate = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test832_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        cubeToRotate = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test833_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        cubeToRotate = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test834_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        cubeToRotate = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test835_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        cubeToRotate = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test836_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        cubeToRotate = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test837_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        cubeToRotate = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test838_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        cubeToRotate = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test839_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        cubeToRotate = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test840_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test830_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        cubeToRotate = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test815_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        cubeToRotate = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)

    def test826_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        cubeToRotate = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test824_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        cubeToRotate = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test820_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        cubeToRotate = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test900_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        cubeToRotate = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test901_upperLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        cubeToRotate = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test1000_upperLayerMixedtest_unsolvableCube(self):
        parms = {}
        parms['cube'] = 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        cubeToRotate = 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        groundTrue = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: unsolvable cube', result['status'])   
        