# sentimentprediction

To execute the codes python NLTK and scikit-learn should be installed

Copy the folder Sentiment Prediction to your local drive.

Now run merge_files. py in command line interface using the command:

python merge_files.py

This file merges the input data (separate positive and negative text files) into training_set.csv.Now

 run svm_crossvalidate.py by using the command: python svm_crossvalidate.py which gives two output files train.dat, test.dat inside svm-light-doc/train_data. Go into svm-light-doc directory by using command: cd svm-light-doc and run the bash file run.sh using the commands:

./run.sh. Once these commands are run, an accuracy will be calculated and shown in the terminal and a prediction file will be created inside the train_data folder. Consider values <=0 as 0(negative reviews) and values >=0 as 1(positive reviews) in the prediction file.

svm_test.py is used for testing the given test set by running command: python svm_test.py and then run the run.sh file by changing train_data inside the run.sh to test_data

Except the files inside svm-light-doc the remaining files are written by us.
