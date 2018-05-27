use test;

delimiter //
create procedure books_fruits (out titles text, out fruits text)
begin
	begin
		declare the_title varchar(50);
        declare finished bool default false;
        
        declare books_cursor cursor for select title from books;
        
        declare continue handler for not found set finished:=true;
        
        set titles:='';
        
        open books_cursor;
			books_loop: loop
				fetch books_cursor into the_title;
			
				if finished then
					leave books_loop;
				end if;
            
				set titles:=concat(titles ,',', the_title);
            
            end loop;
        close books_cursor;
    end;
    
    begin
		
		declare finished boolean default false;
        
        declare the_products varchar(40);
        
        declare fruits_cursor cursor for select product from fruits;
        
        declare continue handler for not found set finished:=true;
        
        set fruits = '';
        
        open fruits_cursor;
			fruits_loop :loop
				fetch fruits_cursor into the_products;
                
                if finished then
					leave fruits_loop;
                end if;
                 
                set fruits:=concat(fruits,',',the_products);	
                
            end loop;
        close fruits_cursor;
        
    end;
    
end //
delimiter ;

call books_fruits (@titles, @fruits);
drop procedure books_fruits;

select @titles, @fruits;

select * from books;

select title from books;