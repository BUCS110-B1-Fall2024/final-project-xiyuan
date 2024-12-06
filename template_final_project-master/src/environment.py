class Environment:
    def __init__(self, width, height, events=None):
        # Initializes the environment
        # Args:
        # - width (int): Width of the environment
        # - height (int): Height of the environment
        # - events (list): List of dynamic events like weather changes
        self.width = width
        self.height = height
        self.events = events if events else []

    def add_event(self, event):
        # Adds a dynamic event to the environment
        self.events.append(event)

    def get_events(self):
        # Returns a list of all active events
        return self.events