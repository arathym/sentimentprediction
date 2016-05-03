#!/usr/bin/env
./svm_learn.exe train_data/train.dat train_data/model

./svm_classify.exe train_data/test.dat train_data/model train_data/predictions

