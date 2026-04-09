import matplotlib.pyplot as plt
import psycopg2
import sys


def PieChart(results):
    labels = [row[0] for row in results]
    sizes = [row[1] for row in results]
    # colors = ['blue', 'orange', 'green', 'red']
    plt.figure('Event Type')
    plt.pie(
            sizes, 
            labels=labels, 
            # colors=colors,
            autopct='%1.1f%%',
        )
    plt.axis('equal')
    plt.show()



if __name__ == '__main__':
    try:
        conn = psycopg2.connect(
            dbname= 'piscineds',
            host='localhost',
            port=5432,
            user='nminotte',
            password='mysecretpassword',
        )

        cur = conn.cursor()
        sql = """
        SELECT  event_type, COUNT(*) AS cnt
        FROM customers
        GROUP BY event_type
        ORDER BY cnt DESC;
        """
        cur.execute(sql)
        results = cur.fetchall()
        # print(results)

        PieChart(results)
    
    except KeyboardInterrupt:
        print("\nInterruption...")
        sys.exit(130)

    except Exception as error:
        print(error)

    finally:
        if conn:
            cur.close()
            conn.close()
        print("Goodbye")