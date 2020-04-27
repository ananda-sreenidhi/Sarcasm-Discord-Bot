import re
import pickle
from nltk.stem.porter import PorterStemmer
import os


import warnings
warnings.filterwarnings("ignore")

ps = PorterStemmer()

path = os.getcwd()
x = open("/app/cogs/modules/model.pickle", "rb")
pm = pickle.load(x)
x.close()
y = open("/app/cogs/modules/tfidf.pickle", "rb")
tm = pickle.load(y)
y.close()

def predict(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = " ".join([ps.stem(i) for i in text.lower().split()])
    text = tm.transform([text]).toarray()
    return "Sarcastic." if pm.predict(text)[0] == 1 else "Serious."





