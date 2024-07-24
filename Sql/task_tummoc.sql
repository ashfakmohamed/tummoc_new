create database tummoc;
use tummoc;
CREATE TABLE routes (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

alter table routes add column number varchar(20);


select * from routes;

insert into routes values (1,'200-D','SBV-BHJ'),(2,'300-A','ASD-WER');

CREATE TABLE route_points (
    id INT PRIMARY KEY,
    route_id INT,
    `order` INT,
    distance INT,
    FOREIGN KEY (route_id) REFERENCES routes(id)
);

select * from route_points;
insert into route_points values (1,1,1,0),(2,1,2,100),(3,2,1,0),(4,2,2,50),(5,2,3,100);

SELECT r.id AS route_id, r.name, SUM(rp.distance) AS total_distance FROM routes r JOIN route_points rp ON r.id = rp.route_id GROUP BY r.id, r.name ORDER BY total_distance DESC, r.id;



CREATE TABLE routes1 (id INT PRIMARY KEY, name VARCHAR(255), number varchar(20));

select * from routes1;

insert into routes1 values (1,'200-D','SBV-BHJ'),(2,'300-A','ASD-WER');

CREATE TABLE route_points1 (
    id INT PRIMARY KEY,
    route_id INT,
    `order` INT,
    stop_id INT,
    FOREIGN KEY (route_id) REFERENCES routes1(id)
);

select * from route_points1;
insert into route_points1 values (1,1,1,1),(2,1,2,2),(3,2,1,1),(4,2,2,2),(5,2,3,3);

SELECT route_id, 
       MIN(CASE WHEN `order` = 1 THEN stop_id END) AS source_stop_id, 
       MAX(stop_id) AS dest_stop_id
FROM route_points1
GROUP BY route_id;



CREATE TABLE station (id INT PRIMARY KEY, name VARCHAR(255));

select * from station;

insert into station values (1,'Sta1'),(2,'Sta2');

CREATE TABLE times (
    id INT PRIMARY KEY,
    station_id INT,
    slot INT,
    `time` time,
    FOREIGN KEY (station_id) REFERENCES station(id)
);

select * from times;

insert into times values (1,1,1,'6:30'),(2,1,2,'6:45'),(3,1,1,'6:40'),(4,1,2,'6:50'),(5,2,1,'8:10'),(6,2,2,'8:20'),(7,2,1,'8:15'),(8,2,2,'8:30');

SELECT 
    t.station_id,
    s.name AS station_name,
    t.slot,
    t.time
FROM 
    times t
JOIN 
    station s ON t.station_id = s.id
WHERE 
    t.station_id = 1 AND t.slot = 1
ORDER BY 
    t.time;