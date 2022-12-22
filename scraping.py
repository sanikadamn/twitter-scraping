import string
import tweepy

bearer_token=" "

obj=tweepy.Client(bearer_token)

hashtag_file={
    "#NovaxDjokovic": "novaxdjokovic.txt",
    "#NovaxDjokovid": "NovaxDjokovid.txt",
    "#DjokovicGoHome": "DjokovicGoHome.txt",
    "#Djocovid": "Djocovid.txt",
    "#NoleFam": "nolefam.txt",
    "#WeStandWithNovak": "westandwithnovak.txt",
    "#WeStandWithDjokovic": "westandwithdjokovic.txt",
    "#NovakDjokovic": "novakdjokovic.txt",
    "#TeamDjokovic": "teamdjokovic.txt"
}
allowed_chars = set(string.ascii_letters + string.digits + string.punctuation + string.whitespace)

def clean_string(text):
    text = [x for x in text if x in allowed_chars]
    text = "".join(text)
    return text

hashtags=["#NovaxDjokovic","#NovaxDjokovid","#DjokovicGoHome", "#Djocovid","#NoleFam","#WeStandWithNovak", "#WeStandWithDjokovic","#NovakDjokovic", "#TeamDjokovic"]
for hashtag in hashtags:
    with open(hashtag[1:] + ".txt", "w", encoding="utf-8") as f:
        for tweet in tweepy.Paginator(
            obj.search_recent_tweets, hashtag + " lang:en -is:retweet", max_results=100
        ).flatten(limit=1000):
            text = clean_string(tweet.text)
            text = text.replace("\n", " ")
            text = text.replace("\r", " ")
            f.write(f"{text}\n")
            #id=clean_string(tweet.id)
            id=tweet.id
