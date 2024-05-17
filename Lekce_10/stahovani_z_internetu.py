# tyto příkazy zapište do terminálu:

# pip3 install requests
# pip install requests
# python - m pip install requests

import requests

path = "https://api.kodim.cz/python-data/people"

response = requests.get(path)
#print(response)
data = response.json()
print(data)
#print(data[0])
#print(data[0]["first_name"])

