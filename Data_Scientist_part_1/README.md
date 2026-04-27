# Python Data Science Training - Module 3

## Overview

This project is part of the Data Science Piscine and focuses on understanding the present state of data through exploration, transformation, and preparation for machine learning.

The goal is to analyze a dataset of Star Wars knights and determine whether it was possible to predict if a knight would turn to the dark side based on their abilities.

You will work with:

Features: knight skills (Strength, Power, Agility…)
Target: knight (Jedi or Sith)

## Objectives

This module introduces key data science concepts:

Data visualization
Feature correlation analysis
Data preprocessing (standardization & normalization)
Data splitting for machine learning
Understanding relationships between features and target

## Sommary

- [Analyse *.csv](#analyse-csv)
- [Prerequisites](#prerequisites)
- [Exercises](#exercises)
    - [Exercise 00 – Histogram](#exercise-00--histogram)
    - [Exercise 01 – Correlation](#exercise-01--correlation)
    - [Exercise 02- scatter plot](#exercise-02--scatter-plots-clustering-visualization)
    - [Exercise 03 - standardization](#exercise-03--standardization)
    - [Exercise 04 - normalization](#exercise-04--normalization)
    - [Exercise 05 - split](#exercise-05--split)
- [Reference](#ref-documentation)

## Project Structure
```
.
├── ex00/
|└─ Histogram.*
├── ex01/
|└─ Correlation.*
├── ex02/
|└─ points.*
├── ex03/
|└─ standardization.*
├── ex04/
|└─ Normalization.*
└── ex05/
 └─ split.*
```

## Analyse *.CSV
```bash
head Test_knight.csv  -n 1 > column_Test_Knight
head Train_knight.csv  -n 1 > column_Train_Knight
diff -u column_*

>> @@ -1 +1 @@
>> ....., knight
```
```bash
tr ',' ' ' < column_Test_Knight | wc -w
>> 30
```

## Prerequisites

```bash
wget -P ./ex05 https://cdn.intra.42.fr/document/document/45777/Test_knight.csv
wget -P ./ex05 https://cdn.intra.42.fr/document/document/45778/Train_knight.csv
```


-----
### Exercises
-----
### Exercise 00 – Histogram

#### Goal

Visualize the distribution of data using histograms.

#### Tasks
- Create a histogram using Test_knight.csv
- Create another histogram using Train_knight.csv
- Display both:
    - feature distributions
    - relationship between features and the target (knight)

| Observation	| Interpretation |
| ----- | ----- |
| Separate curves | Important feature for predicting the side
| Overlapping curves | Feature with low discriminatory power



-----
### Exercise 01 – Correlation

#### Goal

Identify the most important features.

#### Tasks
- Compute correlation between:
    - ``knight`` (target)
    - all other columns (features)

Encode target: Jedi=1, Sith=0



[**Interpreting correlation coefficient values**](https://en.wikipedia.org/wiki/Correlation_coefficient) 
| r or R | r or R | Strength or weakness of association between variables |
| ---- | ----- | ---- |
| +0.8 to +1.0	| -1.0 to -0.8 | Perfect or very strong association|
| +0.6 to +0.8	| -0.8 to -0.6 | Strong association|
| +0.4 to +0.6	| -0.6 to -0.4 | Moderate association|
| +0.2 to +0.4	| -0.4 to -0.2 | Weak association|
| +0.0 to 0.2	| -0.2 to 0.0 | Very weak or no association|

#### Expected Result

A ranked list showing which features are most correlated with the target.

This helps identify:

- important variables
- irrelevant features

-----
### Exercise 02 – Scatter Plots (Clustering Visualization)

#### Goal

Visualize how data points are distributed.

#### Tasks

Create 4 graphs (using both datasets):

For each dataset:

1. A graph where clusters are clearly separated
    - use strong correlation from +0.8 to +1.0
2. A graph where clusters are mixed
    - use weak correlation from +0.0 to 0.2

These visualizations help understand:

- separability of classes
- data complexity

-----
### Exercise 03 – Standardization

#### Goal

Standardize the dataset.

#### Tasks
Apply standardization (mean = 0, standard deviation = 1)
Print the transformed data
Recreate one graph from using standardized data

***Formula***
`` 
z = (x - mean) / std
``

> [!IMPORTANT]  
> remove column knight during standardization but keep it for the graph

Standardization ensures that all features have the same scale, it's essential for some algorithms like clustering.


-----
### Exercise 04 – Normalization

#### Goal

Normalize the dataset.

#### Tasks
Apply normalization (values scaled between 0 and 1)
Print the transformed data
Recreate the other graphs from *Exercise 02* using normalized data

***Formula***
`` 
x' = (x - min) / (max - min)
``

> [!IMPORTANT]  
> remove column knight during standardization but keep it for the graph

Normalization rescales features to a fixed range [0,1], which helps compare variables with different scales

-----
### Exercise 05 – Split

#### Goal

Prepare data for machine learning with [train test split](https://www.nexa.fr/blog/train-test-split).

#### Tasks
- Split Train_knight.csv into:
    - Training_knight.csv
    - Validation_knight.csv
- The split must be random

#### Why?
to train a model and check if the model is ok

must explain:

the percentage used :  20% to 30% are recommanded
why I chose it? usually we used 20% 

#### Method

1. Random Shuffle (To avoid bias caused by ordered data and ensure randomness)
2. Split data
3. Evaluation

the fonction train_test_split exist from sklearn.model_selection so I will use it.

## Tools

You are free to use any technology:

Any data science tool


## REF DOCUMENTATION

graph:

https://matplotlib.org/stable/plot_types/stats/hist_plot.html

ex01 :

https://en.wikipedia.org/wiki/Correlation_coefficient

ex04:

https://en.wikipedia.org/wiki/Feature_scaling


ex05 :

https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
