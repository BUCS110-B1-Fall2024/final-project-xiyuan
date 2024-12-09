class Environment:
    def __init__(self, width, height, events=None):
        self.width = width
        self.height = height
        self.events = events if events else []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

    def display(self, screen):
        # Code to draw the environment and events (if applicable)
        pass