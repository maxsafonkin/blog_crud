\c postgres;
CREATE TABLE
    posts (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL
    );