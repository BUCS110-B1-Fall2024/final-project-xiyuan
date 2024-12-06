class Gallery:
    def __init__(self):
        # Initializes an empty gallery
        self.photos = []

    def add_photo(self, photo):
        # Adds a photo to the gallery
        self.photos.append(photo)

    def delete_photo(self, photo):
        # Deletes a photo from the gallery
        if photo in self.photos:
            self.photos.remove(photo)

    def get_photos(self):
        # Returns a list of all photos
        return self.photos
