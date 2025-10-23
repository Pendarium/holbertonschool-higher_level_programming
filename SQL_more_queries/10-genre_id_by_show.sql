-- List all shows with at least one genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Sort by tv_shows.title and tv_show_genres.genre_id

SELECT ts.title, tg.genre_id
FROM tv_shows ts, tv_show_genres tg
WHERE ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;
