use comp3421;
show tables;
-- 1 --
SELECT 
    mlb_master.name_first, 
    mlb_master.name_last, 
    mlb_pitching.shut_outs
FROM MLB_MASTER
JOIN MLB_PITCHING ON mlb_master.player_id = mlb_pitching.player_id
WHERE mlb_pitching.shut_outs >= 1
ORDER BY mlb_pitching.shut_outs DESC, mlb_master.name_last ASC;
-- 2 --
SELECT 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    (MLB_BATTING .homeruns * 4) + (MLB_BATTING .triples * 3) + (MLB_BATTING .doubles * 2) + (MLB_BATTING .hits - (MLB_BATTING .doubles + MLB_BATTING .triples + MLB_BATTING .homeruns)) AS total_bases
FROM MLB_MASTER
JOIN MLB_BATTING ON MLB_MASTER.player_id = MLB_BATTING .player_id
WHERE MLB_MASTER.name_last = 'Smith'
ORDER BY total_bases DESC;
-- 3 --
SELECT 
    MLB_TEAM.name, 
    MLB_MASTER.name_first AS manager_name_first, 
    MLB_MASTER.name_last AS manager_name_last
FROM MLB_TEAM
JOIN MLB_MANAGER ON MLB_TEAM.team_id = MLB_MANAGER.team_id
JOIN MLB_MASTER ON MLB_MANAGER.player_id = MLB_MASTER.player_id
WHERE MLB_TEAM.league = 'NL' AND MLB_TEAM.division = 'C'
ORDER BY MLB_TEAM.name ASC;
-- 4 --
SELECT 
    MLB_MASTER.throws, 
    COUNT(DISTINCT MLB_MASTER.player_id) AS number_of_pitchers
FROM MLB_MASTER
JOIN MLB_PITCHING ON MLB_MASTER.player_id = MLB_PITCHING.player_id
WHERE MLB_MASTER.throws IN ('R', 'L')
GROUP BY MLB_MASTER.throws
ORDER BY MLB_MASTER.throws ASC;
-- 5 --
SELECT 
    MLB_TEAM.name, 
    AVG(MLB_MASTER.weight) AS average_pitcher_weight
FROM MLB_TEAM
JOIN MLB_PITCHING ON MLB_TEAM.team_id = MLB_PITCHING.team_id
JOIN MLB_MASTER ON MLB_PITCHING.player_id = MLB_MASTER.player_id
GROUP BY MLB_TEAM.name
ORDER BY average_pitcher_weight DESC;
-- 6 --
SELECT 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    MLB_MASTER.height, 
    MLB_TEAM.name AS team_name
FROM MLB_MANAGER
JOIN MLB_MASTER ON MLB_MANAGER.player_id = MLB_MASTER.player_id
JOIN MLB_TEAM ON MLB_MANAGER.team_id = MLB_TEAM.team_id
WHERE MLB_MASTER.height < 70
ORDER BY MLB_MASTER.name_last ASC, MLB_MASTER.name_first ASC;
-- 7 --
SELECT 
    MLB_MASTER.player_id, 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    SUM(MLB_PITCHING.outs_pitched) / 3 AS total_innings_pitched
FROM MLB_PITCHING
JOIN MLB_MASTER ON MLB_PITCHING.player_id = MLB_MASTER.player_id
GROUP BY MLB_MASTER.player_id, MLB_MASTER.name_first, MLB_MASTER.name_last
HAVING COUNT(DISTINCT MLB_PITCHING.team_id) > 1
ORDER BY total_innings_pitched DESC;
-- 8 --
SELECT 
    CONCAT(MLB_MASTER.name_first, ' ', MLB_MASTER.name_last) AS full_name, 
    MLB_PITCHING.wild_pitches
FROM MLB_PITCHING
JOIN MLB_MASTER ON MLB_PITCHING.player_id = MLB_MASTER.player_id
WHERE MLB_PITCHING.wild_pitches >= 13 
  AND MLB_PITCHING.outs_pitched >= 500;
  -- 9 --
  SELECT 
    MLB_MASTER.name_last, 
    CASE 
        WHEN MLB_BATTING.at_bats > 0 THEN (MLB_BATTING.hits / NULLIF(MLB_BATTING.at_bats, 0))
        ELSE 0 
    END AS batting_average, 
    CASE 
        WHEN MLB_PITCHING.outs_pitched IS NOT NULL THEN (MLB_PITCHING.outs_pitched / 3) 
        ELSE 0 
    END AS innings_pitched
FROM MLB_MASTER
LEFT JOIN MLB_BATTING ON MLB_MASTER.player_id = MLB_BATTING.player_id
LEFT JOIN MLB_PITCHING ON MLB_MASTER.player_id = MLB_PITCHING.player_id
WHERE MLB_MASTER.name_last LIKE 'Z%'
ORDER BY MLB_MASTER.name_last;










