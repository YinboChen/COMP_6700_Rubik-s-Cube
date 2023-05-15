'''
Created on Mar 21, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view.solve import solve
from rubik.controller import middleLayer
import rubik.model.cube as cube
from rubik.model.constants import *


# Create unittest for checking the output solution from the middlelayer
# Rotate the cube based on the solution and checking the rotated cube whether has the middlelayer solved
#happy path: 
#            test010 test func (_isMiddleLayerSolved)
#            test020 test func (_doesTargetInTopCross)
#            test030 test func (_matchAndLRTrigger)
#            test040 test func (_middleLayer_MiddleLayerCornerHasSameColors)
#           
#            test801 - 840  normal test cases

class middleLayerTest(TestCase):
    def _checkComparison(self,cubeToRotate, groundTrue, result):
        theCube = cube.Cube(cubeToRotate)
        # print(result.get('solution'))
        if result.get('solution') == '':
            checkRotatedCube = "".join(
                cubeToRotate[FML] + cubeToRotate[FMM] + cubeToRotate[FMR] + cubeToRotate[FBL] + cubeToRotate[FBM] + cubeToRotate[FBR] +\
                cubeToRotate[RML] + cubeToRotate[RMM] + cubeToRotate[RMR] + cubeToRotate[RBL] + cubeToRotate[RBM] + cubeToRotate[RBR] +\
                cubeToRotate[BML] + cubeToRotate[BMM] + cubeToRotate[BMR] + cubeToRotate[BBL] + cubeToRotate[BBM] + cubeToRotate[BBR] +\
                cubeToRotate[LML] + cubeToRotate[LMM] + cubeToRotate[LMR] + cubeToRotate[LBL] + cubeToRotate[LBM] + cubeToRotate[LBR] +\
                cubeToRotate[DTL] + cubeToRotate[DTM] + cubeToRotate[DTR] + cubeToRotate[DML] + cubeToRotate[DMM] + cubeToRotate[DMR] +\
                cubeToRotate[DBL] + cubeToRotate[DBM] + cubeToRotate[DBR])
        else:
            rotatedCube = theCube.rotate(result.get('solution'))
            checkRotatedCube = "".join(
                rotatedCube[FML] + rotatedCube[FMM] + rotatedCube[FMR] + rotatedCube[FBL] + rotatedCube[FBM] + rotatedCube[FBR] +\
                rotatedCube[RML] + rotatedCube[RMM] + rotatedCube[RMR] + rotatedCube[RBL] + rotatedCube[RBM] + rotatedCube[RBR] +\
                rotatedCube[BML] + rotatedCube[BMM] + rotatedCube[BMR] + rotatedCube[BBL] + rotatedCube[BBM] + rotatedCube[BBR] +\
                rotatedCube[LML] + rotatedCube[LMM] + rotatedCube[LMR] + rotatedCube[LBL] + rotatedCube[LBM] + rotatedCube[LBR] +\
                rotatedCube[DTL] + rotatedCube[DTM] + rotatedCube[DTR] + rotatedCube[DML] + rotatedCube[DMM] + rotatedCube[DMR] +\
                rotatedCube[DBL] + rotatedCube[DBM] + rotatedCube[DBR])
        checkGroundTrueCube = "".join(
                groundTrue[FML] + groundTrue[FMM] + groundTrue[FMR] + groundTrue[FBL] + groundTrue[FBM] + groundTrue[FBR] +\
                groundTrue[RML] + groundTrue[RMM] + groundTrue[RMR] + groundTrue[RBL] + groundTrue[RBM] + groundTrue[RBR] +\
                groundTrue[BML] + groundTrue[BMM] + groundTrue[BMR] + groundTrue[BBL] + groundTrue[BBM] + groundTrue[BBR] +\
                groundTrue[LML] + groundTrue[LMM] + groundTrue[LMR] + groundTrue[LBL] + groundTrue[LBM] + groundTrue[LBR] +\
                groundTrue[DTL] + groundTrue[DTM] + groundTrue[DTR] + groundTrue[DML] + groundTrue[DMM] + groundTrue[DMR] +\
                groundTrue[DBL] + groundTrue[DBM] + groundTrue[DBR])
        self.assertEqual(checkRotatedCube, checkGroundTrueCube)
    
    def test010_funcTest_middleLayer_isMiddleLayerSolved(self):
        encodedCube= 'bogooooooygybbbbbbbygrrrrrroyoggggggybrryyyyrwwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = middleLayer._isMiddleLayerSolved(theCube)
        self.assertEqual(groundTrue, testResult)
    
    def test020_funcTest_middleLayer_doesTopCenterInTopEdgeCross(self):
        encodedCube= 'bogooooooygybbbbbbbygrrrrrroyoggggggybrryyyyrwwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = middleLayer._doesTopCenterInTopEdgeCross(theCube)
        self.assertEqual(groundTrue, testResult)
    
    def test021_funcTest_middleLayer_doesTopCenterInTopEdgeCross(self):
        encodedCube= 'obbyogoooygyobbbbbrybyrgrrrrrgygogggyrgbyryoowwwwwwwww'
        groundTrue = False
        theCube = cube.Cube(encodedCube)
        testResult = middleLayer._doesTopCenterInTopEdgeCross(theCube)
        self.assertEqual(groundTrue, testResult)
        
    def test030_funcTest_middleLayer_matchAndLRTrigger(self):
        encodedCube= 'brroooooogoybbbbbbobyrrrrrrggyggygggoybyygryywwwwwwwww'
        groundTrue = []
        groundTrue.append('U')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        middleLayer._matchAndLRTrigger(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
        
    def test031_funcTest_middleLayer_matchAndLRTrigger(self):
        encodedCube= 'yorooyooogyrobbbbbyborrrrrrygbgggggggybyyrobywwwwwwwww'
        groundTrue = []
        groundTrue.append('URUrufuFU')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        middleLayer._matchAndLRTrigger(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
    
    def test040_funcTest_middleLayer_switchMiddleLayerCorner(self):
        encodedCube= 'yryoogooobobybbbbbyoyrrrrrrgbgggggggoboyyyryrwwwwwwwww'
        groundTrue = 'RUrufuF'
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        middleLayer._switchMiddleLayerCorner(theCube,rotateResult)
        self.assertEqual(groundTrue, rotateResult[0])

    
    def test801_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        cubeToRotate = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test802_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        cubeToRotate = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test803_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        cubeToRotate = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test804_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        cubeToRotate = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test805_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        cubeToRotate = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test806_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        cubeToRotate = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test807_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        cubeToRotate = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test808_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        cubeToRotate = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test809_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        cubeToRotate = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test810_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        cubeToRotate = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test811_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        cubeToRotate = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test812_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        cubeToRotate = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test813_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        cubeToRotate = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test814_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        cubeToRotate = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test816_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        cubeToRotate = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test817_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        cubeToRotate = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test818_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        cubeToRotate = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test819_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        cubeToRotate = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test821_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        cubeToRotate = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test822_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        cubeToRotate = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test823_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        cubeToRotate = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test825_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        cubeToRotate = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test827_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        cubeToRotate = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test828_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        cubeToRotate = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test829_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        cubeToRotate = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test831_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        cubeToRotate = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test832_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        cubeToRotate = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test833_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        cubeToRotate = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test834_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        cubeToRotate = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test835_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        cubeToRotate = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test836_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        cubeToRotate = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test837_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        cubeToRotate = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test838_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        cubeToRotate = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test839_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        cubeToRotate = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test840_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test830_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        cubeToRotate = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test815_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        cubeToRotate = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)

    def test826_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        cubeToRotate = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test824_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        cubeToRotate = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test820_middleLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        cubeToRotate = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        groundTrue = 'yyyoooooogbgbbbbbbyyyrrrrrrbgbggggggrrryyyooowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    
    