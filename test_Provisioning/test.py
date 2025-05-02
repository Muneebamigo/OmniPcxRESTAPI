# data = '{"MSG": "Application is created sucessfully for Project ID: 6cdc3d7f-af9e-48c9-9dbb-b2e1efdd1818","applicationId": "931d0949-acda-4294-86da-be46fdca884b-OPR"}'
#
#
# def parse_application_id(Str):
#     data_response = data.split(':')
#     project_id = data_response[2].split(',')[0]
#     project_id=project_id.replace('"', "")
#     application_id =data_response[3].split('"')[1]
#     return  project_id ,application_id
#
# parse_application_id(data)


import pypyodbc

# Replace the following placeholders with your actual PostgreSQL connection details:
# - your_server: The address of your PostgreSQL server (e.g., localhost or IP address).
# - your_db: The name of your PostgreSQL database.
# - your_user: The username to access the PostgreSQL database.
# - your_password: The password for the username.

connection_string = 'DRIVER={PostgreSQL Unicode};SERVER=172.20.13.30;DATABASE=opcxr_config_apri_253;UID=postgres;PWD=0mniPcx'

try:
    # Try to connect to the PostgreSQL database using the provided connection string.
    conn = pypyodbc.connect(connection_string)
    print("Connection successful!")

    # Close the connection when done.
    conn.close()

except Exception as e:
    # If connection fails, print the error message.
    print(f"Connection failed: {e}")











