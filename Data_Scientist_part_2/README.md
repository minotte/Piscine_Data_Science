# Data Science part 2
The Future (Machine Learning Models)

## Overview

This module focuses on predictive modeling and machine learning algorithms.
The goal is to build models capable of predicting the future based on past data.

Using the knight dataset, you will train models to classify whether a knight belongs to the Jedi or Sith side.

This module represents a complete **machine learning pipeline**:
- Data analysis
- Feature selection
- Model training
- Model evaluation
- Prediction

## Objectives

Evaluate model performance
Understand classification metrics
Reduce dimensionality
Handle multicollinearity
Train machine learning models
Improve prediction accuracy

## Technologies

free to use any tools or languages, like:

- Python
- Pandas / NumPy
- Matplotlib / Seaborn
- Scikit-learn

## Prerequisite attachment
```bash
wget https://cdn.intra.42.fr/document/document/45784/truth.txt
wget https://cdn.intra.42.fr/document/document/45785/Test_knight.csv
wget https://cdn.intra.42.fr/document/document/45786/predictions.txt
wget https://cdn.intra.42.fr/document/document/45787/Train_knight.csv
```
## Sommary

- [Exercises](#exercises)
    - [Exercise 0 - Confusion Matrix](#exercise-00--confusion-matrix)
    - [Exercise 1 – Heatmap](#exercise-01--heatmap)
    - [Exercise 2 – Variances (PCA intuition)](#exercise-01--heatmap)
    - [Exercise 3 – Feature Selection (VIF)](#exercise-03--feature-selection-vif)
    - [Exercise 4 – Tree Model](#exercise-04--tree-model)
    - [Exercise 5 – KNN](#exercise-05--knn)
    - [Exercise 6 – Voting Classifier](#exercise-06--voting-classifier)
- [Reference](#reference)

## Project Structure
```bash
├── ex00/
│   └── Confusion_Matrix.*
├── ex01/
│   └── Heatmap.*
├── ex02/
│   └── variances.*
├── ex03/
│   └── Feature_Selection.*
├── ex04/
│   └── Tree.*
├── ex05/
│   └── KNN.*
└── ex06/
    └── democracy.*
```
## Exercises

----

### Exercise 00 – Confusion Matrix
- Compute manually:
    - Precision
    - Recall
    - F1-score
    - Accuracy
- Display confusion matrix
- Use predictions vs ground truth

#### Except result
```bash
$> ./Confusion\_Matrix.* predictions.txt truth.txt
precision recall f1-score total
Jedi 0.45 0.51 0.48 49
Sith 0.47 0.41 0.44 51
accuracy 0.46 100
[[25 24]
[30 21]]
```


> [Warning] Critical exercise: if incorrect → evaluation stops


### Exercise 01 – Heatmap
- Compute correlation matrix
- Display it as a heatmap
- Identify relationships between features

### Exercise 02 – Variances (PCA intuition)
- Compute variance of each feature
- Calculate cumulative variance
- Determine number of components to reach 90%
- Plot cumulative variance graph

### Exercise 03 – Feature Selection (VIF)
- Detect multicollinearity using ***Variance Inflation Factor*** (VIF)
- Remove highly correlated features
- Keep features with **VIF** < 5

### Exercise 04 – Tree Model
- Train:
    - Decision Tree OR Random Forest
- Display tree structure
- Generate predictions (``Tree.txt``)
- Achieve ≥ 90% F1-score

### Exercise 05 – KNN
- Implement K-Nearest Neighbors
- Test different values of k
- Plot performance vs k
- Generate predictions (``KNN.txt``)
- Achieve ≥ 92% F1-score

### Exercise 06 – Voting Classifier
Combine multiple models
Use a Voting Classifier
Generate predictions (``Voting.txt``)
Achieve ≥ 94% F1-score

## Reference