# Diabetes Prediction - Models and Analysis

## Project Description

This project aims to predict the presence of diabetes in patients based on a set of medical variables. Several machine learning models were tested and compared to identify the one offering the best performance.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Model Saving](#model-saving)
3. [Deployment](#deployment)
4. [Prerequisites](#prerequisites)
5. [Execution Instructions](#execution-instructions)
6. [Authors](#authors)
7. [License](#license)

## Project Structure

### 1. Global Import

Importing the necessary libraries such as `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, and `tensorflow`.

### 2. Global Functions

- `show_graphics`: Visualizes the relationships between independent variables and the target.
- `show_corr_matrix`: Displays the correlation matrix.
- `plot_bar_and_pie`: Graphically represents distributions.
- `select_best_variable`: Selects the best predictive variable.
- `multiple_regression`: Performs multiple linear regression.
- `verify_vif`: Checks for multicollinearity between variables.
- `feature_selection_with_rf`: Selects features using Random Forest.

### 3. Data Understanding

- **Data Size**: 15,000 rows and 10 columns.
- **Column Types**: 8 integer columns and 2 float columns.
- **No Missing Values**: All values are present.
- **Descriptive Statistics**: Analysis of means, medians, and standard deviations.

### 4. Feature Analysis

This section aims to analyze the different features of the dataset to identify the most relevant variables for diabetes prediction.

- **Scatter Plot Visualization**: Graphs were generated to visualize the relationship between each independent variable and the target variable (`Diabetic`), helping to detect possible trends and outliers.
- **Correlation Matrix**: The correlation matrix highlighted the relationships between the different variables. It was observed that some variables like `Pregnancies`, `PlasmaGlucose`, `BMI`, and `Age` showed a stronger correlation with the target variable.
- **Selection of Relevant Variables**: Following this analysis, the most significant variables for prediction were identified:
  - `Pregnancies`: Number of pregnancies.
  - `PlasmaGlucose`: Plasma glucose concentration.
  - `BMI`: Body mass index.
  - `Age`: Patient's age.
  - `SerumInsulin`, `TricepsThickness`, `DiastolicBloodPressure`, and `DiabetesPedigree` were also considered, although their influence was less pronounced.
- **Hypothesis Validation**: Statistical tests were conducted to validate these observations and ensure that the selected variables contribute significantly to the prediction.

### 5. Modeling and Prediction

Different models were trained and evaluated:

- **Linear Regression**: R² of 34%.
- **Logistic Regression**: Accuracy of 79%.
- **Decision Tree**: Accuracy of 89%.
- **SVM (RBF Kernel)**: Accuracy of 83%.
- **Neural Network**: Accuracy of 90%.
- **K-Nearest Neighbors**: Accuracy of 84%.
- **Gradient Boosting Classifier**: Best model with an accuracy of 95%.

### 6. Conclusion

The **Gradient Boosting Classifier** proved to be the most efficient model with an accuracy of 95.24%. This model was saved for future use.

## Model Saving

The final model was saved as `grandiantBoostingClassifier.pkl` using the `joblib` library.

## Deployment

The model was integrated into a web application and deployed via Docker on an AWS EC2 server.

- **Web Application**: A user interface was developed to allow the submission of patient data and real-time diabetes prediction.
- **Docker**: The application was containerized to ensure portability and simplify deployment.
- **AWS EC2**: Deployment was carried out on an AWS EC2 instance, ensuring high availability and optimal scalability.
- **Application URL**: [Access the application](http://ec2-13-53-216-86.eu-north-1.compute.amazonaws.com:5000/)

## Prerequisites

- Python 3.x
- Libraries: pandas, numpy, scikit-learn, seaborn, matplotlib, tensorflow, keras

## Execution Instructions

1. Clone the GitHub repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the notebook or Python scripts to reproduce the analyses and models.

## Authors

- Peyanan Traore
- Melvin Ravi
- Justin Djidonou
- Harishankar Murugan
- Mark Dakroub
- Nandhakumar Chitra Ragupathy

## License

Free
