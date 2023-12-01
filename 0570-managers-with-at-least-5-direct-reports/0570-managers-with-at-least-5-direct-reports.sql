# Write your MySQL query statement below

### method1

# select
#     e2.name
# from
#     Employee e1 join Employee e2 on e1.managerId = e2.id
# group by
#     e1.managerId
# having
#     count(e1.managerId) >= 5;


### method2

# select
#     name
# from
#     Employee
# where
#     id in (
#         select
#             managerId
#         from
#             Employee
#         group by
#             managerId
#         having
#             count(managerId) >= 5);


### method3

select
    name
from
    Employee t1
join (
    select
        managerId
    from
        Employee
    group by
        managerId
    having
        count(managerId) >= 5
    ) t2 on t1.Id = t2.managerId;