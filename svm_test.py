import csv
import utils
from random import randrange
from sklearn.feature_extraction.text import TfidfVectorizer
# these files are in the format <label> <feature>:<value> <feature>:<value>
f1 = open('svm-light-doc\test_data\train.dat','w') # train data file for svm-light
f2 = open('svm-light-doc\test_data\test.dat','w') # test data file for svm-light

train_data = []
train_labels = []
test_data = []
test_labels = []


if __name__ == '__main__':

    with open('training_set.csv') as csv_file:
        reader = csv.reader(csv_file,delimiter=",",quotechar='"')               
        for row in reader:           
            train_data.append(row[1])
            if(int(row[0])==0):
                train_labels.append(-1) #since svm-light takes -1,+1 labels
            else:
                train_labels.append(row[0])                
    with open('test_set.csv') as csv_file:
        reader = csv.reader(csv_file,delimiter=",",quotechar='"')               
        for row in reader:           
                test_data.append(row[0])
     # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 use_idf=True)#
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)
    
    #writting the vectors to a file in the format acceptable for svm-light
    (a,b) = train_vectors.shape
    for i in range(a):
        f1.write(str(train_labels[i]) + ' ')
        for j in range(b):
            if(train_vectors[i,j]!=0.0):
                f1.write(str(j+1) + ':' + str(train_vectors[i,j]) + ' ')
        f1.write('\n')
        
    (l,m) = test_vectors.shape
    for i in range(l):
        f2.write(str(i) + ' ')
        for j in range(m):
            if(test_vectors[i,j]!=0.0):
                f2.write(str(j+1) + ':' + str(test_vectors[i,j]) + ' ')
        f2.write('\n')  
f1.close()
f2.close()
        
        