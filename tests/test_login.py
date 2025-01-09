import pytest

from ControlUp.utils import validation
from ControlUp.utils.config import VALID_CREDENTIALS
from ControlUp.utils.validation import AppValidation


@pytest.mark.parametrize(
    "items",
    [6]
)
@pytest.mark.login
def test_successful_login_and_verify_items_displayed(setup_login_page, validation, items):
    login_page = setup_login_page
    login_page.login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])
    validation.validate_items(expected_items=items)





@pytest.mark.regression
@pytest.mark.parametrize(
    "email, password, expected_error",
    [
        ("wrongemail@example.com", "validpassword123", "Login failed!"),  # Wrong email
        ("validuser@example.com", "wrongpassword", "Login failed!"),      # Wrong password
        ("", "validpassword123", "Login failed!"),                        # No email
        ("validuser@example.com", "", "Login failed!"),                   # No password
    ],
)
def test_unsuccessful_login(setup_login_page, email, password, expected_error):
    login_page = setup_login_page

    with pytest.raises(Exception) as exc_info:
        login_page.login(email, password)

    assert expected_error in str(exc_info.value)