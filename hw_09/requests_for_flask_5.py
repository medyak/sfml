import requests

resp = requests.post(
    'http://localhost:12454/predict',
    data = {
        'text': '''
    кассир кассир кассир кассир
    '''
    }
)

print(resp.json())
