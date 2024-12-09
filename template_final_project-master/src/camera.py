class Camera:
    def __init__(self, x, y, zoom=1.0):
        self.x = x
        self.y = y
        self.zoom = zoom

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def set_zoom(self, zoom_level):
        self.zoom = zoom_level

    def rotate(self, angle):
        # Apply rotation to camera view (if applicable)
        pass

    def get_position(self):
        return self.x, self.y

    def get_zoom(self):
        return self.zoom