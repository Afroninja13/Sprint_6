from selenium.webdriver.common.by import By


class HeaderPageLocators:
    LABEL_SAMOKAT = By.XPATH, './/img[contains(@alt, "Scooter")]'
    LABEL_YANDEX = By.XPATH, './/img[contains(@alt, "Yandex")]'
    BTN_ORDER_IN_HEADER = By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'
