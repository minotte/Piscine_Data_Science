import psycopg2
import os
import sys

def main() -> int:
    try: 
        # database connection
        conn = psycopg2.connect(database = "piscineds", 
                                user = "nminotte", 
                                host= 'localhost',
                                password = "mysecretpassword",
                                port = 5432)

        cur = conn.cursor()

        path = input("Enter the path of item.csv : ")
        if not path.endswith("item.csv"):
            path = path + "item.csv"
            print(path)
        table = "items"
        print("Creating table:", table)

        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                product_id INTEGER,
                category_id BIGINT,
                category_code TEXT,
                brand TEXT
            );
        """)


        with open(path, "r") as f:
            cur.copy_expert( f"COPY {table} FROM STDIN WITH CSV HEADER",
                            f
                                )


        conn.commit()
        cur.close()
        conn.close()


    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)


if __name__ == "__main__":
    main()