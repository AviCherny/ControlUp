from playwright.async_api import Page

from ControlUp.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.inventory_item = self.page.locator("[data-test='inventory-item']")

    def get_all_items(self):
        return self.inventory_item.count()


