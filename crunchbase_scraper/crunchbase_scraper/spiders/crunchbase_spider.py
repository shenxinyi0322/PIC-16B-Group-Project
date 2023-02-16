# to run 
# scrapy crawl crunchbase_spider -o unicorn_company.csv

import scrapy
import pandas as pd
import numpy as np

class CrunchbaseSpider(scrapy.Spider):
    name = 'crunchbase_spider'
    
    start_urls = ['https://www.crunchbase.com/home']
    
    def parse(self, response):
        # read the csv file
        df = pd.read_csv('unicorn.csv')

        # change all company names to lower case
        df["urlsub"]=df["Company"].str.lower()

        # drop NaN values in the dataframe
        df = df.dropna(axis=0,how='all')
        df = df.dropna(axis=1,how='all')
        urlsub_table = df[['urlsub']]
        
        for i in range(len(urlsub_table)):
            url_addition = urlsub_table.iloc[i,0]
            organization_url = 'https://www.crunchbase.com/organization/' + url_addition 
            yield scrapy.Request(organization_url, callback = self.parse_company)
            
            
    def parse_company(self, response):       
        company_financials_url = response.urljoin('/company_financials')
        yield scrapy.Request(company_financials_url, callback = self.parse_company_financials)
        people_url = response.urljoin('/people')
        yield scrapy.Request(people_url, callback = self.parse_company_people)
        technology_url = response.urljoin('/technology')
        yield scrapy.Request(technology_url, callback = self.parse_technology)
        
    def parse_company_financials(self, response):
        pass
        
    def parse_company_people(self, response):
        pass
    
    def parse_company_technoloy(self, response):
        pass