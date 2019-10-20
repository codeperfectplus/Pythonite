SELECT produc_name ,sum(price)
FROM home_equipments
GROUP BY produc_name
HAVING sum(price) >10000;