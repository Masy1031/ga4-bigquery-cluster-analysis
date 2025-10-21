create or replace table `[データセットID].[テーブル名].[新たに作成したいテーブル名]` as 
with access_tb as (
  select
    event_date,
    event_name,
    user_pseudo_id,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS ga_session_id,
  from
    `[プロジェクトID].ga4_obfuscated_sample_ecommerce.events_202101*` 
)
select
  event_date,
  count(distinct user_pseudo_id) as uu_num,
  count(distinct concat(user_pseudo_id, ga_session_id)) as session_num,
  countif(event_name = 'page_view') as pv_num
from
  access_tb
group by event_date
order by event_date;
