#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:12:30 2024

@author: Sriram Pemmaraju
"""
from datetime import datetime
#from project1Phase2Solution import *
from project1Phase1 import *
from project1Phase2 import *
import math
###############################################################################
#
# Specification: The function reads words from the file "words.txt" and creates and
# returns a list with these words. The words should in the same order in the list
# as they appear in the file. Each string in the list of words should be exactly
# 5 characters long.
#
# NEW: if the file word.txt is missing, this function should just return [] instead
# of causing the program to cause an exception.
#
# Examples:
# >>> L = readWords()
# >>> len(L)
# 5757
# >>> L[len(L)-1]
# 'zowie'
# >>> L[0:10]
# ['aargh',
#  'abaca',
#  'abaci',
#  'aback',
#  'abaft',
#  'abase',
#  'abash',
#  'abate',
#  'abbey',
#  'abbot']
# >>> L[1000]
# 'coney'
# >>> sorted(L)==L
# True
#
###############################################################################
def readWords():
    z = []
    try:
        x = open("words.txt","r")
        for line in x:
            z.append(line.rstrip('\n'))
    except:
        return []
    return z
    x.close()
    
###############################################################################     
#
# Specification:  This function takes a list of words and a list of file names.
# It reads from each file in the given list of file names and extracts words from
# the file. For each word in the list of words, it computes the frequency of this
# word in all the files in the given list of file names. The function returns
# the list of frequencies. The order in which frequencies appear in the frequency
# list should match the order in which words appear in the given word list. In other
# words, the frequency in slot 0 should be the frequency of smallerWordList[0],
# the frequency in slot 1 should be the frequency of smallerWordList[1], etc.
# The function should use "try and except" to gracefully deal with missing files.
# If a file is missing, it should just skip over to the next file. If all files
# are missing, then the frequency list returned should contain all 0's.
#
###############################################################################   
def computeFrequencies(smallerWordList, fileNameList):
    startTime = datetime.now()
    frequencyList = [0]*len(smallerWordList)
    count = 0
    L = wholeFrequencyList(fileNameList)
    for word in smallerWordList:
        frequencyList[count] += 1*L.count(word)
        count += 1
    return frequencyList
                    

def listOfFiveLetterWords(fileName):
    try:
        fin = open(fileName,"r", encoding="utf-8")
        letters = "abcdefghijklmnopqrstuvwxyzABDCDEFGHIJKLMNOPQRSTUVWXYZ"

        giantWordList = []
        for line in fin:
            newLine = line
            for ch in line:
                if ch not in letters:
                    newLine = newLine.replace(ch," ")
            
            wordsInThisLine = newLine.split()

            for word in wordsInThisLine:
                lowerCaseWord = word.lower()
                if len(lowerCaseWord) == 5:
                    giantWordList.append(lowerCaseWord)
        
        fin.close()
        return giantWordList
    except:
        return []

def wholeFrequencyList(fileList):
    wholeList = []
    for x in fileList:
        wholeList.extend(listOfFiveLetterWords(x))
    return wholeList

############################################################################### 
# You can add as many other functions as you want to make your code streamlined,
# readable, and efficient
############################################################################### 


############################################################################### 
# main program starts here
############################################################################### 

# STEP 1: Identify the list of words in the largest connected component
# (a) Read the list of all words in words.txt. Make sure that the 
# program exits gracefully if words.txt is not available
# (b) Build the adjacency list representation of the word network of this list of 
# words
# (c) Find all connected components of this word network
# (d) Identify the largest connected component and create a list with the words 
# in the largest connected component in sorted order
#
# Code for STEP 1 goes here
def largeConnectedComponent():
    words = readWords()
    nbrsList = fastMakeNeighborLists(words)
    components = findComponents(words, nbrsList)
    maxLength = 0
    maxIndex = 0
    index = 0
    for x in components:
        if len(x) > maxLength:
            maxLength = len(x)
            maxIndex = index
        index += 1
            
    return components[maxIndex]


# STEP 2: Compute the frequencies of all the words in the largest connected component
# and designate the p % of the words with highest frequency as "easy" words  
# (a) Create a list containing all the names of text files downloaded from Project Gutenberg
# (b) Call the function computeFrequencies to read from these files, extract words, and
# update the frequencies of the words in the largest connected component  
# (c) Read from the file parameters.txt to get the value of parameter p
# (d) Designate the most frequent  p % of these words as "easy" words and the rest
# as "hard" words 
#
# Code for STEP 2 goes here
def frequencyOfAll(componentList):
    files = ['pg84.txt','pg64317.txt','pg37106.txt','pg2701.txt','pg2641.txt','pg1342']
    frequency = computeFrequencies(componentList,files)
    return frequency

def parametersTxt():
    listOfValue = []
    try:
        file = open("parameters.txt","r")
        for line in file:
            values = line.split()
            if values:
                for val in values:
                    if val.endswith(','):
                        val = val[:-1]
                    try:
                        int_val = int(val)
                        listOfValue.append(int_val)
                    except ValueError:
                        try:
                            float_val = float(val)
                            listOfValue.append(float_val)
                        except ValueError:
                            pass
    except:
        return "paramters.txt was not found"
    return listOfValue




def hardAndEasy(frequencyList,componentList,p):
    listOfTopPercent = []
    listOfRest = []
    numberEasy = math.ceil(len(frequencyList)*(p/100))
    
    listOfFrequencyAndWords = []
    count = 0
    for x in range(len(frequencyList)):
        listOfFrequencyAndWords.append([frequencyList[x],componentList[x]])
    listOfFrequencyAndWords.sort()
    for x in listOfFrequencyAndWords:
        if count < (len(listOfFrequencyAndWords) - numberEasy):
            listOfRest.append(x[1])
        if count >= (len(listOfFrequencyAndWords) - numberEasy):
            listOfTopPercent.append(x[1])
        count += 1
    

        
    return [listOfTopPercent,listOfRest]

# STEP 3: Write into the file gameInformation.txt
# (a) Open the file "gameInformation.txt" for writing
# (b) Write the number of easy words, followed by the easy words themselves in alphabetical order
# (c) Write the number of hard words, followed by the hard words themselves in alphabetical order
# (d) Write the adjacency list representation of the word network of the largest connected component
# Make sure that everything is written into the file gameInformation.txt as per the specifications
# in the project 1 handout
#
# Code for STEP 3 goes here

def writeToGameInfo():
    start = datetime.now()
    parameters = parametersTxt()
    connectedComponent = largeConnectedComponent()
    frequency = frequencyOfAll(connectedComponent)

    hardEasy = hardAndEasy(frequency,connectedComponent,parameters[0])
    easyWords = hardEasy[0]
    hardWords = hardEasy[1]
    easyWords.sort()
    hardWords.sort()
    adjacencyList = fastMakeNeighborLists(connectedComponent)
    print(datetime.now()-start)
    
    f = open("gameInformation.txt", "x")
    f.write(str(len(easyWords)) + '\n')
    for x in easyWords:
        f.write(x + '\n')
    f.write(str(len(hardWords)) + '\n')
    for y in hardWords:
        f.write(y + '\n')
    line = ""
    for z in adjacencyList:
        for w in z:
            line += (w + " ")
        f.write(line + '\n')
        line = ""
    pass



