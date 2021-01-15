{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import dependencies\n",
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn import tree\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix, accuracy_score, classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "       date  average_price  total_volume       4046       4225      4770  \\\n",
       "0  1/4/2015           1.22      40873.28    2819.50   28287.42     49.90   \n",
       "1  1/4/2015           1.79       1373.95      57.42     153.88      0.00   \n",
       "2  1/4/2015           1.00     435021.49  364302.39   23821.16     82.15   \n",
       "3  1/4/2015           1.76       3846.69    1500.15     938.35      0.00   \n",
       "4  1/4/2015           1.08     788025.06   53987.31  552906.04  39995.03   \n",
       "\n",
       "   total_bags  small_bags  large_bags  xlarge_bags          type  year  \\\n",
       "0     9716.46     9186.93      529.53          0.0  conventional  2015   \n",
       "1     1162.65     1162.65        0.00          0.0       organic  2015   \n",
       "2    46815.79    16707.15    30108.64          0.0  conventional  2015   \n",
       "3     1408.19     1071.35      336.84          0.0       organic  2015   \n",
       "4   141136.68   137146.07     3990.61          0.0  conventional  2015   \n",
       "\n",
       "              geography  \n",
       "0                Albany  \n",
       "1                Albany  \n",
       "2               Atlanta  \n",
       "3               Atlanta  \n",
       "4  Baltimore/Washington  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>date</th>\n      <th>average_price</th>\n      <th>total_volume</th>\n      <th>4046</th>\n      <th>4225</th>\n      <th>4770</th>\n      <th>total_bags</th>\n      <th>small_bags</th>\n      <th>large_bags</th>\n      <th>xlarge_bags</th>\n      <th>type</th>\n      <th>year</th>\n      <th>geography</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1/4/2015</td>\n      <td>1.22</td>\n      <td>40873.28</td>\n      <td>2819.50</td>\n      <td>28287.42</td>\n      <td>49.90</td>\n      <td>9716.46</td>\n      <td>9186.93</td>\n      <td>529.53</td>\n      <td>0.0</td>\n      <td>conventional</td>\n      <td>2015</td>\n      <td>Albany</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1/4/2015</td>\n      <td>1.79</td>\n      <td>1373.95</td>\n      <td>57.42</td>\n      <td>153.88</td>\n      <td>0.00</td>\n      <td>1162.65</td>\n      <td>1162.65</td>\n      <td>0.00</td>\n      <td>0.0</td>\n      <td>organic</td>\n      <td>2015</td>\n      <td>Albany</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1/4/2015</td>\n      <td>1.00</td>\n      <td>435021.49</td>\n      <td>364302.39</td>\n      <td>23821.16</td>\n      <td>82.15</td>\n      <td>46815.79</td>\n      <td>16707.15</td>\n      <td>30108.64</td>\n      <td>0.0</td>\n      <td>conventional</td>\n      <td>2015</td>\n      <td>Atlanta</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1/4/2015</td>\n      <td>1.76</td>\n      <td>3846.69</td>\n      <td>1500.15</td>\n      <td>938.35</td>\n      <td>0.00</td>\n      <td>1408.19</td>\n      <td>1071.35</td>\n      <td>336.84</td>\n      <td>0.0</td>\n      <td>organic</td>\n      <td>2015</td>\n      <td>Atlanta</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1/4/2015</td>\n      <td>1.08</td>\n      <td>788025.06</td>\n      <td>53987.31</td>\n      <td>552906.04</td>\n      <td>39995.03</td>\n      <td>141136.68</td>\n      <td>137146.07</td>\n      <td>3990.61</td>\n      <td>0.0</td>\n      <td>conventional</td>\n      <td>2015</td>\n      <td>Baltimore/Washington</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 2
    }
   ],
   "source": [
    "## Read in the dataset from wherever it is located\n",
    "data = 'avocado-updated-2020.csv'\n",
    "df = pd.read_csv(data)\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "   average_price  total_volume  total_bags type\n",
       "0           1.22      40873.28     9716.46    1\n",
       "1           1.79       1373.95     1162.65    0\n",
       "2           1.00     435021.49    46815.79    1\n",
       "3           1.76       3846.69     1408.19    0\n",
       "4           1.08     788025.06   141136.68    1"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>average_price</th>\n      <th>total_volume</th>\n      <th>total_bags</th>\n      <th>type</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1.22</td>\n      <td>40873.28</td>\n      <td>9716.46</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1.79</td>\n      <td>1373.95</td>\n      <td>1162.65</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1.00</td>\n      <td>435021.49</td>\n      <td>46815.79</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1.76</td>\n      <td>3846.69</td>\n      <td>1408.19</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1.08</td>\n      <td>788025.06</td>\n      <td>141136.68</td>\n      <td>1</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 53
    }
   ],
   "source": [
    "#Remove the non-essential columns for machine learning model\n",
    "#df.drop(columns =['geography', '4046', '4225', '4770', 'total_bags', 'small_bags', 'large_bags', 'xlarge_bags', 'date', 'year'])\n",
    "#ml_df = df[['average_price','total_volume', '4046', '4225','4770','total_bags','type']]\n",
    "ml_df = df[['average_price','total_volume','total_bags','type']]\n",
    "ml_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the words in the column 'type' to numbers for the machine learning model\n",
    "#ml_df.type.map(dict(conventional=1, organic=0))\n",
    "#ml_df = pd.get_dummies(df, columns=[\"type\"])\n",
    "#ml_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "#df.type.map(dict(conventional=1, organic=0))\n",
    "#df = df.replace(to_replace=\"conventional\", value=\"1\")\n",
    "#df = df.replace(to_replace=\"organic\", value=\"0\")\n",
    "#df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change the 'total_volume' column dtype to a float for the machine learning model\n",
    "#ml_df['total_volume'].astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "   average_price  total_volume  total_bags\n",
       "0           1.22      40873.28     9716.46\n",
       "1           1.79       1373.95     1162.65\n",
       "2           1.00     435021.49    46815.79\n",
       "3           1.76       3846.69     1408.19\n",
       "4           1.08     788025.06   141136.68"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>average_price</th>\n      <th>total_volume</th>\n      <th>total_bags</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1.22</td>\n      <td>40873.28</td>\n      <td>9716.46</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1.79</td>\n      <td>1373.95</td>\n      <td>1162.65</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1.00</td>\n      <td>435021.49</td>\n      <td>46815.79</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1.76</td>\n      <td>3846.69</td>\n      <td>1408.19</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1.08</td>\n      <td>788025.06</td>\n      <td>141136.68</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 57
    }
   ],
   "source": [
    "#Define the features set\n",
    "X = ml_df.copy()\n",
    "X = X.drop(\"type\", axis=1)\n",
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array(['1', '0', '1', '0', '1'], dtype=object)"
      ]
     },
     "metadata": {},
     "execution_count": 58
    }
   ],
   "source": [
    "#Define the target set\n",
    "y = ml_df[\"type\"].values\n",
    "y[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Format the independent variable in the model\n",
    "#y = ml_df['type'].values.reshape(-1, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the shape\n",
    "#print(y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "#y = ml_df[\"type\"]\n",
    "#X = ml_df.drop(columns=\"type\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "(22515, 3)"
      ]
     },
     "metadata": {},
     "execution_count": 62
    }
   ],
   "source": [
    "# Split the data into traing and testing sets\n",
    "#from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)\n",
    "X_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "(22515, 3)\n(7506, 3)\n(22515,)\n(7506,)\n"
     ]
    }
   ],
   "source": [
    "# Determine the shape of our training and testing sets.\n",
    "print(X_train.shape)\n",
    "print(X_test.shape)\n",
    "print(y_train.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Splitting into Train and Test sets into an 80/20 split.\n",
    "X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, random_state=78, train_size=0.75)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "(22515, 3)\n(7506, 3)\n(22515,)\n(7506,)\n"
     ]
    }
   ],
   "source": [
    "# Determine the shape of our training and testing sets.\n",
    "print(X_train2.shape)\n",
    "print(X_test2.shape)\n",
    "print(y_train2.shape)\n",
    "print(y_test2.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "#from sklearn.linear_model import LogisticRegression\n",
    "#classifier = LogisticRegression(solver='lbfgs',\n",
    "                               #max_iter=200,\n",
    "                               #random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "#classifier.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating a StandardScaler instance.\n",
    "scaler = StandardScaler()\n",
    "# Fitting the Standard Scaler with the training data.\n",
    "X_scaler = scaler.fit(X_train)\n",
    "\n",
    "# Scaling the data.\n",
    "X_train_scaled = X_scaler.transform(X_train)\n",
    "X_test_scaled = X_scaler.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating the decision tree classifier instance.\n",
    "model = tree.DecisionTreeClassifier()\n",
    "# Fitting the model.\n",
    "model = model.fit(X_train_scaled, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Making predictions using the testing data.\n",
    "predictions = model.predict(X_test_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "          Predicted 0  Predicted 1\n",
       "Actual 0         3504          173\n",
       "Actual 1          165         3664"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Predicted 0</th>\n      <th>Predicted 1</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Actual 0</th>\n      <td>3504</td>\n      <td>173</td>\n    </tr>\n    <tr>\n      <th>Actual 1</th>\n      <td>165</td>\n      <td>3664</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 71
    }
   ],
   "source": [
    "# Calculating the confusion matrix\n",
    "cm = confusion_matrix(y_test, predictions)\n",
    "\n",
    "# Create a DataFrame from the confusion matrix.\n",
    "cm_df = pd.DataFrame(\n",
    "    cm, index=[\"Actual 0\", \"Actual 1\"], columns=[\"Predicted 0\", \"Predicted 1\"])\n",
    "\n",
    "cm_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculating the accuracy score.\n",
    "acc_score = accuracy_score(y_test, predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Confusion Matrix\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "          Predicted 0  Predicted 1\nActual 0         3504          173\nActual 1          165         3664",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Predicted 0</th>\n      <th>Predicted 1</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Actual 0</th>\n      <td>3504</td>\n      <td>173</td>\n    </tr>\n    <tr>\n      <th>Actual 1</th>\n      <td>165</td>\n      <td>3664</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {}
    },
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Accuracy Score : 0.9549693578470557\nClassification Report\n              precision    recall  f1-score   support\n\n           0       0.96      0.95      0.95      3677\n           1       0.95      0.96      0.96      3829\n\n    accuracy                           0.95      7506\n   macro avg       0.95      0.95      0.95      7506\nweighted avg       0.95      0.95      0.95      7506\n\n"
     ]
    }
   ],
   "source": [
    "# Displaying results\n",
    "print(\"Confusion Matrix\")\n",
    "display(cm_df)\n",
    "print(f\"Accuracy Score : {acc_score}\")\n",
    "print(\"Classification Report\")\n",
    "print(classification_report(y_test, predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.9 64-bit ('mlenv': conda)",
   "metadata": {
    "interpreter": {
     "hash": "9a0cf610b77f61a831486a47fdef06479ba37a7586d8434d51eece190bc25500"
    }
   }
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9-final"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}