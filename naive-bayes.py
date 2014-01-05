import argparse
from os import listdir
from os.path import isfile, join
import math
import random



# Stop word list
stopWords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also',
             'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be',
             'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear',
             'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for',
             'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers',
             'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is',
             'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may',
             'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor',
             'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our',
             'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since',
             'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then',
             'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us',
             've', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which',
             'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet',
             'you', 'your']


def parseArgument():
    """
    Code for parsing arguments
    """
    parser = argparse.ArgumentParser(description='Parsing a file.')
    parser.add_argument('-d', nargs=1, required=True)
    args = vars(parser.parse_args())
    return args


def getFileContent(filename):
    input_file = open(filename, 'r')
    text = input_file.read()
    input_file.close()
    return text


def parseFile(words_dic, text, classifier, totalWords, vocabulary):
    words = text.split(" ")
    for word in words:
        word = word.strip()
        if word not in stopWords and len(word) > 0:
            totalWords[classifier] += 1
            vocabulary[classifier].add(word)

            if word in words_dic[classifier]:
                words_dic[classifier][word] += 1
            else:
                words_dic[classifier][word] = 1
    return totalWords, words_dic, vocabulary


def parseTestFile(testWordsDict, text):
    words = text.split(" ")
    for word in words:
        word = word.strip()
        if word not in stopWords and len(word) > 0:

            if testWordsDict.has_key(word):
                testWordsDict[word] += 1
            else:
                testWordsDict[word] = 1
    return testWordsDict


def calculateProb(probDict, words_dic, totalWords, vocabulary):
    #code to calculate the conditional probabilities
    vocab_union = vocabulary['pos']|vocabulary['neg']
    modV = len(vocab_union)

    for key in words_dic:

        for word in words_dic[key]:
            countWC = words_dic[key][word]
            probabilityWC = (countWC + 1.0)/(totalWords[key] + modV + 1)
            probDict[key][word] = probabilityWC
        probDict[key]["UNK"] = 1.0/(totalWords[key] + modV + 1)


def finalProb(probDict, key, testWordsDict):
    #code to calculate the final probabilities
    Pc = math.log(1./2)
    finalProbability = 0.0
    for word in testWordsDict:
        if word in probDict[key]:
            finalProbability += (testWordsDict[word] * math.log(probDict[key][word]))
        else:
            finalProbability += (testWordsDict[word] * math.log(probDict[key]["UNK"]))
    finalProbability += Pc
    return finalProbability


def GetTrainingAndTestFiles(filesPath):
    #code to get the training and testing data
    trainingFiles = []
    testFiles = []
    allFiles = [f for f in listdir(filesPath) if isfile(join(filesPath, f))]
    totalNumberOfFiles = len(allFiles)
    sample = random.sample(range(0, totalNumberOfFiles), 2*totalNumberOfFiles/3)
    for file in allFiles:
        if allFiles.index(file) in sample:
            trainingFiles.append(file)
        else:
            testFiles.append(file)
    return trainingFiles, testFiles


def main():
    args = parseArgument()
    #directory contains the link where folder with pos and neg files are kept
    directory = args['d'][0]

    iterations = range(1,4)
    ave_accuracy = 0
    for iteration in iterations:
        print "Iteration: ",iteration
        keys = ["pos", "neg"]
        #words_dic is a dictionary with word as key and its count as value under each keys pos an dneg
        words_dic = {}
        #totalWords is the variable that contains total number of words in all the files of each category i.e. pos and neg
        totalWords = {}
        probDict = {}
        vocabulary = {}
        trainingFiles = {}
        testFiles = {}
        countTestFiles = {}
        countTrainingFiles = {}
        probabilityFinal = {}

        for key in keys:
            filesPath = directory + "/" + key
            trainingFiles[key], testFiles[key] = GetTrainingAndTestFiles(filesPath)
            countTrainingFiles[key] = len(trainingFiles[key] )
            countTestFiles[key] = len(testFiles[key])

        for key in keys:
            totalWords[key] = 0
            vocabulary[key] = set()
            words_dic[key] = {}
            probDict[key] = {}
            filesPath = directory + "/" + key
            for file in trainingFiles[key]:
                filename = filesPath + "/" + file
                text = getFileContent(filename)
                totalWords, words_dic, vocabulary = parseFile(words_dic, text, key, totalWords, vocabulary)

        calculateProb(probDict,  words_dic, totalWords, vocabulary)
        correctTestFiles = {}

        for key in keys:
            correct = 0
            filesPath = directory + "/" + key
            for file in testFiles[key]:
                testWordsDict = {}
                probabilityFinal = {}
                filename = filesPath + "/" + file
                text = getFileContent(filename)
                parseTestFile(testWordsDict, text)
                for category in keys:
                    probabilityFinal[category] = finalProb(probDict, category, testWordsDict)
                #classProb = max(probabilityFinal, key=probabilityFinal.get)
                v = list(probabilityFinal.values())
                k = list(probabilityFinal.keys())
                classProb = k[v.index(max(v))]
                if key == classProb:
                    correct += 1
            correctTestFiles[key] = correct

            print "num_",key,"_test_docs: ", countTestFiles[key]
            print "num_post_training_docs: ", countTrainingFiles[key]
            print "num_",key,"_correct_docs: ", correctTestFiles[key]
        accuracy = float(correctTestFiles['pos']+correctTestFiles['neg'])/(countTestFiles['pos'] + countTestFiles['neg']) * 100
        ave_accuracy = ave_accuracy + accuracy

        print "accuracy: ",  accuracy
    print "Average Accuracy:", ave_accuracy/3

main()
