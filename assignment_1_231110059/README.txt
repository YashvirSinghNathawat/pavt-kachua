Testcases Directory:  assignment_1_231110059\Chiron-Framework\KachuaCore\tests

Testcases:
TEST1.tl
TEST2.tl
TEST3.tl
TEST4.tl
TEST5.tl

Outputs Directory: assignment_1_231110059\Chiron-Framework\KachuaCore\tests\outputs

Output Contents for Each Testcase: 1-2 photos showing inputs and final coverage.


Commands:

To run the testcases for fuzzing the inputs , go into assignment_1_231110059\Chiron-Framework\KachuaCore:

python .\kachua.py -t 100 --fuzz .\tests\TEST1.tl -d "{':x':5,':y':20,':z':0,':p':20}"
python .\kachua.py -t 100 --fuzz .\tests\TEST2.tl -d "{':x':5,':y':20}" 
python .\kachua.py -t 70 --fuzz .\tests\TEST3.tl -d "{':x':10,':y':30,':z':20,':p':10}"
python .\kachua.py -t 100 --fuzz .\tests\TEST4.tl -d "{':x':5,':y':20}" 
python .\kachua.py -t 100 --fuzz .\tests\TEST5.tl -d "{':x':10,':y':30,':z':20,':p':10}"