from selenium import webdriver
import os
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")
        self.login()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")


if __name__ == "__main__":
    ig_bot = InstagramBot("uname", "pword")










