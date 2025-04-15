import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ReklamnyiKabinetLocators:
    TEXT_REKLAM_KABINET = (By.XPATH, "//span[text()='Рекламный кабинет']")

class ReklamnyiKabinetHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(ReklamnyiKabinetLocators.TEXT_REKLAM_KABINET)