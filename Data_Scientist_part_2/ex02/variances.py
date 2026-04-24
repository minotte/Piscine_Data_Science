import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def graph(cumulative_variances, component_90):
    plt.figure()
    plt.plot(cumulative_variances)
    plt.axhline(y=90, color="red", linestyle="--")
    plt.axvline(x=component_90, color="red", linestyle="-.")
    plt.xlabel("Number of components")
    plt.ylabel("Explained variance(%)")
    plt.title("PCA")
    plt.show()

if __name__ == '__main__':
    try:
        df = pd.read_csv("../Train_knight.csv")
        df['knight'] = df["knight"].map({'Jedi': 1, 'Sith': 0})
        X = df.values
        scaler = StandardScaler()
        scaler.fit(X)
        X_scaled = scaler.transform(X)
        pca = PCA()
        pca.fit(X_scaled)
        variances =  pca.explained_variance_ratio_ * 100
        print("Variances (Percentage):")
        print("Cumulative Variances (Percentage):")
        print(variances)
        cumulative_variances = np.cumsum(variances)
        print(cumulative_variances)
        component_90 = np.argmax(cumulative_variances >= 90) + 1
        print("----------------")
        print(f"90%: {component_90} components")
        graph(cumulative_variances, component_90)


    except KeyboardInterrupt:
        print("\nInterruption...")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")