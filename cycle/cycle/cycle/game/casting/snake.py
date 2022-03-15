import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position):
        "Constructs a new instance of Snake."
        super().__init__()
        self._segments = []
        self._prepare_body(position)
        self._color = Color(255, 255, 255)
        self._name= ""

    def get_segments(self):
        """Creates segments of the snake.
        Returns:
            segments: The segments of the snake.
        """

        return self._segments

    def move_next(self):
        """Moves segments of the snake.
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Creates head of the snake.
        Returns:
            segments (head): The head of the snake.
        """
        return self._segments[0]

    def grow_tail(self, match):
        """Grows the snake as it moves.
        """
        tail = self._segments[-1]
        velocity = tail.get_velocity()
        offset = velocity.reverse()
        position = tail.get_position().add(offset)
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        self._segments.append(segment)

        if not match:
            segment.set_color(self._color)
        else:
            segment.set_color(constants.WHITE)

    def turn_head(self, velocity):
        """Turns the snake's head in four possible directions as it moves.
        """       
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, position):
        """Positions the snake body parts on the video with the snake color.
        """
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)

    # Return players' name
    def get_name(self):
        """Gets the names of the players (You and Opponent).
        Returns:
            name: The name of the player.
        """        
        return self._name

    # Store players' name
    def set_name(self, name):
        """Sets the names of the players (You and Opponent).
        """   
        self._name = name

    # Set snake color
    def set_color(self, color):
        """Sets the colors of the players (You and Opponent).
        """
        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)

    def snake_tail(self, game):  
        """Generates the tails of the players (You and Opponent).
        """
        tail = self._segments[-1]
        velocity = tail.get_velocity()
        offset = velocity.reverse()
        position = tail.get_position().add(offset)

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        if not game:
            segment.set_color(self._color)
        else:
            segment.set_color(constants.WHITE)
        self._segments.append(segment)