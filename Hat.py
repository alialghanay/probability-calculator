import random

import random

class Hat:

    def __init__(self, **balls):
        """
        Initialize the Hat class with balls of different colors.
        The balls argument is a dictionary where keys are colors and values are the count of balls for each color.
        The contents list holds each ball as a color name.
        """
        self.__contents = []
        for ball, count in balls.items():
            self.__contents += [ball] * count
        if len(self.__contents) == 0:
            raise ValueError('No balls in the hat!')

    @property
    def contents(self):
        '''
        Getter for the contents property
        '''
        return self.__contents

    @contents.setter
    def contents(self, value):
        '''
        Setter for the contents property
        '''
        self.__contents = value

    def draw(self, num_balls):
        """
        Draw a number of balls randomly from the hat.
        If the number of balls requested exceeds the available balls, return all balls and empty the hat.
        """
        if num_balls >= len(self.__contents):
            drawn = self.__contents.copy()  # return all balls
            self.__contents.clear()  # empty the hat
            return drawn

        # Otherwise, draw the requested number of balls
        drawn = random.sample(self.__contents, num_balls)
        for ball in drawn:
            self.__contents.remove(ball)  # remove drawn balls from contents
        return drawn

    def __repr__(self):
        return f'Hat({self.contents})'
    
    def __str__(self):
        return f"""Hat with the following balls:
        {self.contents}"""