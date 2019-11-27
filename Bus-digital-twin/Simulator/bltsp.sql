CREATE TABLE stations (
    id INTEGER PRIMARY KEY
);

CREATE TABLE buses (
    id INTEGER PRIMARY KEY,
    position INTEGER,
    load INTEGER,
    capacity INTEGER,
    status INTEGER,
    waiting INTEGER,
    direction INTEGER,
    type INTEGER,
    FOREIGN KEY (position) REFERENCES stations(id)
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    position INTEGER,
    early_time INTEGER,
    late_time INTEGER,
    destination INTEGER,
    FOREIGN KEY (position) REFERENCES stations(id),
    FOREIGN KEY (destination) REFERENCES stations(id)
);