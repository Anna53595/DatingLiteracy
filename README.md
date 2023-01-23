**Data Science Project as part of the class: Data Literacy, Wintersemester 2022/23, Professor Macke**


# Dating Literacy: Can we predict your political belief, given less than 20 questions?

## Data set
We downloaded the [data set](https://figshare.com/articles/dataset/OKCupid_Datasets/14987388) created by Kirkegaard and Bjerrekaer. 

The authors descrive the data as following:
"A very large dataset (N=68,371, 2,620 variables) from the dating site OKCupid is presented and made publicly available for use by others. As an example of the analyses one can do with the dataset, a cognitive ability test is constructed from 14 suitable items. To validate the dataset and the test, the relationship of cognitive ability to religious beliefs and political interest/participation is examined. Cognitive ability is found to be negatively related to all measures of religious belief (latent correlations -.26 to -.35), and found to be positively related to all measures of political interest and participation (latent correlations .19 to .32). To further validate the dataset, we examined the relationship between Zodiac sign and every other variable. We found very scant evidence of any influence (the distribution of p-values from chi square tests was flat). Limitations of the dataset are discussed."
## Download train and test set, models:
- [train and test set](https://drive.google.com/drive/folders/1uP7PbnwCvYoie7Ee41mib9TyeG6yqOVn?usp=sharing) 
- [models](https://drive.google.com/drive/folders/1fEdsZcNmAjC8sddz109Q4MxPCXS0uzp2?usp=sharing)
## Brief summary:
### Reseach Question: 
Can we predict people’s political orientation based on how they portray their character traits and habits?
### Motivation:
- It shows us something about the uniformity of groups of people who report the same political orientation.
- Hypthesis: People with similar lifestyles are more likely to have the same political orientation
- Examples of descriptive questions and hypothetical implications, e.g. Someone who owns a gun is more likely to be conservative?
- If this hypothesis can not be confirmed, it’s also an interesting result because it indicates that lifestyle choices (e.g. owning a gun, having tattoos, drinking alcohol) are independent of political beliefs

## Repository structure:

**File stucture:**
```
DatingLiteracy
│   README.md
│   data_preprocessing.ipynb    
│   data_anylsis.ipynb
│   evaluation_testset.ipynb
│
└───data
│   │   question_data.csv
│   │   parsed_data_public.parquet
│   │   train.parquet
│   │   test.parquet
│ 
│   
└───models
    │   nv_downsampled_trn_set.joblib
    │   rf_downsampled_trn_set.joblib
```
**Content**
### ```data_preprocessing.ipynb:```
- Exclude all non-descriptive questions from dataframe
- Train-test-split
### ```data_anylsis.ipynb```
- Data preprocessing: Downsampling and feature selection
- Baseline Model: Naive Bayes
- Random Forest Model with HPO
- Evaluation 
### ```evaluation_testset.ipynb```
- Confusion Matrix, etc. on test set





