class Session:
    def __init__(self):
        self._session_points = 0
    
    def add_point(self):
        self._session_points += 1

    def session_points(self):
        return self._session_points

    