from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocator
from pages.ReklamnyiKabinetPage import ReklamnyiKabinetHelper
import allure

BASE_URL = "https://ok.ru/help"

@allure.suite("Тест страницы Help")
@allure.title("Тест перехода на страницу Рекламный кабинет")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocator.REKLAMNYI_KABINET)
    ReklamnyiKabinetHelper(browser)