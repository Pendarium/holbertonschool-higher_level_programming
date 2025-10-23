-- List all genres of the show Dexter
-- Display: tv_genres.name
-- Results sorted by genre name in ascending order
-- Only one SELECT statement is allowed

SELECT g.name
FROM tv_shows ts
JOIN tv_show_genres tg ON ts.id = tg.show_id
JOIN tv_genres g ON tg.genre_id = g.id
WHERE ts.title = 'Dexter'
ORDER BY g.name ASC;
