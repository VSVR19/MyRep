-- CASTING

select cast('6-10-2017' as character);
select cast('6-10-2017' as date);

select * from books;

select count(*) from books;

select concat("Total Books across 3 locations:", count(*))
from books;

select concat("Total Books across 3 locations: ",cast(count(*)as char))
as Summary
from books;