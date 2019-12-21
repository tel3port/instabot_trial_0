from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")
        self.login()
        self. base_url = "https://www.instagram.com"

    def login(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver.get(f"{self.base_url}/accounts/login/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()

    def nav_user(self, user):
        self.driver.get(f'{self.base_url}/{user}/')


if __name__ == "__main__":
    ig_bot = InstagramBot("mr_magpie2020", "f9ptENkcPYUznCD")
    ig_bot.nav_user('realmadrid')










