





class DependentsPage:

    def __init__(self, driver):
        self.driver = driver

    def dependents(self):
        self.driver.find_element_by_link_text('Dependents').click()

    def add_dependents(self):
        self.driver.find_element_by_id('btnAddDependent').click()

    def dependents_name(self):
        self.driver.find_element_by_id('dependent_name').clear()
        self.driver.find_element_by_id('dependent_name').send_keys('Mark Sayfou')

    def dependents_date_of_birth(self):
        self.driver.find_element_by_id('dependent_dateOfBirth').clear()
        self.driver.find_element_by_id('dependent_dateOfBirth').send_keys('03-12-2020')

    def save_dependents(self):
        self.driver.find_element_by_id('btnSaveDependent').click()

    def check_all_dependents(self):
        self.driver.find_element_by_id("checkAll").click()

    def del_dependents(self):
        self.driver.find_element_by_id('delDependentBtn').click()

    def dependents_relatioship(self):
        self.driver.find_element_by_id('dependent_relationship').clear()
        self.driver.find_element_by_id('dependent_relationship').send_keys('nephew')