from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ContactDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    def contact(self):
        self.driver.find_element_by_link_text('Contact Details').click()

    def clear_street_1(self):
        self.driver.find_element_by_id('contact_street1').clear()

    def street_adress_1(self, adress_1):
        driver = self.driver
        driver.find_element_by_id('contact_street1').send_keys(adress_1)

    def clear_street_2(self):
        self.driver.find_element_by_id('contact_street2').clear()

    def street_adress_2(self, adress_2):
        driver = self.driver
        driver.find_element_by_id('contact_street2').send_keys(adress_2)

    def clear_city(self):
        self.driver.find_element_by_id('contact_city').clear()

    def city(self, city):
        driver = self.driver
        driver.find_element_by_id('contact_city').send_keys(city)

    def clear_province(self):
        self.driver.find_element_by_id('contact_province').clear()


    def save_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def setup_address_1(self, address_1):
        self.driver.find_element_by_id('contact_street1').clear()
        self.driver.find_element_by_id('contact_street1').send_keys(address_1)
