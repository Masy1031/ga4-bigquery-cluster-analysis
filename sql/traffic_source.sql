create or replace table `[データセットID].[テーブル名].[新たに作成したいテーブル名]` as
select
  traffic_source.medium,
  count(*) as cnt,
  count(*) / sum(count(*)) over() as share
from
  `[プロジェクトID].ga4_obfuscated_sample_ecommerce.events_202101*`
group by traffic_source.medium
order by cnt;
