use comp3421;
show tables;
-- 1 --
SELECT 
    MLB_MASTER.name_last
FROM MLB_BATTING
JOIN MLB_MASTER ON MLB_BATTING.player_id = MLB_MASTER.player_id
WHERE MLB_BATTING.doubles > 45
GROUP BY MLB_MASTER.name_last;

-- 2 --
SELECT name_last 
FROM MLB_MASTER 
WHERE player_id IN (
    SELECT player_id 
    FROM MLB_BATTING 
    WHERE doubles > 45
);

-- 3 --
SELECT 
    MLB_MASTER.name_last, 
    MLB_BATTING.doubles
FROM MLB_BATTING
JOIN MLB_MASTER ON MLB_BATTING.player_id = MLB_MASTER.player_id
WHERE MLB_BATTING.doubles > 45
ORDER BY MLB_BATTING.doubles DESC;

-- 4 --
SELECT 
    MLB_TEAM.name AS team_name, 
    MLB_TEAM.wins
FROM MLB_TEAM
WHERE MLB_TEAM.wins > (
    SELECT AVG(wins) 
    FROM MLB_TEAM
)
ORDER BY MLB_TEAM.wins DESC;

-- 5 --
SELECT 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    MLB_PITCHING.hit_by_pitch
FROM MLB_PITCHING
JOIN MLB_MASTER ON MLB_PITCHING.player_id = MLB_MASTER.player_id
WHERE MLB_PITCHING.hit_by_pitch = (
    SELECT MAX(hit_by_pitch) 
    FROM MLB_PITCHING
)
LIMIT 1;

-- 6 --
SELECT 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    MLB_MASTER.height, 
    MLB_TEAM.name AS team_name
FROM MLB_MANAGER
JOIN MLB_MASTER ON MLB_MANAGER.player_id = MLB_MASTER.player_id
JOIN MLB_TEAM ON MLB_MANAGER.team_id = MLB_TEAM.team_id
WHERE MLB_MASTER.height = (
    SELECT MIN(height) 
    FROM MLB_MASTER
    JOIN MLB_MANAGER ON MLB_MASTER.player_id = MLB_MANAGER.player_id
);


-- 7 --
SELECT 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    (MLB_PITCHING.strikeouts / MLB_PITCHING.walks) AS k_bb_ratio
FROM MLB_PITCHING
JOIN MLB_MASTER ON MLB_PITCHING.player_id = MLB_MASTER.player_id
WHERE MLB_PITCHING.walks >= 1
  AND MLB_PITCHING.games >= 25
  AND MLB_PITCHING.walks > 0
ORDER BY k_bb_ratio DESC
LIMIT 10;

SELECT 
    MLB_MASTER.name_first, 
    MLB_MASTER.name_last, 
    (SUM(MLB_PITCHING.strikeouts) / SUM(MLB_PITCHING.walks)) AS k_bb_ratio
FROM MLB_PITCHING
JOIN MLB_MASTER ON MLB_PITCHING.player_id = MLB_MASTER.player_id
GROUP BY MLB_PITCHING.player_id, MLB_MASTER.name_first, MLB_MASTER.name_last
HAVING SUM(MLB_PITCHING.walks) >= 1
   AND SUM(MLB_PITCHING.games) >= 25
ORDER BY k_bb_ratio DESC
LIMIT 10;

-- 8 --
SELECT DISTINCT MLB_BATTING.team_id
FROM MLB_BATTING
WHERE MLB_BATTING.homeruns > 35

UNION

SELECT DISTINCT MLB_BATTING.team_id
FROM MLB_BATTING
WHERE MLB_BATTING.stolen_bases > 40
ORDER BY team_id ASC;

-- 9 --
SELECT player_id
FROM MLB_BATTING
WHERE homeruns > 10
  AND player_id IN (
      SELECT player_id
      FROM MLB_PITCHING
  );

-- 10 --
CREATE VIEW mlb_national AS
SELECT *
FROM MLB_TEAM
WHERE league = 'NL';







