# Topic: Aggregation
# 1. Weather Observation Station 14

Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than ``137.2345``. Truncate your answer to 4 decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution:**

```sql
SELECT CAST(MAX(LAT_N) AS DECIMAL(10, 4))
FROM STATION
WHERE LAT_N < 137.2345;
```

# 2. Weather Observation Station 15

Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than ``137.2345``. Truncate your answer to 4 decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution:**

```sql
SELECT CAST(LONG_W AS DECIMAL(10, 4))
FROM STATION
WHERE LAT_N IN (
    SELECT MAX(LAT_N)
    FROM STATION
    WHERE LAT_N < 137.2345
);
```

# 3. Weather Observation Station 16

Query the smallest Northern Latitude (LAT_N) from STATION that is greater than ``38.7780``. Round your answer to 4 decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution:**

```sql
SELECT CAST(MIN(LAT_N) AS DECIMAL(10,4))
FROM STATION
WHERE LAT_N > 38.7780;
```

# 4. Weather Observation Station 17

Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION that is greater than ``38.7780``. Round your answer to 4 decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution:**

```sql
SELECT CAST(LONG_W AS DECIMAL(10, 4))
FROM STATION
WHERE LAT_N IN (
    SELECT MIN(LAT_N)
    FROM STATION
    WHERE LAT_N > 38.7780
);
```

# 5. Weather Observation Station 18

Consider ``P1(a,b)`` and ``P2(c,d)`` to be two points on a 2D plane.

* `a` happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
* `b` happens to equal the minimum value in Western Longitude (LONG_W in STATION).
* `c` happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
* `d` happens to equal the maximum value in Western Longitude (LONG_W in STATION).

Query the `Manhattan Distance` between points `P1` and `P2` and round it to a scale of `4` decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution:**

```sql
SELECT CAST(ABS(subquery.a - subquery.c) + ABS(subquery.b - subquery.d) AS DECIMAL(10,4)) 
FROM (
    SELECT 
        MIN(LAT_N) AS a, 
        MIN(LONG_W) AS b, 
        MAX(LAT_N) AS c, 
        MAX(LONG_W) AS d 
    FROM STATION) AS subquery;
```

# 6. Weather Observation Station 19

Consider ``P1(a,b)`` and ``P2(c,d)`` to be two points on a 2D plane.

Consider ``P1(a,b)`` and ``P2(c,d)`` to be two points on a 2D plane where `(a,b)` are the respective minimum and   `(c,d)` maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the `Euclidian Distance` between points `P1` and `P2` and round it to a scale of `4` decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution:**

```sql
SELECT CAST(
    SQRT(SQUARE(subquery.b - subquery.a) + SQUARE(subquery.d - subquery.c))
AS DECIMAL(10,4)) 
FROM (
    SELECT 
        MIN(LAT_N) AS a, 
        MIN(LONG_W) AS c, 
        MAX(LAT_N) AS b, 
        MAX(LONG_W) AS d 
    FROM STATION) AS subquery;
```

# 7. Weather Observation Station 20

A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

**Input Format**

The STATION table is described as follows:

![alt text](image-1.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Solution: MS SQL Server**

``` sql
WITH MEDIAN AS ( 
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY LAT_N) OVER () AS Median 
    FROM STATION
) 
    
SELECT TOP 1 CAST(Median AS DECIMAL(10,4)) 
FROM MEDIAN;
```