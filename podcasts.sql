CREATE TABLE podcasts (
	id SERIAL,
	feed_id INTEGER REFERENCES feeds(id) NOT NULL,
	name VARCHAR,
	duration INTEGER
);
