## Deliverable 4

Team members submit the working code for their machine learning model, as well as the following:
## Description of data preprocessing:
The preprocessing of the data was done in jupyter notebook until the final week of preparing the final project. I moved the data into Colab in order to connect with the database our team member had created. The final steps of preprocessing were made and all error messages were corrected. All code is working and accomplished our preferred outcomes. 
The following functions were used to preprocess the data: 

--	fit_transform – I used LabelEncoder to transform the ‘geography’ column to a unique number for each location. Each location shared a duplicate number representing conventional and organic avocados. I also transformed the ‘type’ column into a numerical value for both types of avocados, conventional and prganic, with the numbers 1 and 0 respectively.

--	StandardScaler – I imported sklearn.preprocessing to fit and scale the ‘geography’ column for the model. 

## Description of feature engineering and the feature selection, including the team's decision-making process:
We decided to train our model to predict a location. In order for the model to work correctly it was important to convert the date, type and geography columns to numerical values. It was also important to determine which columns would represent the best features for the model. To accomplish the task our team decided to remove some of the rows of data that represented summarized sales data. For example, we dropped California in favor of keeping Los Angeles and San Francisco. We decided to do this because we didn’t want large sums of duplicated data to skew the prediction, if possible. 
I also used a heatmap to visualize the correlation between each feature column and we discovered a strong relationship among several of the columns. It was our decision to include all of the columns in the model because of the balance of the data.

## Description of how data was split into training and testing sets: 
The data was split using the ‘geography’ column as our test target and all remaining columns as our feature set. The data was randomly split 75/25. 

## Explanation of model choice, including limitations and benefits 
The choice of our model changed throughout the experience. There was a little confusion about our ability to predict a location using the ‘geography’ column with a regression model. However, we were aware that a classification model is capable of predicting at most two possible outcomes. We needed to use a regression model to account for the nearly forty possible outcomes from our data. We choose the linear regression model. The following points speak to the advantages and disadvantages we considered when we chose this model:

### Advantages –
1.	The algorithm is easy to implement and gives good results usually. It also has a lower time complexity when compared to other algorithms. And the mathematical equations are not that difficult to understand.
2.	Linear regression is good at finding the nature of the relationship between variables. With the strong relationship between variables in this dataset it made sense to use this to our advantage.
3.	Overfitting arises when a model fits a dataset very closely and captures the unnecessary or ‘noisy’ data at the cost of accurately predicting the best performance of the test set. Since we took the time to remove what we considered ‘noisy’ data from the dataset, we decided that this algorithm would work well with regularization to reduce the risk of overfitting the data.

### Disadvantages—
1.	Linear Regression is prone to underfitting which occurs when the function cannot fit the data well. Because the relationship between the variables isn’t often linear, a straight line won’t fit the data and a more complex function would be needed.
2.	 This algorithm is also sensitive to outliers which are extremely high or low values that deviate from the other data points.

## Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)  
We had looked at using classification algorithms but changed our mind wen we realized the full nature of our question and the limitations of the classification models to answer ‘yes’ or ‘no’ decisions. When we decided to use the Linear Regression algorithm, I needed to change several other steps to accurately train the dataset.   

## Description of how model was trained (or retrained if they are using an existing model) 
The model was trained using the same target and features as the previous deliverables. It was trained using the ‘geography’ column as the target and the remaining columns as the feature set.  

## Description and explanation of model’s confusion matrix, including final accuracy score:
From the research I’ve done a confusion matrix won’t work with the regression model we have chosen. Rather, the use of RMSE is preferred. Root Mean Square Error is the measure of how well a regression line fits the data points. The RMSE results for our Linear Regression model are:
train data: 0.9843
test data: 0.9951 

## Additionally, the model obviously addresses the question or problem the team is solving. Note: If statistical analysis is not included as part of the current analysis, include a description of how it would be included in the next phases of the project.
The model does address the problem our team is solving.

The next phases of the project might include additional graphs depicting the RMSE. We believe it would be a good idea to also look at population density as a factor in making the prediction for an appropriate location. Although Los Angeles and San Francisco both have dense populations when compared to the other locations it could possibly be helpful to have another column in the feature set with the data.  
