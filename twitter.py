import openai, tweepy, random, time
import dotenv as _dotenv
import os as _os

_dotenv.load_dotenv()

API_KEY = _os.environ["API_KEY"]
API_KEY_SECRET = _os.environ["API_KEY_SECRET"]
ACCESS_TOKEN = _os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["ACCESS_TOKEN_SECRET"]

OPENAI_API_KEY = _os.environ["OPENAI_API_KEY"]

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

openai.api_key = OPENAI_API_KEY

prompts = [
    {'text': "tweet something smart for machine learning"},
    {'text': "ask something smart realted to machine learning"},
    {'text': "tweet something smart for andorid"},
    {'text': "ask something smart realted to android"},
    {'text': "tweet something smart for java"},
    {'text': "ask something smart realted to java"},
    {'text': "tweet something smart for kotlin"},
    {'text': "ask something smart realted to kotlin"},
    {'text': "tweet something smart for python programming language"},
    {'text': "ask something smart realted to python programming language"},
    {'text': "tweet something smart for javascript"},
    {'text': "ask something smart realted to javascript"},
    {'text': "tweet something smart for reactjs"},
    {'text': "ask something smart realted to reactjs"},
    {'text': "tweet something smart for nodejs"},
    {'text': "ask something smart realted to nodejs"},
    {'text': "tweet something smart for devops"},
    {'text': "ask something smart realted to devops"},
    {'text': "tweet something smart for web development"},
    {'text': "ask something smart realted to web development"},
    {'text': "tweet something smart for artificial intelligence"},
    {'text': "ask something smart realted to artificial intelligence"},
    {'text': "tweet something smart for augmented reality"},
    {'text': "ask something smart realted to augmented reality"},
    {'text': "tweet something smart for virtual reality"},
    {'text': "ask something smart realted to virtual reality"},
    {'text': "tweet something smart for mixed reality"},
    {'text': "ask something smart realted to mixed reality"},
    {'text': "tweet something smart for unity3d"},
    {'text': "ask something smart realted to unity3d"},
    {'text': "tweet something smart for game development"},
    {'text': "ask something smart realted to game development"},
    {'text': "tweet something smart for mobile development"},
    {'text': "ask something smart realted to mobile development"}
]


def generate_tweets(text):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=text,
        max_tokens=64
    )

    return response.choices[0].text

def tweet():
    chosen_prompt = random.choice(prompts)
    text_openai = chosen_prompt["text"]
    text = generate_tweets(text_openai)
    api.update_status(text)

while True:
    tweet()
    time.sleep(43200)