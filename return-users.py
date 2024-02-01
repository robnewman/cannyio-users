import requests
from dotenv import dotenv_values

secrets = dotenv_values(".env")

def loop_canny_users():
    increment = 100 # Canny API caps increment at 100
    for i in range(0, 1000, increment):
        print(f"Iterating through users {i}-{i+100}...")
        users = get_canny_users(secrets["API_KEY"], increment, i)
        if users:
            print("Users with no Company affiliation:")
            for user in users:
                if len(user['companies']) == 0:
                    print(f"\t- User ID: {user['userID']}, Name: {user['name']}, Email: {user['email']}")
        else:
            print(f"\t- No users for users {i}-{i+100}.")

def get_canny_users(api_key, limit, skip):
    payload = {
        "apiKey": {api_key},
        "limit": {limit},
        "skip": {skip}
    }
    url = "https://canny.io/api/v1/users/list"
    try:
        response = requests.post(url, params=payload)
        response.raise_for_status()  # Check for errors
        users = response.json()
        return users
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    loop_canny_users()
