from web.pages.main_page import MainPage


class TestClass:

    def test_1(self, driver):
        page = MainPage(driver=driver)
        page.get()
        page.go_to_promo()
        page.open_catalog()
        pass

    def test_2(self):
        pass
