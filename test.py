import unittest
from box.box_class import Box

class TestBox(unittest.TestCase):
    def setUp(self):

        self.iters = 100000
        self.num_balls=10000
        self.box = Box(num_balls=self.num_balls)

    def test_print_results(self):

        self.box.print_results(self.iters)


if __name__ == '__main__':

    unittest.main()
