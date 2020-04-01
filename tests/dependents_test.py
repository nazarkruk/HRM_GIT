import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class DependentsTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='/Users/nazarkruk/PycharmProjects/HRM100Full/browsers_drivers/chromedriver')
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_26_add_dependent(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        dependent_name = driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr/td[2]/a').text

        self.assertEqual("Mark Sayfou", dependent_name)

        # clean up
        driver.find_element_by_id("checkAll").click()
        driver.find_element_by_id('delDependentBtn').click()

    def test_27_dependent_name_required(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpDependent"]/fieldset/ol/li[1]/span').text == "Required")


    def test_28_dependent_relationship_required(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="frmEmpDependent"]/fieldset/ol/li[2]/span').text == "Required")

    def test_29_add_dependent_other_relationship(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Other")
        driver.find_element_by_id('dependent_relationship').clear()
        driver.find_element_by_id('dependent_relationship').send_keys('nephew')
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        dependent_name = driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr/td[2]/a').text

        self.assertEqual("Mark Sayfou", dependent_name)

        # clean up
        driver.find_element_by_id("checkAll").click()
        driver.find_element_by_id('delDependentBtn').click()

    def test_30_add_dependent_other_specify(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Other")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.assertTrue(driver.find_element_by_xpath('//*[@id="relationshipDesc"]/span').text == "Required")

    def test_31_add_dependent(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        dependent_name = driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr/td[2]/a').text

        self.assertEqual("Mark Sayfou", dependent_name)

        # clean up
        driver.find_element_by_id("checkAll").click()
        driver.find_element_by_id('delDependentBtn').click()

    def test_32_delete_dependent(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        sleep(1)

        driver.find_element_by_xpath('//*[@id="dependent_list"]/tbody/tr[1]/td[1]/input').click()
        driver.find_element_by_id('delDependentBtn').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Deleted'))

    def test_33_delete_all_dependents(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Dependents').click()

        sleep(1)

        driver.find_element_by_id('btnAddDependent').click()
        driver.find_element_by_id('dependent_name').clear()
        driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')
        Select(driver.find_element_by_id('dependent_relationshipType')).select_by_visible_text("Child")
        driver.find_element_by_id('dependent_dateOfBirth').clear()
        driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')
        driver.find_element_by_id('btnSaveDependent').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))

        sleep(1)

        driver.find_element_by_id("checkAll").click()
        driver.find_element_by_id('delDependentBtn').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),'Successfully Deleted'))



if __name__ == '__main__':
    unittest.main()
