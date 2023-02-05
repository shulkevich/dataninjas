-- 1. распределение событий по часам;

drop table if exists datamart.t_01_events;

create table datamart.t_01_events (
    id serial primary key,
    hour integer,
    event_type varchar,
    event_count integer
);

-- 2. количество купленных товаров в разрезе часа;

drop table if exists datamart.t_02_goods;

create table datamart.t_02_goods (
    id serial primary key,
    hour integer,
    event_count integer
);


-- 3. топ-10 посещённых страниц, с которых был переход в покупку — список ссылок с количеством покупок.

drop table if exists datamart.t_03_top_links;

-- id формируется из row_number

create table datamart.t_03_top_links (
    id integer primary key,
    page_url varchar
);