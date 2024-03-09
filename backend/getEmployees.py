import requests
import datetime

# This script takes shift data from sling to get who is working on the current date and when they are working

# An object that holds the relevant data for an employee
class employee:
    def __init__(self, firstName, lastName, profilePic, id):
        self.firstName = firstName
        self.lastName = lastName
        self.profilePic = profilePic
        self.id = id

    def __str__(self):
        return(f"{self.firstName} {self.lastName} {self.profilePic} {self.id}")
    

# A function to get the raw data from the Sling API
def get_data(myToken, myID):
    # Headers for the API
    headers = {
        "Content-Type": "application/json",
        "Authorization": myToken
    }

    # Make a request to get all users
    users = requests.get("https://api.getsling.com/v1/users", headers=headers)

    # Status code for debug
    # print(users.status_code)
    
    users = users.json()

    # Create a dictionary for employees
    employees = []

    # Add the user to the dictionary with their ID as the key and their name as the value
    for user in users:
        employees.append(employee(user.get("name"), user.get("lastname"), user.get("avatar"), user.get("id")))


    employees.append(employee("No", "Employees", "https://live.staticflickr.com/65535/48049105116_c6178c5b91_b.jpg","0"))

    # Return a tuple with the rawdata and my list of employees
    return(employees)

# Main function
def main():
    # The info I need for my API session
    myToken = "N/A"
    myID = 0

    # Get the raw data and then parse it
    rawData = get_data(myToken, myID)

    # Print my parsed data
    for data in rawData:
        print(data)

# Run the main function
if __name__ == "__main__":
    main()