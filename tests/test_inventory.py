
def test_add_item_to_cart_and_verify_cart_badge(setup_logged_in_page, validation):
    inventory_page = setup_logged_in_page
    inventory_page.add_first_inventory_item()
    validation.validate_cart_badge_amount(1)