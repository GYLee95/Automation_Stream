# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:39:59 2024

@author: gangylee
"""

import requests

def get_news(country, api_key, language='en'):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&language={language}&apiKey={api_key}"
    
    r = requests.get(url)
    content = r.json()
    
    articles = content['articles']

    result = []
    for article in articles:
        result.append(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}\n")
    
    return result

def main():
    news_list = get_news('US', "39612b1a081d457f9af5b22a54d6dc2b")
    
    for news in news_list:
        print(news)

if __name__ == "__main__":
    main()