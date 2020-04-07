
from selenium import webdriver
from fixtures.params import DOMAIN, CHROME_EXECUTABLE_PATH
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


class AddPhotographPage:

    def __init__(self, driver):
        self.driver = driver

    def employee_picture(self):
        self.driver.find_element_by_id('empPic').click()

