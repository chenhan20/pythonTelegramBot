CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP 
);


CREATE TABLE follow_stock(
	follow_stock_id serial PRIMARY KEY,
	user_id bigint ,
	stock_code VARCHAR ( 10 )
);