# Write your MySQL query statement below
select p.firstname,p.lastname,a.city,a.state
from Address as a
right join Person as p
on p.personId=a.personId