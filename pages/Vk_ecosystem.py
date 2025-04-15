import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class VKEcosystemPageLocators:
    VK_LOGO = (By.XPATH, "//*[@id='header-logo']")


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.VK_LOGO)