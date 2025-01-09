from playwright.async_api import Page

from ControlUp.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.inventory_item = self.page.locator("[data-test='inventory-item']")
        self.backpack_item = self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.badge_locator = self.page.locator("[data-test='shopping-cart-badge']")

    def get_all_items(self):
        return self.inventory_item.count()

    def add_first_inventory_item(self):
        self.click_element(self.backpack_item)

    def get_cart_badge_displayed_amount(self):
        return self.badge_locator.text_content()



