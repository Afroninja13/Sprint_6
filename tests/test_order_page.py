from conftest import driver
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData
import allure


class TestOrderPage:

    @allure.title('Проверка полного сценария заказа самоката по кнопке в хедере сайта')
    def test_order_samokat_from_header_order_btn(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        driver.get(TestData.MAIN_URL)
        main_page.click_on_cookie_agree()
        header_page.click_on_btn_order_in_header()
        order_page.input_fields_on_first_order_page(
            'Сергей', 'Устинов', 'Санкт-Петербург', 'Сокольники', '89215853447')
        order_page.click_btn_then()
        order_page.input_fields_on_second_order_page('27.02.2024', 'сутки', 'Комментарий')
        order_page.click_on_checkbox_black_colour()
        order_page.click_on_btn_order_final()
        order_page.click_on_btn_order_yes()
        assert order_page.check_order_placed_label_is_displayed()

    @allure.title('Проверка полного сценария заказа самоката по кнопке в теле сайта')
    def test_order_samokat_from_body_order_btn(self, driver):
        driver.get(TestData.MAIN_URL)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_cookie_agree()
        main_page.click_on_btn_order_in_body()
        order_page.input_fields_on_first_order_page(
            'Иван', 'Иванов', 'Москва', 'Лубянка', '89212455520')
        order_page.click_btn_then()
        order_page.input_fields_on_second_order_page('29.02.2024', 'трое суток', 'Коммент')
        order_page.click_on_checkbox_black_colour()
        order_page.click_on_btn_order_final()
        order_page.click_on_btn_order_yes()
        assert order_page.check_order_placed_label_is_displayed()
