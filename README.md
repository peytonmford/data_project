# Deliverable 4

### Result of Analysis:
Best Locations:
Los Angeles, California
San Francisco, California 
Plan:
Pick a limit of stores to test our new product with avocados 

### Recommendation for future analysis:

### Anything the team would have done differently


# Best Locations to Sell New Avocado Product

## Deliverable 1
### Selected topic

The topic we have selected is the prices of avocados and what variables effect the price. Is it the type of avocado, for example does organic type make the price higher, or is the season/region? We aim to answer questions similar to these and see the real reason for the prices of avocados. 

### Reason we have selected the topic

The reason we have selected the topic was due to the shared loved of avocados from half of the group. We saw this dataset and knew this is what we wanted to do our project over. While the dataset may need to be cleaned, we believe this is a great data source to complete the project. 

### Description of the source of data

We discovered this dataset on Kaggle by Hass Avocado Board Website (2013-2020). This dataset has 13 columns, including: average price, total volume, product look-up code, bag sizes of avocados, the type of avocados, year, and geography of where the avocado was being sold. This dataset has over 30,000 rows of data. 

### Questions they hope to answer with the data

As Chipotle’s endeavor to expand a new avocado product, where are the best locations for testing a new product for the best avocado prices?

# Deliverable 2 - Machine Learning Role Team members submit the code for their machine learning model, as well as the following:
## Description of preliminary data preprocessing
I began the preprocessing by reading the dataset into a jupyter notebook using pandas. I created a pandas dataframe to take a look at the structure of the dataset. I paid attention to the number of rows and columns, the column headings, and the different types of data in the dataset that were identifiable by just looking at the data. Next I took a deeper look at the data and the info by using the .info function to learn how many rows and columns there are in the dataset, to see if the data was well organized, and to see the non-null count. I then checked for missing data using the .isnull().sum() function. Just to make sure, I examined the data for null values and dropped the null rows and columns where all values were null. I then took a look at the specific types of data by running the .dtypes function. 
## Description of preliminary feature engineering and preliminary feature selection, including their decisionmaking process  
I began the preliminary feature engineering by realizing that the machine learning model would need for all columns to be numbers, not time, date or geographic locations. I changed the date using to.datetime, changed the type column using .replace, and reduced the number of geographic locations to those locations that represented specific areas and not summarized areas. For example, I deleted California in favor of keeping Los Angeles and San Franciso. I wanted to make sure large numbers of data did not skew my results unnecessarily.
## Description of how data was split into training and testing sets
Since the purpose of the project is to predict a location I decided the test column would be geography. I ran .corr over the dataframe and plotted the results to see the heatmap results of how the cloumns were related to each other. I determined from my observation to use all of the remaining columns as features for the model.
## Explanation of model choice, including limitations and benefits
I ran several different models and decided to use Random Forest Regression because it does well with many regression tasks because of its nonlinear nature, uses leafs that reduce the complexity and tends to generalize the model better than other models I tried. The RFR cannot extrapolate, but I didn't need that feature for this task because I need a prediction that is an average of previously observed labels. RFR provided the better accuracy over the data. I also tried Lasso, Ridge and Polynomial models.  
### Google Slides
https://docs.google.com/presentation/d/1afKGKIfgfxIHac8w4pZt3iSGRL1X7rJ6-6nF6OLW_ko/edit#slide=id.gb4a23a5970_0_354


# Deliverable 3 

### Description of the data exploration phase of the project:
- We want to see where the best locations would be to set up Chipotle stores around the country.
- First, we looked at the prices statewide to give us a general understanding. 
- Then, we moved onto specific regions and then cities.
- We will be using Tableau for our data exploration and by using the “Details” function, users can hover over each individual visual to see the exact averages.

### Description of the analysis phase of the project:
- Clean the data
  - Remove null values
  - Ambiguity values ex: Total U.S was too broad 
  - Changing the nomical value to numeric value
- Take the cleaned data (CSV) and create a database 
  - Create an ERD - Entity–relationship model
  - PostgresSQL will be used 
  - Creat tables
    - Inner join
- Take the tables that was created and apply Machine Learning to answer our main question: As Chipotle’s endeavor to expand a new avocado product, which location would be the best to sell avocados to? 
  - Python
    - Pandas
    - NumPy
    - VS Code
    - Jupyter Notebook
      - RandomForest Regression
      - Polynomial Regression
      - Ridge Regression
      - Lasso Regression
      - Bayesian Ridge Regression

### Technologies, languages, tools, and algorithms used throughout the project:
- PostGres
- Tableau
- Python
  - Pandas
  - NumPy
  - VS Code
  - Jupyter Notebook
    - RandomForest Regression
    - Polynomial Regression
    - Ridge Regression
    - Lasso Regression
    - Bayesian Ridge Regression

## Machine Learning Role: Team member submits the code for machine learning model, as well as the following:
### Description of data preprocessing 
I've been experiencing some instances of error messages that read, "strings were unable to be converted to floats". The challenge has been to figure out why some locations in the 'geography' column are not converting from words to numbers even after label encoding. I haven't figured it out, yet.   
### Description of feature engineering and the feature selection, including their decisionmaking process
The features have worked well in the training and testing of the data. The challenge has been working with the 'geography' column and converting the data to numbers for the machine learing model. The results clearly state that the desired results have been produced, but later in the process error codes continue to arise stating the strings have not been converted to floats.
### Description of how data was split into training and testing sets
No changes have been made to the code pertaining to how the data was split.
### Explanation of model choice, including limitations and benefits 
I ran several different models and decided to use Random Forest Regression because it does well with many regression tasks because of its nonlinear nature, uses leafs that reduce the complexity and tends to generalize the model better than other models I tried. The RFR cannot extrapolate, but I didn't need that feature for this task because I need a prediction that is an average of previously observed labels. RFR provided the better accuracy over the data. I also tried Lasso, Ridge and Polynomial models.  
### Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables) 
I decided to include the other four models that were rejected in the final code: Lasso, Ridge, Polynomial, and Bayesian Ridge for the purpose of comparison. No changes have been made to the model choice, only the inclusion of additional models for support of why I chose Random Forest.
### Description of the trained model(s) thus far, and any additional training that will take place  
### Description of current accuracy score 
The slide depicting the current accuracy score is found in our google slides. The following results are for the Random Forest model:

train data accuracy : 0.9760720442962847

test data accuracy : 0.8258906559136814

loss of train data : 3.364313990347702

loss of test data : 23.925179973678443
### Additionally, the model obviously addresses the question or problem the team is solving
The model does address the question of location as the target of the machine learning model. I will continue to work on creating validation pots and graphs for the next deliverable and our presentation next week.
### Google Slides
https://docs.google.com/presentation/d/1afKGKIfgfxIHac8w4pZt3iSGRL1X7rJ6-6nF6OLW_ko/edit#slide=id.gb4a23a5970_0_354

### Tableau Link
https://public.tableau.com/profile/peyton5401#!/vizhome/AvocadoPrices_16112778290490/AvocadoPrices
