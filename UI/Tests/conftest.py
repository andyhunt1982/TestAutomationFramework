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
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = f"reports/{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html"


@pytest.fixture(params=["chrome", "edge"], scope="class")
def init_driver(request):
    ######################### AMEND THIS VALUE TO RUN IN HEADLESS MODE #########################
    HEADLESS = True
    ######################### AMEND THIS VALUE TO RUN IN HEADLESS MODE #########################

    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if HEADLESS:
            chrome_options.headless = True
            chrome_options.add_argument("window-size=3840,2160")
            chrome_options.add_argument("ignore-certificate-errors")

        else:
            chrome_options.add_argument("window-size=1920,1080")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    if request.param == "edge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        if HEADLESS:
            edge_options.headless = True
            edge_options.add_argument("disable-gpu")
            edge_options.add_argument("window-size=3840,2160")
            edge_options.add_argument("ignore-certificate-errors")
        else:
            edge_options.add_argument("window-size=1920,1080")
        web_driver = Edge(EdgeChromiumDriverManager().install(), options=edge_options)

    if request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if HEADLESS:
            firefox_options.headless = True
            firefox_options.add_argument("window-size=3840,2160")
            firefox_options.add_argument("ignore-certificate-errors")
        else:
            firefox_options.add_argument("window-size=1920,1080")
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=firefox_options)

    request.cls.driver = web_driver

    yield

    web_driver.close()
    web_driver.quit()
