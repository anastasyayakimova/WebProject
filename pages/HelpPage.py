from selenium.webdriver import ActionChains
import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class HelpPageLocator:
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    SEGODNYA_AKTUALNO = (By.XPATH, "//a[contains(@href, 'segodnya-aktualno')]")
    REGISTRACIYA = (By.XPATH, "//a[contains(@href, 'registraciya')]")
    MOI_PROFIL = (By.XPATH, "//a[contains(@href, 'moi-profil')]")
    OBSHCHENIE = (By.XPATH, "//a[contains(@href, 'obshchenie')]")
    DOSTUP_K_PROFILU = (By.XPATH, "//a[contains(@href, 'dostup-k-profilu')]")
    BEZOPASNOST = (By.XPATH, "//a[contains(@href, 'bezopasnost')]")
    GRUPPY = (By.XPATH, "//a[contains(@href, 'gruppy')]")
    PLATNYE_FUNKCII = (By.XPATH, "//a[contains(@href, 'platnye-funkcii')]")
    NARUSHENIYA_I_SPAM = (By.XPATH, "//a[contains(@href, 'narusheniya-i-spam')]")
    IGRY_I_PRILOJENIYA = (By.XPATH, "//a[contains(@href, 'igry-i-prilojeniya')]")
    DRUGIE_SERVISY = (By.XPATH, "//a[contains(@href, 'drugie-servisy')]")
    POLEZNAYA_INFORMACIYA = (By.XPATH, "//a[contains(@href, 'poleznaya-informaciya')]")
    REKLAMNYI_KABINET = (By.XPATH, "//a[contains(@href, 'reklamnyi-kabinet')]")

class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(HelpPageLocator.SEARCH_INPUT)
        self.find_element(HelpPageLocator.SEGODNYA_AKTUALNO)
        self.find_element(HelpPageLocator.REGISTRACIYA)
        self.find_element(HelpPageLocator.MOI_PROFIL)
        self.find_element(HelpPageLocator.OBSHCHENIE)
        self.find_element(HelpPageLocator.DOSTUP_K_PROFILU)
        self.find_element(HelpPageLocator.BEZOPASNOST)
        self.find_element(HelpPageLocator.GRUPPY)
        self.find_element(HelpPageLocator.PLATNYE_FUNKCII)
        self.find_element(HelpPageLocator.NARUSHENIYA_I_SPAM)
        self.find_element(HelpPageLocator.IGRY_I_PRILOJENIYA)
        self.find_element(HelpPageLocator.DRUGIE_SERVISY)
        self.find_element(HelpPageLocator.POLEZNAYA_INFORMACIYA)
        self.find_element(HelpPageLocator.REKLAMNYI_KABINET)

    @allure.step("Проскроллить до элемента")
    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()