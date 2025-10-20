-- this script can be use to return all not NULL value right score and name by desc
SELECT name FROM second_table WHERE name IS NULL AND name != '';
SELECT score, name FROM second_table ORDER BY score DESC;