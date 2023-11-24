import unittest
import problem6

class FreewayTest(unittest.TestCase):
    def setUp(self):
        self._freeway = problem6.Freeway(600, 800)

    def test_initial_height_and_width_is_correct(self):
        self.assertEqual(self._freeway._width, 600)
        self.assertEqual(self._freeway._height, 800)

    def test_left_chicken_is_on_the_bottomleft_of_the_screen(self):
        coordinate = self._freeway.draw_left_chicken()
        self.assertTrue(coordinate[0] < (self._freeway._width) / 2)

    def test_right_chicken_is_on_the_bottomright_of_the_screen(self):
        coordinate = self._freeway.draw_right_chicken()
        self.assertTrue(coordinate[0] > (self._freeway._width) / 2)

    def test_left_chicken_is_moved_up_when_call_the_function(self):
        coordinate = self._freeway.move_left_chicken_up()
        self.assertTrue(coordinate[1] > (self._freeway._height) / 2)

    def test_left_chicken_is_moved_up_everytime_when_call_the_function(self):
        coordinate_1 = self._freeway.move_left_chicken_up()
        coordinate_2 = self._freeway.move_left_chicken_up()
        coordinate_3 = self._freeway.move_left_chicken_up()
        coordinate_4 = self._freeway.move_left_chicken_up()
        self.assertTrue(coordinate_4[1] == 0)

    def test_left_chicken_is_moved_up_without_limit(self):
        coordinate_1 = self._freeway.move_left_chicken_up()
        coordinate_2 = self._freeway.move_left_chicken_up()
        coordinate_3 = self._freeway.move_left_chicken_up()
        coordinate_4 = self._freeway.move_left_chicken_up()
        coordinate_5 = self._freeway.move_left_chicken_up()
        self.assertTrue(coordinate_5[1] < 0)



if __name__ == '__main__':
    unittest.main()
