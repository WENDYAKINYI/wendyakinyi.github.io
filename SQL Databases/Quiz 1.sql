use comp3421
show tables;
-- 1 --
SELECT*
FROM candy_customer;
-- 2 --
SELECT cust_id, cust_name 
FROM candy_customer 
WHERE cust_type = 'W';
-- 3 --
SELECT username
FROM candy_customer
WHERE cust_phone LIKE '434%';
-- 4 --
SELECT prod_desc, prod_price - prod_cost AS profit
FROM candy_product
ORDER BY PROFIT DESC

