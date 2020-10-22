# -*- coding: utf-8 -*-
from selenium import webdriver

class TestEditSeleniums():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_editseleniums(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-25244 .title > a").click()
        # el = self.driver.find_element(By.CSS_SELECTOR, ".topic-25244 .node")
        # print(el.text)
