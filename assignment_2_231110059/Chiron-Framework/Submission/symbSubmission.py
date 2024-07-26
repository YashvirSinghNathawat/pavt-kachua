from z3 import *
import argparse
import json
import sys
import re


sys.path.insert(0, '../KachuaCore/')

from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))

def checkEq(args,ir):

    # output = args.output
    # example(s)
    # TODO: write code to check equivalence

    # Reading File 1
    file1 = open("../Submission/testData.json","r+")
    testData=json.loads(file1.read())
    file1.close()
    s = zs.z3Solver()
    testData = convertTestData(testData) 

    # Reading File 2
    file2 = open("../Submission/testData_2.json","r+")
    testData_2=json.loads(file2.read())
    file2.close()
    s = zs.z3Solver()
    testData_2 = convertTestData(testData_2) 

    # Output Variables
    outputs_var = args.output
    

    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = [Int(char) for char in 'abcdefghijklmnopqrstuvwxyz']
    c1 , c2 ,c3, c4,c5,c6  = [Int(i) for i in ['c1','c2','c3','c4','c5','c6']]

    # Extract inputs and outputs from p1
    inputs = []
    outputs = []
    for key,value in testData_2.items():
        inputs.append(value["params"])
        outputs.append(value["symbEnc"])
    print(inputs)
    print(outputs)


    # Extract constraints and SymbEnc
    constraints = []
    symbEnc = []
    for key,value in testData.items():
        const_split = value["constraints"][0].split(',')
        constraints.append(const_split)
        symbEnc.append(value["symbEnc"])
    print("Constraints_P2 : ",constraints)
    print("SymbEnc_P2 ", symbEnc)

    # Iterate over input and satisfy conditions
    conditions = []
    for i, input_set in enumerate(inputs):
        # Add all Constraint
        for j,const_list in enumerate(constraints):
            s1 = zs.z3Solver()
            # Add all Symbol variables
            for key in symbEnc[i].keys():
                s1.addSymbVar(key)
            # Add all inputs of input_set
            for key,value in input_set.items():
                s1.addConstraint("{}=={}".format(key,value))
            for const in const_list:
                s1.addConstraint(const)
            res = s1.s.check()
            print(res)
            print("Solution is : {}".format("Satisfiable" if str(res)=="sat" else "UnSatisfiable"))
            if str(res)=="sat":
                print(input_set,const)
                print(outputs[i])
                print(symbEnc[j])

                condition = [] 
                for out_var in outputs_var:
                    condition.append(("{}=={}".format(outputs[i][out_var],symbEnc[j][out_var])))
                
                for key,value in input_set.items():
                    for i,cond in enumerate(condition):
                        condition[i] = cond.replace(key,"{}".format(value))
                conditions.extend(condition)


                    
    # Adding all Constraints to z3 Solver
    print("Conditions : ",conditions)
    s =  zs.z3Solver()
    for const in conditions:
        s.addConstraint(const)
    
    #Printing all conditions
    print("----" * 20)
    print("Assertions : ")
    print(s.s.assertions()) 
    print("----" * 20)
    res = s.s.check()
    print(res)

    #Checking satisfiability and modelling answer
    print("Solution is : {}".format("Satisfiable" if str(res)=="sat" else "UnSatisfiable"))
    if str(res)=="sat":
        m = s.s.model()
        print("Value of Constant Params : ",m)



    
            



if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
