# Data Engeneer
Piscine datascience - 0

Creation of a DB

This project is part of the Data Science Piscine.  
The goal of this module is to learn the basics of **database creation and data preparation** using PostgreSQL.

A data engineer is responsible for preparing and organizing data so that analysts and data scientists can use it efficiently.

## Project Structure

| Exercice | Description |
|:------:| ----------- |
| [ex00](#ex00--create-postgresql-database) | Create PostgreSQL Database |
| [ex01](#ex01--database-visualization) | Database Visualization |
| [ex02](#ex02--first-table) | First Table |
| [ex03](#ex03--automatic-table-creation) | Automatic Table Creation |
| [ex04](#ex04--items-table) | Items Table |

## Exercises

### ex00 – Create PostgreSQL Database
Create a PostgreSQL database.

Requirements:
- Username: your student login
- Database name: `piscineds`
- Password: `mysecretpassword`

Connection example: ```psql -U your_login -d piscineds -h localhost -W```


### ex01 – Database Visualization
Use a software tool to visualize and manage the database.

Examples of tools:
- pgAdmin
- DBeaver
- Postico

I choose DBeaver because it's opensource, free and very popular

--- 

*to connect at the DB* ***(shift + ctrl + N)***

| Param: | value |
|:------:| ----------- |
| Host: | localhost  |
| Port: | 5432  |
| Database: | piscineds  |
| User: | your_login  |
| Password: | mysecretpassword  |

![alt](printscreen)

The tool should allow easy browsing and manipulation of records.

---

### ex02 – First Table
Create a PostgreSQL table using data from a CSV file located in the `customer` folder.

Requirements:
- Table name must match the CSV filename
- Column names must match the CSV file
- Use at least **six different data types**
- The **first column must be a DATETIME**


what column you need:
```bash
cat data_2022_dec.csv  | head -n 1
>> event_time,event_type,product_id,price,user_id,user_session
```

connection 
```bash
sudo apt install postgresql-client-common
psql -U your_login -d piscineds -h localhost -W
>> Password: ******
```

```SQL
CREATE TABLE data_2022_oct(
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price NUMERIC(100,2),
    user_id BIGINT,
    user_session uuid
    );
```
``uuid`` : *Universally Unique Identifiers* (ex : a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11)

```SQL
\copy data_2022_oct FROM 'path/Piscine_datascience_0/subject/customer/data_2022_oct.csv' DELIMITER ',' CSV HEADER;
```

---

### ex03 – Automatic Table Creation
Automatically create database tables from all CSV files in the `customer` folder.

Each table must:
- Be named after the CSV file (without `.csv`)
- Contain the same columns as the CSV file

---

### ex04 – Items Table
Create a table named `items` using the data from `items.csv`.

Requirements:
- Use the column names from the file
- Use at least **three different data types**

---

## Project Goal

The objective of this module is to understand how to:
- Create and configure a database
- Import and structure data
- Prepare datasets for analysis


### reference 

https://www.datacamp.com/fr/tutorial/tutorial-postgresql-python

https://www.postgresql.org/docs/current/datatype.html

https://dbeaver.com/docs/dbeaver/