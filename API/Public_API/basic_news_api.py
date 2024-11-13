# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:14:14 2024

@author: gangylee
"""

import requests

# --- basic way of code
# from_date = "2024-11-11"
# to_date = "2024-11-12"
# sort_by = "popularity"
# api_key = "39612b1a081d457f9af5b22a54d6dc2b"

# r = requests.get(f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from={from_date}&to={to_date}&sortBy={sort_by}&language=en&apiKey={api_key}")
# content = r.json()

# articles = content['articles']

# for article in articles:
#     print(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}")

# -----------------------------------------------------------------------------------------

def get_news(topic, from_date, to_date, api_key, language='en'):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    
    r = requests.get(url)
    content = r.json()
    
    articles = content['articles']

    result = []
    for article in articles:
        result.append(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}\n")
    
    return result

def main():
    news_list = get_news('UK', "2024-11-1", "2024-11-13", "39612b1a081d457f9af5b22a54d6dc2b")
    
    for news in news_list:
        print(news)

if __name__ == "__main__":
    main()