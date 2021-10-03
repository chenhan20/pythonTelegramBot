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

CREATE TABLE system_parameter (
	system_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	value VARCHAR ( 50 ) NOT NULL,
	update_on TIMESTAMP NOT NULL
);


INSERT INTO public.accounts(
	username, email, created_on, last_login, telegram_user_id, telegram_push_enabled)
	VALUES ('林信毅', 'XXXXX@gmail.com', now(), now(), '1888409915', true);