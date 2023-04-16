import unittest
from fibonacciIterative import fibonacciIterative
from fibonacciRecursive import fibonacciRecursive

class TestFibonacci(unittest.TestCase):
    def test1Iterative(self):
        result = fibonacciIterative(1)
        self.assertEqual(result, 1)

    def test2Iterative(self):
        result = fibonacciIterative(2)
        self.assertEqual(result, 1)
        
    def test5Iterative(self):
        result = fibonacciIterative(5)
        self.assertEqual(result, 5)
        
    def test10Iterative(self):
        result = fibonacciIterative(10)
        self.assertEqual(result, 55)

    def test0Recursive(self):
        result = fibonacciRecursive(0)
        self.assertEqual(result, 0)

    def test2Recursive(self):
        result = fibonacciRecursive(2)
        self.assertEqual(result, 1)

    def test5Recursive(self):
        result = fibonacciRecursive(5)
        self.assertEqual(result, 5)
        
    def test10Recursive(self):
        result = fibonacciRecursive(10)
        self.assertEqual(result, 55)        

if __name__ == '__main__':
    unittest.main()