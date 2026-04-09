import matplotlib.pyplot as plt
import psycopg2
import sys


def plot_full_box(prices):
    plt.title("Full boxes")
    plt.boxplot(prices, vert=False, widths=0.5, notch=True,
        boxprops=dict(facecolor='green', edgecolor='none'),
        flierprops=dict(marker='D', markersize=8, 
        markerfacecolor='lightgray', markeredgecolor='none'),
        patch_artist=True)
    plt.xlabel('Price')
    plt.show()


def plot_IQR(price):
    plt.title("Interquartile Range")
    plt.boxplot(price, vert = False,
        boxprops=dict(facecolor='green', edgecolor='black'), 
        medianprops=dict(linestyle='-', linewidth=2, color='black'),
        showfliers=False, patch_artist=True)
    plt.xlabel('Price')
    plt.show()

def plot_basket_per_user(avg_carts):
    plt.boxplot(avg_carts, vert=False, widths=0.6, notch=False,
                boxprops=dict(facecolor='blue', edgecolor='black'),
                flierprops=dict(marker='D', markersize=8, markerfacecolor='gray', markeredgecolor='none'),
                patch_artist=True, whis=0.2)
    plt.xticks(range(int(min(avg_carts)), int(max(avg_carts)) + 1, 2))
    plt.tight_layout()
    plt.xlim(min(avg_carts) - 1, max(avg_carts) + 1)
    plt.yticks([])
    plt.show()

def print_stat(result):
    print(f"count  {result[0]}")
    print(f"mean   {float(result[1]):.6f}")
    print(f"std    {float(result[7]):.6f}")
    print(f"min    {float(result[3]):.6f}")
    print(f"25%    {float(result[5]):.6f}")
    print(f"50%    {float(result[2]):.6f}")
    print(f"75%    {float(result[6]):.6f}")
    print(f"max    {float(result[4]):.6f}")


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

        print("--- Stats ---")
        sql = """
        SELECT 
            COUNT(*) as count,
            AVG(price)::numeric(10,6) as mean,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price)::numeric(10,6) as median,
            MIN(price) as min,
            MAX(price) as max,
            PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY price)::numeric(10,6) as Q1,
            PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY price)::numeric(10,6) as Q3,
            STDDEV(price)::numeric(10,6) as std
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01';
        """
        cur.execute(sql)
        result = cur.fetchone()
        print_stat(result)

        sql_prices = """
        SELECT price
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01';
        """
        cur.execute(sql_prices)
        prices = [float(r[0]) for r in cur.fetchall()]
        plot_full_box(prices)
        plot_IQR(prices)


        sql_basket = """
        SELECT user_id, AVG(price) as avg_cart_price
        FROM customers
        WHERE event_type = 'cart' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01'
        GROUP BY user_id
        HAVING AVG(price) BETWEEN 26 AND 43;
        """
        cur.execute(sql_basket)
        avg_carts = [float(r[1]) for r in cur.fetchall()]
        plot_basket_per_user(avg_carts)

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
