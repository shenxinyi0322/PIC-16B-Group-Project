# PIC-16B-Group-Project
## Introduction

We live in a fast-growing world with around 4.4 million startups created every year. It is very possible that we might one day work for a startup business, invest in startups, or start a company on our own. In this project, we will analyze the trend of newest unicorn startups in the past few years to find the fastest-growing industries or the startup company with highest potentials using data scraped from the internet. We will also look into the characteristics of successful companies (such as their founders, products, revenue stream) to find the important qualities that contribute to a company's success. Results will be displayed through interactive visualizations, providing valuable insights for venture capital companies, private equity investors, and aspiring startup entrepreneurs.

Blog Post: https://shenxinyi0322.quarto.pub/myblog/posts/project/project.html

Our Project can be divided into 5 different steps:
- Webscraping from Google to determine the Crunchbase Links
- Webscraping from Crunchbase for Data Augmentation
- Data Augmentation using ChatGPT API
- Predictive Modeling and SHAP Analysis
- Website Developing



## What You Will Learn
Covering web-scraping, data cleansing and analysis, web development, and visualization, this project will bring us  an integrated learning experience in data science. Our first learning goal would be to create an ideal database with appropriate web-scraping techniques; as we are extracting data from a variety of sources, including CBinsigts, Crunchbase, Wikipedia, etc., we are expecting challenges to transform the raw information into accurate, quantitative data for analysis. Another major learning goal is to select the appropriate variables and models for machine learning; as the companies vary from each other in many aspects, such as specialization, size, funding stages, etc., it is uncertain what variables and models are the most accurate in predicting the success of the companies, so we are expecting to deal with this concern by testing a great number of models, including but not limited to Neural Network Model and Random Forest Regression Model. Finally, the result will be displayed in an interactive web page where you can search for company's name and features to see the corresponding information and analytical visualization.


## Risks
The first concern we have is the inconsistency of data from different internet sources. As we are scraping data from multiple sources and we are expecting to deal with a certain amount of qualitative data, inconsistencies among different sources may occur and may lead to ineffective data analysis. To address this concern, we could study and utilize more approaches to deal with missing or inaccurate data, such as, substituting missing data with mean.

Our second concern is the applicability of machine learning. Even if we succeed in training our dataset, the prediction of our model may not be accurate to other companies due to a number of factors, such as, the great discrepancy between companies, the limited access to key financial index, etc. To address this concern, we have to scrape as much data as we can before data processing, and we are expecting to test each combination of variables of machine learning models to compare their predictions and select the most optimized model. 



## Github Instruction
This Github Repo includes our code and dataset used for this project. For the web development part, please refer our blog post. 
- `crunchbase_data.csv` is our raw data obtained from CB Insights.
- `get_links.ipynb` and `crunchbase_links.csv` are how we get all the Crunchbase links.
- `crunchbase git` folder includes everything for scraping the Crunchbase data.
- files stared with `VC` are our code for model and SHAP analysis.
- `VC_Final_Data.csv` is the finalized full dataset.

