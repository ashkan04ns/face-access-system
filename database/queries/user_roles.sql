-- Display users with their assigned role

SELECT
    users.name,
    users.email,
    roles.role_name
FROM users
JOIN roles
    ON users.role_id = roles.role_id;