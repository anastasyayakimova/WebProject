from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
import allure

BASE_URL = "https://ok.ru/"
@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода к восстановлению после несколкьких неудачных попыток авторизации")
def test_go_to_recovery_after_fails_login(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.send_keys_login("test")

    for i in range(3):
        LoginPage.send_keys_password("1")
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)
