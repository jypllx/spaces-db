CREATE TABLE plays (
    id          SERIAL PRIMARY KEY,
    item_id     INTEGER NOT NULL REFERENCES items(id),
    user_id     INTEGER NOT NULL REFERENCES users(id),
    length_sec  INTEGER,
    start_sec   INTEGER,
    end_sec     INTEGER
);