from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('Кликаем по вопросу {num} и получаем текст его ответа')
    def click_on_question_and_get_answer(self, locator_q, locator_a, num):
        method_q, new_locator_q = locator_q
        new_locator_q = new_locator_q.format(num)
        self.click_on_element((method_q, new_locator_q))
        method_a, new_locator_a = locator_a
        new_locator_a = new_locator_a.format(num)
        return self.get_text_from_element((method_a, new_locator_a))

    @allure.step('Кликаем по кнопке "Принять куки"')
    def click_on_cookie_agree(self):
        self.click_on_element(MainPageLocators.BTN_AGREE_COOKIE)

    @allure.step('Кликаем про кнопке "Заказать" в теле страницы')
    def click_on_btn_order_in_body(self):
        self.click_on_element(MainPageLocators.BTN_ORDER_IN_BODY)

    @allure.step('Функция проверки отображения логотипа главной страницы')
    def check_main_label_is_displayed(self):
        return self.find_element_with_wait(MainPageLocators.LABEL_MAIN_PAGE).is_displayed()
