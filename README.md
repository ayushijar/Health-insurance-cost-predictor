# Health-insurance-cost-predictor :

This web application leverages machine learning and is powered by Flask to provide accurate predictions of medical insurance costs. By inputting key features such as age, gender, body mass index, number of children, smoking status, and region through the user-friendly web interface, users can obtain personalized forecasts for their insurance premiums.


# Screenshots of user interface :

 ![Alt text](<Initial-Interface.png>) 
 
 ![Alt text](<Input-Values.png>)

 ![Alt text](<Predicted-Results.png>)


# Data collection and training :

- Data was collected and separated into train and test data.
- Separate pipelines for data cleaning, transformation, and feature engineering were created to prevent data leakage. 
- Sklearn pipelines were utilized for preprocessing and transformations on both the training and test data independently, ensuring a streamlined and clean code approach. 
- The attached Jupyter notebook comprehensively covers exploratory data analysis, the creation of sklearn pipelines, and detailed model selection. 
- Five distinct pipelines were employed to train various regression models (Vanilla Linear Regression, Lasso and Ridge versions of Linear regression, Decision Tree, Random Forest). 
- Hyperparameter tuning was conducted through grid search CV. 
- Based on metric results, the Random Forest model outperformed others, with better accuracy compared to Decision Tree which exhibited signs of overfitting. 
- The best model was saved as a pickle file.

# Tasks performed :
<ul>
    <li>Exploring the dataset and performing exploratory data analysis.</li>
    <li>Converting Categorical values to Numerical.</li>
    <li>Plotting Heatmap to see dependency of Dependent value on Independent features.</li>
    <li>Data Visualization (Plots of feature vs feature).</li>
    <li>Plotting Skew and Kurtosis.</li>
    <li>Data Preparation.</li>
    <li>Prediction using Linear Regression.</li>
    <li>Prediction using Lasso and Ridge version of Linear Regression.</li>
    <li>prediction using Decision Tree classifier.</li>
    <li>Prediction using Random Forest Regression.</li>
    <li>Performing Hyper tuning for above mentioned models.</li>
    <li>Preparing model for deployment.</li>
    <li>Deployed model using Flask.</li>
    <li>Created a user interface integrated with model for predictions.</li>
</ul>

# Results :

-  Model gave 86% accuracy for Medical Insurance Amount Prediction using Random Forest Regression.

## :file_folder: Dataset
The dataset used can be downloaded here (Kaggle) - [Click to Download](https://www.kaggle.com/mirichoi0218/insurance)
