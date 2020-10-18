select company.company_code,
    company.founder,
    count(distinct lead_manager.lead_manager_code),
    count(distinct senior_manager.senior_manager_code),
    count(distinct manager.manager_code),
    count(distinct employee.employee_code)
From Company
    INNER JOIN lead_manager ON company.company_code = lead_manager.company_code
    INNER JOIN senior_manager ON lead_manager.lead_manager_code = senior_manager.lead_manager_code
    INNER JOIN manager ON senior_manager.senior_manager_code = manager.senior_manager_code
    INNER JOIN employee ON manager.manager_code = employee.manager_code
group by company.company_code,
    company.founder
order by company.company_code;