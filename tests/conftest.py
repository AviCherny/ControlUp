import logging

import pytest

from ControlUp.pages.inventory_page import InventoryPage
from ControlUp.pages.login_page import LoginPage
from ControlUp.utils.config import BASE_URL, VALID_CREDENTIALS
from ControlUp.utils.utils import log_message, LogLevel
from ControlUp.utils.validation_ui import AppValidation

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

@pytest.fixture
def setup_logged_in_page(setup_playwright):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(BASE_URL)
    return login_page.login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])


@pytest.fixture
def setup_all_pages(setup_playwright):
    login_page = LoginPage(setup_playwright)
    inventory_page = InventoryPage(setup_playwright)
    yield login_page, inventory_page

@pytest.fixture
def validation(setup_all_pages):
    yield AppValidation(setup_all_pages)
