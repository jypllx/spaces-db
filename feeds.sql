CREATE TABLE feeds (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	genre VARCHAR,
	language VARCHAR,
	producer_id INTEGER REFERENCES producers(id),
	url VARCHAR,
	link VARCHAR
);	
