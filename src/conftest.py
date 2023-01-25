# グローバルで利用する共通のfixtureを記載

import pytest


@pytest.fixture
def csv_file():
    yield 'csv file!!!'

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os_name')

