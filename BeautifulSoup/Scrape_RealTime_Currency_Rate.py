import requests
from bs4 import BeautifulSoup

default_from_rate = "USD"
default_to_rate = "MYR"
default_amount = 1

def get_currency_rate(from_rate, to_rate, amount):
  url = f"https://www.x-rates.com/calculator/?from={default_from_rate}&to={default_to_rate}&amount={default_amount}"
  response = requests.get(url)
  content = response.content
  soup = BeautifulSoup(content, "html.parser")
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  #rate = float(rate.replace(",", ""))
  rate = float(rate.split(" ")[0])
  return rate


def main(run=False):
  if run:
    rate = get_currency_rate(default_from_rate,default_to_rate,default_amount)
    print("Current Currency Rate\n{} : {}\n{} : {}".format(default_from_rate, default_to_rate, default_amount, rate))