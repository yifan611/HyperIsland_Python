"""Use snscrape to scrape from Twitter, 
  Tweet amounts: 30 tweets /  per day in April
  Topics: elon mushm, takeover, twitter, crypto
  Save the dataframe to csv file."""


import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, date

attributes_container = []

for n in range (1,30):
    
    t1 = date(year = 2022, month = 4, day = n)
    t2 = date(year = 2022, month = 4, day = n+1)

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('elon musk "twitter" (takeover) -crypto lang:en since:' + str(t1) + ' until:' + str(t2)).get_items()):

        if i>29:
            break
                   
        attributes_container.append([tweet.user.username,
                                    tweet.user.verified,
                                    tweet.user.created,
                                    tweet.user.followersCount,
                                    tweet.user.friendsCount,
                                    tweet.retweetCount,
                                    tweet.lang,
                                    tweet.date,
                                    tweet.likeCount,
                                    tweet.sourceLabel,
                                    tweet.id,
                                    tweet.rawContent,
                                    tweet.hashtags,
                                    tweet.conversationId,
                                    tweet.inReplyToUser,
                                    tweet.coordinates,
                                    tweet.place])
    n += 1  

# get dataframe    
df = pd.DataFrame(attributes_container, columns=["User",
                                                   "verified",
                                                   "Date_Created",
                                                   "Follows_Count",
                                                   "Friends_Count",
                                                   "Retweet_Count",
                                                   "Language",
                                                   "Date_Tweet",
                                                   "Number_of_Likes",
                                                   "Source_of_Tweet",
                                                   "Tweet_Id",
                                                   "Tweet",
                                                   "Hashtags",
                                                   "Conversation_Id",
                                                   "In_reply_To",
                                                   "Coordinates",
                                                   "Place"])

print(df)

df.to_csv('df_m4.1-29.csv')
