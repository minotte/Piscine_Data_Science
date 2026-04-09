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

        cur = conn.cursor()  # able to make operation on the db

        path = input("Enter the path of the CSV folder : ")
        for file in os.listdir(path):
            if file.endswith(".csv"):
                table = file.replace(".csv", "")
                file_path = os.path.join(path, file)
                print("Creating table:", table)
                
                cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {table} (
                    event_time TIMESTAMP,
                    event_type TEXT,
                    product_id INTEGER,
                    price NUMERIC,
                    user_id BIGINT,
                    user_session UUID
                );
                """)
                

                with open(file_path, "r") as f:
                    cur.copy_expert( f"COPY {table} FROM STDIN WITH CSV HEADER NULL ''",
                                    f)

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