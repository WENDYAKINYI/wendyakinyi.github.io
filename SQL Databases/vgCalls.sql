use comp3421;

-- Call to gameProfitByRegion for Worldwide profits greater than $35 million
CALL gameProfitByRegion(35, 'WD');

-- Results:
-- # GameTitle	           Profit
-- Wii Sports	           82.74000000000001
-- Super Mario Bros.       40.24
-- Mario Kart Wii	       35.830000000000005

-- Call to gameProfitByRegion for European profits greater than $12 million
CALL gameProfitByRegion(12, 'EU');

-- Results:
-- # GameTitle	    Profit
-- Wii Sports	    29.02
-- Mario Kart Wii	12.88

-- Call to gameProfitByRegion for Japanese profits greater than $10 million
CALL gameProfitByRegion(10, 'JP');

-- Results:
-- # GameTitle	               Profit
-- Pokemon Red/Pokemon Blue	   10.22

CALL genreRankingByRegion('Sports', 'WD');

-- Results:
-- Attached RankingbyregionWD.csv

-- Call to genreRankingByRegion for Role-playing games in North America
CALL genreRankingByRegion('Role-playing', 'NA');

-- Results:
-- Attached RankingbyregionNA.csv

-- Call to genreRankingByRegion for Role-playing games in Japan
CALL genreRankingByRegion('Role-playing', 'JP');

-- Results:
-- Attached RankingbyregionJP.csv


-- Calls to published releases
call publishedReleases('Electronic Arts', 'Sports');
-- Results:
# TotalReleases
-- 561

call publishedReleases('Electronic Arts', 'Action');
-- Results:
# TotalReleases
-- 183

-- Call to addNewRelease
CALL addNewRelease('Foo Attacks', 'X360', 'Strategy', 'Stevenson Studios');

SELECT * FROM vg_games WHERE name = 'Foo Attacks';
SELECT * FROM vg_platforms WHERE platform_name = 'X360';
SELECT * FROM vg_genres WHERE genre_name = 'Strategy';
SELECT * FROM vg_publishers WHERE publisher_name = 'Stevenson Studios';












