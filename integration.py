import requests;
from requests.auth import HTTPBasicAuth;
import json;
import base64;

def getAPIToken():
    getAPITokenURL = "https://instance.fique.online/webhook/merge/88d8701e-a1d6-4fee-b15b-53e90dc1d126/autenticacao/57441afd5a59ccd4c62816683fcc8d665c42bb7b12857fc64a6cace4ababdc67f78c70b044";
    basicAuthToGetAPIToken = HTTPBasicAuth('teste_fiqon', 'senha@115#');
    
    getAPITokenAPIResponse = requests.post(getAPITokenURL, auth=basicAuthToGetAPIToken);
    finalAPIToken = json.loads(getAPITokenAPIResponse.text)['api_token'];
    return finalAPIToken;
    
def getPillarsAPI():
    getPillarsURL = "https://instance.fique.online/webhook/merge/88d8701e-a1d6-4fee-b15b-53e90dc1d126/listar_pilares/76b07f1dbf18eabde7b8e3611ab078daa0f34b094cc9856d20d6d0b15fb3b7a99f697e451d";
    apiToken = getAPIToken()
    pagesCounter = 5;
    finalPillarsString = "";
    
    for i in range(pagesCounter):
        getPillarsAPIParams = {"api_token": apiToken, "page": i}
        getPillarsAPIResponse = requests.get(getPillarsURL, params=getPillarsAPIParams);
        getPillarsAPIResponseToString = json.loads(getPillarsAPIResponse.text)['data'];
        finalPillarsString += getPillarsAPIResponseToString;
        
    finalPillarsStringTo64Base = base64.b64encode(finalPillarsString.encode()).decode();
    return finalPillarsStringTo64Base;

def postPillarsToAPI():
    postPillarsURL = "https://instance.fique.online/webhook/merge/88d8701e-a1d6-4fee-b15b-53e90dc1d126/envia_resposta/7b56940678e89802e02e1981a8657206d639f657d4c58efb8d8fb74814799d1c001ec121c6"
    apiToken = getAPIToken();
    pillarsTo64Base = getPillarsAPI();
    postPillarsParams = {"api_token": apiToken};
    postPillarsBody = {"answer": pillarsTo64Base};
    postPillarsAPIResponse = requests.post(postPillarsURL, params=postPillarsParams, json=postPillarsBody);
    finalTestAnswer = json.loads(postPillarsAPIResponse.text)['message'];
    print(finalTestAnswer);

if __name__ == "__main__":
    postPillarsToAPI();