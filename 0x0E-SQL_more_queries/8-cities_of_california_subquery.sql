-- a script that lists all the ctz_ of California that can be found in the database hbtn_0d_usa.
SELECT id, name
FROM ctz_
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

