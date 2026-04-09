# Data Warehouse
Training Piscine Data Science


## Project Overview

This project focuses on the creation and manipulation of a Data Warehouse.

The main objective is to understand the ETL process (Extract, Transform, Load) by combining data from multiple tables, cleaning it, and structuring it into a unified dataset that can be easily analyzed.

Throughout the exercises, we will:
 
- Visualize and interact with a database
- Merge multiple datasets
- Clean duplicate data
- Combine customer data with product information


## ETL Concept

ETL stands for:

- Extract – Collect data from different sources
- Transform – Clean, format, and process the data
- Load – Store the processed data in a Data Warehouse

This workflow ensures that data becomes consistent, reliable, and ready for analysis.

## Project Structure

| Exercice | Description |
|:------:| ----------- |
| [ex00](#exercise-00--show-me-your-db) | Show me your DB |
| [ex01](#exercise-01--customers-table) | Customers Table |
| [ex02](#exercise-02--remove-duplicates) | Remove Duplicates |
| [ex03](#exercise-03--fusion) | Fusion |


> [!WARNING]
> We use the db of Piscine_datascience_0 and there is an other csv: [data_2023_feb.csv](https://cdn.intra.42.fr/document/document/45779/data_2023_feb.csv)

connection 
```bash
sudo apt install postgresql-client-common
psql -U your_login -d piscineds -h localhost -W
>> Password: ******
```

```SQL
CREATE TABLE data_2023_feb(
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price NUMERIC(100,2),
    user_id BIGINT,
    user_session uuid
    );
\copy data_2023_feb FROM 'path/Piscine_datascience_0/subject/customer/data_2023_feb.csv' DELIMITER ',' CSV HEADER;
```

## Lexical of the project

The exercice simulate a web maketplace.
we have 2 types of db:
1. data_202*_* : action on the site and price by months
2. items : all information on items 

| feature | correspond | have in data* and items | var type |
|:------:| ----------- | ----------- | ----------- |
| event_time | when the server have an event | no | TIMESTAMP |
| event_type | what type of event | no | TEXT  |
| user_id | id of the client: "email" | no |  BIGINT |
| user_session | During the time the client is connected, finish when client  |disconnect | uuid
| price | price of the product, depending on the stock exchange | no | NUMERIC(100,2) |
| product_id | reference (name) of product |  int4 |
| category-id | ???? | no | int8 |
| category_code | kind of item |  no | text |
| brand | brand | no | text |

## Exercises


### Exercise 00 – Show me your DB

#### Goal

Find an easy way to visualize and interact with the database.

**Recommended tools**

- pgAdmin
- DBeaver
- Postico
- Any other SQL database client


The selected tool must allow:

- Easy browsing of tables
- Quick search of IDs
- Clear visualization of database structure

I choose DBeaver because it's opensource, free and very popular

--------------

### Exercise 01 – Customers Table

#### Goal

Create a unified table called:

``customers``

This table must contain the combined data from all tables named:

`data_202*_***`


*Expected result*

All customer data from the different yearly tables should be merged into a single table.

--------------

### Exercise 02 – Remove Duplicates

Sometimes the server sends the same instruction with a 1-second delay, which creates duplicate events.

#### Goal

Remove duplicate rows from the `customers` table.


Example:

| event_time |	event_type	|product_id |
| :---: | --- | --- |
| 2022-10-01 00:00:32	 |remove_from_cart | 5779403 |
| 2022-10-01 00:00:33	|remove_from_cart | 5779403 |
| 2022-10-01 00:00:39	| add_from_cart | 5779404 |
| 2022-10-01 00:00:40	| remove_from_cart | 5779405 |

These events should be considered duplicates and cleaned from the dataset.

| event_time |	event_type	|product_id |
| :---: | --- | --- |
| 2022-10-01 00:00:33	|remove_from_cart | 5779403 |
| 2022-10-01 00:00:39	| add_from_cart | 5779404 |
| 2022-10-01 00:00:40	| remove_from_cart | 5779405 |


### Approach:

1. Make sure that the base tables has ID's. (product_id)

2. check how lign find duplicate rows

3. Delete records other than records wich have come from step 2







--------------

## Exercise 03 – Fusion

#### Goal

Combine the **customers table** with the **items table**.

The resulting table should still be called:

``customers``

Important requirement

No information must be lost during the merge.


### Aproach:

check if items have some duplicates rows.
use dbeaver tools ```right click order by ``` on the product_id column 
or 
```sql
SELECT product_id, COUNT(*) as cnt
FROM items
GROUP BY product_id
HAVING COUNT(*) > 1;
```
for the table  ```ITEMS```, we must clean the data:

#### exemple:

|product_id  | category_id           | category_code | brand |
| :---: | --- | --- | --- |
|3929       | 1487580005411062528  | NULL          | cnd |
|3929       | 1487580005411062528  | chair          | NULL |
|3929       | NULL                 | NULL          | NULL |
|3929       | 1487580005411062528  | NULL          | NULL |

#### result

| product_id  | category_id           | category_code | brand |
| :---: | --- | --- | --- |
| 3929       | 1487580005411062528  | chair          | cnd |

I use MAX() to keep the non NULL if that exist.


now we can merge the 2 tables in a table_tmp : 
-  we notice the commun column **product_id**
- with  [LEFT JOIN](https://www.w3schools.com/postgresql/postgresql_left_join.php)

## Reference 

https://dbeaver.com/docs/dbeaver/