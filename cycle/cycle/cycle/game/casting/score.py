from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._name = ""
        self._points = 0
        #self.add_points(0)
        position = Point(1, 0)
        self.set_position(position)
        self.set_text(f"{self._name}: {self._points}")

        

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._name} score: {self._points}")

    def decrease_score(self):
        """reduces points for the user"""
        self._points = self._points - 1
        self.set_text(f"{self._name}: {self._points}")

    def get_points(self):
        """returns the users points
        """
        return self._points

    def set_name(self, name):
        """sets the player's name
        
        Args:
            name (name): gets the user name
        """
        self._name = name
        self.set_text(f"{self._name}: {self._points}")