#!/usr/bin/python
#Reducer.py

import sys
dept_salary = {}
#Partitoner

for line in sys.stdin:
    line = line.strip()
    dept, salary = line.split('\t')
    if dept in dept_salary:
        dept_salary[dept].append(int(salary))
    else:
        dept_salary[dept] = []
        dept_salary[dept].append(int(salary))

#Reducer
for dept in dept_salary.keys():
    min_salary = min(dept_salary[dept])
    print '%s\t%s'% (dept, min_salary)