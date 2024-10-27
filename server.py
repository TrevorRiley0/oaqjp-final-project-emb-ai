''' serves the emotion detection api
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def get_emotion_detection():
    ''' GET request, processes text input with emotion detector
        and gives response as a formatted string
    '''
    # get the text to be analyzed from the request args
    text_to_analyze = request.args.get('textToAnalyze')

    # analyze the text with the emotion_detector
    response = emotion_detector(text_to_analyze)

    # error handling
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    # create a formatted string to return
    # the string is really long, so I spit it up over multiple lines
    formatted_str = (f"For the given statement, the system response is "
        f"'anger': {response['anger']}, " 
        f"'disgust': {response['disgust']}, " 
        f"'fear': {response['fear']}, " 
        f"'joy': {response['joy']} " 
        f"and 'sadness': {response['sadness']}. " 
        f"The dominant emotion is {response['dominant_emotion']}.")
    return formatted_str


@app.route("/")
def render_index_page():
    ''' renders the index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
