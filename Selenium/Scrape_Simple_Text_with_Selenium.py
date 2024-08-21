from selenium import webdriver
import time

webpage = "http://automated.pythonanywhere.com"

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

#--- normal text
def get_quote(driver):
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  print(element.text)

#--- Dynamic value
def get_world_temp(driver):
  # the dynamic temp value only appear approx 2 sec after page loaded
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  print(element.text)

def get_only_temp(driver):
  print("Reading 5 temperature continuously :")
  for i in range(5):
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    temp = element.text.split(": ")[1]
    print(temp)

def main(run=False):
  if run:
    driver = get_drvier()
    get_quote(driver)
    get_world_temp(driver)
    get_only_temp(driver)