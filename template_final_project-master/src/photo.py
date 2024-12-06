class Photo:
    def __init__(self, filename, timestamp, location):
        # Initializes a photo object
        # Args:
        # - filename (str): Path to the saved photo file
        # - timestamp (str): Time when the photo was taken
        # - location (tuple): (x, y) coordinates of the camera when photo was taken
        self.filename = filename
        self.timestamp = timestamp
        self.location = location
