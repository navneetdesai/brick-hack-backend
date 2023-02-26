from data import OOP, OS_CN
from keys import API_KEY
import cohere


def generate_summary(co):
    return co.summarize(model='summarize-xlarge', text=OOP, length='long', extractiveness='medium', temperature=0.25)


def main():
    co = cohere.Client(API_KEY)
    return generate_summary(co).summary
