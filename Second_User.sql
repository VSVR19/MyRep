use test;

create user FedEX@localhost identified by '19';

DELIMITER $$

create definer = VSVR19@localhost procedure GrandSlams()
grant execute on procedure test.GrandSlams to FedEx@localhost;


sql security definer

begin

select * from books;

end $$

delimiter ;

call GrandSlams();

select * from mysql.proc;

call My_Teams();
use mysql;