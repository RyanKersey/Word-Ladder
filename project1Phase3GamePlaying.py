#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 07:23:03 2024

@author: sriram
"""
from project1Phase3Preprocessing import *
import random
import time
###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It takes the 
# word network of all the words in wordList, represented as the corresponding 
# list of neighbor lists. It also takes a word called source in wordList and 
# it performs a breadth first search of the word network starting from
# the word source. In addition, it takes a list of words called easyWordList,
# all of which belong to wordList. These words have weight 0, whereas the remaining
# words have weight given by the non-negative integer parameter w.
# It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Definition: The length of a path is the sum of the number of edges in the path
# plus the sum of the weights of all the nodes in the path.
#
# Definition: The distance between a pair of nodes u and v is the length of the
# shortest path betwwen them.
#
# Notes: 
# (a) If the length of wordList is n, then the returned list contains two lists,
# each of length n.
# (b) If the returned list is [L1, L2] and a word w has index i in wordList, then
# the parent information of w is stored in L1[i] and the distance information of
# w is stored in L2[i].
# (c) The parent information of a word is "" if it is the source word or if it
# is not reachable from the source word.
# (d) The distance information for any word that is not reachable from the source
# word is -1.
#
###############################################################################
def searchWeightedWordNetwork(wordList, nbrsList, source, easyWordList, w):
    # Initialization: processed and reached are two lists that will help in the exploration. 
    # reached: contains all words that have been reached but not processed.
    # processed: contains all words that have been reached and processed, i.e., their neighbors 
    # have also been explored.    

    n = len(wordList)
    parents = ['']*n
    distances = [-1]*n
    
    queue = []
    
    source_index = wordList.index(source)

    queue.append(source_index)
    distances[source_index] = 0
    parents[source_index] = "" 
    
    
    while queue:
        current_index = queue.pop(0)
        current_word = wordList[current_index]
        
        for neighbor in nbrsList[current_index]:
            neighbor_index = wordList.index(neighbor)
            
            if neighbor in easyWordList:
                weight = 0
            else:
                weight = w
            
            new_distance = distances[current_index] + 1 + weight
            
            if distances[neighbor_index] == -1 or new_distance < distances[neighbor_index]:
                distances[neighbor_index] = new_distance
                parents[neighbor_index] = current_word
                
                queue.append(neighbor_index)
    
    return [parents, distances]

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It also takes a word 
# called source in wordList and a list of distances of all nodes in wordList
# from this network. It returns a list of words, in aphabetical order,
# that are between distance d1 and d2 from source (inclusive of d1 and d2).
# You can assume that d1 and d2 are non-negative integers and d1 <= d2. 
#
# You can assume that distanceList has been produced by a call to searchWordNetwork
# or searchWeightedWordNetwork. 
#
###############################################################################
def wordsAtDistanceRange(wordList, source, distanceList, d1, d2):
    wordsInRange = []
    count = 0
    for number in distanceList:
        if number >= d1 and number <= d2:
            wordsInRange.append(wordList[count])
        count += 1
    return wordsInRange

###############################################################################
# Main program

# Read parameters.txt; use default values if parameters.txt is missing
# The paremeters.txt file has the format:
#   p = value1
#   w = value2
#   ed1 = value3, ed2 = value4
#   hd1 = value5, hd2 = value6
#   eh = value7, hh = value8
#   r = value9
# ADD CODE HERE. Ideally, this should be a fuction call

parameters = parametersTxt()


# Read gameInformation.txt 
# Create easyWordList, hardWordList, wordList, nbrsList
# if gameInformation.txt is missing, provide a message to the user and construct all these lists
# from scratch.
# ADD CODE HERE. Ideally, this should be a function call

easyWordList = []
hardWordList = []
wordList = []
nbrsList = []
fin = open("gameInformation.txt","r")
easyListLen = int(fin.readline())
for x in range(easyListLen):
    word = fin.readline()
    easyWordList.append(word.strip())
hardListLen = int(fin.readline())
for y in range(hardListLen):
    word = fin.readline()
    hardWordList.append(word.strip())
wordList = easyWordList + hardWordList
wordList.sort()
for z in range(len(wordList)):
    string = fin.readline()
    nbrsList.append(string.strip().split())

# Start initial user interaction
# Welcome them to the game and ask them to pick game playing mode.
# E for "easy mode" and H for "hard mode"
# ADD CODE HERE
random.seed()
print("Welcome to word-links!")

# Once user has picked a mode, initialize parameter values for the game.
# (a) [d1, d2] = [ed1, ed2] for easy mode, [d1, d2] = [hd1, hd2] for hard mode
# (b) numWordHints = eh for easy mode, numWordHints = hh for hard mode 
# (c) distanceHintRate = r
# ADD CODE HERE

# In the easy mode, pick a random word from easyWordList
# In the hard mode, pick a random word from wordList
# This is your target word.
# ADD CODE HERE
userMode = ""
while userMode != 'E' and userMode != 'H':
    userMode = input("Would you like to play easy or hard mode? Type E (for Easy) or H (for Hard)\n")
    if userMode == 'E':
        d1 = parameters[2]
        d2 = parameters[3]
        numWordHints = parameters[6]
        distanceHintRate = parameters[8]
        target = easyWordList[random.randrange(len(easyWordList))]
        network = searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, parameters[1])
        break

    if userMode == 'H':
        d1 = parameters[4]
        d2 = parameters[5]
        numWordHints = parameters[7]
        distanceHintRate = parameters[8]
        target = wordList[random.randrange(len(wordList))]
        network = searchWordNetwork(wordList, nbrsList, target)
        break

# (a) Call searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, w) 
# to get parentList and distanceList
# (b) Call wordsAtDistanceRange(wordList, target, distanceList, d1, d2)
# to obtain all words at distance in the range [d1, d2] from target.
# Pick a word at random from this list; this is your source word
# ADD CODE HERE

network = searchWeightedWordNetwork(wordList,nbrsList,target, easyWordList, parameters[1])
parentList = network[0]
distanceList = network[1]
distanceRange = wordsAtDistanceRange(wordList,target, distanceList, d1, d2)
source = distanceRange[random.randrange(len(distanceRange))]
# Start main user interaction
# Provide the source word and target word. Ask the user to complete the word ladder
# from source word to target word. Let them know if they need to type the source word 
# and target word also. Inform them that they can type "Q" to quit the game at any 
# point and "H" if they want a next word hint.
# MAke sure messsages are clear. For example, you could use:
# "Excellent!" if the next word they type is a valid word in the ladder
# "Not a word in my dictionary!" if the next word they typs is not a word in wordList
# "The ladder can't go from xxxxx to yyyyy!" if the current word yyyyy is not a neighbor 
# of the previous word "xxxxx"
# ADD CODE HERE
path = findPath(wordList,nbrsList,source,target)
print("Your starting word is",source)
time.sleep(0.25)
print("Your ending word is",target)
time.sleep(0.25)
print("You do not need to include the starting word but do need to type the ending word in your ladder")
print("Also type next word, to skip to the next word in the ladder (You only get",numWordHints,"Hints)")
userWord = ''
currentWord = source
current = False
won = False
stepsLeft = len(path)-1
totalHints = 0
currentIndex = 0
guessPath = [source]
while userWord != "Q" and not won:
    if random.randrange(1,10) <= distanceHintRate*10:
        print("Hint: You have:",stepsLeft,"steps left")
    userWord = input("Enter the next step:")
    if userWord == "next word" and totalHints < numWordHints:
        print("The next word is:",path[currentIndex+1])
        currentWord = path[currentIndex+1]
        totalHints += 1
        currentIndex += 1
        stepsLeft = stepsLeft - 1
        guessPath.append(currentWord)
    if totalHints >= numWordHints and userWord == "next word":
        print("Out of Hints!")
    if userWord in wordList:
        if userWord not in nbrsList[getIndex(wordList,currentWord)]:
            print("The ladder can't go from",currentWord,"to",userWord,"!")
        else:
            current = True
        if (userWord in path) and (userWord in nbrsList[getIndex(wordList,currentWord)]) and userWord not in guessPath:
            print("Excellent!")
            currentIndex += 1
            stepsLeft = stepsLeft - 1
        guessPath.append(userWord)
    elif userWord != "Q" and userWord != "next word":
        print("Not a word in my dictionary!")
    if (userWord in path) and (userWord in nbrsList[getIndex(wordList,currentWord)]) and (userWord == target):
        print("Congrats, you win!")
        won = True
    if current:
        currentWord = userWord
        current = False
        




