CREATE TABLE Tari (
	id serial PRIMARY KEY,
	nume_tara character varying (20) UNIQUE,
	latitudine double precision,
	longitudine double precision
);

CREATE TABLE Orase (
    id serial PRIMARY KEY,
    id_tara serial,
    nume_oras character varying (20),
    latitudine double precision,
	longitudine double precision,
    CONSTRAINT fk_id_tara
        FOREIGN KEY(id_tara)
            REFERENCES Tari(id)
	UNIQUE(id_tara, nume_oras)
);

CREATE TABLE Temperaturi (
	id serial PRIMARY KEY,
	valoare double precision,
	timestamp timestamptz,
	id_oras serial,
	CONSTRAINT fk_id_oras
		FOREIGN KEY(id_oras)
			REFERENCES Orase(id)
	UNIQUE(id_oras, timestamp)
);

INSERT INTO Tari(nume_tara, latitudine, longitudine)
VALUES('Romania', 45.94, 24.96),
	('Franta', 98.3, 26.09);

--delete all content from table
SELECT * FROM Tari;
SELECT * FROM Orase;

DELETE FROM Tari;
ALTER SEQUENCE tari_id_seq RESTART
DELETE FROM Orase;
ALTER SEQUENCE orase_id_seq RESTART


SELECT * FROM Tari;

DELETE FROM Tari;
ALTER SEQUENCE tari_id_seq RESTART


--resetare autoincrement la 0
ALTER SEQUENCE tari_id_seq RESTART

--aflare denumire camp
select pg_get_serial_sequence('Tari', 'id');