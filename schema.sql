CREATE DATABASE IF NOT EXISTS juventus_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'juventus_user'@'%' IDENTIFIED BY 'strongpassword123';
GRANT ALL PRIVILEGES ON juventus_db.* TO 'juventus_user'@'%';
FLUSH PRIVILEGES;

USE juventus_db;
