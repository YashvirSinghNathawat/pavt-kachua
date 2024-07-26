import copy
import math
import sys
import json
from typing import overload

sys.path.insert(0, "../ChironCore/")

import cfg.ChironCFG as cfgK
import cfg.cfgBuilder as cfgB
from lattice import  *
import ChironAST.ChironAST as ChironAST
import abstractInterpretation as AI

'''
    Class for interval domain
'''
class IntervalDomain(Lattice):

    '''Initialize abstract value'''
    def __init__(self, data):
        pass

    '''To display abstract values'''
    def __str__(self):
        pass

    '''To check whether abstract value is bot or not'''
    def isBot(self):
        pass

    '''To check whether abstract value is Top or not'''
    def isTop(self):
        pass

    '''Implement the meet operator'''
    def meet(self, other):
        pass

    '''Implement the join operator'''
    def join(self, other):
        pass

    '''partial order with the other abstract value'''
    def __le__(self, other):
        pass

    '''equality check with other abstract value'''
    def __eq__(self, other):
        pass

    '''
        Add here required abstract transformers
    '''
    pass
 

def area(a, b):  
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx>=0) and (dy>=0):
        return dx*dy  


class IntervalTransferFunction(TransferFunction):
    global var
    
    
    def __init__(self):
        pass

    def transferFunction(self, currBBIN, currBB):
        '''
            Transfer function for basic block 'currBB'
            args: In val for currBB, currBB
            Returns newly calculated values in a form of list

            This is the transfer function you write for Abstract Interpretation.
        '''
        #implement your transfer function here
        
        current_out = copy.deepcopy(currBBIN)
        
        if(currBB.__str__() == 'END' ):
            outVal = [{'OUT' : current_out['IN']}]
            return outVal
        
        if('rep_counter' in str(currBB.instrlist[0][0])):
            outVal = [{'OUT' : current_out['IN']}]
            return outVal

        # Logic For Forward Backward Right Left
        if(type(currBB.instrlist[0][0]) == ChironAST.AssignmentCommand):
            instruction = str(currBB.instrlist[0][0])
            command = str.split(instruction)[0][1:]
            value = int(str.split(instruction)[2])
            current_out['IN']['variable'][command]['min'] = value
            current_out['IN']['variable'][command]['max'] = value

        if(type(currBB.instrlist[0][0]) == ChironAST.ConditionCommand):
            if(str(currBB.instrlist[0][0]) != 'False'):
                l = len(currBB.instrlist[0][0].__str__())
                instruction = str(currBB.instrlist[0][0])[2:-1]
                variable = str.split(instruction)[0]
                operator = str.split(instruction)[1]
                value = int(str.split(instruction)[2])
                true_out = copy.deepcopy(current_out)
                false_out = copy.deepcopy(current_out)
                if operator == '>':
 
                    true_out['IN']['variable'][variable]['min'] = max(true_out['IN']['variable'][variable]['min'],value + 1)
                    false_out['IN']['variable'][variable]['max'] = min(false_out['IN']['variable'][variable]['max'] ,value)

                # Check for validacy
                flag = False
                for key,value in true_out['IN']['variable'].items():
                    if value['min']>value['max']:
                        flag = True
                if flag==True:
                    true_out['IN']['isTop'] = True

                flag = False
                for key,value in false_out['IN']['variable'].items():
                    if value['min']>value['max']:
                        flag = True
                if flag==True:
                    false_out['IN']['isTop'] = True

                outVal = [{'OUT' : true_out['IN']},{'OUT' : false_out['IN']}]
                return outVal
            else:
                outVal = [{'OUT' : current_out['IN']},{'OUT' : current_out['IN']}]
                return outVal
            
        if(type(currBB.instrlist[0][0]) == ChironAST.MoveCommand):
            instruction = str(currBB.instrlist[0][0])
            command = str.split(instruction)[0]
            value_string = str.split(instruction)[1]
            
            value_min = 0
            value_max = 0
            value = 0
            if value_string[1:] in ['a','b','c']:
                value_min = current_out['IN']['variable'][str.split(instruction)[1][1:]]['min']
                value_max = current_out['IN']['variable'][str.split(instruction)[1][1:]]['max']
            else:
                value_min = int(str.split(instruction)[1])
                value_max = int(str.split(instruction)[1])
                value = int(str.split(instruction)[1])
            
            
            if command == 'forward':
                if currBBIN['IN']['d'] == 'r':
                    current_out['IN']['x']['min'] = current_out['IN']['x']['min'] + value_min
                    current_out['IN']['x']['max'] = current_out['IN']['x']['max'] + value_max
                if currBBIN['IN']['d'] == 'l':
                    current_out['IN']['x']['min'] = current_out['IN']['x']['min'] - value_min
                    current_out['IN']['x']['max'] = current_out['IN']['x']['max'] - value_max
                if currBBIN['IN']['d'] == 't':
                    current_out['IN']['y']['min'] = current_out['IN']['y']['min'] + value_min
                    current_out['IN']['y']['max'] = current_out['IN']['y']['max'] + value_max
                if currBBIN['IN']['d'] == 'b':
                    current_out['IN']['y']['min'] = current_out['IN']['y']['min'] - value_min
                    current_out['IN']['y']['max'] = current_out['IN']['y']['max'] - value_max
            if command == 'backward':
                if currBBIN['IN']['d'] == 'r':
                    current_out['IN']['x']['min'] = current_out['IN']['x']['min'] - value_min
                    current_out['IN']['x']['max'] = current_out['IN']['x']['max'] - value_max
                if currBBIN['IN']['d'] == 'l':
                    current_out['IN']['x']['min'] = current_out['IN']['x']['min'] + value_min
                    current_out['IN']['x']['max'] = current_out['IN']['x']['max'] + value_max
                if currBBIN['IN']['d'] == 't':
                    current_out['IN']['y']['min'] = current_out['IN']['y']['min'] - value_min
                    current_out['IN']['y']['max'] = current_out['IN']['y']['max'] - value_max
                if currBBIN['IN']['d'] == 'b':
                    current_out['IN']['y']['min'] = current_out['IN']['y']['min'] + value_min
                    current_out['IN']['y']['max'] = current_out['IN']['y']['max'] + value_max
            if command == 'left':
                if currBBIN['IN']['d'] == 'r':
                    current_out['IN']['d'] = 't'
                if currBBIN['IN']['d'] == 'l':
                    current_out['IN']['d'] = 'b'
                if currBBIN['IN']['d'] == 't':
                    current_out['IN']['d'] = 'l'
                if currBBIN['IN']['d'] == 'b':
                    current_out['IN']['d'] = 'r'
            if command == 'right':
                if currBBIN['IN']['d'] == 'r':
                    current_out['IN']['d'] = 'b'
                if currBBIN['IN']['d'] == 'l':
                    current_out['IN']['d'] = 't'
                if currBBIN['IN']['d'] == 't':
                    current_out['IN']['d'] = 'r'
                if currBBIN['IN']['d'] == 'b':
                    current_out['IN']['d'] = 'l'
            

        outVal = [{'OUT' : current_out['IN']}]
        return outVal

danger = False
class ForwardAnalysis():
    global var,danger
    def __init__(self):
        self.transferFunctionInstance = IntervalTransferFunction()
        self.type = "IntervalTF"

    '''
        This function is to initialize in of the basic block currBB
        Returns a dictinary {varName -> abstractValues}
        isStartNode is a flag for stating whether currBB is start basic block or not
    '''
    def initialize(self, currBB, isStartNode):
        val = {}
        #Your additional initialisation code if any
        variables = {}
        for char in range(ord('a'), ord('z')+1):
            variable_name = chr(char)
            variables[variable_name] = {'min': -300, 'max': 300}
        if(isStartNode):
            val =  {'IN' : {'x' : {'min' : 0, 'max' : 0} , 'y' : {'min' : 0, 'max' : 0},'d':'r' , 'isTop':False ,'variable':variables}}
        return val

    #just a dummy equallity check function for dictionary
    def isEqual(self, dA, dB):
        for i in dA.keys():
            if i not in dB.keys():
                return False
            if dA[i] != dB[i]:
                return False
        return True

    '''
        Define the meet operation
        Returns a dictinary {varName -> abstractValues}
    '''
    def meet(self, predList):
        assert isinstance(predList, list)
        meetVal = {}

        count = 0
        for pred in predList:
            count+=1
        if count<=1:
            for pred in predList:
                meetVal['IN'] = pred['OUT']
            return meetVal


        x_min = -3001
        x_max = -3001
        y_min = -3001
        y_max = -3001
        a_min = -3001
        a_max = -3001
        b_min = -3001
        b_max = -3001
        c_min = -3001
        c_max = -3001
        d_min = -3001
        d_max = -3001
        e_min = -3001
        e_max = -3001
    
        d_fin = 'x'
        for pred in predList:

            if pred['OUT']['variable']['a']['min'] > pred['OUT']['variable']['a']['max']:
                continue
            
            if pred['OUT']['variable']['b']['min'] > pred['OUT']['variable']['b']['max']:
                continue

            if pred['OUT']['variable']['c']['min'] > pred['OUT']['variable']['c']['max']:
                continue
            
            # For a
            if pred['OUT']['variable']['a']['min'] <= pred['OUT']['variable']['a']['max']:
                if a_min == -3001:
                    a_min = pred['OUT']['variable']['a']['min']
                    a_max = pred['OUT']['variable']['a']['max']
                else:
                    a_min = min(a_min,pred['OUT']['variable']['a']['min'])
                    a_max = max(a_max,pred['OUT']['variable']['a']['max'])
            
            # For b
            if pred['OUT']['variable']['b']['min'] <= pred['OUT']['variable']['b']['max']:
                if b_min == -3001:
                    b_min = pred['OUT']['variable']['b']['min']
                    b_max = pred['OUT']['variable']['b']['max']
                else:
                    b_min = min(b_min,pred['OUT']['variable']['b']['min'])
                    b_max = max(b_max,pred['OUT']['variable']['b']['max'])
            
            # For c
            if pred['OUT']['variable']['c']['min'] <= pred['OUT']['variable']['c']['max']:
                if c_min == -3001:
                    c_min = pred['OUT']['variable']['c']['min']
                    c_max = pred['OUT']['variable']['c']['max']
                else:
                    c_min = min(c_min,pred['OUT']['variable']['c']['min'])
                    c_max = max(c_max,pred['OUT']['variable']['c']['max'])
            
            # For d
            if pred['OUT']['variable']['d']['min'] <= pred['OUT']['variable']['d']['max']:
                if d_min == -3001:
                    d_min = pred['OUT']['variable']['d']['min']
                    d_max = pred['OUT']['variable']['d']['max']
                else:
                    d_min = min(d_min,pred['OUT']['variable']['d']['min'])
                    d_max = max(d_max,pred['OUT']['variable']['d']['max'])

            # For e
            if pred['OUT']['variable']['e']['min'] <= pred['OUT']['variable']['e']['max']:
                if e_min == -3001:
                    e_min = pred['OUT']['variable']['e']['min']
                    e_max = pred['OUT']['variable']['e']['max']
                else:
                    e_min = min(e_min,pred['OUT']['variable']['e']['min'])
                    e_max = max(e_max,pred['OUT']['variable']['e']['max'])


            # Define for x_value
            if x_min==-3001:
                x_min = pred['OUT']['x']['min']
                x_max = pred['OUT']['x']['max']
            else:
                x_min = min(x_min,pred['OUT']['x']['min'])
                x_max = max(x_max,pred['OUT']['x']['max'])
            

            # Define for y_value
            if y_min==-3001:
                y_min = pred['OUT']['y']['min']
                y_max = pred['OUT']['y']['max']
            else:
                y_min = min(y_min,pred['OUT']['y']['min'])
                y_max = max(y_max,pred['OUT']['y']['max'])

            # Define for variables 
            if d_fin == 'x' or d_fin == pred['OUT']['d']:
                d_fin = pred['OUT']['d']
            else:
                print("\n\"--------------------------------KACHUA IS DANGER STATE---------------------------------\"")
                print("\n\"-----------------------At MEET DIRECTIONS OF PATHS IS DIFFERENT-------------------------\"")
                sys.exit()

        
        meetVal = { 'IN' : {'x' : {'min' : x_min , 'max' : x_max} , 'y' : {'min' : y_min , 'max' : y_max} , 'd' : d_fin, 'isTop':False ,'variable':{'a':{'min' : a_min, 'max' : a_max},'b':{'min' : b_min, 'max' : b_max},'c':{'min' : c_min, 'max' : c_max},'d':{'min' : d_min, 'max' : d_max},'e':{'min' : e_min, 'max' : e_max}}}}

        return meetVal

def RectIntersect(R1_topLeft,R1_bottomRight, R2_topLeft,R2_bottomRight):
    if (
        R1_topLeft[0] > R2_bottomRight[0]
        or R1_bottomRight[0] < R2_topLeft[0]
        or R1_topLeft[1] < R2_bottomRight[1]
        or R1_bottomRight[1] > R2_topLeft[1]
    ):
        return False
    else:
        return True
        

def analyzeUsingAI(irHandler):
    '''
        get the cfg outof IR
        each basic block consists of single statement
    '''
    ir = irHandler.ir
    for i in ir:
        if('__rep_counter_1' in str(i[0])):
            print("\n\"KACHUA IS UNSAFE\" :: KACHUA CAN BE INSIDE MAGARMACH'S REGION GIVEN")
            sys.exit()


    # call worklist and get the in/out values of each basic block
    abstractInterpreter = AI.AbstractInterpreter(irHandler)
    bbIn, bbOut = abstractInterpreter.worklistAlgorithm(irHandler.cfg)

    print("BBIN : ",bbIn)
    print("BBOUT :",bbOut)

    # #implement your analysis according to the questions on each basic blocks

    file = open("../ChironCore/tests/test.json","r+")
    d = json.loads(file.read())

    Mag_top_left = d['reg'][0]
    Mag_bottom_right = d['reg'][1]
    print("Mag_point_1: ",Mag_top_left)
    print("Mag_point_2: ",Mag_bottom_right)

    turtle_X_pos = list(bbOut['END'][0]['OUT']['x'].values())  
    turtle_Y_pos = list(bbOut['END'][0]['OUT']['y'] .values())
    print("turtle_X_pos: ",turtle_X_pos)
    print("turtle_Y_pos: ",turtle_Y_pos)

    top_left_user = [turtle_X_pos[0],turtle_Y_pos[1]]
    bottom_right_user = [turtle_X_pos[1],turtle_Y_pos[0]]
    print("top_left_user: ",top_left_user)
    print("bottom_right_user: ",bottom_right_user)

    isIntersection = RectIntersect(top_left_user,bottom_right_user,Mag_top_left,Mag_bottom_right)
    if isIntersection or danger:
        print("-------------------------------Kachua is in DANGER ZONE!!!!------------------------------------------------")
    else:
        print("--------------------------------Kachua is in SAFE ZONE!!!!-------------------------------------------------")


