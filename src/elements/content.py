from .element import Element
from .table import Table


class Content(Element):

    def __init__(
            self,
            title: str,
            changes: list,
            conclusion: list,
            ideas: list,
            table: Table
    ):
        super().__init__()
        self.content = self._formed_title(title) \
                       + self._formed_note("Изменения:", changes) \
                       + self._formed_table(table) \
                       + self._formed_note("Выводы:", conclusion) \
                       + self._formed_note("Идеи:", ideas)

    @staticmethod
    def _formed_title(title: str):
        return f"""<div class="title primary">{title}</div>"""

    @staticmethod
    def _formed_note(name: str, list_: list) -> str:
        result = "<div class='block__note'>"
        result += f"""<div class='body2'>{name}</div>\n"""
        result += "<div class='body1'>\n"
        result += "<ul class='list'>\n"
        for c in list_:
            result += f"""<li>{c}</li>"""
        result += "</ul>\n"
        result += "</div>\n"
        result += "</div>\n"
        return result

    @staticmethod
    def _formed_table(table: Table):
        result = "<div class='block__note'>\n"
        result += "<div class='body2'>Результат</div>\n"
        result += "<details class='body1'>\n"
        result += "<summary>Таблица</summary>\n"
        result += str(table) + "\n"
        result += "</details>\n"
        result += "</div>\n"
        return result
