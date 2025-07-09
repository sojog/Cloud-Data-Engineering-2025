import requests

response = requests.get("https://www.bnr.ro/")
print(response.text)

with open("bnr.ro.txt", "w") as fwriter:
    fwriter.write(response)