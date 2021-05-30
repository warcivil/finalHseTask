import requests

r = requests.delete("http://127.0.0.1:5000/old_currency=USD&new_currency=EUR")
print(r.text)