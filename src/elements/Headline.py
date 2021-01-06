from .Element import Element


class Headline(Element):

    def __init__(self, headline: str):
        super().__init__()
        self.content = self._formed_headline(headline)

    @staticmethod
    def _formed_headline(headline: str) -> str:
        return f"""<div class='headline primary'>{headline}</div>"""
