-- List all shows and all genres linked to that show
-- If a show doesn't have a genre, display NULL in the genre column
-- Display: tv_shows.title - tv_genres.name
-- Results sorted by show title and genre name
-- Only one SELECT statement is allowed

SELECT ts.title, g.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tg ON ts.id = tg.tv_show_id
LEFT JOIN genres g ON tg.genre_id = g.id
ORDER BY ts.title ASC, g.name ASC;
