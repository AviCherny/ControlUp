import pytest

from ControlUp.utils.config import VALID_CREDENTIALS


@pytest.mark.parametrize(
    "items",
    [6]
)
@pytest.mark.login
def test_successful_login_and_verify_items_displayed(setup_login_page, validation, items):
    login_page = setup_login_page
    login_page.login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])
    validation.validate_inventory_items(expected_items=items)
