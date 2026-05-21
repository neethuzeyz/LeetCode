-- Write your PostgreSQL query statement below
SELECT
    CASE 
        WHEN MOD(s.id, 2) = 1 AND s.id + 1 <= (SELECT MAX(id) FROM Seat) THEN s.id + 1
        WHEN MOD(s.id, 2) = 0 THEN s.id - 1
        ELSE s.id
    END AS id,
    s.student
FROM Seat s
order by id;


