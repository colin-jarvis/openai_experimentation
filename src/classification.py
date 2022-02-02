import os
import openai
import pandas as pd

from helpers import OPENAI_API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

imdb = pd.read_csv('../data/IMDB Dataset.csv')

print(imdb.head())