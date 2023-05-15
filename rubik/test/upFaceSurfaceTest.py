'''
Created on Apr 4, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view.solve import solve
from rubik.controller import upFaceSurface
import rubik.model.cube as cube
from rubik.model.constants import *

# Create unittest for checking the output solution from the upFaceSurface
# Rotate the cube based on the solution and checking the rotated cube whether has the upFaceSurface solved
#happy path: 
#            test010 test func (_isUpFaceSurfaceSolved)
#            test020 test func (_doesCleanCrossExist)
#            test030 test func (_doRUrURUUr)
#            test040 test func (_doesAFishExist)
#            test050 test func (_checkTopHeavyExist)
#           
#            test801 - 840  normal test cases

class upFaceSurfaceTest(TestCase):
    
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
                cubeToRotate[UMR] + cubeToRotate[UBM] + cubeToRotate[UTL] + cubeToRotate[UTR] + cubeToRotate[UBL] + cubeToRotate[UBR])
        else:
            rotatedCube = theCube.rotate(result.get('solution'))
            checkRotatedCube = "".join(
                rotatedCube[FML] + rotatedCube[FMM] + rotatedCube[FMR] + rotatedCube[FBL] + rotatedCube[FBM] + rotatedCube[FBR] +\
                rotatedCube[RML] + rotatedCube[RMM] + rotatedCube[RMR] + rotatedCube[RBL] + rotatedCube[RBM] + rotatedCube[RBR] +\
                rotatedCube[BML] + rotatedCube[BMM] + rotatedCube[BMR] + rotatedCube[BBL] + rotatedCube[BBM] + rotatedCube[BBR] +\
                rotatedCube[LML] + rotatedCube[LMM] + rotatedCube[LMR] + rotatedCube[LBL] + rotatedCube[LBM] + rotatedCube[LBR] +\
                rotatedCube[DTL] + rotatedCube[DTM] + rotatedCube[DTR] + rotatedCube[DML] + rotatedCube[DMM] + rotatedCube[DMR] +\
                rotatedCube[DBL] + rotatedCube[DBM] + rotatedCube[DBR] + rotatedCube[UTM] + rotatedCube[UML] + rotatedCube[UMM] +\
                rotatedCube[UMR] + rotatedCube[UBM] + rotatedCube[UTL] + rotatedCube[UTR] + rotatedCube[UBL] + rotatedCube[UBR])
        checkGroundTrueCube = "".join(
                groundTrue[FML] + groundTrue[FMM] + groundTrue[FMR] + groundTrue[FBL] + groundTrue[FBM] + groundTrue[FBR] +\
                groundTrue[RML] + groundTrue[RMM] + groundTrue[RMR] + groundTrue[RBL] + groundTrue[RBM] + groundTrue[RBR] +\
                groundTrue[BML] + groundTrue[BMM] + groundTrue[BMR] + groundTrue[BBL] + groundTrue[BBM] + groundTrue[BBR] +\
                groundTrue[LML] + groundTrue[LMM] + groundTrue[LMR] + groundTrue[LBL] + groundTrue[LBM] + groundTrue[LBR] +\
                groundTrue[DTL] + groundTrue[DTM] + groundTrue[DTR] + groundTrue[DML] + groundTrue[DMM] + groundTrue[DMR] +\
                groundTrue[DBL] + groundTrue[DBM] + groundTrue[DBR] + groundTrue[UTM] + groundTrue[UML] + groundTrue[UMM] +\
                groundTrue[UMR] + groundTrue[UBM] + groundTrue[UTL] + groundTrue[UTR] + groundTrue[UBL] + groundTrue[UBR])
        self.assertEqual(checkRotatedCube, checkGroundTrueCube)
        
    def test010_funcTest_upFaceSurface_isUpFaceSurfaceSolved(self):
        encodedCube= 'bggooooooobbbbbbbbrrrrrrrrrgooggggggyyyyyyyyywwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upFaceSurface._isUpFaceSurfaceSolved(theCube)
        self.assertEqual(groundTrue, testResult) 
    
    def test020_funcTest_upFaceSurface_doesCleanCrossExist(self):
        encodedCube= 'ybyoooooogrybbbbbboogrrrrrrygrggggggrybyyybyowwwwwwwww'
        rotateResult = []
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upFaceSurface._doesCleanCrossExist(theCube,rotateResult)
        self.assertEqual(groundTrue, testResult) 
    
    def test021_funcTest_upFaceSurface_doesCleanCrossExist(self):
        encodedCube= 'ybyoooooogrybbbbbboogrrrrrrygrggggggrybyyybyowwwwwwwww'
        rotateResult = []
        groundTrue = []
        groundTrue.append('U')
        theCube = cube.Cube(encodedCube)
        testResult = upFaceSurface._doesCleanCrossExist(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
    
    def test030_funcTest_upFaceSurface_doRUrURUUr(self):
        encodedCube= 'gryoooooooogbbbbbbygrrrrrrrybyggggggbyryyyoybwwwwwwwww'
        rotateResult = []
        groundTrue = []
        groundTrue.append('RUrURUUr')
        theCube = cube.Cube(encodedCube)
        upFaceSurface._doRUrURUUr(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
    
    def test040_funcTest_upFaceSurface_doesAFishExist(self):
        encodedCube= 'bogooooooorybbbbbbogyrrrrrrrbygggggggybyyyryywwwwwwwww'
        rotateResult = []
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upFaceSurface._doesAFishExist(theCube,rotateResult)
        self.assertEqual(groundTrue, testResult) 
    
    def test041_funcTest_upFaceSurface_doesAFishExist(self):
        encodedCube= 'rbyoooooobogbbbbbboryrrrrrrogyggggggbyyyyygyrwwwwwwwww'
        rotateResult = []
        groundTrue = []
        groundResult = True
        groundTrue.append('UU')
        theCube = cube.Cube(encodedCube)
        testResult = upFaceSurface._doesAFishExist(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult))
        self.assertEqual(groundResult, testResult) 
    
    def test050_funcTest_upFaceSurface_checkTopHeavyExist(self):
        encodedCube= 'bbgooooooyoybbbbbbbggrrrrrroroggggggyyryyyyyrwwwwwwwww'
        rotateResult = []
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = upFaceSurface._checkTopHeavyExist(theCube,rotateResult)
        self.assertEqual(groundTrue, testResult)  
    
    def test801_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        cubeToRotate = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    def test802_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        cubeToRotate = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test803_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        cubeToRotate = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test804_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        cubeToRotate = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test805_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        cubeToRotate = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test806_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        cubeToRotate = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test807_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        cubeToRotate = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test808_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        cubeToRotate = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test809_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        cubeToRotate = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test810_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        cubeToRotate = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test811_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        cubeToRotate = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test812_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        cubeToRotate = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test813_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        cubeToRotate = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test814_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        cubeToRotate = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test816_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        cubeToRotate = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test817_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        cubeToRotate = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test818_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        cubeToRotate = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test819_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        cubeToRotate = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test821_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        cubeToRotate = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test822_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        cubeToRotate = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test823_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        cubeToRotate = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test825_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        cubeToRotate = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test827_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        cubeToRotate = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test828_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        cubeToRotate = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test829_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        cubeToRotate = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)   
    
    def test831_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        cubeToRotate = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test832_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        cubeToRotate = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test833_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        cubeToRotate = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test834_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        cubeToRotate = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test835_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        cubeToRotate = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test836_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        cubeToRotate = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test837_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        cubeToRotate = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test838_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        cubeToRotate = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test839_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        cubeToRotate = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test840_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test830_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        cubeToRotate = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test815_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        cubeToRotate = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test826_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        cubeToRotate = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test824_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        cubeToRotate = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test820_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        cubeToRotate = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test900_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        cubeToRotate = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test901_upFaceSurfaceMixedtest(self):
        parms = {}
        parms['cube'] = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        cubeToRotate = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        




    