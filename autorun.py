from src.reporter import Reporter
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
    # reporter.create_reports("reports1")
