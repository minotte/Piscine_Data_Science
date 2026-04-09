-- find duplicated rows
CREATE TABLE customers_tmp AS
SELECT DISTINCT ON (user_id, product_id, event_type, user_session) 
       event_time, event_type, product_id, price, user_id, user_session
FROM customers;

---3. delete the table 
DROP TABLE customers;

---4. rename table
ALTER TABLE customers_tmp RENAME TO customers;

---5. check duplicated rows
SELECT COUNT(*) - COUNT(*) FROM (
    SELECT user_id, product_id, event_type, user_session, COUNT(*) as cnt
    FROM customers
    GROUP BY user_id, product_id, event_type, user_session
    HAVING COUNT(*) > 1
) t;


CREATE TABLE items_tmp AS
SELECT 
    product_id,
    MAX(category_id) AS category_id,
    MAX(category_code) AS category_code,
    MAX(brand) AS brand
FROM items
GROUP BY product_id;