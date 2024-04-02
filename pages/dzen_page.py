import allure
from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


class DzenPage(BasePage):

    @allure.step('Функция проверки отображения хедера на сайте Яндекс Дзен')
    def check_header_dzen_is_displayed(self):
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[1])
        return self.find_element_with_wait(DzenPageLocators.DZEN_HEADER).is_displayed()
