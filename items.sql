CREATE TABLE items (
	id             SERIAL PRIMARY KEY,
	channel_id     INTEGER REFERENCES channels(id) NOT NULL,
    item_id        VARCHAR,
	name           VARCHAR,
	duration       VARCHAR,
    created        TIMESTAMP(0) NOT NULL DEFAULT NOW()
);
