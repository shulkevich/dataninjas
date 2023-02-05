
drop table if exists staging.events;

create table staging.events (
	id serial primary key,
    event_id varchar,
--	2020-07-05 14:32:45.407110
	event_timestamp timestamp, 
--	pageview	
	event_type varchar,
--  http://merch.practicum.ru/home	
	page_url varchar,
--  /home	
	page_url_path varchar,
--  www.instagram.com	
	referer_url varchar,
--  http
	referer_url_scheme varchar,
-- 	80
	referer_url_port integer,
--  internal
	referer_medium varchar,
--  organic
	utm_medium varchar,
--  instagram
	utm_source varchar,
--  ad_2
	utm_content varchar,
--  campaign_2
	utm_campaign varchar,
--  b6b1a8ad-88ca-4fc7-b269-6c9efbbdad55
	click_id varchar,
--  -25.54073
	geo_latitude double precision,
--  152.70493
	geo_longitude double precision,
--  AU
	geo_country varchar,
--  Australia/Brisbsane
	geo_timezone varchar,
--  Maryborough
	geo_region_name varchar,
--  209.139.207.244
	ip_address varchar,
--  Firefox
	browser_name varchar,
--  Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_5; rv:1.9.6.20) Gecko/2012-06-06 09:24:19 Firefox/3.6.20
	browser_user_agent varchar,
--  tn_ZA
	browser_language varchar,
--  2.0.1
	os varchar,
--  Android
	os_name varchar,
--  Australia/Brisbane
	os_timezone varchar,
--  Mobile
	device_type varchar,
--  true
	device_is_mobile varchar,
--  vsnyder@hotmail.com
	user_custom_id varchar,
--  3d648067-9088-4d7e-ad32-45d009e8246a
	user_domain_id varchar
);

