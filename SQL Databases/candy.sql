use comp3421;
SELECT 
    candy_customer.cust_name,
    candy_cust_type.cust_type_desc,
    candy_product.prod_desc,
    candy_purchase.pounds
FROM 
    candy_purchase
JOIN 
    candy_customer ON candy_purchase.cust_id = candy_customer.cust_id
JOIN 
    candy_cust_type ON candy_customer.cust_type = candy_cust_type.cust_type
JOIN 
    candy_product ON candy_purchase.prod_id = candy_product.prod_id;

DROP TABLE IF EXISTS candy_matview;

CREATE TABLE candy_matview (
    view_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(30),
    cust_type_desc VARCHAR(10),
    prod_desc VARCHAR(30),
    pounds FLOAT
);

INSERT INTO candy_matview (cust_name, cust_type_desc, prod_desc, pounds)
SELECT 
    candy_customer.cust_name,
    candy_cust_type.cust_type_desc,
    candy_product.prod_desc,
    candy_purchase.pounds
FROM 
    candy_purchase
JOIN 
    candy_customer ON candy_purchase.cust_id = candy_customer.cust_id
JOIN 
    candy_cust_type ON candy_customer.cust_type = candy_cust_type.cust_type
JOIN 
    candy_product ON candy_purchase.prod_id = candy_product.prod_id;

DELIMITER //

CREATE TRIGGER after_insert_candy_purchase
AFTER INSERT ON candy_purchase
FOR EACH ROW
BEGIN
    INSERT INTO candy_matview (cust_name, cust_type_desc, prod_desc, pounds)
    SELECT 
        candy_customer.cust_name,
        candy_cust_type.cust_type_desc,
        candy_product.prod_desc,
        NEW.pounds
    FROM 
        candy_customer
    JOIN 
        candy_cust_type ON candy_customer.cust_type = candy_cust_type.cust_type
    JOIN 
        candy_product ON candy_product.prod_id = NEW.prod_id
    WHERE 
        candy_customer.cust_id = NEW.cust_id;
END//

DELIMITER ;

INSERT INTO candy_purchase VALUES
(100,
 (SELECT prod_id FROM candy_product WHERE prod_desc = 'Nuts Not Nachos'),
 (SELECT cust_id FROM candy_customer WHERE cust_name = 'The Candy Kid'),
 '2020-11-2', 
 '2020-11-6',
 5.2,
 'PAID');

SELECT * FROM candy_matview;

