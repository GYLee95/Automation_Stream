from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

webpage = "http://automated.pythonanywhere.com/login/"

def get_drvier():
  # Set options to make browsing easier
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
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  print(driver.current_url)

def write_file(text):
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, "w") as f:
    f.write(text)

def get_only_temp(driver):
  print("Reading 5 temperature continuously :")
  for i in range(5):
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    temp = float(element.text.split(": ")[1])
    write_file(str(temp))
    print(temp)

def main(run=False):
  if run:
    driver = get_drvier()
    login(driver)
    
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)

    get_only_temp(driver)