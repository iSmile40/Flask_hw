import requests


# resp = requests.post('http://127.0.0.1:5070/ads/',
#                      json={
#                          "title": "продам компьютер",
#                          "text": "хорошее состояние, мышка в подарок",
#                          "owner": "Александр"
#                      }).json
#
# print(resp)


# resp = requests.get('http://127.0.0.1:5070/ads/2')

# print(resp)

resp = requests.delete('http://127.0.0.1:5070/ads/',
                       json={'id': 2})
print(resp)
