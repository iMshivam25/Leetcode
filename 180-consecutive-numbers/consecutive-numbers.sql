with LogsNeighbors as(
    select *,
    lag(num) over(order by id) as prev_num,
    lead(num) over(order by id) as next_num
    from Logs
)
select distinct num  
as ConsecutiveNums
from LogsNeighbors where
num = prev_num and
num = next_num;