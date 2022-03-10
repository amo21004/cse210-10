import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlCycle1Action(Action):
    """
    An input action that controls the first cycle.
    
    The responsibility of ControlCycle1Action is to get the direction and move the cycle's head and to create and
    make the cycle's trail grow then to add points as the trail grows.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        collision = script.get_actions('update')[1]

        if collision._is_game_over:
            return

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        cycle = cast.get_first_actor("cycles")
        cycle.turn_head(self._direction)

        if self._keyboard_service.is_key_down('a') or self._keyboard_service.is_key_down('d') or self._keyboard_service.is_key_down('w') or self._keyboard_service.is_key_down('s'):
            cycle.grow_trail(1)
            score = cast.get_first_actor("scores")
            score.add_points(1)