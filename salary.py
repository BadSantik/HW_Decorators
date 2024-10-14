import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            log_entry = (
                f"Date and Time: {datetime.datetime.now()}\n"
                f"Function Name: {old_function.__name__}\n"
                f"Arguments: args={args}, kwargs={kwargs}\n"
                f"Return Value: {result}\n"
                "-------------------------\n"
            )
            with open(path, 'a') as log_file:
                log_file.write(log_entry)
            return result
        return new_function
    return __logger


@logger('salary.log')
def calculate_salaries(employees):
    print("Calculating salaries...")
    for employee in employees:
        salary = employee['salary']
        print(f"Name: {employee['name']}, Position: {
              employee['position']}, Calculated Salary: {salary}")


employees = [
    {'name': 'Alice', 'position': 'Developer', 'salary': 5000},
    {'name': 'Bob', 'position': 'Designer', 'salary': 4500},
    {'name': 'Charlie', 'position': 'Manager', 'salary': 6000}
]

calculate_salaries(employees)
