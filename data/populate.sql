-- SQLite

INSERT INTO asielen (naam, plaats)
VALUES ("Animal Exodus", "Gent"),
       ("Dierenhart", "Hasselt")
;

INSERT INTO dieren (naam, soort, geslacht, opname_datum, asiel_id)
VALUES ("Bennie", "hond", "M", "2020-10-19", 1),
       ("Kitty", "kat", "V", "2019-05-06", 1),
       ("Sammy", "hamster", "M", "2021-01-01", 2),
       ("Dixie", "kat", "V", "2021-02-04", 2)
;