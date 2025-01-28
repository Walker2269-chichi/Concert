CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);

INSERT INTO bands (name, hometown) VALUES ("One Direction", "Melbourne");
INSERT INTO bands (name, hometown) VALUES ("Westlife", "London");
INSERT INTO bands (name, hometown) VALUES ("Sauti Saul", "Mombasa");
INSERT INTO bands (name, hometown) VALUES ("Beta", "Perth");
INSERT INTO bands (name, hometown) VALUES ("Oracle", "Madrid");


CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);

INSERT INTO venues (title, city) VALUES ("The Pavilion", "Melbourne");
INSERT INTO venues (title, city) VALUES ("The O2 Arena", "London");
INSERT INTO venues (title, city) VALUES ("The Millennium Ballroom", "Mombasa");
INSERT INTO venues (title, city) VALUES ("The Blue Room", "Perth");
INSERT INTO venues (title, city) VALUES ("The Grand Ole Opry", "Madrid");

CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);

INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, "2022-01-01");
INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, "2022-02-15");
INSERT INTO concerts (band_id, venue_id, date) VALUES (3, 3, "2022-03-30");
INSERT INTO concerts (band_id, venue_id, date) VALUES (4, 4, "2022-04-10");
