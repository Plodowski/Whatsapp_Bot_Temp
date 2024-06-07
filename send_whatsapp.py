from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
profiile = "--user-data-dir=/Users/gabrielmenezes/Library/Application Support/Google/Chrome/"
option.add_argument(profiile)
option.add_argument("--profile-directory=profile 1")

driver = webdriver.Chrome(options=option)
driver.get("web.whatsapp.com")
time.sleep(40)
