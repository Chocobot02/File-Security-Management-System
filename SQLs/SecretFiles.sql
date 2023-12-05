drop database if exists Secured_Files;
create database if not exists Secured_Files;
use Secured_Files;

-- creating table
create table securedfiles(
	inputfiles_id int primary key auto_increment,
	srcode varchar(10) default null,
    student_name varchar(255) not null,
	application_name varchar(255) not null,
	username varchar(255) not null,
    app_password varchar(255) not null,

    profile_status enum('student', 'not-student') default 'student'
    );


-- make the update of status automtic
DELIMITER //
CREATE TRIGGER statuschecker
BEFORE INSERT ON securedfiles
FOR EACH ROW
BEGIN
    IF NEW.srcode = '' THEN
        SET NEW.profile_status = 'not-student';
    END IF;
END;
//
DELIMITER ;

