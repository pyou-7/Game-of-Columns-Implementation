
class Freeway:
    #initiate the game basics
    def __init__(self, width, height):
        '''
        self._width is equal to the game width, and self._height
        is equal to the game height. self._frac_move_up is the
        fraction of height that the chicken move up when the move
        up function is called.
        '''
        self._width = width
        self._height = height
        self._frac_move_up = 1

    # draw the leftbottom chicken
    def draw_left_chicken(self) -> tuple:
        '''
        frac_width is that left chicken occupies 1/3 of the screen width.
        Use frac_width times width get the pixel x coordinate. Y coordinate
        is just the height of the screen being the bottommost position
        without the consideration of the graphical outputs.
        '''
        frac_width = (self._width / 3) / self._width
        center_x = frac_width * self._width
        center_y = self._height
        return (center_x, center_y)

    # draw the rightbottom chicken
    def draw_right_chicken(self) -> tuple:
        '''
        frac_width is that right chicken occupies 2/3 of the screen width.
        Use frac_width times width get the pixel x coordinate. Pixel y
        coordinate is just the height of the screen being the bottommost
        position without the consideration of the graphical outputs.
        '''
        frac_width = (self._width / 3 * 2) / self._width
        center_x = frac_width * self._width
        center_y = self._height
        return (center_x, center_y)

    # move the left chicken up few pixels
    def move_left_chicken_up(self) -> tuple:
        '''
        The pixel x coordinate is unchanged every time. The pixel y
        coordinate is changing every time this function is called.
        I divide the screen height by 4 and each fraction times the
        width is the length that the chicken being moved up. the
        varible self._frac_move_up will add one every time this function
        is called.
        '''
        frac_width = (self._width / 3) / self._width
        center_x = frac_width * self._width
        frac_height = (self._height / 4 * self._frac_move_up) / self._height
        center_y = self._height - frac_height * self._height
        self._frac_move_up += 1
        return (center_x, center_y)
