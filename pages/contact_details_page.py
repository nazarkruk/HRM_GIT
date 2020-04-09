from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ContactDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    def contact(self):
        self.driver.find_element_by_link_text('Contact Details').click()

    def setup_city(self, city):
        self.driver.find_element_by_id('contact_city').clear()
        self.driver.find_element_by_id('contact_city').send_keys(city)

    def clear_province(self):
        self.driver.find_element_by_id('contact_province').clear()


    def save_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def edit_button(self):
        self.driver.find_element_by_id('btnSave').click()

    def setup_address_1(self, address_1):
        self.driver.find_element_by_id('contact_street1').clear()
        self.driver.find_element_by_id('contact_street1').send_keys(address_1)

    def setup_address_2(self, address_2):
        self.driver.find_element_by_id('contact_street2').clear()
        self.driver.find_element_by_id('contact_street2').send_keys(address_2)

    def setup_state_province(self, state_province):
        self.driver.find_element_by_id('contact_province').clear()
        self.driver.find_element_by_id('contact_province').send_keys(state_province)

    def setup_zip_code(self, zip_code):
        self.driver.find_element_by_id('contact_emp_zipcode').clear()
        self.driver.find_element_by_id('contact_emp_zipcode').send_keys(zip_code)

    def setup_zipcode(self, zipcode):
        self.driver.find_element_by_id('contact_emp_zipcode').clear()
        self.driver.find_element_by_id('contact_emp_zipcode').send_keys(zipcode)

    def set_home_phone(self, phone_number):
            self.driver.find_element_by_id('contact_emp_hm_telephone').clear()
            self.driver.find_element_by_id('contact_emp_hm_telephone').send_keys(phone_number)

    def set_mobile_phone(self, phone_number):
            self.driver.find_element_by_id('contact_emp_mobile').clear()
            self.driver.find_element_by_id('contact_emp_mobile').send_keys(phone_number)

    def set_work_phone(self, phone_number):
        self.driver.find_element_by_id('contact_emp_work_telephone').clear()
        self.driver.find_element_by_id('contact_emp_work_telephone').send_keys(phone_number)

    def set_work_email(self, work_email):
            self.driver.find_element_by_id('contact_emp_work_email').clear()
            self.driver.find_element_by_id('contact_emp_work_email').send_keys(work_email)

    def set_other_email(self, other_email):
            self.driver.find_element_by_id('contact_emp_oth_email').clear()
            self.driver.find_element_by_id('contact_emp_oth_email').send_keys(other_email)