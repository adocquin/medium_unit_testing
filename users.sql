CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
INSERT INTO users (id, name, age)
VALUES (uuid_generate_v4(), 'Alice', 28),
    (uuid_generate_v4(), 'Bob', 34),
    (uuid_generate_v4(), 'Charlie', 22);
-- SELECT * FROM users;
-- DROP TABLE users;