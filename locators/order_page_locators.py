from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIELD_NAME = By.XPATH, './/input[@placeholder="* Имя"]' #  Локатор поля Имя
    FIELD_SURNAME = By.XPATH, './/input[@placeholder="* Фамилия"]' #  Локатор поля Фамилия
    FIELD_ADDRESS = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]' #  Локатор поля Адрес
    FIELD_METRO = By.CLASS_NAME, 'select-search__input' #  Локатор поля Станция метро
    FIELD_PHONE = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]' #  Локатор поля Телефон
    BTN_THEN = By.XPATH, './/button[text()="Далее"]' #  Локатор кнопки Далее на первой странице оформления заказа
    BTN_ORDER_FINAL = By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Заказать" ]'
    BTN_ORDER_YES = By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Да" ]'
    FIELD_DATE = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]' #  Локатор поля Когда привезти самокат
    FIELD_RENT_PERIOD = By.XPATH, './/div[@class="Dropdown-placeholder"]' #  Локатор поля Срок аренды
    CHECKBOX_BLACK_COLOUR = By.XPATH, './/input[@id="black"]'
    CHECKBOX_GRAY_COLOUR = By.XPATH, './/input[@id="gray"]'
    FIELD_COMMENT_COURIER = By.XPATH, './/input[@placeholder="Комментарий для курьера"]'
    LABEL_ORDER_PLACED = By.XPATH, './/*[text()="Заказ оформлен"]'
    BTN_METRO_STATION = By.XPATH, './/*[text()="{}"]'
    BTN_RENT_PERIOD = By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="{}"]'
