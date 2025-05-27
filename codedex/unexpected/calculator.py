import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class TestCalculator(unittest.TestCase):

  # Setup method: New Calculator instance before each test
  def setUp(self):
    self.calculator = Calculator()

  # Teardown method: Clean up resources after each test
  def tearDown(self):
    self.calculator = None

  def test_addition(self):
    self.assertEqual(self.calculator.add(3, 5), 8)

  def test_subtraction(self):
    self.assertEqual(self.calculator.subtract(10, 4), 6)

if __name__ == '__main__':
  unittest.main()