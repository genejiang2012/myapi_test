import pytest
from py.xml import html


def pytest_html_report_title(report):
    report.title = "CC API Testing"