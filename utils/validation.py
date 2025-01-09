class AppValidation:

    def __init__(self, all_pages):
        self.login_page, self.inventory_page = all_pages


    def validate_items(self, expected_items):
        all_inventory_items = self.inventory_page.get_all_items()
        assert all_inventory_items == expected_items, f"Expected {expected_items}, but got {all_inventory_items}."
