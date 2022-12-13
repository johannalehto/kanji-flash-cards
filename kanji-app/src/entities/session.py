class Session:
    """Class for storing points of each round of cards"""

    def __init__(self):
        """Class constructor to create a new session
        Args:
            _session_points(int): Stores the points of each session
        """
        self._session_points = 0

    def add_point(self):
        self._session_points += 1

    def session_points(self):
        return self._session_points
