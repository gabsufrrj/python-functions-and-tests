import src.jobs


def get_unique_job_types(path):
    jobs_list = src.jobs.read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    jobs_data = list(jobs_types)
    return jobs_data


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs_list = src.jobs.read(path)
    industries = set()
    for industry in jobs_list:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    industries_list = list(industries)
    return industries_list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
