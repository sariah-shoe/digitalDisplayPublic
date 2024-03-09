from django.shortcuts import render
from subprocess import check_output
from homepage.models import Employee

# Create your views here.

# Function for showing the homepage
def home(request):
    # Run the get employees script to find who is currently working
    script_output = check_output(["python", "backend/getShifts.py"])

    # Put the output through the format_employees functions
    employees = get_list(script_output)

    return render(request, "homepage/home.html", {"working_people": employees})

# A function to turn my output into employee objects
def get_working(output):
    # Begin by making a list of the IDs of all employees working
    formattedOutput = output.decode('utf-8')
    formattedOutput = formattedOutput.splitlines()
    formattedOutput.pop(-1)

    # Get all the employees saved
    employees = Employee.objects.all()
    for employee in employees:
        if employee.id in formattedOutput:
            employee.working = True
            employee.save()
            formattedOutput.remove(employee.id)
        else:
            employee.working = False
            employee.save()

    # If there are values left in formattedOutput then the employees need updated
    if len(formattedOutput) != 0:
        employees = Employee.objects.all()
        for employee in employees:
            employee.delete()

        get_employees()
        get_working(output)

def get_employees():
    employee_output = check_output(["python", "backend/getEmployees.py"])
    formatted_str = employee_output.decode('utf-8')

    # Split the string at the new lines, then split it at the spaces, making formatted_str like [[firstName, lastName, image], [firstName, lastName, image]...]
    formatted_str = formatted_str.splitlines()
    for i in range(0, len(formatted_str)):
        formatted_str[i] = formatted_str[i].split()

    # Take the info from the formatted_str and put it into Employee models, then save it
    for i in range(0, len(formatted_str)):
        new_instance = (Employee(firstName=formatted_str[i][0], lastName=formatted_str[i][1], image=formatted_str[i][2], id=formatted_str[i][3], working=False))
        new_instance.save()

def get_list(output):
    get_working(output)

    return_list = []
    employees = Employee.objects.all()

    for employee in employees:
        if employee.working:
            return_list.append(employee)

    return(return_list)
