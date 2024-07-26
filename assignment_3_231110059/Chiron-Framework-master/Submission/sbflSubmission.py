#!/usr/bin/env python3

import argparse
import sys
import numpy as np
import math
sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv


def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite

    '''
     print(activity_mat)
    # Density
    count = 0
    num_ones = 0
    num_rows = len(activity_mat)
    num_columns = len(activity_mat[0])

    for i in range(num_rows):
        for j in range(num_columns):
            if(activity_mat[i][j]==1):
                num_ones +=1
    print("Num ones :",num_ones)
    density = num_ones/(num_rows*num_columns)
    print("Density :" ,density)

    # Diversity
    activity_count = {}
    for activity in activity_mat:
        activity_tuple = tuple(activity)
        if activity_tuple in activity_count:
            activity_count[activity_tuple] += 1
        else:
            activity_count[activity_tuple] = 1
    
    sum = 0
    diversity = 0
    for activity,count in activity_count.items():
        sum += (count * (count-1))
    if(num_rows==1):
        diversity = 1
    else:
        diversity = 1 - (sum/(num_rows*(num_rows-1)))   
    print("Diversity : ",diversity)

    # Uniqueness
    # Transpose the matrix
    transposed_matrix = np.transpose(activity_mat)
    unique_rows, indices = np.unique(transposed_matrix, axis=0, return_index=True)
    uniqueness = len(unique_rows)/num_columns
    print("Uniqueness : ",uniqueness)

    # DDU score
    density_prime = 1 - abs(1-2*density)
    fitness_score = density_prime*diversity*uniqueness
    return -1*fitness_score
    '''


    # Ulysis
    activity_dict = {}
    num_rows = len(activity_mat)
    num_cols = len(activity_mat[0])
    print("Activity : ", activity_mat)

    # Extract Columns with their index
    for col in range(num_cols):
        list = []
        for row in range(num_rows):
            list.append(activity_mat[row][col])
        activity_dict[col] = list
    
    print("Activity_Dictionary : " , activity_dict)

    # Find Wastage Effort assume each component is faulty in some multiverse
    w_score_list = []
    for col in range(num_cols):
        w_score = 0
        for col_2 in range(num_cols):
            if(col!=col_2):
                list = []
                for row in range(num_rows):
                    list.append(activity_mat[row][col_2])
                if list==activity_dict.get(col):
                    w_score +=1
        w_score_list.append(w_score)
    
    print("W_Score : ",w_score_list)

    # Dividing W_score of each component by m-1 and summing up
    w_score_list = [x / (num_cols-1) for x in w_score_list]
    ulysis_score = np.sum(w_score_list)

    # Divide by M i.e number of component to get fitness_Score
    fitness_score = ulysis_score/num_cols
    print("Fitness Score : ",fitness_score)
    return fitness_score
   


# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """
        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        sus_score = 0
        # ToDo : implement the suspiciousness score function.

        # Find cf,cp,np and nf
        cf=0
        cp=0
        nf=0
        np=0

        for i in range(0,len(self.errorVec)):
            if(self.errorVec[i]==1 and self.activity_mat[i][comp_index]==1):
                cf += 1
            if(self.errorVec[i]==0 and self.activity_mat[i][comp_index]==1):
                cp += 1
            if(self.errorVec[i]==1 and self.activity_mat[i][comp_index]==0):
                nf += 1
            if(self.errorVec[i]==0 and self.activity_mat[i][comp_index]==0):
                np += 1

        # Ochiai Score
        # if(((cf+nf)*(cf+cp))!=0):
        #     sus_score = ( cf / (  math.sqrt((cf+nf)*(cf+cp)) )) 
        # else:
        #     sus_score=0

        # Tarantula Score
        try:
            if cf and (cp or np):
                sus_score = (cf / (cf+nf))/ (( cf /(cf+nf)) + (cp / (cp+np)))
            else:
                sus_score = 0
        except ZeroDivisionError:
            sus_score = 1
        
        # Jaccard Index
        # if (cf+cp+nf)!=0:
        #     sus_score = cf / (cf + cp + nf)
        # else:
        #     sus_score = 0
        

        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        """
        rankList = []
        # ToDo : implement rankList

        # List to store all rankList before sorting
        unsorted_rankList = []
        num_columns = len(self.activity_mat[0])

        # Getting the suspiciousness for each column
        for i in range(num_columns):
            unsorted_rankList.append(['c'+str(i+1),self.suspiciousness(i)])

        #Sorting the ranklist based on suspiciousness_score
        rankList = sorted(unsorted_rankList, key=lambda x: x[1] , reverse=True)

        # print("Activity Matrix : ", self.activity_mat)
        # print(" Error vector : ",self.errorVec)
        # print("RankList : ",rankList)

        # Getting the ranks for each component
        counter = 1
        maxe = rankList[0][1]
        for i in range(len(rankList)):
            if maxe != rankList[i][1]:
                counter += 1
                maxe = rankList[i][1]
            rankList[i][1] = counter

        print("Rank List : ",rankList)
        return rankList


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)
