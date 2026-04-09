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

def norm(df):
        if (df.attrs['name'].startswith('Train')):
            x = df.drop(columns='knight')
        else:
            x = df
        min_vals = x.min()
        max_vals = x.max()
        x_norm = (x - min_vals) / (max_vals - min_vals).replace(0, 1e-10)
        if (df.attrs['name'].startswith('Train')):
            x_norm['knight'] = df['knight']
        x_norm.attrs['name'] = df.attrs['name'] + "_normalization"
        return x_norm

if __name__ == '__main__':
    try:
        f_train = pd.read_csv('../ex05/Train_knight.csv')
        f_train.attrs['name'] = "Train_knight" 
        f_test = pd.read_csv('../ex05/Test_knight.csv')
        f_test.attrs['name'] = "Test_knight" 

        feature3 = 'Deflection'
        feature4 = 'Survival'

        #################
        # Normalization #
        #################
        train_norm = norm(f_train)
        test_norm = norm(f_test)
        ################
        # Print result #
        ################
        print(f"{f_train.attrs['name']} ")
        print(f_train.head())

        print(f"\n{train_norm.attrs['name']} ")
        print(train_norm.head())

        print(f"\n{test_norm.attrs['name']}")
        print(test_norm.head())

        ##############
        # call graph #
        ##############
        graph(train_norm, feature3, feature4)

    
    except KeyboardInterrupt:
        print("\nInterruption...")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")