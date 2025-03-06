use comp3421;
-- Creating MUSIC_ARTIST table
CREATE TABLE MUSIC_ARTIST (
    ARTIST_ID INT AUTO_INCREMENT,            -- Surrogate primary key
    ARTIST_NAME VARCHAR(100) NOT NULL,       -- Artist name, max 100 characters
    ORIGIN_CITY VARCHAR(50) NOT NULL,        -- Origin city, max 50 characters
    GENRE_NAME ENUM('Rock', 'Jazz', 'Pop', 'Hip Hop', 'Country') NOT NULL,  -- Only these genres allowed
    CONSTRAINT PK_ARTIST PRIMARY KEY (ARTIST_ID)  -- Named primary key constraint
);

-- Creating MUSIC_LABEL table
CREATE TABLE MUSIC_LABEL (
    LABEL_ID INT AUTO_INCREMENT,             -- Surrogate primary key
    LABEL_NAME VARCHAR(75) NOT NULL,         -- Label name, max 75 characters
    CONSTRAINT PK_LABEL PRIMARY KEY (LABEL_ID)  -- Named primary key constraint
);
-- Creating MUSIC_FORMAT table
CREATE TABLE MUSIC_FORMAT (
    FORMAT_ID CHAR(1),                    -- Primary key, single-character
    FORMAT_NAME VARCHAR(50) NOT NULL,     -- Format name, max 50 characters
    CONSTRAINT PK_FORMAT PRIMARY KEY (FORMAT_ID)  -- Named primary key constraint
);

-- Creating MUSIC_ALBUM table
CREATE TABLE MUSIC_ALBUM (
    ALBUM_ID INT AUTO_INCREMENT,              -- Surrogate primary key
    ALBUM_NAME VARCHAR(100) NOT NULL,         -- Album name, max 100 characters
    ARTIST_ID INT NOT NULL,                   -- Foreign key to MUSIC_ARTIST table
    RELEASE_DATE DATE NOT NULL,               -- Release date
    RECORDS_SOLD INT UNSIGNED,                -- Records sold, less than 1 billion
    ORIGINAL_FORMAT CHAR(1) NOT NULL,         -- Format ID (to be linked to MUSIC_FORMAT table)
    LABEL_ID INT NOT NULL,                    -- Foreign key to MUSIC_LABEL table
    CONSTRAINT PK_ALBUM PRIMARY KEY (ALBUM_ID),    -- Named primary key constraint
    CONSTRAINT CK_RECORDS_SOLD CHECK (RECORDS_SOLD < 1000000000), -- Limit records sold to less than 1 billion
    CONSTRAINT FK_ALBUM_ARTIST FOREIGN KEY (ARTIST_ID) 
        REFERENCES MUSIC_ARTIST(ARTIST_ID),    -- Foreign key constraint to MUSIC_ARTIST
    CONSTRAINT FK_ALBUM_LABEL FOREIGN KEY (LABEL_ID) 
        REFERENCES MUSIC_LABEL(LABEL_ID),      -- Foreign key constraint to MUSIC_LABEL
    CONSTRAINT FK_ALBUM_FORMAT FOREIGN KEY (ORIGINAL_FORMAT) 
        REFERENCES MUSIC_FORMAT(FORMAT_ID)     -- Foreign key constraint to MUSIC_FORMAT
);
