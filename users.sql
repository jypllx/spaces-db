CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR,
    lastname VARCHAR,
    login VARCHAR,
    created TIMESTAMP(0) NOT NULL DEFAULT NOW()
);