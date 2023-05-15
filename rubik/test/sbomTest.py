'''
Created on Jan 17, 2023

@author: yinbo
'''
import unittest
import app


class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'yzc0129'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)

