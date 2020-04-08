DROP DATABASE IF EXISTS epytodo;
CREATE DATABASE IF NOT EXISTS epytodo;
USE epytodo;

CREATE TABLE IF NOT EXISTS user (
       user_id INT NOT NULL AUTO_INCREMENT,
       username nvarchar(255) NOT NULL,
       password nvarchar(255) NOT NULL,
       email nvarchar(255) DEFAULT NULL,
       PRIMARY KEY(user_id, username)
);

CREATE TABLE IF NOT EXISTS task (
       task_id INT NOT NULL AUTO_INCREMENT,
       title nvarchar(255) NOT NULL,
       begin datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
       end datetime DEFAULT NULL,
       status enum('not started', 'in progress', 'done') NOT NULL DEFAULT 'not started',
       PRIMARY KEY(task_id)
);

CREATE TABLE IF NOT EXISTS user_has_task (
       fk_user_id INT NOT NULL,
       fk_task_id INT NOT NULL,
       PRIMARY KEY(fk_user_id, fk_task_id)
);
