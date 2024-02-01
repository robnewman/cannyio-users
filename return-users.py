import requests
from dotenv import dotenv_values
from slack_sdk import WebClient

secrets = dotenv_values(".env")

def loop_canny_users():
    increment = 100 # Canny API caps increment at 100
    missing_users = [] 
    message ="Seqera Canny.io users with no Company affiliation:\n"
    # Naively assume a max of 1000 users
    for i in range(0, 1000, increment): 
        users = get_canny_users(secrets["API_KEY"], increment, i)
        if users:
            for user in users:
                if len(user['companies']) == 0:
                    missing_users.append(f"- Name: {user['name']}, Email: {user['email']}")

    joined_users = '\n'.join(missing_users)

    if len(missing_users) > 0:
        client = WebClient(token=secrets["SLACKBOT_OAUTH_TOKEN"])
        client.chat_postMessage(
            channel = "proj-canny-launch",
            text = message + joined_users,
            username = "Bot User"
        )
    else:
        print("No Seqera Canny users missing a Company affiliation")

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
