#!/usr/bin/python
# -*- coding: utf-8 -*-

#pyramidTest.py
import unittest
import pyramid

"""
各テストを実行するとき ex) python pyramidTest.py pyramidTestCase.testdouble
"""

class pyramidTestCase(unittest.TestCase):

    def testsingle(self):
        self.assertEqual("*", pyramid.returnAster(1))

    def testdouble(self):
        self.assertEqual("*\n**", pyramid.returnAster(2))

if __name__ == "__main__":

    suite = unittest.TestSuite(map(pyramidTestCase, ["testdouble"]))
    #こちらでも大丈夫
#    suite = unittest.TestSuite()
#    suite.addTest(pyramidTestCase('testsingle'))
    unittest.TextTestRunner(verbosity=2).run(suite)

