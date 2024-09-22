CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE offsetVal INT;
    SET offsetVal = N - 1;
    
    RETURN (
        select ifnull(
        (select distinct salary as getNthHighestSalary
        from Employee
        order by salary desc
        limit 1 offset offsetVal),
        NULL)
    );
END