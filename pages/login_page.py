import allure
from pytest_playwright.pytest_playwright import page

from ControlUp.pages.base_page import BasePage
from playwright.sync_api import Page

from ControlUp.pages.inventory_page import InventoryPage
from ControlUp.utils.utils import log_message, LogLevel, take_screenshot


class LoginPage(BasePage):
    def __init__(self, page: Page):

        super().__init__(page)
        self.username_field = self.page.locator("[id = 'user-name']")
        self.password_field = self.page.locator("[id = 'password']")
        self.login_button = self.page.locator("[id = 'login-button']")

    @allure.step("login")
    def login(self, username: str, password: str):
        log_message(self.logger, "Performing login action", level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)
        try:
            return InventoryPage(self.page)
        except():
            log_message(self.logger, "Login failed!", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failure")
            raise Exception("Login failed!")