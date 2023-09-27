from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.pages.base import BasePage


class Mediator(BasePage):
    """Класс-прослойка"""

    # Локаторы
    BUTTON_CATALOG = (By.XPATH, '//button[@data-test-id="button__catalog"]')

    def __init__(self, driver: WebDriver):
        """
        Args:
            driver: Инстанс WebDriver
        """
        super().__init__(driver=driver)

    def open_catalog(self):
        """Открыть каталог"""
        self.click_to_element(locator=self.BUTTON_CATALOG)
