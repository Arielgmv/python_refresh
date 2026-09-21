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
