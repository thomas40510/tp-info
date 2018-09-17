/*select name, LifeExpectancy from country
where LifeExpectancy>60
order by LifeExpectancy ASC;

select name,GNP from country
order by GNP desc;

select name,District from city
where CountryCode = "NLD"
order by District;

select distinct GovernmentForm from country;

select count(*) from country
where IndepYear is  not null: 

select sum(Population) from country; 

select Continent, sum(Population) from country group by Continent;

select Name, Population from country where Population = (select max(Population) from country);

select avg(Population) from city where CountryCode = "FRA";

select Name from country where LifeExpectancy > 70 union select Name from country where GNP > 1000;


select Name from country where LifeExpectancy > 70 intersect select Name from country where GNP > 1000;

select Name, GovernmentForm from country 
except select Name,GovernmentForm from country where GovernmentForm = "Republic";

insert into country(Code, Name, Continent, Population, LifeExpectancy, GovernmentForm, HeadOfState, Capital)
values("P3", "PCSI3", "Lycée Clemenceau", 47, 2, "Dictatorship", "BBX", "L204");

delete from city where CountryCode = "AFG";

update country set LifeExpectancy = 78.5 where Name = "Belgium";*/



