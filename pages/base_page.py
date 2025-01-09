import logging

from playwright.sync_api import Page, Locator

from ControlUp.utils.utils import log_message, take_screenshot, LogLevel


class BasePage:
    def __init__(self, page: Page):
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

    def navigate_to(self, url: str):
        self.safe_execute(self.page.goto, "navigate_to", url)

    def click_element(self, locator: Locator):
        self.safe_execute(locator.click, "click_element")

    def type_text(self, locator: Locator, text: str):
        self.safe_execute(locator.fill, "type_text", text)


