from kast import kachuaAST
import numpy as np
import math
import sys
import random
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')

# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        for metric_value in curr_metric:
            if metric_value not in total_metric:
                return True
        return False

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        for metric_value in curr_metric:
            if metric_value not in total_metric:
                total_metric.append(metric_value)
        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        
        # Defining Range
        min_range = -500
        max_range = +500


        # Mutation Function 1: This will jump high from -500 to 500
        def mutation_function_one(input_data, min_range, max_range):
            ran_num = np.random.randint(min_range, max_range)
            ran_sign = random.choice([-1, 1])
            for i in input_data.data.keys():
                if np.random.rand() < 0.5:
                    input_data.data[i] = ran_sign*(input_data.data[i] | ran_num)
                else:
                    input_data.data[i] = ran_sign*(input_data.data[i] ^ ran_num)
    
            return input_data

        # Mutation Function 2: This will jump mid from -100 to 100
        def mutation_function_two(input_data, min_range, max_range):
            ran_num = np.random.randint(-100, +100)
            ran_sign = random.choice([-1, 1])
            for i in input_data.data.keys():
                if np.random.rand() < 0.5:
                    input_data.data[i] = ran_sign*(input_data.data[i] & ran_num)
                else:
                    input_data.data[i] = ran_sign*(input_data.data[i] | ran_num)
    
            return input_data

        # Mutation Function 3: This will jump low from -20 to 20
        def mutation_function_three(input_data,min_range,max_range):
            ran_num = np.random.randint(-20, +20)
            ran_sign = random.choice([-1, 1])
            for i in input_data.data.keys():
                if np.random.rand() < 0.5:
                    input_data.data[i] = ran_sign*(input_data.data[i] & ran_num)
                else:
                    input_data.data[i] = ran_sign*(input_data.data[i] ^ ran_num)
    
            return input_data

        # Mutation Function 3: This will take care of edge cases
        def mutation_function_four(input_data, min_range,max_range):
            for i in input_data.data.keys():
                rand_val = np.random.rand()
                if rand_val < 0.5:
                    input_data.data[i] = 0
                elif rand_val < 0.6:
                    input_data.data[i] = -1
                elif rand_val < 0.7:
                    input_data.data[i] = 1
                elif rand_val < 0.8:
                    input_data.data[i] = min_range
                else:
                    input_data.data[i] = max_range
            return input_data

        # Choosing randomly out of above 4 functions
        conditions = [
        (lambda x: x <= 30, mutation_function_one),
        (lambda x: x <= 70, mutation_function_two),
        (lambda x: x <= 90, mutation_function_three),
        (lambda x: x > 90, mutation_function_four)
        ]
        x = random.randint(1, 100)
        for condition, mutation_function in conditions:
            if condition(x):
                input_data = mutation_function(input_data, min_range, max_range)
                break
        
        # Checking coverage
        print("Coverage percentage = {} %".format((len(coverageInfo.total_metric))*100/(len(irList)+1)))
        return input_data


# Reuse code and imports from
# earlier submissions (if any).



# Where are previous inputs are stored.
# coverage info not applicable