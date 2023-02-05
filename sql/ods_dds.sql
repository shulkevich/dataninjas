
truncate dds.events;

insert into dds.events (
    event_timestamp, hour, event_type, prior_event_type, referer_url)
select
    event_timestamp,
    extract(hour from event_timestamp) as hour,
    event_type,
    lag(event_type) over (partition by user_custom_id order by event_timestamp) as prior_event_type,
    referer_url
from
    ods.events;