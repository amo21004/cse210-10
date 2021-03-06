import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long cycle that grows as it moves.
    
    The responsibility of Cycle is to move itself.

    Arg:
        type (int): Number of cycle (1 or 2)

    Attributes:
        _segments (list): Trail of the cycle.
        _type (int): Associated with the argument to allow more than one cycle to be made.
    """
    def __init__(self, type):
        super().__init__()
        self._segments = []
        self._type = type
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
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
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")

            if self._type == 1:
                segment.set_color(constants.GREEN)
            else:
                segment.set_color(constants.RED)
            
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._type == 1:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
        else:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 4)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            
            if self._type == 1:
                color = constants.GREEN
            else:
               color = constants.RED 
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)      