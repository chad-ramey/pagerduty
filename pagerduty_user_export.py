"""
Script: PagerDuty User Export

Description:
This script exports user information from PagerDuty to a CSV file. It retrieves user details including UserName, Email, Role, JobTitle, InvitationSent status, associated Teams, and Schedules. The script reads an API token from a text file to authenticate requests and handles pagination to fetch all users.

Functions:
- get_token_from_file: Reads the PagerDuty API token from a specified text file.
- get_pd_users: Fetches user information from PagerDuty API and writes it to a CSV file.
- main: Main function to run the script.

Usage:
1. Run the script.
2. Enter the path to the PagerDuty token file when prompted.
3. The script will fetch user data from PagerDuty and export it to 'pagerduty_users.csv' on the current directory.

Notes:
- Ensure the API token has the necessary permissions to access user information.
- Handle the API token securely and do not expose it in the code.

Author: Chad Ramey
Date: August 3, 2024
"""

import requests
import csv
import os

def get_token_from_file():
    """
    Reads the PagerDuty API token from a specified text file.

    Returns:
        str: The API token.
    """
    token_file_path = input("Enter the path to the PagerDuty token file: ")
    try:
        with open(token_file_path, "r") as file:
            token = file.read().strip()
            return token
    except FileNotFoundError:
        print(f"Error: The file {token_file_path} was not found.")
        exit(1)

def get_pd_users(token):
    """
    Fetches user information from PagerDuty and writes it to a CSV file.

    Args:
        token (str): The PagerDuty API token.

    Returns:
        str: The absolute path to the CSV file.
    """
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": f"Token token={token}"
    }

    url = 'https://api.pagerduty.com/users'
    params = {'limit': 100}
    csv_headers = ['UserName', 'Email', 'Role', 'JobTitle', 'InvitationSent', 'Teams', 'Schedules']
    csv_file = 'pagerduty_users.csv'

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()

        while True:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            users = data.get('users', [])

            for user in users:
                row = {
                    'UserName': user.get('name', ''),
                    'Email': user.get('email', ''),
                    'Role': user.get('role', ''),
                    'JobTitle': user.get('job_title', ''),
                    'InvitationSent': user.get('invitation_sent', ''),
                    'Teams': ', '.join([team.get('summary', '') for team in user.get('teams', [])]),
                    'Schedules': ', '.join([schedule.get('summary', '') for schedule in user.get('schedules', [])])
                }
                writer.writerow(row)

            # Check if there are more users to fetch
            if 'more' in data and data['more']:
                params['offset'] = data.get('offset', 0) + params['limit']
            else:
                break

    return os.path.abspath(csv_file)

def main():
    """
    Main function to run the script.
    """
    token = get_token_from_file()
    csv_file_path = get_pd_users(token)
    print("PagerDuty user export is complete.")
    print("CSV file location:", csv_file_path)

if __name__ == "__main__":
    main()
