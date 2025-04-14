from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,sign_in']")
    QR_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,get_qr']")
    QR_CODE_BUTTON = (By.XPATH, "//*[@data-l='t,qr_tab']")
    DOESNT_WORK_BUTTON = (By.XPATH, "//*[@data-l='t,restore']")
    REGISTRATION_BUTTON = (By.XPATH, "//div[@class='external-oauth-login-footer']//a[@data-l='t,register']")
    VK_BUTTON = (By.XPATH, "//*[@class='i ic social-icon __s __vk_id']")
    MAIL_BUTTON = (By.XPATH, "//*[@class='i ic social-icon __s __mailru']")
    YANDEX_BUTTON = (By.XPATH, "//*[@class='i ic social-icon __s __yandex']")

class LoginPageHelper(BasePage):
    pass