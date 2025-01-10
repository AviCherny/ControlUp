import logging

import requests
from playwright.sync_api import Page, Locator

from ControlUp.utils.utils import log_message, take_screenshot, LogLevel
from ControlUp.utils.http_enums import HttpStatusCode, HttpMethod
from ControlUp.utils.validation_api import validate_airport_count, validate_airport_name, validate_airport_distance, \
    validate_status_code


class BasePage:
    def __init__(self, page: Page=None):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def safe_execute(self, action, action_name: str, *args):
        """
        Wrapper to safely execute an action with logging and failure handling.
        Captures a screenshot and attaches it to Allure if the action fails, without saving it locally.
        """
        try:
            log_message(self.logger, f"Executing action: {action_name} with arguments: {args}", LogLevel.INFO)
            action(*args)  # Call the action with unpacked arguments
        except Exception as e:
            log_message(self.logger, f"Action failed: {action_name}. Error: {str(e)}", LogLevel.ERROR)
            take_screenshot(self.page, action_name)
            raise

    def safe_api_call(self, method: HttpMethod, url: str, validate_status=True, expected_status=HttpStatusCode.OK, **kwargs):
        """
        Wrapper to safely execute api request with logging and attach to allure
        """
        try:
            log_message(self.logger, f"API Call: {method} -> {url}", LogLevel.INFO)
            response = requests.request(method.value, url, **kwargs)
            response.raise_for_status()

            if validate_status:
                validate_status_code(response, expected_status, message="Status code mismatch")

            log_message(self.logger, f"Success: {response.status_code}", LogLevel.INFO)
            return response
        except requests.exceptions.RequestException as e:
            log_message(self.logger, f"API Error: {str(e)}", LogLevel.ERROR)
            raise

    def navigate_to(self, url: str):
        self.safe_execute(self.page.goto, "navigate_to", url)

    def click_element(self, locator: Locator):
        self.safe_execute(locator.click, "click_element")

    def type_text(self, locator: Locator, text: str):
        self.safe_execute(locator.fill, "type_text", text)

    def assert_with_context(self, actual, expected, message, screenshot_name="assertion_failure"):
        """
        safe assert if fail log and screenshot will be attached to allure
        """
        try:
            assert actual == expected, message
        except AssertionError as e:
            log_message(self.logger, f"Assertion failed: {message}", LogLevel.ERROR)
            take_screenshot(self.page, screenshot_name)
            raise e





