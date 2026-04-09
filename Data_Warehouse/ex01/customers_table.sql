CREATE TABLE customers AS
SELECT * FROM data_2023_jan;

DO
$$
-- var
DECLARE
    it RECORD; -- iterable
-- fonction
BEGIN
    FOR it IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_name LIKE 'data_202%'
        AND table_name <> 'data_2023_jan'
    LOOP
        -- RAISE NOTICE 'it : % ', it;
        EXECUTE format('INSERT INTO customer SELECT * FROM %I', it.table_name); -- %I identifier
    END LOOP;
END;
$$;