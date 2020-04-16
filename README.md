# Wine Data Science Project

This purpose of this project to us data about the physiochemical properties of wine to predict the quality of the wine. 

# How to Reproduce 

* Just clone the repo. This repo contains all the required files to reproduce the project.

# Planning

- [X] Acquire.py
    - [X] Retrieve data from [UCI website](https://archive.ics.uci.edu/ml/datasets/wine+quality)
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

# Citations

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
Modeling wine preferences by data mining from physicochemical properties.
In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

Available at:

[@Elsevier](http://dx.doi.org/10.1016/j.dss.2009.05.016)

[Pre-press (pdf)](http://www3.dsi.uminho.pt/pcortez/winequality09.pdf)

[bib](http://www3.dsi.uminho.pt/pcortez/dss09.bib)