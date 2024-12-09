class Gallery:
    def __init__(self):
        self.photos = []

    def add_photo(self, photo):
        self.photos.append(photo)

    def delete_photo(self, photo):
        if photo in self.photos:
            self.photos.remove(photo)

    def get_photos(self):
        return self.photos

    def show_gallery(self, screen):
        # Code to display photos in the gallery on the screen
        pass