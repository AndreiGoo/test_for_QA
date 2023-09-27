from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.pages.mediator import Mediator


class MainPage(Mediator):
    """Класс главной страницы"""

    # Локаторы
    PROMO = (By.XPATH, '//div[@class= "swiper-container"]')

    def __init__(self, driver: WebDriver):
        """
        Args:
            driver: Инстанс WebDriver
        """
        super().__init__(driver=driver)
        self.url = 'https://kazanexpress.ru/'

    def go_to_promo(self):
        """Перейти в раздел "Акции" """
        self.click_to_element(locator=self.PROMO)
