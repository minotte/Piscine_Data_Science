import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

def graph(model, X):
    plt.figure(figsize=(15,10))
    tree.plot_tree(model, feature_names=X.columns,
                   class_names=["Jedi", "Sith"], filled=True)
    plt.show()

def load_data_train(path):
    df = pd.read_csv(path)
    # df['knight'] = (df['knight'] == 'Jedi').astype(int)
    X = df.drop(columns= "knight", axis = 1)
    Y = df["knight"]
    return X, Y

def load_data_test(path):
    df = pd.read_csv(path)
    if df.columns[-1] == 'knight':
        # df['knight'] = (df['knight'] == 'Jedi').astype(int)
        X = df.drop(columns= "knight", axis = 1)
        return X
    return df

def save_prediction(predictions):
    with open("Tree.txt", "w") as f:
        f.write("\n".join(predictions))

def decision_tree(X, y, X_test, X_train, X_t, y_train, y_t):
    # model = DecisionTreeClassifier(max_depth=10, min_samples_split=7, 
                                #    min_samples_leaf=2)
    model = DecisionTreeClassifier(max_depth=7)
    # Model decision tree
    model.fit(X_train, y_train)
    y_pred = model.predict(X_t)
    score = f1_score(y_t, y_pred, pos_label="Jedi")
    print(f"F1-score Tree: {score:.6f}")
    #train on all the dataset
    model.fit(X, y)
    predictions = model.predict(X_test)
    save_prediction(predictions)
    graph(model, X)

def random_forest(X,y, X_test, X_train, X_t, y_train, y_t):
    model = RandomForestClassifier(n_estimators=100,
                                   max_depth=10,
                                   min_samples_leaf=2,
                                   min_samples_split=5,
                                   random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_t)
    score = f1_score(y_t, y_pred, pos_label="Jedi")
    print(f"F1-score Forest: {score:.6f}")
    graph(model, X)


if __name__ == '__main__':
    try:
        assert len(sys.argv) == 3, "Usage: python script.py Train.csv Test.csv"
        X, y = load_data_train(sys.argv[1])
        X_test = load_data_test(sys.argv[2])
        X_train, X_t, y_train, y_t = train_test_split(X, y, test_size=0.2, 
                                                    random_state=42)
        decision_tree(X, y, X_test, X_train, X_t, y_train, y_t)
        random_forest(X,y, X_test, X_train, X_t, y_train, y_t)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")