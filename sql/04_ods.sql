

drop table if exists ods.events;

create table ods.events (
    id serial primary key,
    --	2020-07-05 14:32:45.407110
    event_timestamp timestamp,
    -- суррогатный тип события  (pageview, purchase)
    event_type varchar,
    -- ссылка на струницу, откуда пользователь пришел
    page_url varchar,
    user_custom_id varchar,
    referer_url varchar
);
