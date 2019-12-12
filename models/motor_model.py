
class MotorModel:

    def __init__(self, name, description, main_image, images=[], videos=[], specifications=[]):
        self.name = name
        self.description = description
        self.main_image = main_image
        self.images = images
        self.videos = videos
        self.specifications = specifications