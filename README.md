# Salary Prediction using Machine Learning Model

## Project Overview
- Predict a continuous dependent variable from a number of independent variables using a regression model. The dataset was taken from [Stack Overflow Annual Developer Survey 2021](https://insights.stackoverflow.com/survey)
- Data transformation and machine learning to create a model that predicts a salary based on: country of residence, profession (job type), education level and years of experience. Access the full Python code **[here](https://github.com/ThiPauli/Salary_Prediction_ML/blob/main/salary_prediction_regression_ML.ipynb)**.
- Creating a User Interface (Web App) using streamlit and deploying it, which the end-users can input data and then get the predicted salary as the output. You can acess the web app [here](https://share.streamlit.io/thipauli/salary_prediction_ml/main/app.py).

## Objectives
* Making accurate salary predictions that are based on existing known salaries. As a result, the model can help companies and existing/future employees to negotiate more competitive payments.

## Methodology
- Data Wrangling - `Dropped misssing or null salaries values in the dataset, replacing the Years of Experience to the mean and analyzed outliers.`
- Exploratory Data Analysis - `Analyzed the data and summarized the main characteristics.`
- Data Visualization - `Used boxplot, bar plot, scatter plot and violin plot to visualize the data and it's characteristics.`
- Machine Learning Algorithms - ` The models trained were: Lasso, ElasticNet, Decision Tree Regressor, KNeighbors Regressor, Random Forest Regressor and Gradient Boosting Regressor.`
- Evaluation Metrics Used - `Mean Absolute Error (MAE) and R-squared`

## Web App (streamlit)
#### End-users are able to predict the output based on the features:
- **Country of residence:**: United States of America, Germany, Canada, Brazil, and so on.
- **Profession (job type):** Developer, full-stack, Developer, front-end, Data scientist or machine learning specialist, and so on.
- **Education Level:** Less than a Bachelor’s, Bachelor’s degree', Master’s degree or Postgraduate.
- **Years of Experience:** How many years of experience.

## Conclusions
* 

