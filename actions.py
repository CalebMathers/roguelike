"""File that contains possible user actions"""


class Action:
    """Superclass used for any action"""
    pass


class EscapeAction(Action):
    """Subclass of action, used for presses of the Esc key"""
    pass


class MovementAction(Action):
    """Subclass of action, used for presses of movement keys"""

    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
