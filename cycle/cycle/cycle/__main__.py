import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # Create two snakes, gets their position and color
    snake_one = Snake(Point(int(constants.MAX_X - 650), int(constants.MAX_Y / 2)))
    snake_two = Snake(Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
    snake_one.set_color(constants.GREEN)
    snake_two.set_color(constants.RED)
    #snake_one_name = input("Please enter player 1 name: ")
    #snake_two_name = input("Please enter player 2 name: ")
    snake_one_name = "You"
    snake_two_name = "Opponent"
    snake_one.set_name(snake_one_name)
    snake_two.set_name(snake_two_name)


    # create the cast

    # player 1
    cast = Cast()
    score1 = Score()
    score1.add_points(5)
    score1.set_name(snake_one_name)
    cast.add_actor("snake_one", snake_one)
    cast.add_actor("score1", score1)
    score1.set_position(Point(constants.MAX_X+150, 10))

    # player 2
    score2 = Score()
    score2.add_points(5)
    score2.set_name(snake_two_name)
    cast.add_actor("snake_two", snake_two)
    cast.add_actor("score2", score2)
    score2.set_position(Point(constants.MAX_X-200, 10))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()