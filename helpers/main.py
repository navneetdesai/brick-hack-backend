import cohere
from data import OOP, OS_CN
from keys import API_KEY

co = cohere.Client(API_KEY)
response = co.generate(
    model='medium',
    prompt=f'Extract the concepts from: {OS_CN}',
    max_tokens=200,
    temperature=0,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
print(f'Result: {response.generations[0].text}')
