-- this script can be use to return all not NULL value right score and name by desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;