import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,sign_in']")
    QR_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,get_qr']")
    QR_CODE_BUTTON = (By.XPATH, "//*[@data-l='t,qr_tab']")
    DOESNT_WORK_BUTTON = (By.XPATH, "//*[@data-l='t,restore']")
    RESTORE_LINK = (By.XPATH, "//div[@class='form-actions']/*[@data-l='t,restore']")
    REGISTRATION_BUTTON = (By.XPATH, "//div[@class='external-oauth-login-footer']//a[@data-l='t,register']")
    VK_BUTTON = (By.XPATH, "//*[@class='i ic social-icon __s __vk_id']")
    MAIL_BUTTON = (By.XPATH, "//*[@class='i ic social-icon __s __mailru']")
    YANDEX_BUTTON = (By.XPATH, "//*[@class='i ic social-icon __s __yandex']")
    ERROR_TEXT = (By.XPATH, "//*[@class='input-e login_error']")
    GO_BACK_BUTTON = (By.XPATH, "//*[@data-l='t,cancel']")
    SUPPORT_BUTTON = (By.XPATH, "//*[text()='Служба поддержки']")

class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.DOESNT_WORK_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)

    @allure.step("Кликнуть на кнопку Войти")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Заполнить поле Логин")
    def send_keys_login(self, text):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text)
        self.attach_screenshot()

    @allure.step("Заполнить поле Пароль")
    def send_keys_password(self, text):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(text)
        self.attach_screenshot()

    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Кликнуть на кнопку Восстановить профиль")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_LINK).click()

    @allure.step("Кликнуть на кнопку Зарегистрироваться")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()