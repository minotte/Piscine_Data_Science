import pandas as pd
import matplotlib.pyplot as plt
import sys

def graph(df, feature1, feature2):
    title = df.attrs['name'] + ' - ' + feature2 +' vs ' + feature1
    plt.figure(title, figsize=(8,6))
    if (df.attrs['name'].startswith('Train')):
        jedi = df[df['knight'] == 'Jedi']
        sith = df[df['knight'] == 'Sith']
        plt.scatter(jedi[feature1], jedi[feature2], c='blue', label='Jedi', alpha=0.5)
        plt.scatter(sith[feature1], sith[feature2], c='red', label='Sith', alpha=0.5)
    else:
        plt.scatter(df[feature1], df[feature2], label='Knight',
                    color='green', alpha=0.5)
    plt.ylabel(feature2)
    plt.xlabel(feature1)
    plt.title(title)
    plt.legend()
    plt.show()



if __name__ == '__main__':
    try:
        f_train = pd.read_csv('../ex05/Train_knight.csv')
        f_train.attrs['name'] = "Train_knight.csv" 
        f_test = pd.read_csv('../ex05/Test_knight.csv')
        f_test.attrs['name'] = "Test_knight.csv" 

        feature1 = 'Empowered'
        feature2 = 'Stims'

        # Standardization
        features_train = f_train.drop(columns='knight')
        train_std = (features_train - features_train.mean()) / features_train.std()
        train_std['knight'] = f_train['knight']
        train_std.attrs['name'] = "Train_knight_standardization"
        
        test_std = (f_test - f_test.mean()) / f_test.std()
        test_std.attrs['name'] = "Test_knight_standardization"

        # Print result
        print(f"{f_train.attrs['name']} ")
        print(f_train.head())

        print(f"\n{train_std.attrs['name']} ")
        print(train_std.head())

        print(f"\n{test_std.attrs['name']}")
        print(test_std.head())

        # call graph
        graph(train_std, feature1, feature2)

    
    except KeyboardInterrupt:
        print("\nInterruption...")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")