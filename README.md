# Wine Data Science Project

This purpose of this project to us data about the physiochemical properties of wine to predict the quality of the wine. 

# How to Reproduce 

* This repo will contain all the required files to reproduce the project as long as you have access to the Kaggle API.
    * If you have not already set up access to the Kaggle API, follow the directions on [Kaggle API](https://github.com/Kaggle/kaggle-api) to set up your access.

# Planning

- [ ] Acquire.py
    - [ ] Retrieve data from [Red Wine Quality](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009) using the kaggle api
- [ ] Prepare.py
    - [ ] Fix dtype issues
    - [ ] Handel missing values
        - [ ] Replace missing values with np.nan
        - [ ] Decide whether to impute or drop
            - [ ] Attempt using Regression and KNN Imputer if possible
    - [ ] Drop unnecessary columns
    - [ ] Check for scaling needs
- [ ] Explore.ipynb
- [ ] Model.ipynb