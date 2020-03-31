import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class PersonalDetailsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='/Users/nazarkruk/PycharmProjects/HRM100Full/browsers_drivers/chromedriver')
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_01_see_personal_details(self):

        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()

        page_title = driver.find_element_by_xpath("//*[@id='pdMainContainer']/div[1]/h1").text
        self.assertEqual("Personal Details", page_title)


    def test_02_edit_personal_details(self):
        driver = self.driver
        input_middle_name = 'Richard'
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_id('btnSave').click()
        driver.find_element_by_id('personal_txtEmpMiddleName').clear()
        driver.find_element_by_id('personal_txtEmpMiddleName').send_keys(input_middle_name)
        driver.find_element_by_id('personal_txtEmployeeId').clear()
        driver.find_element_by_id('personal_txtEmployeeId').send_keys('0101010')
        driver.find_element_by_id('personal_txtOtherID').clear()
        driver.find_element_by_id('personal_txtOtherID').send_keys('12345')
        driver.find_element_by_id('personal_txtEmpNickName').clear()
        driver.find_element_by_id('personal_txtEmpNickName').send_keys('rick')
        driver.find_element_by_id('personal_txtMilitarySer').clear()
        driver.find_element_by_id('personal_txtMilitarySer').send_keys('n/a')
        driver.find_element_by_id('btnSave').click()

        sleep(3)

        employee_full = driver.find_element_by_xpath('//*[@id="profile-pic"]/h1').text
        self.assertTrue(input_middle_name in employee_full)

    def test_03_edit_restiricted_personal_details(self):
        driver = self.driver
        input_ssn = '50001000'
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_id('btnSave').click()
        driver.find_element_by_id('personal_txtLicenNo').clear()
        driver.find_element_by_id('personal_txtLicenNo').send_keys('Richard')
        driver.find_element_by_id('personal_txtSINNo').clear()
        driver.find_element_by_id('personal_txtSINNo').send_keys('0101010')
        driver.find_element_by_id('personal_txtNICNo').clear()
        driver.find_element_by_id('personal_txtNICNo').send_keys(input_ssn)
        driver.find_element_by_id("personal_chkSmokeFlag").click()
        driver.find_element_by_name('personal[DOB]').clear()
        driver.find_element_by_name('personal[DOB]').send_keys('03-09-1985')
        Select(driver.find_element_by_id('personal_cmbMarital')).select_by_visible_text("Married")
        driver.find_element_by_id('btnSave').click()

        sleep(3)

        typed_ssn = driver.find_element_by_id('personal_txtNICNo')
        value_snn = typed_ssn.get_attribute('value')

        self.assertEqual(input_ssn, value_snn)




if __name__ == '__main__':
    unittest.main()
