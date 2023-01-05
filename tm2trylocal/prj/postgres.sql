SELECT * FROM Tari;
SELECT * FROM Orase;

DELETE FROM Orase;
ALTER SEQUENCE orase_id_seq RESTART;
DELETE FROM Tari;
ALTER SEQUENCE tari_id_seq RESTART;



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
	
);

ALTER TABLE Orase
ADD UNIQUE (id_tara, nume_oras);

CREATE TABLE Temperaturi (
	id serial PRIMARY KEY,
	valoare double precision,
	timestamp timestamptz,
	id_oras serial,
	CONSTRAINT fk_id_oras
		FOREIGN KEY(id_oras)
			REFERENCES Orase(id)
	
);

ALTER TABLE Temperaturi
ADD UNIQUE (id_oras, timestamp);
