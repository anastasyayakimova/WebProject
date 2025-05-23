import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGO_BUTTON = (By.ID, "nohook_logo_link")
    VK_ECOSYSTEN_BUTTON = (By.XPATH, "//*[@data-l='t,vk_ecosystem']")
    PROJECTS_BUTTON = (By.XPATH, "//*[@data-l='t,more']")

class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step("Проверить корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.VK_ECOSYSTEN_BUTTON)
        self.find_element(BasePageLocators.PROJECTS_BUTTON)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f'Не удалось найти элемент {locator}')

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message=f'Не удалось найти элемент {locator}')

    @allure.step("Открыть страницу")
    def get_url(self, url):
        return self.driver.get(url)


    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step("Открыть меню")
    def click_vk_system(self):
        self.find_element(BasePageLocators.VK_ECOSYSTEN_BUTTON).click()

    @allure.step("Нажать на кнопку Еще")
    def click_project_button(self):
        self.find_element(BasePageLocators.PROJECTS_BUTTON).click()


    @allure.step("Получить id открытого окна")
    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    @allure.step("Изменить окно")
    def change_window(self, window_id):
        self.driver.switch_to.window(window_id)
