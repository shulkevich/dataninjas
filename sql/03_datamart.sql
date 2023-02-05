-- 1. распределение событий по часам;

drop table if exists datamart.t_01_events;
drop view if exists datamart.t_01_events;

create view datamart.t_01_events
as
select
    "hour",
    event_type,
    count(*) as event_count
from
    dds.events;


-- 2. количество купленных товаров в разрезе часа;

drop table if exists datamart.t_02_goods;
drop view if exists datamart.t_02_goods;

create view datamart.t_02_goods
as
select "hour", count(event_type)
from dds.events
where event_type = 'confirmation'
group by 1;


-- 3. топ-10 посещённых страниц, с которых был переход в покупку — список ссылок с количеством покупок.

drop table if exists datamart.t_03_top_links;
drop view if exists datamart.t_03_top_links;

-- id формируется из row_number

create view datamart.t_03_top_links
as
select
from
    dds.events;