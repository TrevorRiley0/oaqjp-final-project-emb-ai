''' defines emotion detection logic 
    using Watson NLP library Emotion Predict
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' uses Emotion Predict to determine emotion of text_to_analyze
    '''
    # defining post request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObj = { "raw_document": { "text": text_to_analyze } }
    
    # post and get response
    response = requests.post(url, json = jsonObj, headers = headers)
    
    if response.status_code == 200:
        # formatting the response
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion'] # holds emotion score data
    
        # getting the dominant emotion
        # iterate over key/value pairs to find the highest value
        dominant_emotion = None # initialize dominant_emotion
        for key, score in emotions.items():
            if dominant_emotion is None or score >= dominant_emotion[1]:
                dominant_emotion = (key, score)

        # add dominant emotion to the emotions dictionary
        # the dictionay is already in the correct format
        # but is just missing the dominant_emotion key
        emotions['dominant_emotion'] = dominant_emotion[0]
    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions
    