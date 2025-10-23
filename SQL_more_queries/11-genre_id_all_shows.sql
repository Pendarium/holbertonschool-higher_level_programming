-- List all shows, including those with no genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Results sorted by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement is allowed

SELECT ts.title, tg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tg ON ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;
