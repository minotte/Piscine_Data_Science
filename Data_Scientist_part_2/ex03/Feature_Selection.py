import sys
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculated_vif(df):
    vif_data = pd.DataFrame()
    vif_data["Skill"] = df.columns
    vif_data["VIF"] = [variance_inflation_factor(df.values, i) \
                       for i in range(df.shape[1])]
    vif_data["Tolerance"] = 1 / vif_data["VIF"]
    return vif_data

def remove_multicollinearity(df, vif, limit=5):
    while True:
        vif_max = vif["VIF"].max()
        if vif_max <= limit:
            break
        skill_max_remove = vif.sort_values("VIF", ascending=False)["Skill"].iloc[0]
        df = df.drop(columns= skill_max_remove, axis=1)
        vif = calculated_vif(df)
    print(vif)


if __name__ == '__main__':
    try:
        df = pd.read_csv("../Train_knight.csv")
        df = df.drop(columns="knight", axis=1)
        vif = calculated_vif(df)
        print(vif)
        print("---------------------------------------")
        remove_multicollinearity(df, vif)

    except KeyboardInterrupt:
        print("\nInterruption...")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")