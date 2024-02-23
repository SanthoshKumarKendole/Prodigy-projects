import matplotlib.pyplot as pt
from textblob import TextBlob
import re

social_media_data=['I love this brand! Its amazing',
                   'This customer service is terrible',
                   'Just tried their new products adn its fantastic',
                   'Im not sure about this brand.Its so-so',
                   'Terrible experience with their support team',
                   'Neutral',"Awesomw product",'Great product','Money waste']

def analyze_content(text):
    analysis=TextBlob(text)
    if analysis.sentiment.polarity>0:
        return 'Positive'
    elif analysis.sentiment.polarity<0:
        return "Negative"
    else:
        return "Neutral"
sentiments=[analyze_content(text) for text in social_media_data]

positive_count=sentiments.count("Positive")
negative_count=sentiments.count("Negative")
neutral_count=sentiments.count("Neutral")

sentiments_labels=['Positive','Negative','Neutral']
sentiments_counts=[positive_count,negative_count,neutral_count]
pt.bar(sentiments_labels,sentiments_counts,color=['Green','red','blue'])
pt.title("Sentiments analysis of social media data")
pt.xlabel("Sentiments")
pt.ylabel("Counts")
pt.show()