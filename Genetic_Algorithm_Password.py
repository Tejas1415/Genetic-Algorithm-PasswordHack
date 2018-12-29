# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Genetic Algorithm own code 
Dec'18
"""

import datetime 
import random
import numpy as np
import math

populationSize = 30;
mutationRate = 0.01;

# Full Set
geneSet = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
# Target to reach
target = "TejasK"

targetLength = len(target)

def newPopulation(targetLength, geneSet, populationSize):   # A function to generate new population for next gen(Working)

    new_pop = [0]*targetLength;                             # To start off with the algorithm    
    for i in range(0,populationSize): 
        sample2 = random.sample(geneSet, targetLength)
        new_pop = np.vstack((new_pop, sample2))
    new_pop = np.delete(new_pop, (0), axis = 0)             # Delete the initially padded zeros
    return new_pop;

def fitness(target, samp):                                  # A function to calculate the fitness(Working) 
    fit = 0;
    for i in range(0,targetLength):
        if (str(target[i]) == str(samp[i])):
            fit = fit + 1;
    return fit

# A function to find index of top n fitness scores in the newPop.
def Nmaxindex(scores, N):
    finalList = [];
    finalIndex = [];
    
    for i in range(0, N):
       max1 = 0;
       max_index = 0;
       for j in range(len(scores)):
           if scores[j] > max1:
               max1 = scores[j];
               max_index = j;
       np.delete(scores, [max_index]);
       finalIndex.append(max_index);
       finalList.append(max1);
       return finalIndex;
   

# Start the main part of the program
# let targetFound be the flag, which turns high when the target is found.
generationCount = 1; # To count and print the number of generations
targetFound = 0;
#while(targetFound != 1):
while(generationCount < 100):
    fitScore = 0; 
    fitScore1 = 0;
    num_of_genes_2mutate = math.ceil(mutationRate * targetLength);
    newPop = newPopulation(targetLength, geneSet, populationSize);    # Cross Over done
    
    #Check if target achieved, fitnessScore = targetLength
    # Fitness Step
    for i in range(0, populationSize):
        samp1 = newPop[i,:];
        fitScoretemp1 = fitness(target, samp1);
        fitScore1 = np.vstack((fitScore1,fitScoretemp1));
    fitScore1 = np.delete(fitScore1, (0), axis = 0);
    
    if(max(fitScore1) == targetLength):                          # Checking for target before mutation
        print("Target Found at generation = ", generationCount);
        targetFound = 1; # Turn Flag high
    
    # Now mutate the children in the locations where the Traget_answer is not yet found.
    # in range the last element is nt counted
    for j in range(0, populationSize):
        sample = newPop[j,:];
        for n in range(0,num_of_genes_2mutate):
            randomindex = random.randint(0,len(sample)-1);
            sample[randomindex] = random.choice(geneSet);
        newPop[j,:] = sample;
                    
    # Fitness Step
    for i in range(0, populationSize):
        samp = newPop[i,:];
        fitScoretemp = fitness(target, samp);
        fitScore = np.vstack((fitScore,fitScoretemp));
    fitScore = np.delete(fitScore, (0), axis = 0);
    
    if(max(fitScore) == targetLength):                         # Checking after mutation
        print("Target Found at generation = ", generationCount);
        targetFound = 1; # Turn Flag high
    
# Now choose 3 best fitness scores, extract their corresponding children and then form newPop from them.
    
    arr = np.array(np.transpose(fitScore))         # to extract the indices of top 3 scores
    finalArray = np.concatenate(arr.tolist())      #to remove array([[3,4,5]]) to array([3,4,5]) combine all lsits inside 
    top3parents = finalArray.argsort()[-3:][::-1];

    concatenateParents = [];
    for k in top3parents:
        concatenateParents = concatenateParents + newPop[k,:].tolist(); # putting all elements in best parents in one list (newGeneSet)
    
    arr1 = np.array(np.transpose(fitScore))         # to extract the indices of top 3 scores
    finalArray1 = np.concatenate(arr1.tolist())      #to remove array([[3,4,5]]) to array([3,4,5]) combine all lsits inside 
    bestParentIndex = finalArray1.argsort()[-1:][::-1];
    bestParent = newPop[bestParentIndex,:];
    geneSet = concatenateParents;
    
    bestParent = np.array(bestParent)
    bestParent = bestParent.tolist()    #Convert from ndarray to list to print it
    for ii in bestParent:               #  ready to print
        x = ''.join(ii)
    
    del fitScore
    del fitScore1
    del concatenateParents
    print("\nGeneration = ", generationCount, " ans = ", x)
    generationCount +=1;
    
         
        
   