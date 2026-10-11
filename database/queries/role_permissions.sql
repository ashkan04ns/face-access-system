-- Display every role and its assigned permissions

SELECT
    roles.role_name,
    permissions.permission_name
FROM role_permissions
JOIN roles
    ON role_permissions.role_id = roles.role_id
JOIN permissions
    ON role_permissions.permission_id = permissions.permission_id
ORDER BY
    roles.role_id,
    permissions.permission_id;
