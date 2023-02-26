import cohere
from . import django_auth

co = cohere.Client(django_auth.API_KEY)


def generate_summary(text):
    return co.summarize(model='summarize-xlarge', text=text, length='long', extractiveness='medium', temperature=0.25)

def generate_outline(text):
    response = co.generate(
        model='command-xlarge-20221108',
        prompt=f'extract all concepts from lecture: {text}',
        max_tokens=200,
        temperature=0,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text