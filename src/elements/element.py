class Element:

    def __init__(self):
        self.content = None

    def __str__(self):
        if self.content is None:
            raise ValueError("Content is none!")
        return str(self.content)
