
import  snscrape.modules.twitter as sntwitter
import pandas as pd




# query = "(#الحج OR #العمره OR #الحرم OR #الميقات OR #الاحرام OR #الطواف OR #السعي OR #جبل_الرحمه OR #عرفة OR #منى) until:2022-12-12 since:2012-01-01 -filter:replies"
# tweets = []
# limits = None

# for tweet in sntwitter.TwitterSearchScraper(query).get_items():

#     # print(vars(tweet))
#     # break
#     if len(tweets) == limits:
#         break
#     else:
#         tweets.append([tweet.date, tweet.user.username, tweet.content])

# df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
# # df['Date'] = pd.to_datetime( df['Date'], errors='coerce',utc=True)




# read the xlxs u created
excel_file_path = 'not_clean.xlsx'
df = pd.read_excel(excel_file_path)

# for showing timezone. otherwise prints #######
# date_columns = df.select_dtypes(include=['datetime64[ns, UTC]']).columns
# for date_column in date_columns:
#     df[date_column] = df[date_column].apply(str)

# remove duplicates
# df.drop_duplicates(subset="Tweet", keep='first', inplace= True)

# df.drop_duplicates(subset=['Tweet'])



# remove unwanted char & الحركات الاعرابية
spec_chars = ["!",'"',"%","&","'","(",")",
              "=",">","?","@","[","\\","]","^",".","#","/"
              "*",",","-",":",";","<","+","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
              "`","{","|","}","~","–","َ","ُ","ِ","ّ","ً","ٍ","ٌ","ْ","ٓ","ٌ","","ٰ","ـ"]
for char in spec_chars:
    df['Tweet'] = df['Tweet'].str.replace(char,'', regex=True)





# to remove numbers
df['Tweet'] = df['Tweet'].str.replace('\d+', '', regex=True)

## to remove emojis
import re
# df['Tweet'] = df['Tweet'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE, regex=True)

# import re
# df['Tweet'] = df['Tweet'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

# remove linksS
# df['Tweet'] = df['Tweet'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)




## numbers of tokenz
# df['sents_length'] = df.apply(lambda row: len(row['Tweet']), axis=1)


# tweet_num = df['sents_length']
# for Tweet in df['Tweet']
#     if len(df['sent_length']) < 3:
#      df_clean = df.drop(tweet_num)
# else: 
#     continue

# tweet_num = df['sents_length']
# for df['Tweet'] in df.iterrows():
#      if len(tweet_num) <= 10:
#         df_clean = df.drop(tweet_num)
   

     

# import nltk
# from nltk.stem.isri import ISRIStemmer
# st = ISRIStemmer()

# df['Stemmed']=df['Tweet'].apply(lambda x : [st.stem(y) for y in x])

# def get_indices(df,Tweet,n=3): 





# to tokenize      
# import nltk
# from nltk import word_tokenize
# df['Tokens'] = df['Tweet'].apply(word_tokenize)



# from nltk.tokenize import word_tokenize

# df['Tweet'].dropna(inplace=True)
# tweetText = df['Tweet'].astype(str)

# ## to tokenize 
# tweetText = tweetText.apply(word_tokenize)
# df['Tokens']= tweetText



# from nltk.stem.isri import ISRIStemmer
# st = ISRIStemmer()
# df['stemmed'] = df['Tokens'].apply(lambda x: [st.stem(y) for y in x])
# df['tweet_stemmed_sentence']=df['stemmed'].apply(lambda x : " ".join(x))

# df = df.drop(columns=['stemmed']) 
# df = df.drop(columns=['Tokens']) 


# from farasa.pos import FarasaPOSTagger
# from farasa.ner import FarasaNamedEntityRecognizer
# from farasa.diacratizer import FarasaDiacritizer
# from farasa.segmenter import FarasaSegmenter
# from farasa.stemmer import FarasaStemmer






##Get the indices of dataframe where exist more than n tokens in a specific column

##Parameters:


#remove URL - ALL NOT WORK
# df['Tweet'].str.replace('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ',regex=True)
# def clean_data(df):
#replace URL of a tex
    # df['Tweet'] = df['Tweet'].str.replace('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', regex=True)
# clean_data(df)



# df['Tweet'].apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
# import re
# df['Tweet'] = df['Tweet'].str.encode('ascii', 'ignore').str.decode('ascii')


# import re
# def remove_emojis(df['Tweet']):
#     emoj = re.compile("["
#         u"\U00002700-\U000027BF"  # Dingbats
#         u"\U0001F600-\U0001F64F"  # Emoticons
#         u"\U00002600-\U000026FF"  # Miscellaneous Symbols
#         u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols And Pictographs
#         u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
#         u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
#         u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
#                       "]+", re.UNICODE)
#     return re.sub(emoj, '', subset= "Tweet")



# main ----
# df['Date'] = df['Date'].dt.tz_localize(None)

# date method 1
# date_columns = df.select_dtypes(include=['datetime64[ns, UTC]']).columns
# for date_column in date_columns:
#     df[date_column] = df[date_column].dt.date
    




# emoji_pattern = re.compile("["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            "]+", flags=re.UNICODE)
# print(emoji_pattern.sub(r'', df['Tweet'])) # no emoji


df.to_excel("remove_All.xlsx")



# df.to_excel("sheet01.xlsx")
# print(df)
