"""
@author: kavishsanghvi
@purpose: to demonstrate a simple unittest implementation
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testRightTriangle(self): 
        """ test classify triangle function

            :rtype: None
            :return: None
        """

        self.assertEqual(classifyTriangle(3, 4, 5),'Right')
        self.assertEqual(classifyTriangle(5, 3, 4),'Right')
        
    def testEquilateralTriangle(self): 
        """ test classify triangle function

            :rtype: None
            :return: None
        """

        self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral')
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')

    def testIsoscelesTriangle(self):
        """ test classify triangle function

            :rtype: None
            :return: None
        """

        self.assertEqual(classifyTriangle(150, 155, 155), 'Isosceles')
        self.assertEqual(classifyTriangle(2, 3, 3), 'Isosceles')
        
    def testScaleneTriangle(self):
        """ test classify triangle function

            :rtype: None
            :return: None
        """

        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene')
        self.assertEqual(classifyTriangle(6, 5, 4), 'Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()