use comp3421;
DELIMITER $$

CREATE PROCEDURE gameProfitByRegion(
    IN min_profit DOUBLE,     -- Minimum profit to filter results
    IN region VARCHAR(2)      -- Region code (e.g., WD, NA, EU, JP)
)
BEGIN
    -- Dynamically calculate profit based on the region
    SELECT 
        g.name AS GameTitle, 
        CASE
            WHEN region = 'WD' THEN (rs.na_sales + rs.eu_sales + rs.jp_sales + rs.other_sales)
            WHEN region = 'NA' THEN rs.na_sales
            WHEN region = 'EU' THEN rs.eu_sales
            WHEN region = 'JP' THEN rs.jp_sales
            ELSE 0 -- Fallback for unexpected regions (shouldn't occur)
        END AS Profit
    FROM vg_games g
    JOIN vg_regional_sales rs ON g.game_id = rs.game_id
    HAVING Profit > min_profit;
END$$

DELIMITER ;
DELIMITER $$

CREATE PROCEDURE genreRankingByRegion(
    IN genre_name VARCHAR(50),   -- Genre to filter by
    IN region VARCHAR(2)         -- Region code (e.g., WD, NA, EU, JP)
)
BEGIN
    -- Dynamically calculate profit by region and rank them
    SELECT 
        g.name AS GameTitle,
        (CASE
            WHEN region = 'WD' THEN (rs.na_sales + rs.eu_sales + rs.jp_sales + rs.other_sales)
            WHEN region = 'NA' THEN rs.na_sales
            WHEN region = 'EU' THEN rs.eu_sales
            WHEN region = 'JP' THEN rs.jp_sales
            ELSE 0
        END) AS Profit,
        RANK() OVER (
            ORDER BY 
            CASE
                WHEN region = 'WD' THEN (rs.na_sales + rs.eu_sales + rs.jp_sales + rs.other_sales)
                WHEN region = 'NA' THEN rs.na_sales
                WHEN region = 'EU' THEN rs.eu_sales
                WHEN region = 'JP' THEN rs.jp_sales
                ELSE 0
            END DESC
        ) AS GenreRank
    FROM vg_games g
    JOIN vg_regional_sales rs ON g.game_id = rs.game_id
    JOIN vg_genres gen ON g.genre_id = gen.genre_id
    WHERE gen.genre_name = genre_name;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE publishedReleases(
    IN publisher_name VARCHAR(100),   -- Publisher name to filter by
    IN genre_name VARCHAR(50)         -- Genre name to filter by
)
BEGIN
    SELECT 
        COUNT(g.game_id) AS TotalReleases -- Count the total number of titles
    FROM vg_games g
    JOIN vg_publishers p ON g.publisher_id = p.publisher_id
    JOIN vg_genres gen ON g.genre_id = gen.genre_id
    WHERE p.publisher_name = publisher_name
      AND gen.genre_name = genre_name;
END$$

DELIMITER ;


DROP PROCEDURE IF EXISTS addNewRelease;

DELIMITER $$

CREATE PROCEDURE addNewRelease(
    IN game_title VARCHAR(100),
    IN platform_name VARCHAR(50),
    IN genre_name VARCHAR(50),
    IN publisher_name VARCHAR(100)
)
BEGIN
    DECLARE platform_id INT DEFAULT NULL;
    DECLARE genre_id INT DEFAULT NULL;
    DECLARE publisher_id INT DEFAULT NULL;
    DECLARE game_id INT DEFAULT NULL;

    -- Step 1: Fetch or Insert Platform
    SELECT platform_id INTO platform_id
    FROM vg_platforms
    WHERE TRIM(LOWER(platform_name)) = TRIM(LOWER(platform_name))
    LIMIT 1;

    IF platform_id IS NULL THEN
        INSERT INTO vg_platforms (platform_name)
        VALUES (TRIM(platform_name));
        SELECT LAST_INSERT_ID() INTO platform_id;
    END IF;

    -- Step 2: Fetch or Insert Genre
    SELECT genre_id INTO genre_id
    FROM vg_genres
    WHERE TRIM(LOWER(genre_name)) = TRIM(LOWER(genre_name))
    LIMIT 1;

    IF genre_id IS NULL THEN
        INSERT INTO vg_genres (genre_name)
        VALUES (TRIM(genre_name));
        SELECT LAST_INSERT_ID() INTO genre_id;
    END IF;

    -- Step 3: Fetch or Insert Publisher
    SELECT publisher_id INTO publisher_id
    FROM vg_publishers
    WHERE TRIM(LOWER(publisher_name)) = TRIM(LOWER(publisher_name))
    LIMIT 1;

    IF publisher_id IS NULL THEN
        INSERT INTO vg_publishers (publisher_name)
        VALUES (TRIM(publisher_name));
        SELECT LAST_INSERT_ID() INTO publisher_id;
    END IF;

    -- Step 4: Check if the Game Already Exists
    SELECT game_id INTO game_id
    FROM vg_games
    WHERE TRIM(LOWER(name)) = TRIM(LOWER(game_title))
      AND genre_id = genre_id
      AND publisher_id = publisher_id
    LIMIT 1;

    -- Step 5: Insert Game if it Doesn’t Exist
    IF game_id IS NULL THEN
        INSERT INTO vg_games (name, publisher_id, genre_id)
        VALUES (TRIM(game_title), publisher_id, genre_id);
        SELECT LAST_INSERT_ID() INTO game_id;
    END IF;

    -- Step 6: Link Game to Platform
    INSERT IGNORE INTO vg_game_platforms (game_id, platform_id)
    VALUES (game_id, platform_id);

    -- Success Message
    SELECT CONCAT('Game "', game_title, '" added successfully with Platform "', platform_name, '", Genre "', genre_name, '", and Publisher "', publisher_name, '".') AS Message;
END$$

DELIMITER ;















