import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        # creating a list of tuples to define the test cases
        # item 0 is the input statement
        # item 1 is the expected dominant emotion in the output
        statements_with_expected_dominant = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]

        # using a for loop to iterate over each test case
        for test in statements_with_expected_dominant:
            response = emotion_detector(test[0])
            self.assertEqual(response['dominant_emotion'], test[1])

unittest.main()