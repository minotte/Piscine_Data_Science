import sys
import pandas as pd

if __name__ == '__main__':
    try:
        df = pd.read_csv('../ex05/Train_knight.csv')
        df['knight'] = df['knight'].map({
            'Jedi': 1,
            'Sith': 0
        })
        corr = df.corr()
        corr_knight = corr['knight']
        corr_knight = corr_knight.sort_values(ascending=False)
        corr_knight.name = None
        print(corr_knight.to_string())

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")