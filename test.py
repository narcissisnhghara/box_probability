import unittest
from box.box_class import Box

class TestBox(unittest.TestCase):
    
    def setUp(self):

        self.iters = 1000000
        self.box = Box()

    def test_print_results(self):

        self.box.print_results(self.iters)


if __name__ == '__main__':

    unittest.main()
