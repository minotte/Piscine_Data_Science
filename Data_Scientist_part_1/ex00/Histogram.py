import sys
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    try:
        f_test = pd.read_csv('../Test_knight.csv', sep=',')
        f_knight = pd.read_csv('../Train_knight.csv', sep=',')

        # histogram for test_knight
        f_test.hist(figsize=(15,12), bins=60, color="lightgreen")
        plt.tight_layout()
        plt.grid()
        plt.show()


        # histogram for f_knight_knight with color for the sith and jedi
        fig, axes = plt.subplots(6, 5, figsize=(15,10))
        axes = axes.flatten()

        for i, col in enumerate(f_knight.columns[:-1]):
            axes[i].hist(
                f_knight[f_knight['knight'] == 'Jedi'][col],
                bins=60,
                alpha=0.5,
                color='blue',
                label='Jedi'
            )
            axes[i].hist(
                f_knight[f_knight['knight'] == 'Sith'][col],
                bins=60,
                alpha=0.5,
                color='red',
                label='Sith'
            )
            axes[i].legend()
            axes[i].set_title(col, fontsize=8)
        # plt.grid()
        plt.tight_layout()
        plt.show()

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")
        