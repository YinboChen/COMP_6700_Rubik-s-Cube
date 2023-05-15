'''
Created on Apr 5, 2023

@author: yinbo
'''
from unittest import TestCase
from rubik.view.solve import *
import rubik.model.cube as cube
from rubik.model.constants import *
import hashlib

# Create unittest for checking the hashToken from the solve

class hashTokenTest(TestCase):
    
    def test010_funcTest_solve_calRandomHashToken(self):
        parms = {}
        cubeList = []
        parms['cube'] = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        cubeToRotate = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        cubeList.append(cubeToRotate)
        result = solve(parms)
        solutions = result.get('solution')
        testResult = calRandomHashToken(cubeList, solutions)
        self.assertEqual(8, len(testResult)) 
        
    def test011_funcTest_solve_calRandomHashToken(self):
        parms = {}
        cubeList = []
        itemToTokenizeList = []
        parms['cube'] = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        cubeToRotate = 'yyroooooogyybbbbbbbygrrrrrroybggggggyrrgybooywwwwwwwww'
        cubeList.append(cubeToRotate)
        itemToTokenizeList.append(cubeToRotate)
        result = solve(parms)
        solutions = result.get('solution')
        itemToTokenizeList.append(solutions)
        itemToTokenizeList.append('yzc0129')
        stringToHash = ''.join(itemToTokenizeList)
        sha256Hash = hashlib.sha256()
        sha256Hash.update(stringToHash.encode())
        fullToken = sha256Hash.hexdigest()
        testResult = calRandomHashToken(cubeList, solutions)
        self.assertIn(testResult, fullToken)