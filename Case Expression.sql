-- CASE EXPRESSION!!!!!!!!
use test;

create table products_case(id int primary key auto_increment, 
product varchar(40) not null, category enum('bakery', 'fruit', 'vegetable'));

insert into products_case (product, category) values ('cat treats', null);

create table fruits(id int primary key, product varchar(40) not null);
create table vegetables(id int primary key, product varchar(40) not null);
create table bakery(id int primary key, product varchar(40) not null);


select * from products_case;

insert into products_case (id, product,category) values
(2,'Potatoes','Vegetable'),(3,'Carrots','Vegetable'),
(4,'Bananas','Fruit'),(5,'Orange','Fruit'),(6,'WholeWheatBread','Bakery'),
(7,'White Bread','Bakery'),(8,'Maple Sprial','Bakery'),(9,'Dog Food',null);


delimiter //

create procedure multi_table(out unassigned longtext)
begin
	declare the_id int;
    declare the_product varchar(50);
    declare the_category enum('vegetable','fruit','bakery');
    
    declare finished boolean default false;
    
    declare cur cursor for select id, product, category 
	from products_case
	order by id;
    
    declare continue handler for not found set finished:=true;
    
    open cur;
    set unassigned:= '';
    
		the_loop: loop
			fetch cur into the_id, the_product, the_category;
            
            if finished = true then
				leave the_loop;
			end if;
            
            case the_category
				when 'fruit' then
					insert into fruits(id, product) values (the_id, the_product);
				when 'vegetable' then
					insert into vegetables(id, product) values (the_id, the_product);
				when 'bakery' then
					insert into bakery(id, product) values (the_id, the_product);
				else
					set unassigned:= concat(unassigned, the_product, ' ,');
			end case;
            
        end loop;
    close cur;
end //

delimiter ;

call multi_table(@unassigned);

drop procedure multi_table;

select id, product, category 
from products_case
order by id;

select * from products_case as products_case;

select * from fruits as fruits;
select * from bakery as bakery;
select * from vegetables;
select @unassigned;

drop table fruits; 
drop table bakery;
drop table vegetables;

create table vegetable (id int, product varchar(50));