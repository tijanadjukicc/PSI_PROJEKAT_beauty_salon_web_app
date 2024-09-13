from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #executable_path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

    def test_add_to_cart(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/login/')  # Replace with your login URL

        # Log in first
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.XPATH, '//input[@value="Uloguj se"]')

        username.send_keys('Ana123')
        password.send_keys('ana123')
        login_button.click()

        time.sleep(2)  # Wait for page to load

        driver.get('http://127.0.0.1:8000/proizvodi/')  # Replace with your products page URL

        add_to_cart_button = driver.find_element(By.XPATH, '//button[@value="dugmeKupi"]')  # Adjust selector as needed
        add_to_cart_button.click()

        time.sleep(2)  # Wait for page to load

        driver.get('http://127.0.0.1:8000/korpa/')  # Replace with your cart page URL

        time.sleep(2)  # Wait for page to load


        self.assertIn("Nuxe boost", driver.page_source)  # Adjust according to your product name

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
