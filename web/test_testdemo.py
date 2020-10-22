from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTestdemo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(15)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testdemo(self):
    self.driver.get("https://ceshiren.com/")
    self.driver.set_window_size(1518, 804)
    self.driver.find_element(By.LINK_TEXT, "所有分类").click()
    # 断言
    element = self.driver.find_element(By.LINK_TEXT, "所有分类")
    result = element.get_attribute("class")
    assert 'active' == result
