-- Script that lists all the cities of California found in the database hbtn_0d_usa
-- Results are sorted by cities.id in ascending order
-- Not allowed to use JOIN

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
