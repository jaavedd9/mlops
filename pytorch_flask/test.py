import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('./cat.jpeg','rb')})

print(resp.json())
