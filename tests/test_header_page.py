from conftest import driver
from pages.dzen_page import DzenPage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from data import TestData
import allure


class TestHeaderPage:

    @allure.title('Тест перехода на главную страницу нажатием на логотип самоката')
    def test_click_on_logo_samokat_redirect_to_main_page(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        driver.get(TestData.MAIN_URL)
        main_page.click_on_cookie_agree()
        header_page.click_on_btn_order_in_header()
        header_page.click_on_logo_samokat()
        assert main_page.check_main_label_is_displayed()

    @allure.title('Тест перехода на страницу Дзен нажатием на логотип яндекса')
    def test_click_on_logo_yandex_redirect_to_dzen_page(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        dzen_page = DzenPage(driver)
        driver.get(TestData.MAIN_URL)
        main_page.click_on_cookie_agree()
        header_page.click_on_logo_yandex()
        assert dzen_page.check_header_dzen_is_displayed()
