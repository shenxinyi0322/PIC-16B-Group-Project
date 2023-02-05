# PIC-16B-Group-Project
## Abstract
We live in a fast-growing world with around 4.4 million startups created every year. It is very possible that we might one day work for a startup business, invest in startups, or start a company on our own. In this project, we will analyze the trend of newest unicorn startups in the past few years to find the fastest-growing industries or the startup company with highest potentials using data scraped from the internet. We will also look into the characteristics of successful companies (such as their founders, products, revenue stream) to find the important qualities that contribute to a company's success. Results will be displayed through interactive visualizations, providing valuable insights for venture capital companies, private equity investors, and aspiring startup entrepreneurs.

The technical components of our project include: 
Web-scraping, collecting information from websites/Linkedin
Create and deploy machine learning algorithms that evaluates the success of companies
Perform SHAP analysis to evaluate the importance of each features (characteristics of companies)
create interactive visualizations to display the results


## Planned Deliverables
For this project, we plan to create a novel data set, a machine learning model with high accuracy (say R-squared higher than 0.8), and visualizations of feature importance and effects. 
For Full Success, we would successfully web-scrape data from Linkedin and wikipedia to enlarge our current dataset, have a machine learning model with high accuracy (say R-squared higher than 0.8), successfully perform SHAP analysis on the machine learn model, visualize and analyze the results, and write a report of our findings and located explanations to our findings. 
For Partial Success, while we may not be able to fully web-scrape data from Linkedin and wikipedia to enlarge our current dataset, as long as we find ways to web-scrape some data from the internet, the dataset would be considered partial success. Additionally, machine learning models with decent accuracy (not necessarily 0.8, but at least should show efforts of hyperparameter optimizations) would be considered partial success. Above are the two problems we hypothesize that we may run into, and the partial-success solution to each case. 

 

## Resources Required
Since this project is aimed to create a novel dataset and learn the features of a successful startup company, we need resources of various data to build our model. Our basic dataset is acquired from CBinsights, which is called The Complete List Of Unicorn Companies. This dataset includes over 1200 companies’ six features, where only two of them can be considered as numerical variables. Realizing that more information is required to conduct the study, we plan to use web-scraping techniques on LinkedIn, crunchbase, and possibly Wikipedia. From these websites, we are able to get data about the number of employees, number of followers, and funding amount etc. The links to the dataset and webpages are attached below. 

The Complete List Of Unicorn Companies data set from CBinsights: https://www.cbinsights.com/research-unicorn-companies 
Examples of the webpages for scraping:
LinkedIn: ByteDance, Zhaogang
Crunchbase: SpaceX, Instacart
Wikipedia: ByteDance, Xiaohongshu


## Tools and Skills Required
Since this project aims to create a novel dataset and learn the features of a successful startup company, machine learning is required. Potential Python packages are Numpy, Scikit-learn, PyTorch, and pandas. Before establishing and training the model, we need to indicate features for evaluating the success of companies. Therefore, more quantitative data needs to be included in our current dataset. For such a purpose, web scraping will be conducted through packages like Scrapy to extract quantitative data from the company’s related websites. Meanwhile, we could utilize natural language processing models to evaluate the annual financial reports of these companies, obtaining more measurables. Finally, after determining the features of a successful startup company, we can present them through complex and interactive data visualization, in which Bokeh and Plotly are two good libraries to include.


## What You Will Learn
Covering web-scraping, data cleansing and analysis, and visualization, this project will bring us  an integrated learning experience in data science. Our first learning goal would be to create an ideal database with appropriate web-scraping techniques; as we are extracting data from a variety of sources, including CBinsigts, Crunchbase, Linkedin, etc., we are expecting challenges to transform the raw information into accurate, quantitative data for analysis. Another major learning goal is to select the appropriate variables and models for machine learning; as the companies vary from each other in many aspects, such as specialization, size, funding stages, etc., it is uncertain what variables and models are the most accurate in predicting the success of the companies, so we are expecting to deal with this concern by testing a great number of models, including but not limited to Neural Network Model and Random Forest Regression Model. 


## Risks
The first concern we have is the inconsistency of data from different internet sources. As we are scraping data from multiple sources and we are expecting to deal with a certain amount of qualitative data, inconsistencies among different sources may occur and may lead to ineffective data analysis. To address this concern, we could study and utilize more approaches to deal with missing or inaccurate data, such as, substituting missing data with mean.

Our second concern is the applicability of machine learning. Even if we succeed in training our dataset, the prediction of our model may not be accurate to other companies due to a number of factors, such as, the great discrepancy between companies, the limited access to key financial index, etc. To address this concern, we have to scrape as much data as we can before data processing, and we are expecting to test each combination of variables of machine learning models to compare their predictions and select the most optimized model. 


## Ethics
The existence of our product will benefit various stakeholders. For venture capital companies and private equity investors, this product can provide them with better evaluations of the potential success of a company and make smarter investment decisions. It will also help startup entrepreneurs or individuals looking to work in startup companies to understand factors that drive success at the company, allowing them to determine traceable objects and choose more sustainable companies as a career. 

This product may also harm different stakeholders due to confounding variables and a lack of inclusivity within the dataset. Since the companies come from different industries and countries, these features generated may not equally evaluate startups with all backgrounds. Such generalizations may lead to inaccurate predictions, leading to bad decision-making. ,

Overall, the world will become an overall better place due to this product. Firstly,  since essential qualities to a startup's success are indicated, entrepreneurs are more likely to succeed in building their startups based on such guidelines. Secondly, since a more detailed evaluation of a startup's success is created, it will help existing startups with great potential to gain more funding to accelerate their achievements.

## Tentative Timeline
Feb 16: Project update presentation I:
- Attend the discussions in person
- Show web-scraping process
- Have Machine Learning Models Completed 
- Visualized Findings

Mar 7: Project update presentation II
- Attend the discussions in person
- Complete web-scraping process
- Tuned Hyperparameters and Optimized Machine Learning Models
- Visualizations and Explanations for them

## TicTacToe

O X .<br>
. O .<br>
X . O<br>


