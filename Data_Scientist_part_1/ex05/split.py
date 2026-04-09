import sys
import pandas as pd
from sklearn.model_selection import train_test_split

def verification(df, train, test):
        df_rows = len(df)
        train_rows = len(train)
        test_rows = len(test)
        train_purcent = (train_rows * 100) / df_rows
        total = test_rows + train_rows
        print(f"Training: {train_rows} rows, it's {round(train_purcent)}% of {df.attrs['name']}")
#         print(f"Test: {test_rows} rows")
#         print(f"So {total} in total and \
# {df.attrs['name']} have {df_rows} rows")

if __name__ == '__main__':
    try:
        df = pd.read_csv('./Train_knight.csv')
        df.attrs['name'] = 'Train_knight.csv'
        X = df.drop('knight', axis=1)
        y = df['knight']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42, # fix the random
            shuffle=True,
            stratify=y) # maintain the class ratios
        train = pd.concat([X_train, y_train], axis=1)
        test = pd.concat([X_test, y_test], axis=1)

        verification(df, train, test)

        train.to_csv('Training_knight.csv', index=False)
        test.to_csv('Validation_knight.csv',  index=False)


    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")
