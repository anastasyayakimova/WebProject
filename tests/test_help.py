from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocator
from pages.ReklamnyiKabinetPage import AdvertisingOfficeHelper
import allure

BASE_URL = "https://ok.ru/help"

@allure.suite("Тест страницы Help")
@allure.title("Тест перехода на страницу Рекламный кабинет")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocator.ADVERTISING_OFFICE)
    AdvertisingOfficeHelper(browser)