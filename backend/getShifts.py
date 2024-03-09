import requests
import datetime

def get_shifts(myToken, myID):
    # Headers for the API
    headers = {
        "Content-Type": "application/json",
        "Authorization": myToken
    }

    # Format the datetime for my date parameter
    current_time = datetime.datetime.now().time()

    current_time = current_time.hour
    future_time = current_time + 1

    # Ensure leading zeros for single-digit hours
    current_time = str(current_time).zfill(2)
    future_time = str(future_time).zfill(2)

    current_date = datetime.datetime.now().date()
    full_time = f"{current_date}T{current_time}:00:00-0700/{current_date}T{future_time}:00-0700"

    # Parameters for the endpoint I'm getting. Today's current date, a userID, and a nonce
    parameters = {
        "dates" : full_time,
        "user-fields" : f"{myID}",
        "nonce" : 1701987506976,
    }

    # Make the request to get all the shifts on the calendar for the day
    data = requests.get(f"https://api.getsling.com/v1/94756/calendar/94756/users/{myID}", headers=headers, params=parameters)

    # Status code for debug
    # print(data.status_code)

    data = data.json()

    return(data)

def process_shifts(rawData):
    # The raw data has everything on the calendar, including unavailabilty, and I don't want unaviability
    # So I go through and I get a list of shift events
    shiftData = []
    for data in rawData:
        if (data.get("type") == "shift"):
            currentLocation = data.get("location")
            if (currentLocation.get('id') == 10811709):
                currentUser = data.get("user")
                if currentUser is not None:
                    shiftData.append(currentUser.get("id"))

    if (len(shiftData)) == 0:
        shiftData.append("0")

    return_value = ""
    for shift in shiftData:
        return_value += f'{shift}\n'

    return(return_value)

def main():
    # The info I need for my API session
    myToken = "N/A"
    myID = 0

    rawData = get_shifts(myToken, myID)
    print(process_shifts(rawData))

# Run the main function
if __name__ == "__main__":
    main()




