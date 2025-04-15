from selenium.webdriver import ActionChains
import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class HelpPageLocator:
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    RELEVANT = (By.XPATH, "//a[contains(@href, 'segodnya-aktualno')]")
    REGISTRATION = (By.XPATH, "//a[contains(@href, 'registraciya')]")
    MY_PROFILE = (By.XPATH, "//a[contains(@href, 'moi-profil')]")
    COMMUNICATION = (By.XPATH, "//a[contains(@href, 'obshchenie')]")
    ACCESS_TO_PROFILE = (By.XPATH, "//a[contains(@href, 'dostup-k-profilu')]")
    SAFETY = (By.XPATH, "//a[contains(@href, 'bezopasnost')]")
    GROUPS = (By.XPATH, "//a[contains(@href, 'gruppy')]")
    PAID_FEATURES = (By.XPATH, "//a[contains(@href, 'platnye-funkcii')]")
    VIOLATIONS_AND_SPAM = (By.XPATH, "//a[contains(@href, 'narusheniya-i-spam')]")
    GAMES_AND_APPLICATION = (By.XPATH, "//a[contains(@href, 'igry-i-prilojeniya')]")
    OTHER_SERVICES = (By.XPATH, "//a[contains(@href, 'drugie-servisy')]")
    USEFUL_INFORMATION = (By.XPATH, "//a[contains(@href, 'poleznaya-informaciya')]")
    ADVERTISING_OFFICE = (By.XPATH, "//a[contains(@href, 'reklamnyi-kabinet')]")

class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(HelpPageLocator.SEARCH_INPUT)
        self.find_element(HelpPageLocator.RELEVANT)
        self.find_element(HelpPageLocator.REGISTRATION)
        self.find_element(HelpPageLocator.MY_PROFILE)
        self.find_element(HelpPageLocator.COMMUNICATION)
        self.find_element(HelpPageLocator.ACCESS_TO_PROFILE)
        self.find_element(HelpPageLocator.SAFETY)
        self.find_element(HelpPageLocator.GROUPS)
        self.find_element(HelpPageLocator.PAID_FEATURES)
        self.find_element(HelpPageLocator.VIOLATIONS_AND_SPAM)
        self.find_element(HelpPageLocator.GAMES_AND_APPLICATION)
        self.find_element(HelpPageLocator.OTHER_SERVICES)
        self.find_element(HelpPageLocator.USEFUL_INFORMATION)
        self.find_element(HelpPageLocator.ADVERTISING_OFFICE)

    @allure.step("Проскроллить до элемента")
    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()