from selenium.webdriver.common.by import By


class MainPageLocators:
    LABEL_QUESTION_SECTION = By.XPATH, './/div[text()="Вопросы о важном"]'
    BTN_QUESTION = By.ID, 'accordion__heading-{}'
    ANSWER = By.XPATH, './/div[@id="accordion__panel-{}"]/p'
    BTN_ORDER_IN_BODY = By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'
    BTN_AGREE_COOKIE = By.ID, 'rcc-confirm-button'
    LABEL_MAIN_PAGE = By.XPATH, './/div[contains(@class, "Home_Header")]'
