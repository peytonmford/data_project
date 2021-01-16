# Avocado Prices: Organic or Conventional? 

## Deliverable 1
### Selected topic

The topic we have selected is the prices of avocados and what variables effect the price. Is it the type of avocado, for example does organic type make the price higher, or is the season/region? We aim to answer questions similar to these and see the real reason for the prices of avocados. 

### Reason they selected the topic

The reason we have selected the topic was due to the shared loved of avocados from half of the group. We saw this dataset and knew this is what we wanted to do our project over. While the dataset may need to be cleaned, we believe this is a great data source to complete the project. 

### Description of the source of data

We discovered this dataset on kaggle by Hass Avocado Board Website (2013-2020). This dataset has 13 columns, including: average price, total volume, product look-up code, bag sizes of avocados, the type of avocados, year, and geography of where it was being sold. This dataset has over 30,000 rows of data. 

### Questions they hope to answer with the data

Is the avocado's being bought going to be conventional or organic? The type of the avocado could indicate a reason why the price is the way it is. 

### Who Did What:
Pete did the machine learning, Tania did the database, and Peyton did all the Github.

# Deliverable 2 - Machine Learning Role Team members submit the code for their machine learning model, as well as the following:
## Description of preliminary data preprocessing
I began the preprocessing by reading the dataset into a jupyter notebookusing pandas. I created a pandas dataframe to take a look at the structure of the dataset. I paid attention to the number of rows and columns, the column headings, and the different types of data in the dataset that were identifiable by just looking at the data. Next i took a deeper look at the data and the info by using the .info function to learn how many rows and columns there are in the dataset, to see if the data was well organized, and to see the non-null count. I then checked for missing data using the .isnull().sum() function. Just to make sure, I examined the data for null values and dropped the null rows and columns where all values were null. I then took a look at the specific types of data by running the .dtypes function. 
## Description of preliminary feature engineering and preliminary feature selection, including their decisionmaking process  
I began the preliminary feature engineering by realizing that the machine learning model would need for all columns to be numbers, not time, date or geographic locations. I changed the date using to.datetime, changed the type column using .replace, and reduced the number of geographic locations to those locations that represented specific areas and not summarized areas. For example, I deleted California in favor of keeping Los Angeles and San Franciso. I wanted to make sure large numbers of data did not skew my results unnecessarily.
## Description of how data was split into training and testing sets
Since the purpose of the project is to predict a location I decided the test column would be geography. I ran .corr over the dataframe and plotted the results to see the heatmap results of how the cloumns were related to each other. I determined from my observation to use all of the remaining columns as features for the model.
## Explanation of model choice, including limitations and benefits
I ran several different models and decided to use Random Forest Regression because it does well with many regression tasks because of its nonlinear nature, uses leafs that reduce the complexity and tends to generalize the model better than other models I tried. The RFR cannot extrapolate, but I didn't need that feature for this task because I need a prediction that is an average of previously observed labels. RFR provided the better accuracy over the data. I also tried Lasso, Ridge and Polynomial models.  
   
