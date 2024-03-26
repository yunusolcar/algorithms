-- 1757. Recyclable and Low Fat Products
-- https://leetcode.com/problems/recyclable-and-low-fat-products/description/

Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+

-- Solution
SELECT product_id
FROM Products
WHERE low_fats='Y' recyclable AND ='Y'

-- Output
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+