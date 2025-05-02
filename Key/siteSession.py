import requests
import config  # Import your configuration file
from datetime import datetime  # Import datetime for getting the current time

# Endpoint for GetSessionAuthToken
endpoint = 'Authentication/GetSessionAuthToken'

# Full URL for the API call
url = config.base_url + endpoint

# Headers for the request
headers = {
    'AuthToken': config.integrated_auth_token,
    'AuthUser': config.auth_user,
    'SiteCode': config.site_code,
    'AuthPassword': config.auth_password_site,
    'AuthenticationType': config.authentication_type
}

# Get the current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Send GET request
response = requests.get(url, headers=headers)

# Initialize result variables
case_result = "Fail"  # Default case result in case of failure
token = None  # Default token value is None

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()  # Assuming the response is JSON
    response_code = response_data.get('ResponseCode', None)

    # Determine the case result based on ResponseCode
    case_result = "Pass" if response_code == 200 else "Fail"
    print("Pass:", response_data)

    # Extract the AuthToken from the response
    auth_token = response_data.get('AuthToken', None)

    # Set the token variable if it exists
    if auth_token:
        token = auth_token
    else:
        case_result = "Fail"

    # Prepare data for logging (including case result and token)
    log_entry = {
        'ResponseCode': response_code,
        'ResponseDescription': response_data.get('ResponseDescription', None),
        'AuthToken': auth_token,
        'CaseResult': case_result,
        'CurrentTime': current_time
    }

    # Log response (you can modify this if you need logging for debugging)
    print(log_entry)

else:
    print("Fail:", response.status_code, response.text)

# Update the sessionkeysite in the config.py file
if token:
    # Open the config.py file in append mode to update the sessionkeysite
    config_file_path = 'config.py'
    with open(config_file_path, 'r') as file:
        config_content = file.read()

    # Replace or insert the sessionkeysite value into the config.py content
    if 'sessionkeysite' in config_content:
        # If sessionkeysite already exists, replace its value
        config_content = config_content.replace(
            f'sessionkeysite = "{config.sessionkeysite}"',
            f'sessionkeysite = "{token}"'
        )
    else:
        # If sessionkeysite doesn't exist, add it to the file
        config_content += f'\nsessionkeysite = "{token}"\n'

    # Write the updated content back to the config.py file
    with open(config_file_path, 'w') as file:
        file.write(config_content)

    print(f"sessionkeysite has been saved to {config_file_path}")
else:
    print("No token generated, 'No token generated' information will not be saved.")
