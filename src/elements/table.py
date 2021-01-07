from .element import Element
import pandas as pd


class Table(Element):

    def __init__(self, content: dict):
        super().__init__()
        self.content = self._formed_table(content)

    @staticmethod
    def _formed_table(content: dict) -> str:
        df = pd.DataFrame.from_dict(content)
        result = df.to_html(index_names=False, classes="table")
        return result
