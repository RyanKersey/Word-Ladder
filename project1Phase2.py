#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:12:30 2024

@author: Sriram Pemmaraju
"""

from project1Phase1 import *
from datetime import datetime
###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and it performs a breadth first search of the word network starting from
# the word source. It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Examples: 
# >>> L1 = ['added', 'aided', 'bided']
# >>> nL1 = makeNeighborLists(L1)
# >>> searchWordNetwork(L1, nL1, "aided")
# [['aided', '', 'aided'], [1, 0, 1]]
# >>> searchWordNetwork(L1, nL1, "added")
# [['', 'added', 'aided'], [0, 1, 2]]
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
# Two more examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> searchWordNetwork(L2, nL2, "tides")
# [['bides', 'tides', 'sides', 'tides', 'tides', ''], [2, 1, 2, 1, 1, 0]]
#
###############################################################################
def searchWordNetwork(wordList, nbrsList, source):
    # Initialization: processed and reached are two lists that will help in the exploration. 
    # reached: contains all words that have been reached but not processed.
    # processed: contains all words that have been reached and processed, i.e., their neighbors 
    # have also been explored.    
    reached = [source]
    processed = []
    
    # Initialization: parent lists
    parents = [""]*len(wordList)
    distances = [-1]*len(wordList)
    
    sourceIndex = getIndex(wordList, source)
    distances[sourceIndex] = 0

    # Repeat until reached set becomes empty or target is reached 
    while reached:
        currentWord = reached.pop(0)

        # Find all neighbors of this item and add new neighbors to reached
        currentWordIndex = getIndex(wordList, currentWord)
        currentNeighbors = nbrsList[currentWordIndex]
        for neighbor in currentNeighbors:
            if (neighbor not in reached) and (neighbor not in processed):
                reached.append(neighbor)
                neighborIndex = getIndex(wordList, neighbor)
                parents[neighborIndex] = currentWord
                distances[neighborIndex] = distances[currentWordIndex] + 1
                
        processed.append(currentWord)
    return [parents, distances]

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and a word called target. The function returns a shortest path
# from the source word to the target word, if there is a path between these two
# words. Otherwise, the function returns []. This function calls searchWordNetwork
# to compute the parent list and then follows the parent pointers from target 
# to source to compute a path; this path is then reversed and returned.
#
# Examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> findPath(L2, nL2, "tides", "sided")
# ['tides', 'sides', 'sided']
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findPath(L3, nL3, "curve", "taste")
# ['curve', 'curse', 'purse', 'parse', 'passe', 'paste', 'taste']
#
###############################################################################
def findPath(wordList, nbrsList, source, target):
    [parents, distances] = searchWordNetwork(wordList, nbrsList, source)
    
    targetIndex = getIndex(wordList, target)
    if parents[targetIndex] == "":
        return []
    
    else:
        path = []
        currentWord = wordList[targetIndex]
        while (currentWord != source):
            path.append(currentWord)
            index = getIndex(wordList, currentWord)
            currentWord = parents[index]
            
        path.append(source)
        path.reverse()
    return path
            
        
###############################################################################     
#
# Specification:  This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns the list of
# connected components in the word network.
#
# Definition: A connected component of a network is the set of all nodes that can
# be reached from each other via paths in the network.
#
# Examples: 
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findComponents(L3, nL3)
# [['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]   
# >>> L4 = L3 +["sided", "tided", "bided"]
# >>> L4.sort()
# >>> nL4 = makeNeighborLists(L4)
# >>> findComponents(L4, nL4)
#  [['bided', 'sided', 'tided'],
#   ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
# >>> L5 = ["abhor"] + L4
# >>> nL5 = makeNeighborLists(L5)
# >>> findComponents(L5, nL5)
# [['abhor'],
#  ['bided', 'sided', 'tided'],
#  ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
#
# Notes: 
# (a) The nodes in each connected component should appear in the same order
# as they appear in wordList. 
# (b) The components themselves should be sorted by the first word in the component.
#
###############################################################################            
def findComponents(wordList, nbrsList):
    visited = [False] * len(wordList)
    components = []
    final = []
    for i in range(len(wordList)):
        if visited[i] == False:
            component = []
            queue = [wordList[i]] 
            while len(queue) != 0:
                current_word = queue[0]
                queue.pop(0)
                word_index = getIndex(wordList,current_word)
                if visited[word_index] == False:
                    visited[word_index] = True
                    component += [current_word]
                    neighbors = nbrsList[word_index]
                    for neighbor in neighbors:
                        queue += [neighbor]
            components += [component]
    for x in range(len(components)):
        final += [sorted(components[x])]
    return final


def fastMakeNeighborLists(wordList):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    nbrsList = []
    
    for x in wordList:
        neighbors = []
        for z in alphabet:
            for i in range(5):
                newWord = x[:i] + z + x[i+1:]
                if getIndex(wordList, newWord) >= 0 and z != x[i]:
                    neighbors.append(newWord)
        nbrsList.append(neighbors)
    return nbrsList





    
    
