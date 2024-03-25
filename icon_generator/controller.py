"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re

# build out the URL based on API docs
base_url = "https://api.dicebear.com/7.x/"
style = "bottts/"
filetype = "svg"
seed = "?seed=HundredVisionsGuy"

url = base_url + style + filetype + seed
response = re.get(url)

if __name__ == "__main__":
    response = re.get(url)
    if response.ok:
        print(response.text)
    else:
        print(f"There was an error: {response.status_code}")
