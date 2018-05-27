use test;


create table randUsers(
id int auto_increment primary key,
email varchar(50) not null,
registered date not null,
active boolean default false);

select round(rand());

select now();
select date(now());
select date(now()) - interval 500 day;
select date(now()) - interval round(10000 * rand()) day;
select date(now()) - interval floor(10000 * rand()) day;

delimiter //

create procedure randInsert(in maxiID int)
begin
	while maxiID <= 10 do
		insert into randUsers(id,email,registered,active)
        values(
        floor(round((55* rand()))),
        concat('user',round((55*rand())),'@gmail.com'),
		date(now()) - interval floor(5555 * rand()) day,
        true
        );
        set maxiID:=maxiID+1;
	end while;
    select * from randUsers;
end //
delimiter ;
call randInsert(1);
drop procedure randInsert;
select * from randUsers;

select rand();
select round(rand());
select floor(round(55 * rand())) as Num;

select concat('user',round((55*rand())),'@gmail.com');

select rand('Y','N');