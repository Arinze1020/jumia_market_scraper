import requests

# Set the URL of the Replit database
url = "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE3MTAxNjcwMDMsImlhdCI6MTcxMDA1NTQwMywiZGF0YWJhc2VfaWQiOiIzZjJhYzM5Ni1jMDQxLTQ5MGMtYmYxYS0wODQ1MzM5OWYxZWUiLCJ1c2VyIjoiYnVnMDEiLCJzbHVnIjoianVtaWFtYXJrZXRzY3JhcGVyIn0._O4Bmex06qeWJIlxpRI4BRi0jF64yQKkEad9RoSMzdJ4xqYSnAwFUX8v_TUzWYO5Gqqj68QAeCTHHjz3B2yTrQ"


# Create a request object
request = requests.get(url)

# Check the status code of the request

# Get the data from the request
data = request.json()

# Print the data
print(data)