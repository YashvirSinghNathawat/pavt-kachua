Testcases Directory:  assignment_4_231110059\Chiron-Framework-master\ChironCore\tests
Testcases:
test_1.tl
test_2.tl
test_3.tl
test_4.tl
test_5.tl
test_6.tl

# Variable Assumption 
Variables can be ['a','b','c','d','e']

MagarMach Region : 
!!!!-------------------Paste test_*.json values in test.json file---------------------!!!
1. First Value is TOP LEFT CORNOR
2. Second Value is BOTTOM RIGHT CORNOR
Without specified configuration, program wont work.
Files:
test_1.json
test_2.json
test_3.json
test_4.json
test_5.json
test_6.json

Commands:

To run the testcases, go into assignment_4_231110059\Chiron-Framework-master\ChironCore:

python3 chiron.py --control_flow -ai ./tests/test_1.tl

python3 chiron.py --control_flow -ai ./tests/test_2.tl

python3 chiron.py --control_flow -ai ./tests/test_3.tl

python3 chiron.py --control_flow -ai ./tests/test_4.tl

python3 chiron.py --control_flow -ai ./tests/test_5.tl

python3 chiron.py --control_flow -ai ./tests/test_6.tl
