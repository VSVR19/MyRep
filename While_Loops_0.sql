-- WHILE LOOPS

use test;

select * from books;

delimiter //

create procedure book_check(in maxiID int, in maxiName varchar(50), out result bool)
begin
	start transaction;
		set @ID = null;
		select id into @ID 
        from books
        where id = maxiID;
		
        if(@ID = null) then
			set result = false;
		else
			set result = true;
		end if;
		select result as Availability;
	commit;
end //
delimiter ;

set @result = true;
call book_check(1, 'Challenging Destiny',@result);

drop procedure book_check;