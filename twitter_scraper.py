# pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#elevy OR #ELEVY OR #ELevy OR #Elevy OR #e-levy OR #E-LEVY OR #E-Levy OR #E-levy) until:2022-10-31 since:2020-01-01"
tweets = []
limit = 5

print("Initialized endpoints\nData collection initiated\nCollecting data from Twitter\nPlease wait....")

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.user.displayname, tweet.user.location, tweet.lang, tweet.content])
        
dataFrame = pd.DataFrame(tweets, columns=['date', 'username', 'displayname', 'location', 'language', 'tweet'])
# print(dataFrame)

print("\nData fetching complete!")

# to save to csv
print("Writing to CSV file...")
dataFrame.to_csv('elevy_tweets.csv')

print("Data collection complete!!")