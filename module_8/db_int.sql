--activate pysports
USE pysports;

--show tables
SHOW tables;

--create user
 CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MyAssignm3nt';

--grant access to user
 GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

--drop user--
 DROP USER IF EXISTS 'pysports_user'@'localhost';

--create team table
 CREATE TABLE team (
     team_id     INT             NOT NULL        AUTO_INCREMENT,
     team_name   VARCHAR(75)     NOT NULL,
     mascot      VARCHAR(75)     NOT NULL,
     PRIMARY KEY(team_id)
 );

--create player table and set foreign key
 CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

--insert team record--
INSERT INTO team(team_name, mascot)
    VALUES('Team Gryffindors', 'Lion');

--Drop table--
DROP TABLE IF EXISTS member;

--select statements--
 SELECT team_id FROM team WHERE team_name = 'Team Gryffindors';
