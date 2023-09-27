from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс с базовыми методами для работы с элементами страницы"""
    url: str

    def __init__(self, driver: WebDriver):
        """
        Args:
            driver: Инстанс WebDriver
        """
        self._driver = driver

    def get(self):
        """Открыть страницу url класса"""
        self._driver.get(self.url)

    def open(self, url: str):
        """Открыть страницу по url

        Args:
            url: Ссылка на страницу
        """
        self._driver.get(url)

    def back(self):
        """Открыть предыдущую страницу."""
        self._driver.back()

    def refresh(self):
        """Обновить текущую страницу."""
        self._driver.refresh()

    def find_element(self, locator: tuple[str, str], timeout: float = 10) -> WebElement:
        """Ожидать присутствия элемента в DOM страницы

            locator: Локатор элемента
            timeout: Время ожидания
       """
        element = WebDriverWait(driver=self._driver, timeout=timeout).until(
            method=EC.presence_of_element_located(locator=locator)
        )

        return element

    def click_to_element(self, locator: tuple[str, str], timeout: float = 10):
        """Найти элемент по локатору и кликнуть по нему

            locator: Локатор элемента
            timeout: Время ожидания
        """
        element = WebDriverWait(driver=self._driver, timeout=timeout).until(
            method=EC.element_to_be_clickable(mark=locator)
        )
        element.click()
