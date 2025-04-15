from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.Vk_ecosystem import VKEcosystemPageHelper
import allure

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка тулбара")
@allure.title("Переход к проектам экосстемы")
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)
    LoginPage.click_vk_system()
    LoginPage.click_project_button()
    new_window_id = LoginPage.get_windows_id(1)
    LoginPage.change_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.change_window(current_window_id)
    LoginPageHelper(browser)