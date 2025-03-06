use comp3421;
show tables;
-- 1 --
SELECT team_id, league, division, name
FROM MLB_TEAM;
-- 2 --
SELECT MAX(complete_games) AS largest_complete_games
FROM MLB_PITCHING;
-- 3 --
SELECT COUNT(*) AS number_of_players
FROM MLB_MASTER
WHERE debut BETWEEN '2014-09-10' AND '2014-09-30';
-- 4 --
SELECT MAX(DATEDIFF(final_game, debut)) AS biggest_difference
FROM MLB_MASTER;
-- 5 --
SELECT AVG(opp_batting_avg) AS average_opponents_batting_avg
FROM MLB_PITCHING
WHERE games >= 25;
-- 6 --
SELECT 
    MAX(attendance) AS biggest_attendance,
    MIN(attendance) AS smallest_attendance,
    MAX(attendance) - MIN(attendance) AS attendance_difference
FROM MLB_TEAM;
-- 7 --
SELECT park
FROM MLB_TEAM
WHERE LOWER(park) LIKE '%park%' 
   OR LOWER(park) LIKE '%field%' 
   OR LOWER(park) LIKE '%stadium%'
ORDER BY park ASC;
-- 8 --
SELECT COUNT(DISTINCT team_id) AS teams_with_multiple_managers
FROM MLB_MANAGER
GROUP BY team_id
HAVING COUNT(stint) > 1;
-- 9 --
SELECT MAX(stolen_bases / (stolen_bases + caught_stealing)) AS highest_stolen_base_percentage
FROM MLB_BATTING
WHERE (stolen_bases + caught_stealing) >= 20;
-- 10 --
SELECT 
    name, 
    league, 
    WON_WS, 
    WON_LG, 
    WON_DIV, 
    WON_WC
FROM MLB_TEAM
WHERE WON_DIV = 'Y' OR WON_WC = 'Y'
ORDER BY 
    WON_WS = 'Y' DESC,   -- World Series winners
    WON_LG = 'Y' DESC,   -- League winners
    WON_DIV = 'Y' DESC,  -- Division winners
    WON_WC = 'Y' DESC,   -- Wild Card winners
    name ASC;









