-- Creating tables for Avocado_finalproject
-- 	 CREATE TABLE Size (
--      	type INT NOT NULL,
--      	small_bags FLOAT NOT NULL,
-- 	 	large_bags FLOAT NOT NULL,
-- 	 	xlarge_bags FLOAT NOT NULL,
-- 	 	total_bags FLOAT NOT NULL,
--    		PRIMARY KEY (type)
-- );

-- CREATE TABLE Avocado (
--  	type INT NOT NULL,
-- 	avg_price FLOAT NOT NULL,
--  	date DATE NOT NULL,
--  	year INT NOT NULL,
-- 	geography VARCHAR (20) NOT NULL,
--  	PRIMARY KEY (type, avg_price)
--  );


--  CREATE TABLE PLU (
--  	avg_price FLOAT NOT NULL,
--  	plu_4946 FLOAT NOT NULL,
-- 	plu_4225 FLOAT NOT NULL,
--   	plu_4770 FLOAT NOT NULL,
--   	total_volume FLOAT NOT NULL,
--  	PRIMARY KEY (avg_price)
-- );

SELECT * FROM Avocado;

-- -- Joining Avocado and PLU
-- SELECT PLU.total_volume,
-- 	 Avocado.type,
--      Avocado.date,
--      Avocado.geography
-- FROM PLU
-- INNER JOIN Avocado
-- ON PLU.avg_price = Avocado.avg_price;

-- DROP TABLE Size;