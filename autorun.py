from src.reporter import Reporter
from src.elements.table import Table
from src.elements.content import Content
import pathlib


if __name__ == '__main__':
    print("start")
    reporter = Reporter()
    reporter.set_report_dir(pathlib.Path(__file__).parent / "reports1")
    reporter.set_report("report1")
    # reporter.add_report("report1")
    # reporter.add_report("report3")
    print(reporter.get_list_reports())
    reporter.add_element_to_end("element")
    table = Table(
        {
            "key": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
            "clock": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        }
    )
    print(table)
    content = Content(
        ["change 1", "change 2"],
        ["conclusion 1"],
        ["idea 1", "idea 2"],
        table
    )
    reporter.add_element_to_end(content)
    # reporter.create_reports("reports1")
