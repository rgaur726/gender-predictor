def gender_features(word):
    return  {'last_letter': word[-1]}
    
gender_features('Rishabh');

namesm = []
def split_line():
    f = open('female.txt')
    m = open('male.txt')
    male1 = m.read();
    female1 = f.read();
    
import nltk 
from nltk.corpus import names            
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
#testVar = raw_input("Enter Name: ")
import random
random.shuffle(labeled_names)




train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names];
train_set, test_set = featuresets[500:], featuresets[:500];
classifier = nltk.NaiveBayesClassifier.train(train_set);


train_set = [(gender_features(n), gender) for (n, gender) in train_names];
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names];
test_set = [(gender_features(n), gender) for (n, gender) in test_names];
classifier = nltk.NaiveBayesClassifier.train(train_set);
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )



for (tag, guess, name) in sorted(errors):
   print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))

print classifier.show_most_informative_features(5)

