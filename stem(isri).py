import pandas as pd
import nltk

# read the xlxs u created
excel_file_path = 'stem_isri.xlsx'
df = pd.read_excel(excel_file_path)

from nltk.tokenize import word_tokenize

df['Tweet'].dropna(inplace=True)
tweetText = df['Tweet'].astype(str)

# ## to tokenize 
tweetText = tweetText.apply(word_tokenize)
df['Tokens']= tweetText



## import ISRSI packages for Arabic language
from nltk.stem.isri import ISRIStemmer
st = ISRIStemmer()
# stem for evey row
df['stemmed'] = df['Tokens'].apply(lambda x: [st.stem(y) for y in x])
# to have a complete sentence withot qutations.
df['tweet_stemmed_sentence']=df['stemmed'].apply(lambda x : " ".join(x))

# to drop unncessary columns
df = df.drop(columns=['stemmed']) 
df = df.drop(columns=['Tokens']) 

# export
df.to_excel("isri.xlsx")