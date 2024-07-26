
Kachua Version Used : Kachua v5.3

Testcases Directory:  assignment_2_231110059\Chiron-Framework\KachuaCore\tests

# *_1.json is for Program P1(with hole) and *_2.json is for Program P2(without hole)

Testcases: 
eqtest1_1.tl eqtest1_2.tl
eqtest2_1.tl eqtest2_2.tl
eqtest3_1.tl eqtest3_2.tl
eqtest4_1.tl eqtest4_2.tl
eqtest5_1.tl eqtest5_2.tl
eqtest6_1.tl eqtest6_2.tl
 
Outputs Directory: assignment_2_231110059\Chiron-Framework\KachuaCore\tests\outputs

Output Contents for Each Testcase: 1-2 photos showing constraints and satisfiable or not.

Note : When we run command to generate symbolic execution the json is generated in same file that is "textData.json" Please copy
it to the "testData_2.json" for Program P2. (So run P2 program first named *_2.json)

# Command to run testcases

### TEST CASE 1
python ./kachua.py -t 100 -se ./tests/eqtest1_2.tl -d "{':x': 10,':y':20,':z':30}"
python ./kachua.py -t 100 -se ./tests/eqtest1_1.tl -d "{':x': 10,':y':20,':z':30}" -c "{':c1': 2, ':c2': 3,':c3':4}"
python ..\Submission\symbSubmission.py -b .\optimized.kw -e "['y']"

### TEST CASE 2
python ./kachua.py -t 100 -se ./tests/eqtest2_1.tl -d "{':x': 10,':y':20}" -c "{':c1': 2, ':c2': 3,':c3':4,':c4':4}"
python ./kachua.py -t 100 -se ./tests/eqtest2_2.tl -d "{':x': 10,':y':20}"
python ..\Submission\symbSubmission.py -b .\optimized.kw -e "['y']"

### TEST CASE 3
python ./kachua.py -t 100 -se ./tests/eqtest3_1.tl -d "{':x': 5, ':y': 100,':g':100}" -c "{':c1': 1, ':c2': 1,':c3':2,':c4':3,':c5':5}"   
python ./kachua.py -t 100 -se ./tests/eqtest3_2.tl -d "{':x': 5, ':y': 100,':g':100}"
python ..\Submission\symbSubmission.py -b .\optimized.kw -e "['x', 'y','g']" 

### TEST CASE 4
python ./kachua.py -t 100 -se ./tests/eqtest4_1.tl -d "{':x': 5,':y':10,':z':20}" -c "{':c1':1,':c2':2,':c3':3,':c4':4,':c5':5,':c6':10}"
python ./kachua.py -t 100 -se ./tests/eqtest4_2.tl -d "{':x': 5,':y':10,':z':20}"
python ..\Submission\symbSubmission.py -b .\optimized.kw -e "['x', 'y','z']" 

### TEST CASE 5
python ./kachua.py -t 100 -se ./tests/eqtest5_1.tl -d "{':x': 10,':y':20,':p':10,':q':10}" -c "{':c1': 2, ':c2': 3,':c3':4,':c4':4,':c5':5}"     
python ./kachua.py -t 100 -se ./tests/eqtest5_2.tl -d "{':x': 10,':y':20,':p':10,':q':10}"    
python ..\Submission\symbSubmission.py -b .\optimized.kw -e "['out']"

### TEST CASE 6
python ./kachua.py -t 100 -se ./tests/eqtest6_1.tl -d "{':x': 10,':y':20}" -c "{':c1':1,':c2':2}"   
python ./kachua.py -t 100 -se ./tests/eqtest6_1.tl -d "{':x': 10,':y':20}"
python ..\Submission\symbSubmission.py -b .\optimized.kw -e "['y']" 