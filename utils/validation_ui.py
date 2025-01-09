class AppValidation:

    def __init__(self, all_pages):
        self.login_page, self.inventory_page = all_pages

    def validate_inventory_items(self, expected_items):
        all_inventory_items = self.inventory_page.get_all_items()
        assert all_inventory_items == expected_items, f"Expected {expected_items}, but got {all_inventory_items}."

    def validate_cart_badge_amount(self, expected_items):
        cart_badge_amount = self.inventory_page.get_cart_badge_displayed_amount()
        assert int(cart_badge_amount) == expected_items, f"Expected {expected_items}, but got {cart_badge_amount}."
