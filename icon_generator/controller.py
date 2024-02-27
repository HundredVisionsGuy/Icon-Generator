"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re

url = "https://api.dicebear.com/7.x/"
style = "pixel-art"
seed = "/svg?seed=HundredVisionsGuy"

url = url + style + seed
response = re.post(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")
