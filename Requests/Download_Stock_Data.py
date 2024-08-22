import requests
from datetime import datetime
import time

def get_user_input():
  ticker = input("Enter the ticker symbol: ")
  from_date = input('Enter start date in yyyy/mm/dd format:')
  to_date = input('Enter end date in yyyy/mm/dd format:')
  interval_type = input("Enter the interval type (1d, 1wk, 1mo):")

  # --- convert date string to datetime format
  from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
  to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

  from_epoch = int(time.mktime(from_datetime.timetuple()))
  to_epoch = int(time.mktime(to_datetime.timetuple()))

  return ticker, from_epoch, to_epoch, interval_type

def proc_and_download_data(ticker, from_epoch, to_epoch, interval):
  url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval={interval}&events=history&includeAdjustedClose=true"
  
  headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
  
  content = requests.get(url, headers=headers).content
  print(content)

  with open('./Requests/data.csv', 'wb') as file:
    file.write(content)

def main(run=False):
  if run:
    ticker, from_epoch, to_epoch, interval = get_user_input()
    proc_and_download_data(ticker, from_epoch, to_epoch, interval)