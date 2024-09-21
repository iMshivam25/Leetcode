# Write your MySQL query statement below
select p.player_id, min(p.event_date) as first_login
from activity p
group by p.player_id