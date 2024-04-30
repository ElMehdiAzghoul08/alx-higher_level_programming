-- a script that lists all ctz_ contained in the database hbtn_0d_usa.
SELECT ctz_.id, ctz_.name, states.name
FROM ctz_
INNER JOIN states
ON ctz_.state_id = states.id;

