

truncate ods.events;

insert into ods.events (event_timestamp, user_custom_id, event_type, page_url, referer_url)
select
    event_timestamp,
    user_custom_id,
	coalesce(
	    substring(e.page_url_path from '\/(.*)_'),
	    substring(e.page_url_path from '\/(.*)')
	) as event_type,
    page_url,
    referer_url
from
    staging.events e;
