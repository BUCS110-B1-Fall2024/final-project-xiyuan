from src.camera import Camera
from src.gallery import Gallery
from src.environment import Environment
from src.photo import Photo
import time

class Controller:
    def __init__(self):
        # Initializes the controller with models
        self.camera = Camera(0, 0)
        self.gallery = Gallery()
        self.environment = Environment(1000, 1000)

    def move_camera(self, dx, dy):
        # Moves the camera in the virtual world
        self.camera.move(dx, dy)

    def set_camera_zoom(self, zoom_level):
        # Sets the camera zoom level
        self.camera.set_zoom(zoom_level)

    def take_photo(self):
        # Takes a photo and adds it to the gallery
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        location = (self.camera.x, self.camera.y)
        filename = f"photo_{timestamp.replace(':', '-')}.png"
        photo = Photo(filename, timestamp, location)
        self.gallery.add_photo(photo)
        return photo

    def list_gallery_photos(self):
        # Returns a list of all photos in the gallery
        return self.gallery.get_photos()

    def trigger_event(self, event_name):
        # Adds a dynamic event to the environment
        self.environment.add_event(event_name)