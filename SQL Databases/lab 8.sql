use comp3421;
-- Code Comments:
-- Execution time without index (myCreateTable): 382.859 seconds
-- Execution time with index (myCreateTable):380.484 seconds
-- Execution time without index (mySelectTest): 11.688 seconds
-- Execution time with index (mySelectTest): 12.782 seconds
DELIMITER $$

-- Step 1: Drop myCreateTable procedure if it already exists
DROP PROCEDURE IF EXISTS myCreateTable $$

-- Step 2: Stored Procedure to Create and Populate Table
CREATE PROCEDURE myCreateTable(IN numEntries INT)
BEGIN
    -- Declare the variable for looping
    DECLARE i INT DEFAULT 0;

    -- Drop table if it already exists to allow for rerunning the test
    DROP TABLE IF EXISTS test_table;
    
    -- Create table with a BIGINT primary key and a second INT field
    CREATE TABLE test_table (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        random_value INT
    );

    -- Loop to insert random integers
    WHILE i < numEntries DO
        INSERT INTO test_table (random_value) VALUES (FLOOR(RAND() * 1000));
        SET i = i + 1;
    END WHILE;
END$$

-- Step 3: Drop mySelectTest procedure if it already exists
DROP PROCEDURE IF EXISTS mySelectTest $$

-- Step 4: Stored Procedure to Test Selects Without Index
CREATE PROCEDURE mySelectTest(IN target INT, IN numSelects INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE row_count INT;

    -- Loop to execute SELECTs and count rows matching target
    WHILE i < numSelects DO
        SELECT COUNT(*) INTO row_count FROM test_table WHERE random_value = target;
        SET i = i + 1;
    END WHILE;
END$$

DELIMITER ;

-- Step 5: Call myCreateTable to insert 100,000 entries and record execution time
-- Execution time (without index) for CALL myCreateTable(100000): X seconds
CALL myCreateTable(60000);

-- Step 6: Call mySelectTest to perform 1,000 select operations and record execution time
-- Execution time (without index) for CALL mySelectTest(50, 1000): Y seconds
CALL mySelectTest(50, 1000);

-- Step 7: Add an index to the random_value column
CREATE INDEX idx_random_value ON test_table(random_value);

-- Step 8: Rerun myCreateTable with index and record execution time
-- Execution time (with index) for CALL myCreateTable(100000): Z seconds
CALL myCreateTable(60000);

-- Step 9: Rerun mySelectTest with index and record execution time
-- Execution time (with index) for CALL mySelectTest(50, 1000): W seconds
CALL mySelectTest(50, 1000); 

