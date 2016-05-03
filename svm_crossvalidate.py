import csv
import utils
from random import randrange
from sklearn.feature_extraction.text import TfidfVectorizer
# these files are in the format <label> <feature>:<value> <feature>:<value>
f1 = open('svm-light-doc/train_data/train.dat','w') # train data file for svm-light
f2 = open('svm-light-doc/train_data/test.dat','w') # test data file for svm-light

#function which splits the data randomly in to train and test data
def split(data, labels, splitratio):
    trainsize = int(len(data)*splitratio)
    train_data= []
    train_labels = []
    test_data = data
    test_labels = labels   
    while(len(train_data)<=trainsize):
        random_index = randrange(0,len(data))
        train_data.append(data.pop(random_index))
        train_labels.append(labels.pop(random_index)  )  
    return train_data, train_labels, test_data, test_labels   

data = []
labels = []

if __name__ == '__main__':
    with open('training_set.csv') as csv_file:
        reader = csv.reader(csv_file,delimiter=",",quotechar='"')               
        for row in reader: 
            data.append(utils.get_filtered_text(row[1])) 
            if(int(row[0])==0):
                labels.append(-1) #since svm-light takes -1,+1 labels
            else:
                labels.append(row[0])
                

    # Read the data   
    splitratio = 0.6
    train_data,train_labels,test_data,test_labels = split(data,labels,splitratio)
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
        f2.write(str(test_labels[i]) + ' ')
        for j in range(m):
            if(test_vectors[i,j]!=0.0):
                f2.write(str(j+1) + ':' + str(test_vectors[i,j]) + ' ')
        f2.write('\n')  
f1.close()
f2.close()
        
        