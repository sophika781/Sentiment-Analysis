import requests, json

def sentiment_analyzer(text_to_analyse):
    url=  'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' #URL of sentiment analyzer
    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} #Set headers for the API request
    myobj= { "raw_document": { "text": text_to_analyse } } #Creating a dictionary with text to be analyzed
    response= requests.post(url, json= myobj, headers=headers) #Send a POST request to API with text and headers
    formatted_response= json.loads(response.text)
    if(response.status_code == 200):
        label= formatted_response['documentSentiment']['label']
        score= formatted_response['documentSentiment']['score']
    elif (response.status_code == 500):
        label= None
        score= None
    return {"label": label, "score": score}