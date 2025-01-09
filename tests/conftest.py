import logging

import pytest

from ControlUp.pages.login_page import LoginPage
from ControlUp.utils.config import BASE_URL
from ControlUp.utils.utils import log_message, LogLevel

logger = logging.getLogger(__name__)

@pytest.fixture()
def setup_playwright(playwright, request):

    headed = request.config.getoption("--headed", default=False)
    browser = playwright.chromium.launch(headless=not headed)
    page = browser.new_page()
    try:
        yield page
    finally:
        log_message(logger, "Closing browser.", LogLevel.INFO)
        browser.close()

@pytest.fixture
def setup_login_page(setup_playwright):

    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(BASE_URL)
    log_message(logger, "Navigation to login page completed.", LogLevel.INFO)

    yield login_page
