import sys
import pandas as pd



if __name__ == '__main__':
    try:
        df = pd.read_csv('./Train_knight.csv')


    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        print("goodbye")