from flask import Flask, request, render_template
import requests
from requests.structures import CaseInsensitiveDict
from flask import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_data = False

    if request.method == 'POST':
        print(request.form['periode_pengujian'])
        print(request.form['nama_lokasi'])
        print(request.form['parameter'])
        print(request.form['satuan'])
        print(request.form['nilai'])
        periode_pengujian_value = request.form['periode_pengujian']
        nama_lokasi_value = request.form['nama_lokasi']
        parameter_value = request.form['parameter']
        satuan_value = request.form['satuan']
        nilai_value = request.form['nilai']
        
        access_token = get_access_token()

        prediction_value = get_prediction(
            access_token,
            periode_pengujian_value, nama_lokasi_value, parameter_value, satuan_value, nilai_value
        )

        prediction_data = prediction_value
    return render_template('index.html', prediction = prediction_data)

def get_access_token():
    url = "https://iam.cloud.ibm.com/oidc/token"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=oivR2GXrXaxPNYHwflVwD17bLfJoBCvWag28Uv-28mJu"
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        json_resp = resp.json()
        return json_resp.get('access_token')
    else:
        return None

def get_prediction(access_token, *input_values):
    url = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d2afcb56-0a9c-45e6-8885-576105d8920f/predictions?version=2021-05-01"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + access_token

    data = {
        "input_data": [
            {
                "fields": [
                    "periode_pengujian",
                    "nama_lokasi",
                    "parameter",
                    "satuan",
                    "nilai"
                ],
                "values": [list(input_values)]
            }
        ]
    }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 200:
        predictions = resp.json()
        prediction_value = predictions['predictions'][0]['values'][0][0]
        output = json.loads(resp.text)
        print("output >>", output)
        return prediction_value
    else:
        return None
    
#Uncomment code below if you want to host it locally
if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0')



#Made by O. Midiyanto in IBM Academy with Infinite Learning - 2023 