from selenium import webdriver
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        #cls.driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()


        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    def test_02_login_invalid_username(self):
            driver = self.driver
            driver.get("https://opensource-demo.orangehrmlive.com/")

            login = LoginPage(driver)
            login.enter_username("Admin1")
            login.enter_password("admin123")
            login.click_login()
            message = self.driver.find_element_by_xpath("").text
            self.assertEquals(message,"Invalid credentials")



       # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
       # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
       # self.driver.find_element_by_id("btnLogin").click()
       # self.driver.find_element_by_id("welcome").click()
       # self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Ecem/Documents/Repositories/selenium-example-1/Reports"))

