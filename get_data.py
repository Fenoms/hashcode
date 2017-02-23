#!/usr/bin/env python3

import data_model as dm
import pickle

pkList = ['./data/kittens.pk', './data/me_at_the_zoo.pk',
        './data/trendpkg_today.pk', './data/videos_worth_spreadpkg.pk']

def getQuestions():
    result = []
    for pk in pkList:
        pkFile = open(pk, 'rb')
        result.append(pickle.load(pkFile))
        pkFile.close()
    return result
