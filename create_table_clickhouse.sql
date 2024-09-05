-- ClickHouse
CREATE TABLE employees
(
    id Int64 PRIMARY KEY,
    name String,
    age Int32,
    salary Int32,
);

INSERT INTO employees (name, age, salary)
VALUES
('Alice', 30, 70000),
('Bob', 25, 50000),
('Charlie', 35, 100000),
('David', 40, 120000),
('Eve', 28, 60000),
('Frank', 50, 150000),
('Grace', 33, 80000),
('Hank', 29, 55000),
('Ivy', 42, 110000),
('Jack', 31, 90000);
