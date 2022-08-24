import pytest
import os
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cwd = os.getcwd().split("API")
    if not os.path.exists(f"{cwd[0]}/Reports"):
        os.makedirs(f"{cwd[0]}/Reports")
    config.option.htmlpath = f"{cwd[0]}/Reports/API - {datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name")
    parser.addoption("--environment", action="store", default="local", help="Type in environment name")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.env = config.getoption("--environment")

    global ENV
    ENV = config.option.env
