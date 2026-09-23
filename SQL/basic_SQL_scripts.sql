-- exercise 2
select *
from movies m
where m.genre = 'Crime';

select *
from movies m 
order by m.box_office desc
limit 1;

select m.director, avg(m.rating) as average
from movies m 
group by m.director;

update movies 
set rating = rating + 0.5
where director = 'Christopher Nolan';

delete from movies 
where release_year < 1980;

-- exercise 3
