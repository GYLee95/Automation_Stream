from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

webpage = "https://titan22.com/"

def get_drvier():
  # --- Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get(webpage)
  return driver

def login(driver):
  driver.find_element(by="id", value="CustomerEmail").send_keys("vincent.lee010@gmail.com")
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys("abc123")
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/main/article/section/div/div[1]/form/button").click()
  time.sleep(2)
  print(driver.current_url)

def main(run=False):
  if run:
    driver = get_drvier()

    # --- Access to login
    driver.find_element(by="xpath", value="/html/body/header/div[1]/div[1]/div/div[3]/a[2]").click()
    time.sleep(2)
    print(driver.current_url)
    login(driver)

    # --- Goto Contact us
    driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)
    print(driver.current_url)