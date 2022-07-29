import pytest
import os
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = f"reports/{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html"