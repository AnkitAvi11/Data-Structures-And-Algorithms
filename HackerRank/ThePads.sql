select CONCAT(NAME, CONCAT('(',left(occupation,1),')')) as Name from occupations order by name;

SELECT concat("There are a total of ", COUNT(OCCUPATION),' ',lower(occupation),'s.') from occupations group by occupation order by count(occupation), occupation