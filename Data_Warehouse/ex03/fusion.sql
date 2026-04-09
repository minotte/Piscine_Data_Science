-- 1. create tempory table to fusionned items and customers 
CREATE TABLE customers_fusionned AS
SELECT 
    c.event_time,
    c.event_type,
    c.product_id,
    c.price,
    c.user_id,
    c.user_session,
    i.category_id,
    i.category_code,
    i.brand
FROM customers c
LEFT JOIN items i ON c.product_id = i.product_id;



-- 2. delete customers
DROP TABLE customers;
-- 3. rename fusionned table in customers 
ALTER TABLE customers_fusionned RENAME TO customers;
-- 4. check 
-- SELECT * FROM customers LIMIT 10;