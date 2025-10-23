-- List all genres and the number of shows linked to each
-- Display: genre - number_of_shows
-- Only display genres with at least one show linked
-- Results sorted by number_of_shows in descending order
-- Only one SELECT statement is allowed

SELECT g.name AS genre, COUNT(tg.show_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
