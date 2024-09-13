from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        # Replace 'C:/WebDriver/chromedriver.exe' with the actual path to chromedriver on your system
        self.driver = webdriver.Chrome()# mozda mi treba putanja ovde


    def test_login(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/login/')  # Replace with your login URL

        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.XPATH, '//input[@value="Uloguj se"]')

        username.send_keys('Ana123')
        password.send_keys('ana123')
        login_button.click()

        time.sleep(2)  # Wait for page to load

        self.assertIn("Beauty Corner", driver.page_source)  # Adjust according to your success message

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

#python functional_tests/test_login.py
#python functional_tests/test_add_to_cart.py
#python functional_tests/test_finalize_order.py