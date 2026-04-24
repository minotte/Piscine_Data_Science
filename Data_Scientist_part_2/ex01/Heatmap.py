import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import numpy as np

if __name__ == '__main__':
    try:
        df = pd.read_csv("../Train_knight.csv")
        df['knight'] = df['knight'].map({'Jedi': 0, 'Sith': 1})
        corr = df.corr()
        # print(corr)
        print("\nCorrelation knight :")
        print(corr['knight'].sort_values())
        # mask = np.triu(np.ones_like(corr, dtype=bool))
        plt.figure(figsize=(10, 9))
        sns.heatmap(corr, annot=False, square=True)
        # sns.heatmap(corr, mask=mask, annot=False, square=True)
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")