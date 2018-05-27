-- WHILE LOOPS

use test;

select * from books;

delimiter //

create procedure book_check(in maxiName varchar(50), out result varchar(4))
begin
	start transaction;
		set @ID = null;
		select id into @ID 
        from books
        where Title = maxiName;
		
        if(@ID = null) then
			set result = 'NA';
		else
			set result = 'A';
		end if;
		select @ID as ID, result as Availability;
	commit;
end //
delimiter ;

set @result = 'NA';
call book_check('Everest',@result);

drop procedure book_check;


select * from books;
set @maxiName = 'Everest';
set @ID = null;
		select id into @ID 
        from books
        where Title = @maxiName;
select @ID;