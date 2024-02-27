from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Ввод значения в поле "Имя"')
    def input_value_in_name_field(self, name):
        self.input_value_in_field(OrderPageLocators.FIELD_NAME, name)

    @allure.step('Ввод значения в поле "Фамилия"')
    def input_value_in_surname_field(self, surname):
        self.input_value_in_field(OrderPageLocators.FIELD_SURNAME, surname)

    @allure.step('Ввод значения в поле "Адрес куда привезти заказ"')
    def input_value_in_address_field(self, address):
        self.input_value_in_field(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step('Получение локатора нужного значения в поле "Станция метро"')
    def metro_station_locator(self, new_station):
        metro = (By.XPATH, './/*[text()="' + new_station + '"]')
        return metro

    @allure.step('Шаг выбора значения в поле "Станция метро"')
    def chose_value_in_metro_field(self, new_station):
        self.click_on_element(OrderPageLocators.FIELD_METRO)
        metro_locator = self.metro_station_locator(new_station)
        self.click_on_element(metro_locator)

    @allure.step('Ввод значения в поле "Телефон"')
    def input_value_in_phone_field(self, phone):
        self.input_value_in_field(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Шаг заполнения первой страницы заказа самоката')
    def input_fields_on_first_order_page(self, name, surname, address, station, phone):
        self.input_value_in_name_field(name)
        self.input_value_in_surname_field(surname)
        self.input_value_in_address_field(address)
        self.chose_value_in_metro_field(station)
        self.input_value_in_phone_field(phone)

    @allure.step('Клик по кнопке "Далее" на первой странице заказа самоката')
    def click_btn_then(self):
        self.click_on_element(OrderPageLocators.BTN_THEN)

    @allure.step('Ввод значения в поле "Когда привезти самокат"')
    def input_value_in_date_field(self, date):
        self.input_value_in_field(OrderPageLocators.FIELD_DATE, date)

    @allure.step('Закрытие календаря поля "Когда привезти самокат" нажатием кнопки RETURN')
    def input_return_in_date_field(self):
        self.input_value_in_field(OrderPageLocators.FIELD_DATE, Keys.RETURN)

    @allure.step('Шаг заполнения поля "Когда привезти самокат"')
    def chose_value_in_date_field(self, date):
        self.input_value_in_date_field(date)
        self.input_return_in_date_field()

    @allure.step('Получение локатора нужного значения в поле "Срок аренды"')
    def rent_period_locator(self, rent_period):
        period = (By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="' + rent_period + '"]')
        return period

    @allure.step('Клик в поле "Срок аренды"')
    def click_in_rent_period_field(self):
        self.click_on_element(OrderPageLocators.FIELD_RENT_PERIOD)

    @allure.step('Шаг выбора значения в поле "Срок аренды"')
    def chose_value_in_rent_period_field(self, rent_period):
        self.click_in_rent_period_field()
        rent_period_locator = self.rent_period_locator(rent_period)
        self.click_on_element(rent_period_locator)

    @allure.step('Клик по чекбоксу черного цвета')
    def click_on_checkbox_black_colour(self):
        self.click_on_element(OrderPageLocators.CHECKBOX_BLACK_COLOUR)

    @allure.step('Клик по чекбоксу серого цвета')
    def click_on_checkbox_gray_colour(self):
        self.click_on_element(OrderPageLocators.CHECKBOX_GRAY_COLOUR)

    @allure.step('Ввод значения в поле Комментарий для курьера')
    def input_value_in_comment_courier_field(self, comment):
        self.input_value_in_field(OrderPageLocators.FIELD_COMMENT_COURIER, comment)

    @allure.step('Шаг заполнения полей второй страницы заказа самоката')
    def input_fields_on_second_order_page(self, date, rent_period, comment):
        self.chose_value_in_date_field(date)
        self.chose_value_in_rent_period_field(rent_period)
        self.input_value_in_comment_courier_field(comment)

    @allure.step('Клик по кнопке Заказать на второй странице заказа самоката')
    def click_on_btn_order_final(self):
        self.click_on_element(OrderPageLocators.BTN_ORDER_FINAL)

    @allure.step('Клик по кнопке Да при подтверждении заказа самоката')
    def click_on_btn_order_yes(self):
        self.click_on_element(OrderPageLocators.BTN_ORDER_YES)

    @allure.step('Проверка отображения уведомления Заказ оформлен')
    def check_order_placed_label_is_displayed(self):
        return self.find_element_with_wait(OrderPageLocators.LABEL_ORDER_PLACED).is_displayed()
