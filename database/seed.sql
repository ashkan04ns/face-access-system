-- ==========================================
-- Face Access System - Initial Data
-- ==========================================

-- Roles
INSERT INTO roles (role_name)
VALUES
    ('Admin'),
    ('Manager'),
    ('Employee');


-- Test users
INSERT INTO users (
    name,
    email,
    role_id
)
VALUES
    (
        'Test Admin',
        'admin@example.com',
        (SELECT role_id FROM roles WHERE role_name = 'Admin')
    ),
    (
        'Test Manager',
        'manager@example.com',
        (SELECT role_id FROM roles WHERE role_name = 'Manager')
    ),
    (
        'Test Employee',
        'employee@example.com',
        (SELECT role_id FROM roles WHERE role_name = 'Employee')
    );


-- Application permissions
INSERT INTO permissions (permission_name)
VALUES
    ('VIEW_DASHBOARD'),
    ('VIEW_REPORTS'),
    ('MANAGE_USERS'),
    ('VIEW_ACCESS_LOGS');


-- Admin permissions
INSERT INTO role_permissions (role_id, permission_id)
VALUES
    (
        (SELECT role_id FROM roles WHERE role_name = 'Admin'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'VIEW_DASHBOARD')
    ),
    (
        (SELECT role_id FROM roles WHERE role_name = 'Admin'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'VIEW_REPORTS')
    ),
    (
        (SELECT role_id FROM roles WHERE role_name = 'Admin'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'MANAGE_USERS')
    ),
    (
        (SELECT role_id FROM roles WHERE role_name = 'Admin'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'VIEW_ACCESS_LOGS')
    );


-- Manager permissions
INSERT INTO role_permissions (role_id, permission_id)
VALUES
    (
        (SELECT role_id FROM roles WHERE role_name = 'Manager'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'VIEW_DASHBOARD')
    ),
    (
        (SELECT role_id FROM roles WHERE role_name = 'Manager'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'VIEW_REPORTS')
    );


-- Employee permissions
INSERT INTO role_permissions (role_id, permission_id)
VALUES
    (
        (SELECT role_id FROM roles WHERE role_name = 'Employee'),
        (SELECT permission_id FROM permissions
         WHERE permission_name = 'VIEW_DASHBOARD')
    );

