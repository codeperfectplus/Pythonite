SELECT produc_name ,SUM(price)
FROM home_equipments
WHERE price >10000
GROUP BY produc_name;