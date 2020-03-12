import unittest
from time import sleep
from selenium import webdriver


class MyLoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/nazarkruk/PycharmProjects/HRM100Full/browsers_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_01_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        welcome_text = driver.find_element_by_id('welcome').text

        self.assertEqual ('Welcome Admin', welcome_text)

    def test_02_invalid_password(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password1')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        spam_massage = driver.find_element_by_id('spanMessage').text
        self.assertEqual ('Invalid credentials', spam_massage)

    def test_03_invalid_username(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password1')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        spam_massage = driver.find_element_by_id('spanMessage').text
        self.assertEqual('Invalid credentials', spam_massage)

    def test_04_empty_password(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        spam_massage = driver.find_element_by_id('spanMessage').text
        self.assertEqual ('Password cannot be empty', spam_massage)


    def test_05_empty_username(self):
        driver = self.driver
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(3)

        spam_massage = driver.find_element_by_id('spanMessage').text
        self.assertEqual ('Username cannot be empty', spam_massage)


if __name__ == '__main__':
    unittest.main()