-- Date Excercises

use test;

show tables;

select count(*) from books;

select concat("Total: ", cast(count(*) as char)," records")
from books
as Count_C;

select concat("Total: ", cast(count(*) as char), if(count(*) > 1, "records","record"))
from books
where id = 1;
as Count_C;

select * from dates;

-- set @date_t = date_format('2018-03-31','%D of %M, %Y (%W)');
-- select date_format(applied_on,'%D of %M, %Y (%W)') from dates;
select @date_t := date_format(applied_on,'%D of %M, %Y (%W)') from dates;

select @date_t;

-- select str_to_date(@date_t,'%dst of %M,%Y (%W)');
select str_to_date(@date_t,'%D of %M,%Y (%W)');

set @born = 'April 28, 1906';
set @died = 'January 14, 1978';

select date_format(str_to_date(@born, '%M %d, %Y'),'%W')
as Birth_Day; 

select date_format(str_to_date(@died, '%M %d, %Y'), '%W')
as Death_Day;

-- select datediff(
-- str_to_date(@died, '%M %d, %Y'),
-- str_to_date(@born, '%M %d, %Y')
-- ) as Lived_Days;

select from_days(
datediff(
str_to_date(@died, '%M %d, %Y'),
str_to_date(@born, '%M %d, %Y')
)) as Lived_Days;

select datediff(
str_to_date(@died, '%M %d, %Y'),
str_to_date(@born, '%M %d, %Y')
)/365 as Lived_Years;

select datediff(
str_to_date(@died, '%M %d, %Y'),
str_to_date(@born, '%M %d, %Y')
)/30 as Lived_Months;

-- 99 Years, 6 Months, 3 Days old
-- Dead date&& Dead_Day
select @born;

set @born1 = 
date_add(
str_to_date(@born, '%M %d, %Y')
, interval 99 year);
-- as Adding_Year;

select @born1;


set @born2 =
date_add(
str_to_date(@born1, '%Y-%m-%d')
, interval 6 month);
-- as Adding_Months;

select @born2;

set @born3 =
date_add(
str_to_date(@born2, '%Y-%m-%d')
, interval 3 day);

select @born3;

select date_format(
(str_to_date(@born3, '%Y-%m-%d')),
'%W'
) as Img_Day;	

select date_format(
str_to_date(@born, '%M %d, %Y')
+ interval 99 year + interval 6 month + interval 3 day
, '(%W)') as Days;