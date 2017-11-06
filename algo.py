import nltk
from nltk.corpus import movie_reviews,stopwords
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import pickle


class VotedClassifier(ClassifierI):
	def __init__(self,*classifier):
		self._classifier = classifier
			
	def classify(self,feature_set):
		votes= []
		for w in self._classifier:
			votes.append(w.classify(feature_set))
		return mode(votes)

	def confidence(self,feature_set):
		votes = []
		for w in self._classifier:
			votes.append(w.classify(feature_set))
		return votes.count(mode(votes))/float(len(votes))


def filterwords(txt_list):
	txt_list = [w.lower() for w in txt_list if w.isalpha() and (len(w) >= 5 or w in ["n't",'not','bad'])]
	return txt_list


def feature_vec(txt_list,words):
	feature_list = {}
	for w in set(txt_list):
		feature_list[w] = w in words
	return feature_list




words_cat = [(list(filterwords(movie_reviews.words(fileid))),category) for category in movie_reviews.categories() for fileid in 			movie_reviews.fileids(category)]
#print(words_cat[:5])
random.shuffle(words_cat)
words = filterwords(movie_reviews.words())
words = nltk.FreqDist(words)
#print(words.most_common(10))
		
words_feature = words.keys()[:5000]
pickle.dump(words_feature,open("obj/words_feature.p","wb"))
#words_feature = pickle.load(open("obj/words_feature.p","rb"))
words_cat = [(feature_vec(w,words_feature),cat) for w,cat in words_cat]

train_set = words_cat[:1200]
test_set = words_cat[1200:1600]
val_set = words_cat[1600:]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print("Classifier accuracy :", (nltk.classify.accuracy(classifier, test_set))*100)
pickle.dump(classifier,open("obj/classifier.p","wb"))
#classifier = pickle.load(open("obj/classifier.p","rb"))


MNBClassifier = SklearnClassifier(MultinomialNB())
MNBClassifier.train(train_set)
print("MultinomialNB accuracy:", (nltk.classify.accuracy(MNBClassifier,test_set))*100)
pickle.dump(MNBClassifier,open("obj/MNBClassifier.p","wb"))
#MNBClassifier = pickle.load(open("obj/MNBClassifier.p","rb"))


BNBClassifier = SklearnClassifier(BernoulliNB())
BNBClassifier.train(train_set)
print("BernoulliNB accuracy:", (nltk.classify.accuracy(BNBClassifier,test_set))*100)
pickle.dump(BNBClassifier,open("obj/BNBClassifier.p","wb"))
#BNBClassifier = pickle.load(open("obj/BNBClassifier.p","rb"))

LogisticClassifier = SklearnClassifier(LogisticRegression())
LogisticClassifier.train(train_set)
print("LogisticClassifier accuracy:", (nltk.classify.accuracy(LogisticClassifier,test_set))*100)
pickle.dump(LogisticClassifier,open("obj/LogisticClassifier.p","wb"))
#LogisticClassifier = pickle.load(open("obj/LogisticClassifier.p","rb"))

SVCClassifier = SklearnClassifier(SVC())
SVCClassifier.train(train_set)
print("SVCClassifier accuracy:", (nltk.classify.accuracy(SVCClassifier,test_set))*100)
pickle.dump(SVCClassifier,open("obj/SVCClassifier.p","wb"))
#SVCClassifier = pickle.load(open("obj/SVCClassifier.p","rb"))

LinearSVCClassifier = SklearnClassifier(LinearSVC())
LinearSVCClassifier.train(train_set)
print("LinearSVCClassifier accuracy:", (nltk.classify.accuracy(LinearSVCClassifier,test_set))*100)
pickle.dump(LinearSVCClassifier,open("obj/LinearSVCClassifier.p","wb"))
#LinearSVCClassifier = pickle.load(open("obj/LinearSVCClassifier.p","rb"))

NuSVCClassifier = SklearnClassifier(NuSVC())
NuSVCClassifier.train(train_set)
print("NuSVCClassifier accuracy:", (nltk.classify.accuracy(NuSVCClassifier,test_set))*100)
pickle.dump(NuSVCClassifier,open("obj/NuSVCClassifier.p","wb"))
#NuSVCClassifier = pickle.load(open("obj/NuSVCClassifier.p","rb"))


votedClassifier = VotedClassifier(classifier,LinearSVCClassifier,NuSVCClassifier,MNBClassifier,BNBClassifier,LogisticClassifier,SVCClassifier,)
print("votedClassifier accuracy:", (nltk.classify.accuracy(votedClassifier,test_set))*100)
print("votedClassifier prediction", votedClassifier.classify(words_cat[0][0]) ,
	 'votedClassifier confidence', (votedClassifier.confidence(words_cat[0][0])*100))
print("votedClassifier prediction", votedClassifier.classify(words_cat[1][0]) ,
	 'votedClassifier confidence', (votedClassifier.confidence(words_cat[1][0])*100))
print("votedClassifier prediction", votedClassifier.classify(words_cat[500][0]) ,
	 'votedClassifier confidence', (votedClassifier.confidence(words_cat[500][0])*100))
print("votedClassifier prediction", votedClassifier.classify(words_cat[1500][0]) ,
	 'votedClassifier confidence', (votedClassifier.confidence(words_cat[1500][0])*100))
print("votedClassifier prediction", votedClassifier.classify(words_cat[2000-1][0]) ,
	 'votedClassifier confidence', (votedClassifier.confidence(words_cat[2000-1][0])*100))


pickle.dump(votedClassifier,open("obj/votedClassifier.p","wb"))
#votedClassifier = pickle.load(open("obj/votedClassifier.p","rb"))

def sentiment(word_set):
	word_set = [w.lower() for w in word_set]
	feature_set = feature_vec(word_set,words_feature)
	return votedClassifier.classify(feature_set), votedClassifier.confidence(feature_set)

print(sentiment(['I','am','very','good','boy']))







































