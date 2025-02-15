import pytest
import os
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cwd = os.getcwd().split("src")
    if not os.path.exists(f"{cwd[0]}/Reports/UI"):
        os.makedirs(f"{cwd[0]}/Reports/UI")
    config.option.htmlpath = f"{cwd[0]}/Reports/UI/UI - {datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html"

    config.option.env = config.getoption("--environment")

    global ENV
    ENV = config.option.env


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name")
    parser.addoption("--environment", action="store", default="local", help="Type in environment name")
    parser.addoption("--headless", action="store", help="Run in headless mode")


@pytest.fixture(scope="class")
def init_driver(request):
    browser = request.config.getoption("--browser")
    # environment = request.config.getoption("--environment")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if headless == "True":
            chrome_options.headless = True
            chrome_options.add_argument("window-size=3840,2160")
            chrome_options.add_argument("ignore-certificate-errors")
        else:
            chrome_options.add_argument("window-size=1920,1080")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    if browser == "edge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        if headless == "True":
            edge_options.headless = True
            edge_options.add_argument("disable-gpu")
            edge_options.add_argument("window-size=3840,2160")
            edge_options.add_argument("ignore-certificate-errors")
        else:
            edge_options.add_argument("window-size=1920,1080")
        web_driver = Edge(EdgeChromiumDriverManager().install(), options=edge_options)

    if browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless == "True":
            firefox_options.headless = True
            firefox_options.add_argument("window-size=3840,2160")
            firefox_options.add_argument("ignore-certificate-errors")
        else:
            firefox_options.add_argument("window-size=1920,1080")
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=firefox_options)

    print(f"=========TEST CONFIGURATION=========")
    print(f"Browser     = {browser}")
    print(f"Environment = {ENV}")
    print(f"Headless    = {headless}")
    print(f"====================================")

    request.cls.driver = web_driver

    yield

    # delete geckodriver.log file if it exists
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")

    web_driver.close()
    web_driver.quit()
