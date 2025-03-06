use comp3421;
-- Creating the MUSIC_GENRE table
CREATE TABLE MUSIC_GENRE (
    GENRE_ID INT AUTO_INCREMENT,            -- Surrogate primary key
    GENRE_NAME VARCHAR(25) NOT NULL,        -- Genre name, max 25 characters
    CONSTRAINT PK_GENRE PRIMARY KEY (GENRE_ID)  -- Named primary key constraint
);

-- Bulk insert into the MUSIC_GENRE table using data from the MUSIC_ARTIST table
INSERT INTO MUSIC_GENRE (GENRE_NAME)
SELECT DISTINCT GENRE_NAME FROM MUSIC_ARTIST;

-- Select statement to check the inserted data
SELECT * FROM MUSIC_GENRE;

-- Step a: Add a new column for GENRE_ID
ALTER TABLE MUSIC_ARTIST ADD GENRE_ID INT;

-- Step b: Add a foreign key constraint linking GENRE_ID to the MUSIC_GENRE table
UPDATE MUSIC_ARTIST A
JOIN MUSIC_GENRE G ON A.GENRE_NAME = G.GENRE_NAME
SET A.GENRE_ID = G.GENRE_ID;

-- Step c: Remove the old GENRE_NAME column
ALTER TABLE MUSIC_ARTIST DROP COLUMN GENRE_NAME;

-- Select statement to check the updated MUSIC_ARTIST table
SELECT * FROM MUSIC_ARTIST;

-- Find the ARTIST_ID for Lil' Wayne
SELECT ARTIST_ID FROM MUSIC_ARTIST
WHERE ARTIST_NAME = 'Lil\' Wayne';
-- Delete all albums associated with Lil' Wayne
DELETE FROM MUSIC_ALBUM
WHERE ARTIST_ID = (SELECT ARTIST_ID FROM MUSIC_ARTIST WHERE ARTIST_NAME = 'Lil\' Wayne');
-- Delete Lil' Wayne from MUSIC_ARTIST
DELETE FROM MUSIC_ARTIST
WHERE ARTIST_NAME = 'Lil\' Wayne';


