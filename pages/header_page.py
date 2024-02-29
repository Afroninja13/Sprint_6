import allure
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):

    @allure.step('Клик по кнопке "Заказать"')
    def click_on_btn_order_in_header(self):
        self.click_on_element(HeaderPageLocators.BTN_ORDER_IN_HEADER)

    @allure.step('Клик по логотипу Самоката')
    def click_on_logo_samokat(self):
        self.click_on_element(HeaderPageLocators.LABEL_SAMOKAT)

    @allure.step('Клик по логотипу Яндекса')
    def click_on_logo_yandex(self):
        self.click_on_element(HeaderPageLocators.LABEL_YANDEX)
