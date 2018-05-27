-- CONTROL FLOW STATEMENTS

select 'HHM';
use test;

select if(19>12, "VSVR","VSVR19");

create table parts(id int primary key auto_increment,
parts_id varchar(25) default null,
catalog_id varchar(25) not null);

insert into parts
(parts_id,catalog_id)
values
('XZ870','DA654'),
('ZY970','CB124'),
(null,'CD321');

select * from parts;

select id,parts_id,catalog_id,if(parts_id is null,catalog_id,parts_id)
as ifs
from parts;

select id,parts_id,catalog_id,if(parts_id is null,catalog_id,parts_id) as ifs
from parts
where if(parts_id is null,catalog_id,parts_id) = 'ZY970';

select ifnull(parts_id,catalog_id) as ifs
from parts;