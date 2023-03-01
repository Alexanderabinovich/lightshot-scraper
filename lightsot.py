import requests
import random

base_url = "https://prnt.sc/"

# Define the characters that can appear in the image IDs
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define the number of IDs to generate and check
num_ids = 10

# Create a file to write successful links to
with open("successful_links.txt", "w") as f:
    # Loop over the specified number of IDs
    for i in range(num_ids):
        # Generate a random ID by selecting characters at random
        id = "".join([characters[random.randint(0, len(characters) - 1)] for _ in range(6)])

        # Create the full URL for the image
        url = base_url + id

        # Make a request to the URL
        response = requests.get(url)

        # Print the status code for debugging purposes
        print(f"Attempt {i}: {url} returned status code {response.status_code}")

        # If the response status code is 200, write the URL to the file
        if response.status_code == 200:
            f.write(url + "\n")
