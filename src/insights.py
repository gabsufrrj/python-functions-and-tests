import src.jobs


def get_unique_job_types(path):
    jobs_list = src.jobs.read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    jobs_data = list(jobs_types)
    return jobs_data


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for entry in jobs:
        if entry["job_type"] == job_type:
            filtered_jobs.append(entry)
    return filtered_jobs


def get_unique_industries(path):
    jobs_list = src.jobs.read(path)
    industries = set()
    for industry in jobs_list:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    industries_list = list(industries)
    return industries_list


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for entry in jobs:
        if entry["industry"] == industry:
            filtered_industries.append(entry)
    return filtered_industries


def get_max_salary(path):
    jobs_list = src.jobs.read(path)
    all_salaries = []
    for salary in jobs_list:
        if salary["max_salary"].isdigit():
            all_salaries.append(int(salary["max_salary"]))
    the_max_salary = int(max(all_salaries))
    return the_max_salary


def get_min_salary(path):
    jobs_list = src.jobs.read(path)
    all_salaries = []
    for salary in jobs_list:
        if salary["min_salary"].isdigit():
            all_salaries.append(int(salary["min_salary"]))
    the_min_salary = int(min(all_salaries))
    return the_min_salary


def salary_range_validation(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError
    if not isinstance(salary, int):
        raise ValueError
    if job["max_salary"] < job["min_salary"]:
        raise ValueError


def matches_salary_range(job, salary):
    salary_range_validation(job, salary)

    if job["max_salary"] >= salary >= job["min_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    valid_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                valid_salaries.append(job)
        except ValueError:
            print("Argumentos inválidos")
    return valid_salaries
