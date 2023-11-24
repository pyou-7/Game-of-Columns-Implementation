import unittest
import math

def reverse_two(function: 'function') -> 'function':
    def reverse_function(a, b):
        return function(b, a)
    return reverse_function

def compose(function_1: 'function', function_2: 'function') -> 'function':
    def compose_functions(value):
        return function_1(function_2(value))
    return compose_functions

def accumulator(function: 'function') -> 'function':
    def accumulated_functions(a, b):
        total = b
        for i in a:
            total = function(total, i)
        return total
    return accumulated_functions


class HigherOrderFunctionsTest(unittest.TestCase):
    def test_returns_a_function_with_parameters_reversed(self):
         reverse_divide = reverse_two(divide)
         reverse_minus = reverse_two(minus)
         reverse_multiple = reverse_two(multiple_calculation)
         self.assertEqual(reverse_divide(8, 2), 0.25)
         self.assertEqual(reverse_minus(4, 20), 16.0)
         self.assertEqual(reverse_multiple(4, 2), -4)

    def test_returns_a_function_with_composition_of_two_functions(self):
         square_of_length = compose(square, length)
         squareroot_of_length = compose(squareroot, length)
         self.assertEqual(square_of_length('boo'), 9)
         self.assertEqual(square_of_length([1,2,3,4,5]), 25)
         self.assertEqual(squareroot_of_length((1,2,4,5)), 2)

    def test_returns_a_function_accumulates_the_sequence(self):
         sum_all = accumulator(add)
         product_all = accumulator(multiply)
         divide_all = accumulator(divide)
         self.assertEqual(sum_all([1, 2, 3, 4, 5], 0), 15)
         self.assertEqual(product_all((5, 4, 3, 2), 1), 120)
         self.assertEqual(divide_all((10, 5, 2), 100), 1)


def divide(a, b):
    return a / b

def minus(a, b):
    return a - b

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def multiple_calculation(a, b):
    return a + b / a - b * a

def square(n):
    return n * n

def squareroot(n):
    return math.sqrt(n)

def length(n):
    return len(n)

         
if __name__ == '__main__':
    unittest.main()
