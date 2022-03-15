import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.credit import Credit


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._game_over_message = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_snake_tail(cast)
            self._handle_game_over(cast)

    def _handle_snake_tail(self, cast):
        """"Handles the snakes' tails

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        snake_one = cast.get_first_actor("snake_one")
        snake_two = cast.get_first_actor("snake_two")
        snake_one.snake_tail(self._is_game_over)
        snake_two.snake_tail(self._is_game_over)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        # Player 1 = "snake_one"    Player 2 = "snake_two"
        snake_one = cast.get_first_actor("snake_one")
        snake_two = cast.get_first_actor("snake_two")
        # head = snake.get_segments()[0]
        head_one = snake_one.get_head()
        head_two = snake_two.get_head()
        # segments = snake.get_segments()[1:]
        segments_one = snake_one.get_segments()[1:]
        segments_two = snake_two.get_segments()[1:]

        for segment_one in segments_one:
            if head_one.get_position().equals(segment_one.get_position()):
                score1.decrease_score()
                if score1.get_points() < 1:
                    self._is_game_over = True

            elif head_two.get_position().equals(segment_one.get_position()):
                score2.decrease_score()
                if score2.get_points() < 1:
                    self._is_game_over = True

        for segment_two in segments_two:
            if head_one.get_position().equals(segment_two.get_position()):
                score1.decrease_score()
                if score2.get_points() < 1:
                    self._is_game_over = True
            elif head_two.get_position().equals(segment_two.get_position()):
                score2.decrease_score()
                if score2.get_points() < 1:
                    self._is_game_over = True

            

           
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        if self._is_game_over:
            snake_one = cast.get_first_actor("snake_one")
            snake_two = cast.get_first_actor("snake_two")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            # gets segments for snake one and two
            segments_one = snake_one.get_segments()
            segments_two = snake_two.get_segments()

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            message.set_font_size(40)

            if score1.get_points() < 1 and score2.get_points() < 1:
                cast.add_actor("messages", message)
            elif score1.get_points() < 1:
                message.set_text(snake_two.get_name()+" wins!!!")
                cast.add_actor("messages", message)
            elif score2.get_points() < 1:
                message.set_text(snake_one.get_name()+" win!!!")
                cast.add_actor("messages", message)
            else:
                cast.add_actor("messages", message)

            for segment in segments_one:
                segment.set_color(constants.WHITE)
            #food.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)
            #food.set_color(constants.WHITE)

            credits = Credit()
            message.set_text_end(credits.getCredits())
            cast.add_actor("messages", message)
            