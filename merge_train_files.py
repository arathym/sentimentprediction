import glob, string

def main():
  punc = string.punctuation # has all the punctuations
  fw = open('training_set.csv', 'w')
  for files in glob.glob("DATA/train/train/pos/*.txt"):  # this searches all the pathnames(like .csv,.txt) provided in the folder
         fr = open(files,'rb') # opening the file
         data = fr.readline().translate(None, punc).lower() # removing the punctuations and converting all words to lower letters
         fw.writelines(str(1) + ',' + data + '\n') # writing the translated data to the csv file and adding new line at the end
  for files in glob.glob("DATA/train/train/neg/*.txt"):  # this searches all the pathnames(like .csv,.txt) provided in the folder
         fr = open(files,'rb') # opening the file
         data = fr.readline().translate(None, punc).lower() # removing the punctuations and converting all words to lower letters
         fw.writelines(str(0) + ',' + data + '\n') # writing the translated data to the csv file and adding new line at the end
  fw.close() # closing the file to which we wrote




if __name__ == '__main__':
  main()
