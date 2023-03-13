import scrapy
from googlesearch import search
import pandas as pd
import csv
from bs4 import BeautifulSoup


class GoogleSpider(scrapy.Spider):
    name = "google_spider"
    
    
    def start_requests(self):
        with open('crunchbase_data.csv', newline='') as csvfile:
            df = csv.reader(csvfile)
            
        mylist =  list(df["Company"])
        string = 'crunchbase '
        mylist = [ string + s for s in name]
        
        keywords = mylist
        for keyword in keywords:
            for url in search(keyword, num_results=1):
                yield scrapy.Request(url=url, callback=self.parse)
                
    
    
    def parse(self, response):
        
        response = requests.get(url)
        html_content = response.text

        # parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # find the first search result link using CSS selector
        search_result = soup.select_one('div.BNeawe.UPmit.AP7Wnd > a')['href']

        # print the link
        print(search_result)
        
        
        
        # results = response.css('div.g')
        # for result in results:
        #     title = result.css('h3::text').get()
        #     link = result.css('a::attr(href)').get()
        #     yield {
        #         'title': title,
        #         'link': link
        #     }
