#!/usr/bin/env python3

import data_model as dm
import pickle

fileList = ['./data/kittens.in', './data/me_at_the_zoo.in',
        './data/trending_today.in', './data/videos_worth_spreading.in']

def createPickle():
    for f in fileList:
        question = dm.readFile(f)
        pkName = './data/' + f.split('/')[2].split('.')[0] + '.pk'
        pkFile = open(pkName, 'wb')
        pickle.dump(question, pkFile)
        pkFile.close()


if __name__ == '__main__':
    createPickle()
