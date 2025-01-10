import allure

from enum import Enum

class LogLevel(Enum):
    INFO = "info"
    DEBUG = "debug"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

def take_screenshot(page, name: str = "screenshot"):
    """
    Captures a screenshot using the provided driver and attaches it to Allure.
    Does not save the screenshot locally unless required.
    """
    try:
        # Capture the screenshot as binary data
        screenshot_data = page.screenshot(type="png")

        # Attach the screenshot to Allure
        allure.attach(
            screenshot_data,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

        return screenshot_data
    except Exception as e:
        return None



def log_message(logger, message: str, level: LogLevel = LogLevel.INFO, attach_to_allure: bool = True):
    """
    Logs a message and level
    """
    if level == LogLevel.INFO:
        logger.info(message)
    elif level == LogLevel.DEBUG:
        logger.debug(message)
    elif level == LogLevel.WARNING:
        logger.warning(message)
    elif level == LogLevel.ERROR:
        logger.error(message)
    elif level == LogLevel.CRITICAL:
        logger.critical(message)

    if attach_to_allure:
        allure.attach(
            message,
            name=f"Log ({level.value.upper()})",
            attachment_type=allure.attachment_type.TEXT
        )