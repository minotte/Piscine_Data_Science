import matplotlib.pyplot as plt
import psycopg2
import sys

def plot_purchase_frequency(data):
    plt.figure('Purchase Frequency')
    plt.hist(data, bins=5, edgecolor='k')
    plt.ylabel('customers')
    plt.xlabel('frequency')
    plt.title('Purchase Frequency')
    plt.xticks(range(0, 39, 10))
    plt.ylim(0, 70000)
    plt.show()

def plot_monetary(monetary):
    plt.hist(monetary, bins=5, edgecolor='k')
    plt.ylabel('customers')
    plt.xlabel('Monetary value ₳')
    plt.title('Frequency distribution of the purchase prices per customer')
    plt.ylim(0, 50000)
    plt.xticks(range(0, 260, 50)) 
    plt.show()

if __name__ == '__main__':
    try:
        conn = psycopg2.connect(
            dbname='piscineds',
            host='localhost',
            port=5432,
            user='nminotte',
            password='mysecretpassword',
        )
        cur = conn.cursor()


        sql_frequence = """
        SELECT user_id, COUNT(*)
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01'
        GROUP BY user_id
        """
        cur.execute(sql_frequence)
        frequence = [r[1] for r in cur.fetchall() if r[1] <= 40]
        print(len(frequence))

        plot_purchase_frequency(frequence)

        sql_monetary = """
        SELECT user_id, SUM(price)
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01'
        GROUP BY user_id
        HAVING SUM(price) <= 250
        """
        cur.execute(sql_monetary)
        monetary = [r[1] for r in cur.fetchall()]
        print(len(monetary))

        plot_monetary(monetary)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)
    except Exception as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
        print("goodbye")