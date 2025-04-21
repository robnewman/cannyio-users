import requests
from dotenv import dotenv_values
from slack_sdk import WebClient

secrets = dotenv_values(".env")

def missing_company_users():
    missing_users = []
    message ="Canny.io users with no Company affiliation:\n"
    users = get_canny_users(secrets["API_KEY"])
    if users:
        for user in users:
            if len(user['companies']) == 0:
                missing_users.append(f"- Name: {user['name']}, Email: {user['email']}")
        # Clean duplicate entries
        missing_users = list(set(missing_users))
        joined_users = '\n'.join(missing_users)

    if len(missing_users) > 0:
        client = WebClient(token=secrets["SLACKBOT_OAUTH_TOKEN"])
        client.chat_postMessage(
            channel = secrets["SLACK_CHANNEL"],
            text = message + joined_users,
            username = "Bot User"
        )
    else:
        print("No Canny users missing a Company affiliation")

def get_canny_users(api_key):
    """
    Fetch all users from Canny using cursor-based pagination

    Args:
        api_key (str): Canny API key

    Returns:
        list: A list of all user dictionaries
    """
    url = "https://canny.io/api/v2/users/list"
    all_users = []
    cursor = None

    while True:
        payload = {
            "apiKey" : api_key
        }
        if cursor:
            payload['cursor'] = cursor

        response = requests.post(url, params=payload)
        response.raise_for_status()  # Check for errors
        data = response.json()
        users = data.get('users', [])
        all_users.extend(users)
        cursor = data.get('cursor')
        if not cursor:
            break

    return all_users

if __name__ == "__main__":
    missing_company_users()
