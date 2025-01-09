from playwright.async_api import Page

from ControlUp.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = self.page.locator("")

