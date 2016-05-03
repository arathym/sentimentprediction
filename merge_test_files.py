#----- combining all the text files into the csv and also removing the punctuations------
# This program should be run inside the test folder since we are taking all the global .text files from that folder

import glob 
import string

fw = open('test_set.csv','wb') # file to which we are writing all the text files to
punc = string.punctuation # has all the punctuations

for files in glob.glob("DATA/test/test/*.txt"):  # this searches all the pathnames(like .csv,.txt) provided in the folder        
       fr = open(files,'rb') # opening the file
       data = fr.readline().translate(None, punc).lower() # removing the punctuations and converting all words to lower letters          
       fw.writelines(data + '\n') # writing the translated data to the csv file and adding new line at the end    
       
fw.close() # closing the file to which we wrote





