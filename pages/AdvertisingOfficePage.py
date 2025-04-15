import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class AdvertisingOfficeLocators:
    TEXT_ADVERTISING_OFFICE = (By.XPATH, "//span[text()='Рекламный кабинет']")

class AdvertisingOfficeHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(AdvertisingOfficeLocators.TEXT_ADVERTISING_OFFICE)