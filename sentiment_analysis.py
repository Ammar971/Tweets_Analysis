import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import pickle
from sklearn import model_selection, svm, naive_bayes
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import ComplementNB, BernoulliNB, GaussianNB, MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,balanced_accuracy_score,average_precision_score,f1_score,recall_score,classification_report
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn import tree
train = pd.read_excel(r'C:/pyyyyyyyy/OG.xlsx')

## for labelling
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(train['Tweet'].values.astype('U'),train['sentiment'].values.astype('U'),random_state=1,test_size=0.20)

## for sentiment
# Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(train['Tweet'].values.astype('U'),train['sentiment'].values.astype('U'),random_state=1,test_size=0.20)

##### finished spilitting



vectorizer = CountVectorizer(max_features=20000,decode_error="ignore")
Train_X= vectorizer.fit_transform(Train_X)
Test_X= vectorizer.transform(Test_X)

###### convert to vector


##SVM
# clf= svm.LinearSVC(C=0.1)
##Logsistc Regression
# clf = LogisticRegression()
clf = DecisionTreeClassifier()
start = time.time()
end = time.time()

clf.fit(Train_X, Train_Y)
print("The elapsed time", end -start)

############ Linear SVM model (learnin/training model)



clf_predictions= clf.predict(Test_X)

print("f1 score -> ", f1_score(Test_Y, clf_predictions, average='micro')*100)
print('recall score ->', recall_score(Test_Y,clf_predictions,average='micro')*100)
print('balanced accuarcy score ->', balanced_accuracy_score(Test_Y,clf_predictions)*100 )

################ testing


filename = 'finalized_model.pk1'
pickle.dump(clf, open(filename, 'wb'))

with open(filename, 'rb') as file:
    Pickled_LR_Model = pickle.load(file)

print(Pickled_LR_Model)

sample_sub = pd.read_excel(r'C:/pyyyyyyyy/20.xlsx')
Final = vectorizer.transform(sample_sub['Tweet'].values.astype('U'))

y_pre= Pickled_LR_Model.predict(Final)
sub=pd.DataFrame({'Tweet' :sample_sub['Tweet'].values.tolist(), 'sentiment':y_pre})
sub.to_excel('RndmFrst(label).xlsx')

############### saving model


