'''
Created on Apr 3, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view.solve import solve
from rubik.controller import upFaceCross
import rubik.model.cube as cube
from rubik.model.constants import *

# Create unittest for checking the output solution from the upFaceCross
# Rotate the cube based on the solution and checking the rotated cube whether has the upFaceCross solved
#happy path: 
#            test010 test func (_isUpFaceCrossSolved)
#            test020 test func (_doesVerticalExist)
#            test030 test func (_doesTargetOnNineAndTwelv)
#            test040 test func (_doFURurfRotation)
#           
#            test801 - 840  normal test cases

class upFaceCrossTest(TestCase):
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
                cubeToRotate[UMR] + cubeToRotate[UBM])
        else:
            rotatedCube = theCube.rotate(result.get('solution'))
            checkRotatedCube = "".join(
                rotatedCube[FML] + rotatedCube[FMM] + rotatedCube[FMR] + rotatedCube[FBL] + rotatedCube[FBM] + rotatedCube[FBR] +\
                rotatedCube[RML] + rotatedCube[RMM] + rotatedCube[RMR] + rotatedCube[RBL] + rotatedCube[RBM] + rotatedCube[RBR] +\
                rotatedCube[BML] + rotatedCube[BMM] + rotatedCube[BMR] + rotatedCube[BBL] + rotatedCube[BBM] + rotatedCube[BBR] +\
                rotatedCube[LML] + rotatedCube[LMM] + rotatedCube[LMR] + rotatedCube[LBL] + rotatedCube[LBM] + rotatedCube[LBR] +\
                rotatedCube[DTL] + rotatedCube[DTM] + rotatedCube[DTR] + rotatedCube[DML] + rotatedCube[DMM] + rotatedCube[DMR] +\
                rotatedCube[DBL] + rotatedCube[DBM] + rotatedCube[DBR] + rotatedCube[UTM] + rotatedCube[UML] + rotatedCube[UMM] +\
                rotatedCube[UMR] + rotatedCube[UBM])
        checkGroundTrueCube = "".join(
                groundTrue[FML] + groundTrue[FMM] + groundTrue[FMR] + groundTrue[FBL] + groundTrue[FBM] + groundTrue[FBR] +\
                groundTrue[RML] + groundTrue[RMM] + groundTrue[RMR] + groundTrue[RBL] + groundTrue[RBM] + groundTrue[RBR] +\
                groundTrue[BML] + groundTrue[BMM] + groundTrue[BMR] + groundTrue[BBL] + groundTrue[BBM] + groundTrue[BBR] +\
                groundTrue[LML] + groundTrue[LMM] + groundTrue[LMR] + groundTrue[LBL] + groundTrue[LBM] + groundTrue[LBR] +\
                groundTrue[DTL] + groundTrue[DTM] + groundTrue[DTR] + groundTrue[DML] + groundTrue[DMM] + groundTrue[DMR] +\
                groundTrue[DBL] + groundTrue[DBM] + groundTrue[DBR] + groundTrue[UTM] + groundTrue[UML] + groundTrue[UMM] +\
                groundTrue[UMR] + groundTrue[UBM])
        self.assertEqual(checkRotatedCube, checkGroundTrueCube)
        
    def test010_funcTest_upFaceCross_isUpFaceCrossSolved(self):
        encodedCube= 'ybrooooooyoybbbbbbgryrrrrrroggggggggbyoyyyrybwwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upFaceCross._isUpFaceCrossSolved(theCube)
        self.assertEqual(groundTrue, testResult)
        
    def test020_funcTest_upFaceCross_doesVerticalExist(self):
        encodedCube= 'byyoooooogobbbbbbbrygrrrrrrygoggggggrryyyyybowwwwwwwww'
        groundTrue = []
        rotateResult = []
        groundTrue.append('U')
        theCube = cube.Cube(encodedCube)
        upFaceCross._doesVerticalExist(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test030_funcTest_upFaceCross_doesTargetOnNineAndTwelv(self):
        encodedCube= 'bryooooooggobbbbbbbyyrrrrrrryygggggggoybyyryowwwwwwwww'
        groundTrue = []
        rotateResult = []
        groundTrue.append('UU')
        theCube = cube.Cube(encodedCube)
        upFaceCross._doesTargetOnNineAndTwelv(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test040_funcTest_upFaceCross_doFURurfRotation(self):
        encodedCube= 'byyooooooryybbbbbbbryrrrrrrggoggggggoyryybyogwwwwwwwww'
        groundTrue = []
        rotateResult = []
        groundTrue.append('FURurf')
        theCube = cube.Cube(encodedCube)
        upFaceCross._doFURurfRotation(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        
    def test801_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        cubeToRotate = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test802_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        cubeToRotate = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test803_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        cubeToRotate = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test804_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        cubeToRotate = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test805_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        cubeToRotate = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test806_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        cubeToRotate = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test807_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        cubeToRotate = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test808_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        cubeToRotate = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test809_upFaceCrossMixedtestt(self):
        parms = {}
        parms['cube'] = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        cubeToRotate = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test810_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        cubeToRotate = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test811_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        cubeToRotate = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test812_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        cubeToRotate = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test813_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        cubeToRotate = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test814_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        cubeToRotate = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test816_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        cubeToRotate = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test817_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        cubeToRotate = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test818_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        cubeToRotate = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test819_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        cubeToRotate = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test821_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        cubeToRotate = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test822_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        cubeToRotate = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test823_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        cubeToRotate = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test825_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        cubeToRotate = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test827_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        cubeToRotate = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test828_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        cubeToRotate = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test829_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        cubeToRotate = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    
    def test831_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        cubeToRotate = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test832_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        cubeToRotate = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test833_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        cubeToRotate = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test834_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        cubeToRotate = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test835_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        cubeToRotate = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test836_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        cubeToRotate = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test837_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        cubeToRotate = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test838_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        cubeToRotate = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test839_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        cubeToRotate = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test840_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test830_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        cubeToRotate = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test815_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        cubeToRotate = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)

    def test826_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        cubeToRotate = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test824_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        cubeToRotate = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test820_upFaceCrossMixedtest(self):
        parms = {}
        parms['cube'] = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        cubeToRotate = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
