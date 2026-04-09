import pandas as pd
import matplotlib.pyplot as plt
import sys

def graph(df, feature1, feature2):
    title = df.attrs['name'] + ' - ' + feature2 +' vs ' + feature1
    plt.figure(title, figsize=(8,6))
    if (df.attrs['name'] == "Train_knight.csv"):
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
        f_test = pd.read_csv('../Test_knight.csv')
        f_test.attrs['name'] = "Test_knight.csv" 

        feature1 = 'Empowered'
        feature2 = 'Stims'
        feature3 = 'Deflection'
        feature4 = 'Survival'
        graph(f_train, feature1, feature2)
        graph(f_train, feature3, feature4)
        graph(f_test, feature1, feature2)
        graph(f_test, feature3, feature4)
    
    except KeyboardInterrupt:
        print("\nInterruption...")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")
