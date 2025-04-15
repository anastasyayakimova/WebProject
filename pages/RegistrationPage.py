import allure
import random
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    COUNTRY_LIST = (By.XPATH, "//div[@data-l='t,country']")
    COUNTRY_ITEM = (By.XPATH, "//div[@class='country-select_code']")
    PHONE_FIELD = (By.XPATH, "//*[@id='field_phone']")
    BUTTON_FURTHER = (By.XPATH, "//input[@value='Далее']")
    SUPPORT_BUTTON = (By.XPATH, "//*[@class='ext-registration_f-support-link']")

class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)
        self.find_element(RegistrationPageLocators.BUTTON_FURTHER)

    @allure.step("Выбрать рандомную страну из списка")
    def select_random_country(self):
        random_number = random.randint(0, 112)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].text
        country_items[random_number].click()
        self.attach_screenshot()
        return country_code

    @allure.step('Получить ззначение поля Телефон')
    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')