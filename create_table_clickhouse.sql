-- ClickHouse
CREATE TABLE employees
(
    id Int64 PRIMARY KEY,
    name String,
    age Int32,
    salary Int32,
);

INSERT INTO employees (id, name, age, salary)
VALUES
(1, 'Alice', 30, 70000),
(2, 'Bob', 25, 50000),
(3, 'Charlie', 35, 100000),
(4, 'David', 40, 120000),
(5, 'Eve', 28, 60000),
(6, 'Frank', 50, 150000),
(7, 'Grace', 33, 80000),
(8, 'Hank', 29, 55000),
(9, 'Ivy', 42, 110000),
(10, 'Jack', 31, 90000);
