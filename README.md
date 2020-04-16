# Wine Data Science Project

This purpose of this project to us data about the physiochemical properties of wine to predict the quality of the wine. 

# How to Reproduce 

* This repo will contain all the required files to reproduce the project.

# Planning

- [ ] Acquire.py
    - [ ] Retrieve data from [UCI website](https://archive.ics.uci.edu/ml/datasets/wine+quality)
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