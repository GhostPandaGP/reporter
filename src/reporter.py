import pathlib
import shutil
from bs4 import BeautifulSoup


class Reporter:

    def __init__(self):
        self.root = pathlib.Path(__file__).parent.parent
        self.path_files = self.root / "files"
        self.dir_report = None
        self.current_report = None
        self.soup = None

    def create_reports(self, name: str = "reports"):
        """Создает папку с отчетами по шаблону

        Args:
            name: папка, в которой будут хранится отчеты

        Returns:

        """
        self.dir_report = self.root / name
        if self.dir_report.exists():
            raise FileExistsError("This reports dir already exist!")
        shutil.copytree(self.path_files, self.dir_report)

    def add_report(self, name: str = "report1"):
        """Добавление отчета.

        Args:
            name: имя отчета, который будет добавлен в текущую папку с отчетами
            Добавление происходит согласно template.html

        Returns:

        """
        self.current_report = self.dir_report / (name + ".html")
        if self.current_report.exists():
            raise FileExistsError("This report already exist!")
        shutil.copy(self.dir_report / "template.html", self.current_report)
        self.soup = BeautifulSoup(self._get_content(), 'html.parser')

    def set_report_dir(self, name: str):
        """Установить папку с отчетами

        Args:
            name: путь к папке с отчетами

        Returns:

        """
        name = self.root / name
        if name.exists():
            self.dir_report = name
        else:
            raise FileExistsError("This path is not exist!")

    def set_report(self, name: str):
        """Устанавливает текущий отчет, в установленной папке

        Args:
            name: имя html файла в self.dir_report

        Returns:

        """
        if self.dir_report is None:
            raise FileNotFoundError("Reports folder is not set!")
        name = pathlib.Path(self.dir_report / (name + ".html"))
        if name.exists():
            self.current_report = name
        else:
            raise FileExistsError("This name is not exist in reports folder!")
        self.soup = BeautifulSoup(self._get_content(), 'html.parser')

    def get_list_reports(self) -> list:
        return [path.name.split(".")[0] for path in self.dir_report.glob("*.html")
                if path.name not in ["index.html", "template.html"]]

    def add_element_to_end(self, element):
        """Добавляет элемент в конец выбранного отчета

        Args:
            element: элемент, который добавляется в конец. Это может:
            Headline, Content

        Returns:

        """
        if self.soup is None:
            raise FileNotFoundError("Current report not selected or added!"
                                    " Use method .set_report or method .add_report!")
        self.soup.select_one('.block1 > .container').append(str(element))
        with open(self.current_report, mode="r+") as f:
            f.write(str(self.soup.prettify()).replace("&lt;", "<").replace("&gt;", ">"))

    def _get_content(self):
        if self.current_report is None:
            raise FileNotFoundError("No report selected!"
                                    " Please install the report using the method set_report!")
        with open(self.current_report) as f:
            string = f.read()
        return string
