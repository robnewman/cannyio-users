# cannyio-users

Utility to query the Canny Users API endpoint

## Overview

Simple Python script to query the [Canny.io API Users endpoint](https://developers.canny.io/api-reference#users) and return all users that do not have a Company affiliation.

The Seqera Canny API key is stored in a `.env` file and is not part of this repository.
Contact <rob.newman@seqera.io> for the API key.

## Assumptions

- The Canny Users API endpoint allows a maximum of 100 records returned (you can optionally define a `skip` value to skip N records).
- The Python script currently naively assumes a maximum of 1000 users (hardcoded) and iterates in blocks of 100.
- There is a working Slackbot integration with the auth token stored in the `.env` file

## Virtual environment

This script uses a virtual environment called `cannyio`. Use Conda to recreate the environment on your localhost:

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
