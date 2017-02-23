#!/usr/bin/env python3

class EndPntDes(object):
    def __init__(self, inId, inLate):
        self.cacheId = inId
        self.cacheLatency = inLate

class EndPnt(object):
    def __init__(self, inId, inLate, inDes):
        self.endId = inId
        self.dcLatency = inLate
        self.endPntDes = inDes

class Req(object):
    def __init__(self, inId, inEndId, inReqNum):
        self.videoId = inId
        self.endId = inEndId
        self.reqNum = inReqNum

class Question(object):
    def __init__(self, vNum, eNum, rNum, cNum, cSize, vSizeList, eList, rList):
        self.vNum = vNum
        self.eNum = eNum
        self.rNum = rNum
        self.cNum = cNum
        self.cSize = cSize

        self.vSizeList = vSizeList
        self.eList = eList
        self.rList = rList


def readFile(filename):
    inputFile = open(filename, 'r')

    # Read parameters
    param = inputFile.readline().split(' ')
    endPntNum = int(param[1])
    reqNum = int(param[2])
    cacheNum = int(param[3])
    cacheSize = int(param[4])

    # Get video size
    sizes = list(map(lambda x: int(x), inputFile.readline().split(' ')))

    # Read end points and their description
    endPntList = []
    for idx in range(endPntNum):
        currPnt = inputFile.readline().split(' ')
        currPnt = list(map(lambda x: int(x), currPnt))

        # Skip empty end point
        if currPnt[1] == 0:
            continue

        # Read end point description
        desList = []
        for desIdx in range(currPnt[1]):
            currDes = inputFile.readline().split(' ')
            currDes = list(map(lambda x: int(x), currDes))
            desList.append(EndPntDes(currDes[0], currDes[1]))

        # Create one end point
        endPntList.append(EndPnt(idx, currPnt[0], desList))

    # Read requests
    reqList = []
    for req in inputFile:
        currReq = list(map(lambda x: int(x), req.split(' ')))
        newReq = Req(currReq[0], currReq[1], currReq[2])
        reqList.append(newReq)

    # Create question
    question = Question(len(sizes), endPntNum, reqNum, cacheNum, cacheSize,
            sizes, endPntList, reqList)

    return question
