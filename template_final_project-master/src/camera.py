class Camera:
    def __init__(self, x, y, zoom=1.0):
        # Initializes the camera object
        # Args:
        # - x (int): Starting x coordinate of the camera
        # - y (int): Starting y coordinate of the camera
        # - zoom (float): Current zoom level (default 1.0)
        self.x = x
        self.y = y
        self.zoom = zoom

    def move(self, dx, dy):
        # Moves the camera by dx and dy
        self.x += dx
        self.y += dy

    def set_zoom(self, zoom_level):
        # Sets the zoom level of the camera
        self.zoom = zoom_level
