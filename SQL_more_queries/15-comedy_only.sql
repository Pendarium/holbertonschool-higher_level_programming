-- List all shows with the genre Comedy
-- Display: tv_shows.title
-- Results sorted by show title in ascending order
-- Only one SELECT statement is allowed

SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tg ON ts.id = tg.show_id
JOIN tv_genres g ON tg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY ts.title ASC;
