use comp3421;
-- Inserting data into the MUSIC_ARTIST table
INSERT INTO MUSIC_ARTIST (ARTIST_NAME, ORIGIN_CITY, GENRE_NAME)
VALUES
('Nirvana', 'Seattle, WA', 'Rock'),
('Miles Davis', 'Alton, IL', 'Jazz'),
('Michael Jackson', 'Gary, IN', 'Pop'),
('Lil\' Wayne', 'New Orleans, LA', 'Hip Hop'),  
('Willie Nelson', 'Abbott, TX', 'Country');

-- Select statement to check the inserted data
SELECT * FROM MUSIC_ARTIST;

-- Inserting data into the MUSIC_LABEL table
INSERT INTO MUSIC_LABEL (LABEL_NAME)
VALUES
('DGC Records'),
('Columbia'),
('Epic Records'),
('Cash Money');

-- Select statement to check the inserted data
SELECT * FROM MUSIC_LABEL;

-- Inserting data into the MUSIC_FORMAT table
INSERT INTO MUSIC_FORMAT (FORMAT_ID, FORMAT_NAME)
VALUES
('V', 'Vinyl'),
('T', 'Cassette Tape'),
('C', 'Compact Disc'),
('D', 'Digital');

-- Select statement to check the inserted data
SELECT * FROM MUSIC_FORMAT;

-- Inserting data into the MUSIC_ALBUM table with date conversion
INSERT INTO MUSIC_ALBUM (ALBUM_NAME, ARTIST_ID, RELEASE_DATE, RECORDS_SOLD, ORIGINAL_FORMAT, LABEL_ID)
VALUES
('Nevermind', 1, STR_TO_DATE('23-SEP-91', '%d-%b-%y'), 30000000, 'C', 1),
('In Utero', 1, STR_TO_DATE('21-SEP-93', '%d-%b-%y'), 15000000, 'C', 1),
('Kind of Blue', 2, STR_TO_DATE('17-AUG-59', '%d-%b-%y'), 4000000, 'V', 2),
('Thriller', 3, STR_TO_DATE('30-NOV-82', '%d-%b-%y'), 65000000, 'T', 3),
('Bad', 3, STR_TO_DATE('01-SEP-87', '%d-%b-%y'), 45000000, 'T', 3),
('The Carter III', 4, STR_TO_DATE('09-JUN-08', '%d-%b-%y'), 3800000, 'D', 4),
('Red Headed Stranger', 5, STR_TO_DATE('01-MAY-75', '%d-%b-%y'), 2000000, 'V', 2);

-- Select statement to check the inserted data
SELECT * FROM MUSIC_ALBUM;


