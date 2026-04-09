import matplotlib.pyplot as plt
import psycopg2
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import sys

def chart(k_range, inertias):
    plt.figure('Elbow Method')
    plt.plot(k_range, inertias, marker='o')
    plt.xlabel('Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.xticks(k_range)
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
        sql = """
        SELECT user_id, COUNT(*) as purchase_frequency, SUM(price) as total_spent
        FROM customers
        WHERE event_type = 'purchase' 
        AND event_time >= '2022-10-01' 
        AND event_time < '2023-03-01'
        GROUP BY user_id;
        """
        cur.execute(sql)
        results = cur.fetchall()
        data = np.array([[r[1], r[2]] for r in results])

        # Normalize data
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)

        # make the Elbow curve
        k_range = range(1, 11)
        inertias = []
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(data_scaled)
            inertias.append(kmeans.inertia_)
        chart(k_range, inertias)

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