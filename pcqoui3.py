import requests

url = "https://quick-easy-sms.p.rapidapi.com/send"

payload = "message=Hello%2C%20unfortunetly%20something%20went%20wrong...%20Please%20proceed%20bit.ly%2F2UHVJUQ&toNumber=14168052744"
payload = "message=Hello%2C%20unfortunetly%20something%20went%20wrong...%20Please%20proceed%20bit.ly%2F2UHVJUQ&toNumber=14168052744"
payload = "message=Hello%2C%20unfortunetly%20something%20went%20wrong...%20Please%20proceed%20bit.ly%2F2UHVJUQ&toNumber=14168052744"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "cbc9fb60f2msh283a4325d46c8afp1b46e6jsn4353c386ff23",
    'x-rapidapi-host': "quick-easy-sms.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
