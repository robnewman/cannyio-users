# cannyio-users

Utility to query the Canny Users API endpoint and return all users
without a Company affiliation. Then send a Slack notification with
the list of users.

## Overview

Simple Python script to query the [Canny.io API Users
endpoint](https://developers.canny.io/api-reference#users) and
return all users that do not have a Company affiliation.

The following environment variables are stored in a `.env` file and not part of this repository:

- Canny API key
- Slack OAuth token
- Slack channel name
- Total users

The `.env` file contents (in same directory as Python script):

```sh
API_KEY=<canny-api-key>
SLACKBOT_OAUTH_TOKEN=<slack-oauth-token>
SLACK_CHANNEL=<slack-channel-name>
TOTAL_USERS=<total-users-integer>
```

## Assumptions

- The Canny Users API endpoint allows a maximum of 100 records returned (you can optionally define a `skip` value to skip N records).
- The Python script currently naively assumes a maximum of 1000 users (hardcoded) and iterates in blocks of 100.
- There is a working Slackbot integration with the auth token stored in the `.env` file

## Virtual environment

This script uses a virtual environment called `cannyio`. Use Conda
to recreate the environment on your localhost:

```
conda env create -f environment.yml
```

Make sure to activate the environment before running the script:

```
conda activate cannyio
```

## Run the script

Execute the script with the following Python command:

```
$ python return-users.py
```
