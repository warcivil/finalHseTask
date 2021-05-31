import requests

r = requests.delete("http://127.0.0.1:5000/old_currency=MUR&new_currency=GAV")
print(r.text)
#/ratio=<ratio>&old_currency=<old_currency>&new_currency=<new_currency>