
import requests

resp = requests.post(" http://localhost:5000/predict")

print(resp.text)

import pytorch
print(torch.__version__)
