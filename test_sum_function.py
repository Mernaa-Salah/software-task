import unittest
from sum_function import sum

class test_sum_function(unittest.TestCase):

  def test_sum(self):
    self.assertEqual(sum(0, 0), 0)
    self.assertEqual(sum(-10, 5), -5)
    self.assertEqual(sum(10, 20), 30)
    self.assertEqual(sum(-10, -20), -30)

if __name__ == '__main__':
    unittest.main()
