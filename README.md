# Concrete-Compressive-Strength-Estimation
## Concrete Compressive Strength Estimator: Project Overview
This projects aims to predict the compressive strength of concrete materials used in civil engineering. We trained a model on a dataset from the “UCI Machine Learning Repository”. We will train a regression model on the data and then build a very simple client interface with Flask.

## Exploratory Data Analysis:
In this step, we make descriptive analysis to explore and understand each variables in the data. The figures below show the distributions of each features and the correlations between each features.

![download](https://user-images.githubusercontent.com/105801284/204357736-e3917c26-bad2-4490-9d2a-4fb0732ce9b8.png)
![corr_plot](https://user-images.githubusercontent.com/105801284/204357802-e4aad9a9-76cf-4453-9ad1-ae207ceafcd7.png)

## Model Building:
Before we start model building, we remove outliers with the Isolation Forest Algorithm with 5% contamination then rescale the data with RobustScaler so that the rescaled will not be sensitive to some undetected outliers. After building regression models and hyperparameters tuning, the best model has R2 score of 90%. It is an ensemble method called "gradient boosting regressor" and its learning curves is shown below:
![learning_curves](https://user-images.githubusercontent.com/105801284/204358218-00d270b8-ca7b-4fa9-b817-a59190d71bb5.png)

## Streamlit APP VERSION:
You can easily run the streamlit app by changing to current directory to apps then run the app.py script
$ cd apps/
$ streamlit run app.py
