# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id%2=1 AND NOT description="boring"
ORDER BY rating desc