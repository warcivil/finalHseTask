import requests

r = requests.post("http://127.0.0.1:5000/ratio=10.5&old_currency=UD&new_currency=A")
print(r.text)
#/ratio=<ratio>&old_currency=<old_currency>&new_currency=<new_currency>