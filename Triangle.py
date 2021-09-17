"""
@author: kavishsanghvi
@purpose: to demonstrate a simple python program to classify triangles
"""

def classifyTriangle(a,b,c):
    """ classify different types of triangle

        :param a: The side of a triangle
        :type a: float
        :param b: The side of a triangle
        :type b: float
        :param c: The side of a triangle
        :type c: float
        :rtype: str
        :return: str
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
        
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if ((b + c) < a) or ((a + c) < b) or ((a + b) < c):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if (a * a) + (b * b) == (c * c) or (b * b) + (c * c) == (a * a) or (c * c) + (b * b) == (a * a):
        return 'Right'

    if a == b and b == c and a == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'