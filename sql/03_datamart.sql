-- 1. распределение событий по часам;

create table datamart.01_events (
    id serial primary key,
    hour integer,
    event_type varchar,
    event_count integer
);

-- 2. количество купленных товаров в разрезе часа;
create table datamart.02_goods (
    id serial primary key,
    hour integer,
    event_count integer
);


-- 3. топ-10 посещённых страниц, с которых был переход в покупку — список ссылок с количеством покупок.

-- id формируется из row_number

create table datamart.03_links (
    id integer primary key,
    page_url varchar
);