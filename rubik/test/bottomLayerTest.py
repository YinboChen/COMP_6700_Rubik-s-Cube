'''
Created on Feb 27, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view.solve import solve
from rubik.controller import bottomLayer
import rubik.model.cube as cube
from rubik.model.constants import *

# Create unittest for checking the output solution from the bottomlayer
# Rotate the cube based on the solution and checking the rotated cube whether has the bottomlayer solved
#happy path: 
#            test001 test func (isBottomLayerSolved)
#            test002 test func (findOnLeftsidesPatternLocations)
#            test003 test func (findOnRightsidesPatternLocations)
#            test004 test func (findOnTopsidePatternLocations)
#            test005 test func (findOnDownsidePatternLocations)
#            test100 input cube solved already
#            test110 not solved yet. missed one piece on the side(left-trigger)
#            test111 not solved yet. missed multiple pieces on the sides(left-trigger)
#            test120 not solved yet. missed one piece on the side(right-trigger)
#            test121 not solved yet. missed multiple pieces on the sides(right-trigger)
#            test130 not solved yet. missed multiple pieces on the sides(right and left trigger)

#            test150 ...missed piece on the U side
#            test150 ...missed multiple pieces on the U and one side
#            test152 ...missed pieces on U as well as needing left-right triggers
#            test160 mixed test
class BottomLayerTest(TestCase):
           
    def _checkComparison(self,cubeToRotate, groundTrue, result):
        theCube = cube.Cube(cubeToRotate)
        #print(result.get('solution'))
        if result.get('solution') == '':
            checkRotatedCube = "".join(
                cubeToRotate[FMM] + cubeToRotate[FBL] + cubeToRotate[FBM] + cubeToRotate[FBR] +\
                cubeToRotate[RMM] + cubeToRotate[RBL] + cubeToRotate[RBM] + cubeToRotate[RBR] +\
                cubeToRotate[BMM] + cubeToRotate[BBL] + cubeToRotate[BBM] + cubeToRotate[BBR] +\
                cubeToRotate[LMM] + cubeToRotate[LBL] + cubeToRotate[LBM] + cubeToRotate[LBR] +\
                cubeToRotate[DTL] + cubeToRotate[DTM] + cubeToRotate[DTR] + cubeToRotate[DML] +\
                cubeToRotate[DMM] + cubeToRotate[DMR] + cubeToRotate[DBL] + cubeToRotate[DBM] + cubeToRotate[DBR])
        else:
            rotatedCube = theCube.rotate(result.get('solution'))
            checkRotatedCube = "".join(
                rotatedCube[FMM] + rotatedCube[FBL] + rotatedCube[FBM] + rotatedCube[FBR] +\
                rotatedCube[RMM] + rotatedCube[RBL] + rotatedCube[RBM] + rotatedCube[RBR] +\
                rotatedCube[BMM] + rotatedCube[BBL] + rotatedCube[BBM] + rotatedCube[BBR] +\
                rotatedCube[LMM] + rotatedCube[LBL] + rotatedCube[LBM] + rotatedCube[LBR] +\
                rotatedCube[DTL] + rotatedCube[DTM] + rotatedCube[DTR] + rotatedCube[DML] +\
                rotatedCube[DMM] + rotatedCube[DMR] + rotatedCube[DBL] + rotatedCube[DBM] + rotatedCube[DBR])
        checkGroundTrueCube = "".join(
                groundTrue[FMM] + groundTrue[FBL] + groundTrue[FBM] + groundTrue[FBR] +\
                groundTrue[RMM] + groundTrue[RBL] + groundTrue[RBM] + groundTrue[RBR] +\
                groundTrue[BMM] + groundTrue[BBL] + groundTrue[BBM] + groundTrue[BBR] +\
                groundTrue[LMM] + groundTrue[LBL] + groundTrue[LBM] + groundTrue[LBR] +\
                groundTrue[DTL] + groundTrue[DTM] + groundTrue[DTR] + groundTrue[DML] +\
                groundTrue[DMM] + groundTrue[DMR] + groundTrue[DBL] + groundTrue[DBM] + groundTrue[DBR])
        self.assertEqual(checkRotatedCube, checkGroundTrueCube)
    
    def test001_funcTest_bottomLayer_isBottomLayerSolved(self):
        encodedCube= 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        groundTrue = True
        theCube = cube.Cube(encodedCube)
        testResult = bottomLayer._isBottomLayerSolved(theCube)
        self.assertEqual(groundTrue, testResult)
    
    def test002_funcTest_bottomLayer_findOnLeftsidesPatternLocations(self):
        encodedCube= 'ygwoooooybyrybggbbygooryrrrybbrgbggggrbryboyowwrwwwwww'
        groundTrue = []
        groundTrue.append('fuF')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        bottomLayer._findOnLeftsidesPatternLocations(theCube,rotateResult)
        self.assertListEqual(groundTrue, rotateResult)
    
    def test003_funcTest_bottomLayer_findOnRightsidesPatternLocations(self):
        encodedCube= 'ryooorooobyybbgbbbryrrrgrrowbbogbggggggyyryoywwwwwwyww'
        groundTrue = []
        groundTrue.append('LUl')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        bottomLayer._findOnRightsidesPatternLocations(theCube,rotateResult)
        self.assertListEqual(groundTrue, rotateResult)
    
    def test004_funcTest_bottomLayer_findOnTopsidesPatternLocations(self):
        encodedCube= 'ggybooooorbrbbobbbyygyrgrrroyoogyggbygbryrwrgywwwwwwww'
        groundTrue = []
        groundTrue.append('FUUf')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        bottomLayer._findOnTopsidesPatternLocations(theCube,rotateResult)
        self.assertEqual(''.join(groundTrue), ''.join(rotateResult[0]))
    
    def test005_funcTest_bottomLayer_findOnDownsidesPatternLocations(self):
        encodedCube= 'royboowooogrgbybbbybygrorrrgrybgyggoorbyyrgybgwwwwwwww'
        groundTrue = []
        groundTrue.append('FUf')
        rotateResult = []
        theCube = cube.Cube(encodedCube)
        bottomLayer._findOnDownsidesPatternLocations(theCube,rotateResult)
        self.assertListEqual(groundTrue, rotateResult)
    
    
    def test100_bottomLayerSolvedAlready(self):
        parms = {}
        parms['cube'] = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
    
        cubeToRotate = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test110_bottomLayerNotSolvedMissingOne_leftTrigger(self):
        parms = {}
        parms['cube'] = 'ygwoooooybyrybggbbygooryrrrybbrgbggggrbryboyowwrwwwwww'
    
        cubeToRotate = 'ygwoooooybyrybggbbygooryrrrybbrgbggggrbryboyowwrwwwwww'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test111_bottomLayerNotSolvedMissingMultipleOnSides_leftTrigger(self):
        parms = {}
        parms['cube'] = 'gywoooooybgwybybbgryyrrgyrrbrrogbgggrgbbyrybowwowwwwwo'
    
        cubeToRotate = 'gywoooooybgwybybbgryyrrgyrrbrrogbgggrgbbyrybowwowwwwwo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test120_bottomLayerNotSolvedMissingOne_rightTrigger(self):
        parms = {}
        parms['cube'] = 'ryooorooobyybbgbbbryrrrgrrowbbogbggggggyyryoywwwwwwyww'
    
        cubeToRotate = 'ryooorooobyybbgbbbryrrrgrrowbbogbggggggyyryoywwwwwwyww'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test121_bottomLayerNotSolvedMissingMultipleOnSides_rightTrigger(self):
        parms = {}
        parms['cube'] = 'wyyyoogoogbrbbrbbbygbyrgorrwbgogoggyrrbyyrogorwwwwwwwy'
    
        cubeToRotate = 'wyyyoogoogbrbbrbbbygbyrgorrwbgogoggyrrbyyrogorwwwwwwwy'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test130_bottomLayerNotSolvedMissingMultiPieces_leftAndRightTrigger(self):
        parms = {}
        parms['cube'] = 'wywyorrobrrgybyybowbrbrgyrowoooggggggrobygbobywrwwwywb'
    
        cubeToRotate = 'wywyorrobrrgybyybowbrbrgyrowoooggggggrobygbobywrwwwywb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    def test150_bottomLayerNotSolvedMissingOnUpSide(self):
        parms = {}
        parms['cube'] = 'yygooroooryobbgbbbbbyrrgrrggorygbrggoyygyobrwwwwwwwyww'
    
        cubeToRotate = 'yygooroooryobbgbbbbbyrrgrrggorygbrggoyygyobrwwwwwwwyww'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test151_bottomLayerNotSolvedMissingMultiOnUSide(self):
        parms = {}
        parms['cube'] = 'bggbogyobrrbybyybooogorryrrwyrbgyyggobwrygwowowrwwwgwb'
    
        cubeToRotate = 'bggbogyobrrbybyybooogorryrrwyrbgyyggobwrygwowowrwwwgwb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test152_bottomLayerNotSolvedMissingsOnlyExceptDSide(self):
        parms = {}
        parms['cube'] = 'ogrrobborbyrobgybrwowyrybrybbwbgyogyoggryogrwowgwwwgwy'
    
        cubeToRotate = 'ogrrobborbyrobgybrwowyrybrybbwbgyogyoggryogrwowgwwwgwy'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test160_bottomLayerNotSolvedMixedAllSides(self):
        parms = {}
        parms['cube'] = 'ybgroygogrgbrbyrbgobbgryyrywyrbggbgwrowoyobrwowywwwowo'
    
        cubeToRotate = 'ybgroygogrgbrbyrbgobbgryyrywyrbggbgwrowoyobrwowywwwowo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test161_bottomLayerNotSolvedMixedAllSides(self):
        parms = {}
        parms['cube'] = 'obbroogorrggybywbbrbyrrgwrggyyyggrgworwbyoboyowbwwwywo'
    
        cubeToRotate = 'obbroogorrggybywbbrbyrrgwrggyyyggrgworwbyoboyowbwwwywo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    def test162_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rwoyowgwbgrgobyrowyoygroobgowbbgrybrbgrrygygwwbwrwyoyb'
    
        cubeToRotate = 'rwoyowgwbgrgobyrowyoygroobgowbbgrybrbgrrygygwwbwrwyoyb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    def test301_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        cubeToRotate = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    #User tests which didn't pass first time.
    def test302_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test303_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
    
        cubeToRotate = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test304_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bbgooryowryygbgowgryboryobrywrrgbbrgobggygwrwoybwwoyww'
    
        cubeToRotate = 'bbgooryowryygbgowgryboryobrywrrgbbrgobggygwrwoybwwoyww'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test305_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
    
        cubeToRotate = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test501_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        cubeToRotate = 'ooyooorrgogwgbyrbygbworrorwrrbygbggybyrwyywwbbbywwwogg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test502_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        cubeToRotate = 'rgrgoowoyyrwwbbogoobbyrwborywgggrybrowgryywobbygrwygbw'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test503_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        cubeToRotate = 'wywgooooyggowbwrbogwobryywywbbrgoggybrwoyrrbrgybywrrgb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test504_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        cubeToRotate = 'wwrwobyoobgrobggbgyygrrorrorgowgrwyowbbyywbbwbgyowrgyy'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test505_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        cubeToRotate = 'ybrrooyoogybbbwbygwyogrowrrggbggwbggworrybowyowwywrybr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test506_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        cubeToRotate = 'oyywoowoyrgrybbbrbybborrwrrwbgggbggorrbyyoygggwowwywwo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test507_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        cubeToRotate = 'oygwooogywrrwbgrrgwbboryrrbwoyoggwwyrwgbygbbogybrwboyy'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test508_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        cubeToRotate = 'ryyyoogorgywgbggowoworrwbwobbbrgrbyyybgryoygorwwbwbwgr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test509_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        cubeToRotate = 'ooroobwoyyggrbwgyorworrgbrrbwgyggwyoygwbyrywbgbrowbbyw'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test510_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        cubeToRotate = 'yrrooborgbbbybbyowrogrrwrygybbggyoywrgywyoowwbgorwwwgg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test511_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        cubeToRotate = 'wgygoowoogoobbgbbybggrrrgbrrrbwgybbowoyyyyrwogwwrwwyyr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test512_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        cubeToRotate = 'ybrbowoygwbbgbwygbryoorrrrwbggygrgowyoyrywrygbgobwooww'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test513_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        cubeToRotate = 'oygoowbborgrrbwgrbgbworrwogrwyygboyrbrygyobbwywygwgwyo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test514_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        cubeToRotate = 'bygrowroywrrrbbbbwggowrwrrryowgggbbbgoyyyyogowwoowyybg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test515_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        cubeToRotate = 'ggrooyrgoboyrbbwbyrbbwrrboyowwwgwogywrggybrrwbygowygyo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test516_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        cubeToRotate = 'ogbgorryywwrbbwowwyybororrwywbbgogygobbgybwrryggowroyg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test517_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        cubeToRotate = 'yyywoorywbbwgbrogrobrwrbwwowybygbgwggrgryooorygbowrygb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test518_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        cubeToRotate = 'goboogoryrbwybwbgrrrbrroybgogwbggyygwbbrywrwywyoowwoyg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test519_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        cubeToRotate = 'yoooogwrbgyrybbybrwybrryyryobboggogrwrgoybowwbgrwwwgwg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test520_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        cubeToRotate = 'bgoyoggooboyobgggwrbrrrrbrgyywygbobrbwgoywowywbyrwywwr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    
    def test521_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        cubeToRotate = 'oybyowbbryyrrbgbbogyworwwwwggggggboorryrybyoowrywworbg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test522_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        cubeToRotate = 'yyorooywowbwybgyggoobwrbrrrwroogggybrwgbyyggbrbbrwowwy'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test523_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        cubeToRotate = 'orrooywyrywwobwybwbwrrrggrbwggogwoorgboyygygbbbgbwryyo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test524_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        cubeToRotate = 'rowwoygoyoyrbbgbbbggbrrrwwgrowbggwwoyyyyyrbggyworworbo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test525_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        cubeToRotate = 'rooooyybbworgbyywobwgrrywgrooybgwggoybwbyggybbrrrwrwwg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test526_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        cubeToRotate = 'gggboowryywogbgrowwboyrbgrbywwogrobrgyboygrrrbwbwwyyyo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test527_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        cubeToRotate = 'rryyoogwoborgbwyyowyoorrbrrgbwwgbygowogwybbbrygbywrggw'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test528_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        cubeToRotate = 'yrbgorrobygrwbbrogyyboryrwoogoggwwywwrbryogbogwwbwygby'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test529_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        cubeToRotate = 'owyooggogboowbgoyowryyrrybrryggggwwrgybbybyrrwwwbwobrb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test530_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        cubeToRotate = 'wrooowoobwwbbbgybryygorywryygrrgyoggrboryggbbwwrywogwb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test531_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        cubeToRotate = 'oybgoobyroyywboggyrygbrbrwbowwrgrrgyyggbybgrwoowowwwrb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test532_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        cubeToRotate = 'woorobobggrywbwygobgborobwgwrrbggrybryrbyyggwyyoowwyrw'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test533_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        cubeToRotate = 'rwrroowrgyooybyywowwrgrryoogbwbgywwgyrbyybbgbrgoowbggb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test534_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        cubeToRotate = 'boryoryoyboowbbgbwggyrrwryobwoggrbggrrwbywyywogrywowbg'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test535_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        cubeToRotate = 'bbggoyobgygoobowbwwgywrgbroobyygowrybwbryrrwrgyrywogwr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test536_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        cubeToRotate = 'wgggobrbbyybobbowgoygrrywowoobrgrgryygwyybrwrbwywwoogr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test537_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        cubeToRotate = 'wgbboywbbwogobyyboyrggrwyogororgroggygryybbwrrwrowywwb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test538_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        cubeToRotate = 'oryyogbwworrrbyrgbbbobrowwygygbgogrrwwwgybywbyogyworgo'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    
    def test539_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        cubeToRotate = 'yrbroorborwobbogyrgygwrowywywbggwogwrbwbygoyygryrwobgb'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
    

        
        
    def test540_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        cubeToRotate = 'oogooywyrywbbbwggbwrgbryyobowbogbogoybrgyrwwrgrwywrygr'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
    def test541_bottomLayerMixedtest(self):
        parms = {}
        parms['cube'] = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        cubeToRotate = 'oyoboobwwggowbbryybrgorbrggyybwgrywwryygyrwowrggrwboob'
        groundTrue = 'yyyborooogbbbbgbbbyoyyrgrrrbrgogogggryogyyrrowwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)     
        self._checkComparison(cubeToRotate,groundTrue,result)
        
        

