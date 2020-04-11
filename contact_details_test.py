import unittest
from time import sleep

import HtmlTestRunner

from pages.add_photograph_page import AddPhotographPage
from pages.contact_details_page import ContactDetailsPage
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import CHROME_EXECUTABLE_PATH, DOMAIN
from pages.personal_details_page import PersonalDetailsPage


class ContactDetailsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.wait = WebDriverWait(self.driver, 2)
        self.login_page = LoginPage(self.driver)
        self.personal_details_page = PersonalDetailsPage(self.driver)
        self.contact_details_page = ContactDetailsPage(self.driver)
        self.add_photograph_page = AddPhotographPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_08_contact_details(self):

        driver = self.driver
        self.login_page.login()
        sleep(1)
        self.personal_details_page.goto_page()
        self.contact_details_page.contact()
        sleep(1)

        page_title = driver.find_element_by_xpath('//*[@id="contact-details"]/div[2]/div[1]/h1').text
        self.assertEqual('Contact Details', page_title)

    def test_09_is_contact_details_editable(self):
        driver = self.driver
        self.login_page.login()
        self.personal_details_page.goto_page()
        self.contact_details_page.contact()
        self.contact_details_page.save_button()

        status = driver.find_element_by_id('contact_street1').is_enabled()

        print('Text Fields in Contact Details can be editable: ',status)

        self.assertTrue(status)

    def test_10_contact_details_edit(self):
        driver = self.driver
        address_1 = 'address1_1234!@#$'
        address_2 = 'address2_f1234!@#$'
        city = 'city_asdf1234!@#$'
        state_province = 'state_asdf1234!@#$'
        zip_code = 'zip1234!@#$'
        self.login_page.login()
        self.personal_details_page.goto_page()
        self.contact_details_page.contact()
        sleep(1)
        #
        self.contact_details_page.save_button()
        # setup street_1
        self.contact_details_page.setup_address_1(address_1)
        # setup street_2
        self.contact_details_page.setup_address_2(address_2)
        # setup city
        self.contact_details_page.setup_city(city)
        self.contact_details_page.setup_state_province(state_province)
        self.contact_details_page.setup_zip_code(zip_code)

        Select(driver.find_element_by_id('contact_country')).select_by_index(5)

        self.contact_details_page.save_button()
        self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        input_city = driver.find_element_by_id('contact_city')
        value_city = input_city.get_attribute('value')

        self.assertEqual(city, value_city)

    def test_11_contact_zip_10(self):
        driver = self.driver
        zipcode = '1234567890'
        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.contact_details_page.contact()

        sleep(1)
        self.contact_details_page.save_button()
        self.contact_details_page.setup_zipcode(zipcode)
        self.contact_details_page.save_button()
        #self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        input_zip = driver.find_element_by_id('contact_emp_zipcode')
        value_zip_code = input_zip.get_attribute('value')

        self.assertEqual(zipcode, value_zip_code)


    def test_11_contact_zip_more_10(self):
        driver = self.driver
        zip_code = '123456789123456789'
        self.login_page.login()

        sleep(1)

        self.personal_details_page.goto_page()
        self.contact_details_page.contact()

        sleep(1)

        self.contact_details_page.save_button()

        self.contact_details_page.setup_zip_code(zip_code)

        self.contact_details_page.save_button()

        #self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        input_zip = driver.find_element_by_id('contact_emp_zipcode')
        value_zip_code = input_zip.get_attribute('value')
        number_characters = len(value_zip_code)

        self.assertTrue(number_characters <= 10)

    def test_12_contact_valid_phone(self):
        driver = self.driver
        phone_number = '1234567890+ - / ( )'
        self.login_page.login()

        sleep(1)

        self.personal_details_page.goto_page()
        self.contact_details_page.contact()

        sleep(1)

        self.contact_details_page.save_button()
        self.contact_details_page.set_home_phone(phone_number)
        self.contact_details_page.set_mobile_phone(phone_number)
        self.contact_details_page.set_work_phone(phone_number)


        self.contact_details_page.save_button()

        # self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".message.success")))
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Saved'))

        input_num = driver.find_element_by_id('contact_emp_mobile')
        value_mobile = input_num.get_attribute('value')

        self.assertEqual(phone_number, value_mobile)

    def test_13_contact_invalid_phone(self):
        driver = self.driver
        phone_number = 'abc!4567890+ - / ( )'
        self.login_page.login()
        sleep(1)

        self.personal_details_page.goto_page()
        self.contact_details_page.contact()

        sleep(1)

        self.contact_details_page.save_button()
        self.contact_details_page.set_home_phone(phone_number)
        self.contact_details_page.set_mobile_phone(phone_number)
        self.contact_details_page.set_work_phone(phone_number)


        self.contact_details_page.save_button()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpContactDetails"]/fieldset/ol[2]/li[1]/span').text == 'Allows numbers and only + - / ( )')

    def test_14_contact_valid_email(self):
        driver = self.driver
        work_email = 'work@test.test'
        other_email = 'other@test.test'
        self.login_page.login()

        sleep(1)

        self.personal_details_page.goto_page()
        self.contact_details_page.contact()

        sleep(1)

        self.contact_details_page.save_button()
        self.contact_details_page.set_work_email(work_email)
        self.contact_details_page.set_other_email(other_email)


        self.contact_details_page.save_button()

        value_work_email = driver.find_element_by_id('contact_emp_work_email').get_attribute('value')
        value_other_email = driver.find_element_by_id('contact_emp_oth_email').get_attribute('value')

        self.assertEqual(work_email, value_work_email)
        self.assertEqual(other_email, value_other_email)


    def test_15_contact_invalid_email(self):
        driver = self.driver
        work_email = 'work@test'
        other_email = '@test.test'
        self.login_page.login()

        sleep(1)

        self.personal_details_page.goto_page()
        self.contact_details_page.contact()

        sleep(1)

        self.contact_details_page.edit_button()
        self.contact_details_page.set_work_email(work_email)
        self.contact_details_page.set_other_email(other_email)

        self.contact_details_page.save_button()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpContactDetails"]/fieldset/ol[3]/li[1]/span').text == 'Expected format: admin@example.com')



    def test_15_contact_same_email(self):
        driver = self.driver
        work_email = 'work@test.test'
        self.login_page.login()

        sleep(1)

        self.personal_details_page.goto_page()
        self.contact_details_page.contact()
        sleep(1)

        self.contact_details_page.edit_button()

        self.contact_details_page.set_work_email(work_email)
        self.contact_details_page.set_other_email(work_email)

        self.contact_details_page.save_button()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpContactDetails"]/fieldset/ol[3]/li[2]/span').text == 'Already exists')


if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output ='C:/Users/stepan/PycharmProjects/HRM_GIT/Reports'))
