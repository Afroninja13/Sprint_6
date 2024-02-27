import time
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver
import allure


class TestMainPage:

    @allure.title('Проверка текста ответа на вопросы')
    @pytest.mark.parametrize('num, answer_text', [
        (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    def test_question_have_correct_answer(self, driver, num, answer_text):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_cookie_agree()
        time.sleep(3)
        result = main_page.click_on_question_and_get_answer(MainPageLocators.BTN_QUESTION, MainPageLocators.ANSWER, num)
        assert result == answer_text
