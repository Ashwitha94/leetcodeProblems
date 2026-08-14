# Write your MySQL query statement below
select
T1.name as employee
from employee as T1
join employee as T2
on T1.managerid=T2.id
where T1.salary>T2.salary