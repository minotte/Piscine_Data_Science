import matplotlib.pyplot as plt
import psycopg2
import sys
import matplotlib.dates as mdates

def plot_line(month, values):
    plt.plot(month, values, linewidth=1.5)
    plt.xlabel('Month')
    plt.ylabel('Number of customers')
    plt.xticks(rotation=0)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.tight_layout()
    plt.show()

def chart_bar(months, values):
    plt.bar(range(len(months)), values)
    plt.xticks(range(len(months)), [m.strftime('%b') for m in months])
    plt.xlabel('Months')
    plt.ylabel('total sales in million of ₳')
    plt.tight_layout()
    plt.show()

def plot_fill_between(days, values):
    plt.fill_between(days, values, alpha=0.5)
    plt.plot(days, values, color='blue', linewidth=1)
    plt.xlim(days[0], days[-1]) 
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.ylabel('average spend/customers in ₳')
    plt.tight_layout()
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

        ###########
        # Chart 1 #
        ###########
        sql1 = """
        SELECT event_time::date as day, COUNT(*) as purchases
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01'
        GROUP BY event_time::date
        ORDER BY day;
        """
        cur.execute(sql1)
        results0 = [(r[0], r[1]) for r in cur.fetchall()]
        days = [r[0] for r in results0]
        plot_line(days, [r[1] for r in results0])
        
        ########################
        # Chart 2 - bar chart  #
        ########################
        sql2 = """
        SELECT DATE_TRUNC('month', event_time)::date as month, SUM(price)/1000000.0 as sum_price
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01'
        GROUP BY DATE_TRUNC('month', event_time)
        ORDER BY month;
        """
        cur.execute(sql2)
        results2 = [(r[0], r[1]) for r in cur.fetchall()]
        months = [r[0] for r in results2]
        print(results2)
        chart_bar(months, [r[1] for r in results2])

        ############################
        # Chart 3 - fill_between #
        ############################
        sql3 = """
        SELECT event_time::date as day, 
            SUM(price) / COUNT(DISTINCT user_id) as avg_spend_per_customer
        FROM customers
        WHERE event_type = 'purchase' 
          AND event_time >= '2022-10-01' 
          AND event_time < '2023-03-01'
        GROUP BY event_time::date
        ORDER BY day;
        """
        cur.execute(sql3)
        results3 = [(r[0], r[1]) for r in cur.fetchall()]
        days3 = [r[0] for r in results3]
        plot_fill_between(days3, [r[1] for r in results3])
        
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