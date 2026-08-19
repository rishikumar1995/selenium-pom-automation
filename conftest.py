import pytest
import os
import logging
from selenium import webdriver
from config.config import ENV_URLS

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on"
    )

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/automation.log")
    ]
)

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    logging.info(f"Starting {browser} browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    yield driver

    logging.info("Closing browser")
    driver.quit()

@pytest.fixture
def base_url(request):
    env = request.config.getoption("--env")

    if env in ENV_URLS:
        return ENV_URLS[env]

    raise ValueError(f"Unsupported environment: {env}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots",exist_ok=True)

            driver.save_screenshot(
                f"screenshots/{item.name}.png"
            )