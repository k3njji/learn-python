import requests
import os
import datetime
import json

# request.get()
# request.post()
# request.put()
# request.delete()

now = datetime.datetime.now()
now = now.date()
now = now.strftime("%Y%m%d")

print(now)
pixela_endpoint = 'https://pixe.la/v1/users'
username = 'k3ntut'
token = 'thisisamadeupkeyhaha'
graphID = 'graph1'

user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# making an account
# res = requests.post(pixela_endpoint, json=user_params)
# print(res.text)

# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
# graph_config = {
#     'id': 'graph1',
#     'name': 'Cycling Graph',
#     'unit': 'Km',
#     'type': 'float',
#     'color': 'ajisai'
# }

headers = {
    'X-USER-TOKEN': token
}

# res = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}"

optional_data = json.dumps({
    "note": f"Cycling {now}"
})

graphs_params = {
    "date": now,
    "quantity": "12",
    "optionalData": optional_data
}


req = requests.post(graph_endpoint, json=graphs_params, headers=headers)
print(req.text)

import requests
import datetime
import json

now = datetime.datetime.now().strftime("%Y%m%d")

pixela_endpoint = 'https://pixe.la/v1/users'
username = 'k3ntut'
token = 'thisisamadeupkeyhaha'
graphID = 'graph1'

headers = {
    "X-USER-TOKEN": token
}

# ---------- CREATE ----------
create_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}"

create_params = {
    "date": now,
    "quantity": "12"
}

# requests.post(create_endpoint, json=create_params, headers=headers)

# ---------- UPDATE ----------
update_endpoint = f"{create_endpoint}/{now}"

update_params = {
    "quantity": "20",
    "optionalData": json.dumps({"note": f"Updated cycling {now}"})
}

# requests.put(update_endpoint, json=update_params, headers=headers)

# ---------- DELETE ----------
delete_endpoint = update_endpoint

# requests.delete(delete_endpoint, headers=headers)