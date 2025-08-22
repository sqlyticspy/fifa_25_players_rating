-- Find teams with the highest average player rating.
SELECT 
	team, 
    AVG(rating) AS avg_rating,
    COUNT(*) AS player_count
FROM players_rating
GROUP BY team
ORDER BY avg_rating DESC;

-- Compare average skills by position to identify position-specific strenghts.;
SELECT 
	position,
    ROUND(AVG(skill_move),2) AS avg_skill
FROM players_rating pr
JOIN players_info pi
	ON pi.player_id=pr.player_id
GROUP BY position
ORDER BY avg_skill DESC;


-- Compare average player ratings across different leagues.;
SELECT 
	league,
	ROUND(AVG(rating),2) AS avg_rating,
    gender
FROM players_rating pr
JOIN players_info pi
	ON pr.player_id=pi.player_id
GROUP BY league, gender
ORDER BY avg_rating DESC;

-- Analyze physical characteristics by player position.;
SELECT 
	position,
    ROUND(AVG(height), 2) AS avg_height,
    ROUND(AVG(weight), 2) AS avg_weight
FROM players_rating pr
JOIN players_info pi
	ON pr.player_id = pi.player_id
GROUP BY position
ORDER BY avg_height DESC;