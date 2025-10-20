-- this script can be use to group all same value and return number of time is grouped
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;