from ControlUp.utils.utils import log_message, take_screenshot, LogLevel
from pages.base_page import BasePage


class AppValidation(BasePage):

    def __init__(self, all_pages):
        self.login_page, self.inventory_page = all_pages
        super().__init__(self.inventory_page.page)  # Pass the page to BasePage

    def validate_inventory_items(self, expected_items):
        all_inventory_items = self.inventory_page.get_all_items()
        take_screenshot(self.inventory_page.page,"screenshot before assert")
        self.assert_with_context(
            all_inventory_items,
            expected_items,
            f"Expected {expected_items}, but got {all_inventory_items}.",
            "validate_inventory_items_failure"
        )

    def validate_cart_badge_amount(self, expected_items):
        cart_badge_amount = self.inventory_page.get_cart_badge_displayed_amount()
        take_screenshot(self.inventory_page.page, "screenshot before assert")
        self.assert_with_context(
            int(cart_badge_amount),
            expected_items,
            f"Expected {expected_items}, but got {cart_badge_amount}.",
            "validate_cart_badge_amount_failure"
        )
