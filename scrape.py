import  snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#الحج OR #العمره OR #الحرم OR #الميقات OR #الاحرام OR #الطواف OR #السعي OR #جبل_الرحمه OR #عرفة OR #منى) lang:ar until:2022-12-31 since:2010-01-01 -filter:replies"
tweets = []
limits = None

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
# df['Date'] = pd.to_datetime( df['Date'], errors='coerce',utc=True)

# to correct time
date_columns = df.select_dtypes(include=['datetime64[ns, UTC]']).columns
for date_column in date_columns:
    df[date_column] = df[date_column].apply(str)


    
df.to_csv("Test02.csv")



# df.to_excel("sheet01.xlsx")
# print(df)
