from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by moving.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Arg:
        type (int): Number of scoreboard (1 or 2)

    Attributes:
        _type (int): Associated with the argument to allow one scoreboard per player to be made.
        _points (int): The points earned in the game.
    """
    def __init__(self, type):
        super().__init__()
        self._type = type
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")