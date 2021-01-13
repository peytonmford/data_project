-- Creating tables for Avocado_finalproject
--  CREATE TABLE size (
-- 	type VARCHAR (30) NOT NULL,
--  	small_bags FLOAT NOT NULL,
-- 	large_bags FLOAT NOT NULL,
--  	xlarge_bags FLOAT NOT NULL,
-- 	total_bags FLOAT NOT NULL
--  );

--    CREATE TABLE avocado (
--  	type VARCHAR (30) NOT NULL,
--   	average_price FLOAT NOT NULL,
-- 	on_date DATE NOT NULL,
-- 	year INT NOT NULL,
--   	total_volume FLOAT NOT NULL
--    );


--    CREATE TABLE plu (
--  	average_price FLOAT NOT NULL,
--   	plu_4046 FLOAT NOT NULL,
--   	plu_4225 FLOAT NOT NULL,
--  	plu_4770 FLOAT NOT NULL,
--    	geography VARCHAR (40) NOT NULL
--  );
SELECT * FROM plu;

-- Joining Avocado and PLU
 SELECT plu.geography,
		avocado.type,
   		avocado.on_date,
    	avocado.total_volume
 FROM plu
 INNER JOIN avocado
 ON plu.average_price = avocado.average_price;

--  DROP TABLE plu;