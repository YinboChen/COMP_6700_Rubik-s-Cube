'''
Created on Apr 15, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view import solve
import rubik.model.cube as cube
from rubik.model.constants import *
 

class SolveTest(TestCase):
    
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
        
    def test010_funcTest_solve_isCubeSolvable(self):
        #encodedCube= 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        encodedCube= 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        groundTrue = False
        theCube = cube.Cube(encodedCube)
        testResult = solve._isCubeSolvable(theCube)
        self.assertEqual(groundTrue, testResult) 
        
    def test011_funcTest_solve_isCubeSolvable(self):
        #encodedCube= 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        encodedCube= 'gryoooooobogbbbbbbogbrrrrrrybrggggggoyyyyyyyrwwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = solve._isCubeSolvable(theCube)
        self.assertEqual(groundTrue, testResult) 
        
    def test900_solveMixedtest_unsolvableCube(self):
        parms = {}
        parms['cube'] = 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        cubeToRotate = 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        groundTrue = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: unsolvable cube', result['status']) 
        
    def test800_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        cubeToRotate = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 

    def test801_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        cubeToRotate = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test802_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        cubeToRotate = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test803_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'ywoboowwowobbbbgrrwrryrryowywbygwgggbbrgygorbroyywgoyg'
        cubeToRotate = 'ywoboowwowobbbbgrrwrryrryowywbygwgggbbrgygorbroyywgoyg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test804_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'bgyboywbwroogbborryoryrobgrwboygwwwogwgoygywggrbrwybry'
        cubeToRotate = 'bgyboywbwroogbborryoryrobgrwboygwwwogwgoygywggrbrwybry'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test805_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'rwbyobowbrryobgrwwggoorgorgbbgygorygyroryywoywbwbwgywb'
        cubeToRotate = 'rwbyobowbrryobgrwwggoorgorgbbgygorygyroryywoywbwbwgywb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)  
        
    def test806_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'ywowogobwwobrbygyywowgrygrygwrbggbbyrgrrywbbbgoorwooyr'
        cubeToRotate = 'ywowogobwwobrbygyywowgrygrygwrbggbbyrgrrywbbbgoorwooyr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test807_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'wgoroywrrbwybbobggrowbrbyorogorgwggrgwgrybbwybyyowywyo'
        cubeToRotate = 'wgoroywrrbwybbobggrowbrbyorogorgwggrgwgrybbwybyyowywyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test808_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'owrrowybwggobborrbbrbyrbryyowwogbrogwwygyygoyoyggwgbrw'
        cubeToRotate = 'owrrowybwggobborrbbrbyrbryyowwogbrogwwygyygoyoyggwgbrw'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test809_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'boooogooggbwrbgybrgrborwygwrrwbgbbwbywryyyowwyyogwrryg'
        cubeToRotate = 'boooogooggbwrbgybrgrborwygwrrwbgbbwbywryyyowwyyogwrryg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test810_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'ooryoygwoboobbwwbybggrrorrgrybggorwowyyrybwwwyggbwrygb'
        cubeToRotate = 'ooryoygwoboobbwwbybggrrorrgrybggorwowyyrybwwwyggbwrygb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test811_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'orbwoogywwooybwrrygororbrrwggyygboroygwwybbwrygggwbbyb'
        cubeToRotate = 'orbwoogywwooybwrrygororbrrwggyygboroygwwybbwrygggwbbyb'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result) 
        
    def test812_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'broyogyoogoyobwgbbrwwrrbyrrgywwgowgorggrywogwbbyywybbr'
        cubeToRotate = 'broyogyoogoyobwgbbrwwrrbyrrgywwgowgorggrywogwbbyywybbr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test813_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'ogbbobbowrobrbrgrgwgoyrwrowybybgyrrogyroywbwywgogwwgyy'
        cubeToRotate = 'ogbbobbowrobrbrgrgwgoyrwrowybybgyrrogyroywbwywgogwwgyy'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test814_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'ybwbobrowbyywbogoggwrgrrwyygrrygobrbygogybbrowyowwwogr'
        cubeToRotate = 'ybwbobrowbyywbogoggwrgrrwyygrrygobrbygogybbrowyowwwogr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test815_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'wgowowyrgbwrobyogryggorowbbybrggbwygrybyyrgryobwrwwoob'
        cubeToRotate = 'wgowowyrgbwrobyogryggorowbbybrggbwygrybyyrgryobwrwwoob'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test816_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'rywboogwogwobbgyyrwrgoryyrbowwrgwybwybboyrborogbywgrgg'
        cubeToRotate = 'rywboogwogwobbgyyrwrgoryyrbowwrgwybwybboyrborogbywgrgg'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test817_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'ogyooyoowbbbgbwgbgwrrgrwybrgobrgbgobyyrgyrwrrywoywwwyo'
        cubeToRotate = 'ogyooyoowbbbgbwgbgwrrgrwybrgobrgbgobyyrgyrwrrywoywwwyo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test818_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'yoogororywogwbwoowrgbbrrggrrggbgwwbbyrwyybrwbyygywyboo'
        cubeToRotate = 'yoogororywogwbwoowrgbbrrggrrggbgwwbbyrwyybrwbyygywyboo'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test819_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'rgyoowbrwooobbybgywgwrrwgygobgogyywrgwbrybwobygrrwyobr'
        cubeToRotate = 'rgyoowbrwooobbybgywgwrrwgygobgogyywrgwbrybwobygrrwyobr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test820_solveMixedtest_solvableCube(self):  
        parms = {}
        parms['cube'] = 'rwyooyorygrbobrbrgrbwgrwwboryyoggbbgbwygyyggowboowwwyr'
        cubeToRotate = 'rwyooyorygrbobrbrgrbwgrwwboryyoggbbgbwygyyggowboowwwyr'
        groundTrue = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)

        
    