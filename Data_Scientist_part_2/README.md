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

Jedi = Positive
Sith = Negative

#### lexical

| var | definition | means |
| ---- | ---- | ---- | 
| tp | true postitive | predict Jedi AND True |
| tn | true negative | predict Jedi AND False |
| fp | false postitive | predict Sith AND True | 
| fn | false negative | predict Sith AND False | 

the columns are the predict values
the rows are the real values.
![confusing matrix](./img/Confusion_Matrix_for_Binary_Classes.avif)

| Classification Metrics | formula |
| ---- | ---- |
| Precision |![Precision](./img/precision.avif) |
| Recall |![Recall](./img/recall.avif) |
| F1-score |![F1-score](./img/f1.avif) |
| Accuracy |![Accuracy](./img/accuracy.avif) |


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

[doc](#ex00)

> [Warning] Critical exercise: if incorrect → evaluation stops


### Exercise 01 – Heatmap

- Compute correlation matrix
- Display it as a heatmap
- Identify relationships between features

between -1 and 1

which features are usefull to know if it's Jedi:
```
Empowered       -0.793652
Prescience      -0.790066
Stims           -0.786797
Recovery        -0.777633
Sprint          -0.739672
Strength        -0.737403
```

[doc](#ex01)

### Exercise 02 – Variances (PCA intuition)
- Compute variance of each feature
- Calculate cumulative variance
- Determine number of components to reach 90%
- Plot cumulative variance graph

We have 31 column is complex so we will use PCA to reduce on principal componante
#### [Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis):
- linear dimensionnal reduction and keep the maximum of information

- highlighting the hidden structures and relationships in the data


why 90% : it's a benchmark in data science
 |||
 |----|---|
 | too few component  | lose informations |
 | too much component | useless informations |

### Exercise 03 – Feature Selection (VIF)
- Detect multicollinearity using ***Variance Inflation Factor*** (VIF)
- Remove highly correlated features
- Keep features with **VIF** < 5

read [wiki](https://en.wikipedia.org/wiki/Variance_inflation_factor):

#### formula:
Variance Inflation Factor:
``VIF = 1 / (1 - R²)
`` 
- VIF = 1: no correlation (parfait)
- VIF < 5: ok
- VIF > 5: High multicollinearity is present.
- VIF > 10:  This signals serious multicollinearity.

Tolerance:
``Tolerance = 1 / VIF``
weak Tolerence = multicollinearity problem

### Exercise 04 – Tree Model
- Train:
    - Decision Tree OR Random Forest
- Display tree structure
- Generate predictions (``Tree.txt``)
- Achieve ≥ 90% F1-score

#### Decision tree classifier:
1. Start with the ``entire dataset`` at the root node.
2. Select the *best feature* to split the data (based on measures like ***Gini impurity***).
3. Create ``child nodes`` for each possible value of the selected feature.
4. Repeat steps 2–3 for each child node until a stopping criterion is met (e.g., maximum depth reached, minimum samples per leaf, or pure leaf nodes).
5. Assign the majority class to each leaf node.

at the end, we should have something like ``[Yes, Yes, ..., No, Yes]``. there is more yes so the prediction will be **yes**

- max_depth
    - small → simple model (risk underfitting)
    - big → complex model (risk overfitting)

- min_samples_split
    - small(2) → splits everywhere → overfitting
    - big → less splits → more stable

- min_samples_leaf:
    - small(1) → leaves too specific → overfitting
    - big → general leaves

> [!WARNING] Problem:
> Decision tree can ``overfitting``
> it can be perfect for **train** and useless with **test**

> [!TIP]
> PCA: reduce dimensions
> VIF: remove multicollinearity


Gini : 
![Gini](./img/gini.svg)

#### Random Forest Classifier model

- it's base on the implementation of Decision tree classifier
- it's intuitive
- quick to train
but
- difficult to read results

### Exercise 05 – KNN
- Implement K-Nearest Neighbors
- Test different values of k
- Plot performance vs k
- Generate predictions (``KNN.txt``)
- Achieve ≥ 92% F1-score

### Exercise 06 – Voting Classifier
- Combine multiple models
- Use a Voting Classifier
- Generate predictions (``Voting.txt``)
- Achieve ≥ 94% F1-score

## Reference

### ex00
confusion matrice:
https://www.ibm.com/fr-fr/think/topics/confusion-matrix#:~:text=La%20matrice%20de%20confusion%20permet,d%27un%20jeu%20de%20données.
https://www.v7labs.com/blog/confusion-matrix-guide
https://www.youtube.com/watch?v=MNejgy2_1Dc

graph confusion matrice: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html

### ex01

graph heatmap: 
https://seaborn.pydata.org/generated/seaborn.heatmap.html
https://www.youtube.com/watch?v=1fFVt4tQjRE

### ex02
https://www.youtube.com/watch?v=IhBjLeDpOGg
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
https://medium.com/operations-research-bit/principal-component-analysis-with-python-a-deep-dive-0c5195bff087
https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors


### ex03
https://en.wikipedia.org/wiki/Variance_inflation_factor
https://www.datacamp.com/tutorial/variance-inflation-factor

### ex04
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
https://medium.com/data-science/decision-tree-classifier-explained-a-visual-guide-with-code-examples-for-beginners-7c863f06a71e
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
https://www.devoteam.com/fr/expert-view/algorithme-n2-comprendre-comment-fonctionne-un-random-forest-en-5-min/
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html