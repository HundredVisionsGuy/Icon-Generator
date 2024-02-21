"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re

url = "https://api.dicebear.com/7.x/pixel-art/svg"

response = re.post(url)

print(response.text)
