import os
import openai

from helpers import OPENAI_API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

# Completion

## Test

phrase = 'They say the early bird'

response = openai.Completion.create(engine="davinci", prompt=phrase, max_tokens=25)

print(response)

## Another Test

song = '''There was once a brave young girl named Callie. She lived in a middle-class neighbourhood in Glasgow, 
so life had never been tougher. 

One day she'''

song_response = openai.Completion.create(engine="davinci", prompt=song, max_tokens=100)

print(song_response)

## Another Test

question = '''There was once a brave young girl named Callie. She lived in a middle-class neighbourhood in Glasgow, 
so life had never been tougher. 

Where did Callie live?'''

question_response = openai.Completion.create(engine="davinci", prompt=question, max_tokens=100)

print(question_response)



# Classification

# Search

# Question Answering

# Fine-tuning

# Embeddings