-- this script can be use to check a specified values 
USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
