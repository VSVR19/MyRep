use test;

delimiter //
create procedure BalanceCheck (in account_id int, in amount numeric(7,2), out success bool )
begin
	declare current_balance numeric(7,2) default 0.0;
    
    start transaction;
    
		select balance into current_balance from account where id = account_id for update;
		if(current_balance >= amount) then
			update account
			set balance = balance - amount
			where id = account_id;
			
			set success = true;
			select success as Result;
		else
			set success = false;
			select success as Result;
		end if;
		
    commit;
    
end//
delimiter ;
set @money = 100;
call BalanceCheck(1,10000,@success);

drop procedure BalanceCheck;

desc account;

select balance into @amount from account where id = 1;
select @amount;

select * from account;