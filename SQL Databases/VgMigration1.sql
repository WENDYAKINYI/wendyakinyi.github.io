use comp3421;

SELECT COUNT(DISTINCT name) AS unique_games FROM vg_csv;
SELECT COUNT(DISTINCT platform) AS unique_platforms FROM vg_csv;
SELECT COUNT(DISTINCT genre) AS unique_genres FROM vg_csv;
SELECT COUNT(DISTINCT publisher) AS unique_publishers FROM vg_csv;

SELECT platform, COUNT(*) AS total_games
FROM vg_csv
GROUP BY platform
ORDER BY total_games DESC;

SELECT publisher, COUNT(*) AS total_games
FROM vg_csv
GROUP BY publisher
ORDER BY total_games DESC;

SELECT genre, COUNT(*) AS total_games
FROM vg_csv
GROUP BY genre
ORDER BY total_games DESC;

SELECT name, COUNT(DISTINCT platform) AS platforms_count
FROM vg_csv
GROUP BY name
HAVING platforms_count > 1;

-- Step 1: Drop tables if they exist (to start fresh)
DROP TABLE IF EXISTS vg_game_platforms;
DROP TABLE IF EXISTS vg_regional_sales;
DROP TABLE IF EXISTS vg_games;
DROP TABLE IF EXISTS vg_platforms;
DROP TABLE IF EXISTS vg_genres;
DROP TABLE IF EXISTS vg_publishers;

-- Step 2: Create Tables

-- Create vg_publishers Table
CREATE TABLE vg_publishers (
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(100) UNIQUE NOT NULL
);

-- Create vg_genres Table
CREATE TABLE vg_genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) UNIQUE NOT NULL
);

-- Create vg_platforms Table
CREATE TABLE vg_platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(50) UNIQUE NOT NULL
);

-- Create vg_games Table
CREATE TABLE vg_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    ranking INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    release_year YEAR NOT NULL,
    publisher_id INT NOT NULL,
    genre_id INT NOT NULL,
    global_sales DOUBLE NOT NULL,
    FOREIGN KEY (publisher_id) REFERENCES vg_publishers(publisher_id),
    FOREIGN KEY (genre_id) REFERENCES vg_genres(genre_id)
);

-- Create vg_regional_sales Table
CREATE TABLE vg_regional_sales (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    na_sales DOUBLE NOT NULL,
    eu_sales DOUBLE NOT NULL,
    jp_sales DOUBLE NOT NULL,
    other_sales DOUBLE NOT NULL,
    FOREIGN KEY (game_id) REFERENCES vg_games(game_id)
);

-- Create vg_game_platforms Table (Bridge Table for Many-to-Many Relationship)
CREATE TABLE vg_game_platforms (
    game_id INT NOT NULL,
    platform_id INT NOT NULL,
    PRIMARY KEY (game_id, platform_id),
    FOREIGN KEY (game_id) REFERENCES vg_games(game_id),
    FOREIGN KEY (platform_id) REFERENCES vg_platforms(platform_id)
);

-- Output a success message for debugging
SELECT 'Tables created successfully!' AS Status;

-- Step 1: Insert publishers
INSERT INTO vg_publishers (publisher_name)
SELECT DISTINCT publisher
FROM vg_csv
WHERE publisher IS NOT NULL AND publisher <> '';

-- Step 2: Insert  Genres
INSERT INTO vg_genres (genre_name)
SELECT DISTINCT genre
FROM vg_csv
WHERE genre IS NOT NULL AND genre <> '';

-- Step 3: Insert Platforms
INSERT INTO vg_platforms (platform_name)
SELECT DISTINCT platform
FROM vg_csv
WHERE platform IS NOT NULL AND platform <> '';


-- Step 4: Insert Games
INSERT INTO vg_games (ranking, name, release_year, publisher_id, genre_id, global_sales)
SELECT 
    CAST(ranking AS SIGNED),
    name,
    CASE 
        WHEN year REGEXP '^[0-9]{4}$' AND CAST(year AS UNSIGNED) BETWEEN 1901 AND 2155 
        THEN CAST(year AS UNSIGNED) -- Valid 4-digit year within range
        ELSE 1901 -- Default value for invalid or missing year
    END AS release_year,
    (SELECT publisher_id FROM vg_publishers WHERE publisher_name = vg_csv.publisher LIMIT 1),
    (SELECT genre_id FROM vg_genres WHERE genre_name = vg_csv.genre LIMIT 1),
    CASE 
        WHEN global_sales REGEXP '^[0-9]+(\.[0-9]+)?$' THEN CAST(global_sales AS DECIMAL(10, 2))
        ELSE 0.0 -- Default value for missing or invalid sales
    END AS global_sales
FROM vg_csv
WHERE name IS NOT NULL AND name <> '';

-- Step 4: Insert Regional Sales
INSERT INTO vg_regional_sales (game_id, na_sales, eu_sales, jp_sales, other_sales)
SELECT
    (SELECT game_id 
     FROM vg_games 
     WHERE vg_games.name = vg_csv.name 
       AND vg_games.release_year = CASE 
           WHEN vg_csv.year REGEXP '^[0-9]{4}$' AND CAST(vg_csv.year AS UNSIGNED) BETWEEN 1901 AND 2155 
           THEN CAST(vg_csv.year AS UNSIGNED)
           ELSE 1901 -- Default year for invalid or missing year
       END
     LIMIT 1),
    CASE 
        WHEN na_sales REGEXP '^[0-9]+(\.[0-9]+)?$' THEN CAST(na_sales AS DECIMAL(10, 2))
        ELSE 0.0
    END AS na_sales,
    CASE 
        WHEN eu_sales REGEXP '^[0-9]+(\.[0-9]+)?$' THEN CAST(eu_sales AS DECIMAL(10, 2))
        ELSE 0.0
    END AS eu_sales,
    CASE 
        WHEN jp_sales REGEXP '^[0-9]+(\.[0-9]+)?$' THEN CAST(jp_sales AS DECIMAL(10, 2))
        ELSE 0.0
    END AS jp_sales,
    CASE 
        WHEN other_sales REGEXP '^[0-9]+(\.[0-9]+)?$' THEN CAST(other_sales AS DECIMAL(10, 2))
        ELSE 0.0
    END AS other_sales
FROM vg_csv
WHERE name IS NOT NULL AND name <> '';

-- Step 5: Insert Game Platforms
INSERT INTO vg_game_platforms (game_id, platform_id)
SELECT DISTINCT
    (SELECT game_id 
     FROM vg_games 
     WHERE vg_games.name = vg_csv.name 
       AND vg_games.release_year = CASE 
           WHEN vg_csv.year REGEXP '^[0-9]{4}$' AND CAST(vg_csv.year AS UNSIGNED) BETWEEN 1901 AND 2155 
           THEN CAST(vg_csv.year AS UNSIGNED)
           ELSE 1901 -- Default year for invalid or missing year
       END
     LIMIT 1),
    (SELECT platform_id 
     FROM vg_platforms 
     WHERE vg_platforms.platform_name = vg_csv.platform 
     LIMIT 1)
FROM vg_csv
WHERE name IS NOT NULL AND name <> ''
  AND platform IS NOT NULL AND platform <> '';








