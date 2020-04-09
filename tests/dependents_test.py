import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import CHROME_EXECUTABLE_PATH, DOMAIN
from pages.dependents_page import DependentsPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage


class DependentsTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.driver.get(DOMAIN)
        self.wait = WebDriverWait(self.driver, 2)
        self.login_page = LoginPage(self.driver)
        self.personal_details_page = PersonalDetailsPage(self.driver)
        self.dependents_page = DependentsPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_26_add_dependent(self):
        driver = self.driver

        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()

        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")

        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        dependent_name = driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr/td[2]/a').text

        self.assertEqual("Mark Sayfou", dependent_name)

        # clean up
        self.dependents_page.check_all_dependents()
        self.dependents_page.del_dependents()
    def test_27_dependent_name_required(self):
        driver = self.driver
        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()

        sleep(1)
        self.dependents_page.add_dependents()

        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")

        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpDependent"]/fieldset/ol/li[1]/span').text == "Required")


    def test_28_dependent_relationship_required(self):
        driver = self.driver

        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()

        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()
        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpDependent"]/fieldset/ol/li[2]/span').text == "Required")

    def test_29_add_dependent_other_relationship(self):
        driver = self.driver

        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()
        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Other")

        self.dependents_page.dependents_relatioship()
        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        dependent_name = driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr/td[2]/a').text

        self.assertEqual("Mark Sayfou", dependent_name)
        # clean up
        self.dependents_page.check_all_dependents()
        self.dependents_page.del_dependents()

    def test_30_add_dependent_other_specify(self):
        driver = self.driver

        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()

        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()

        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Other")

        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="relationshipDesc"]/span').text == "Required")

    def test_31_add_dependent(self):
        driver = self.driver

        self.login_page.login()

        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()

        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")

        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        dependent_name = driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr/td[2]/a').text

        self.assertEqual("Mark Sayfou", dependent_name)

        # clean up
        self.dependents_page.check_all_dependents()
        self.dependents_page.del_dependents()

    def test_32_delete_dependent(self):
        driver = self.driver

        self.login_page.login()
        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()

        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()

        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        sleep(1)

        driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr[1]/td[1]/input').click()
        driver.find_element_by_id('delDependentBtn').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Deleted'))

    def test_33_delete_all_dependents(self):
        driver = self.driver

        self.login_page.login()
        sleep(1)
        self.personal_details_page.goto_page()
        self.dependents_page.dependents()
        sleep(1)
        self.dependents_page.add_dependents()
        self.dependents_page.dependents_name()
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        self.dependents_page.dependents_date_of_birth()
        self.dependents_page.save_dependents()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        sleep(1)
        self.dependents_page.check_all_dependents()
        self.dependents_page.del_dependents()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))



if __name__ == '__main__':
    unittest.main()
