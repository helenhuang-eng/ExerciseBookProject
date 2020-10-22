# -*- coding: utf-8 -*-
import os
import shelve
import time

from pip._vendor.requests import cookies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestImportAddressBook():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.login_weixin()

    def teardown_method(self, method):
        self.driver.quit()

    def login_weixin(self):
        if not self.is_login_cookies_work():
            self.login_and_save_cookies()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        file = shelve.open('wxcookies')
        cookies = file['cookies']
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def is_login_cookies_work(self):
        """通过保存在文件中的cookies中的过期时间判断cookies是否还有效"""
        if not os.path.exists('wxcookies.dat'):
            return False
        file = shelve.open('wxcookies')
        cookies = file['cookies']
        file.close()
        if len(cookies) == 0:
            return False
        for cookie in cookies:
            if cookie.get('name') in ['_gid']:
                if time.time() < cookie.get('expiry'):
                    return True
        return False

    def login_and_save_cookies(self):
        """打开登陆页面，登陆后抓取cookies信息，保存下来以便之后自动登陆使用"""
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        while not self.is_login_ok():
            time.sleep(3)
        cookies = self.driver.get_cookies()
        db = shelve.open("wxcookies")
        db['cookies'] = cookies
        db.close()

    def is_login_ok(self):
        """校验是否扫码登录完毕"""
        if r'https://work.weixin.qq.com/wework_admin/loginpage_wx' in self.driver.current_url:
            return False
        return True

    def test_import_address_book(self):
        # 读取cookie
        db = shelve.open("wxcookies")
        cookies = db['cookies']
        db.close()

        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        # 找到"导入通讯录"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "D:\\testProject\\ExerciseBookProject\\data\\妍妍通讯录.xlsx")

        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "妍妍通讯录.xlsx" == filename
        time.sleep(3)

