import requests

response = requests.get('http://127.0.0.1:8000/Yaakov')
print(response.json())
responses = set()

def add_response(request):
    responses.add(request.json())