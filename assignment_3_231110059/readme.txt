Testcases Directory:  assignment_3_231110059\Chiron-Framework-master\ChironCore\tests

Testcases:
sbfl1.tl  and sbfl1_buggy.tl
sbfl2.tl and sbfl2_buggy.tl
sbfl3.tl and sbfl3_buggy.tl
sbfl4.tl and sbfl4_buggy.tl
sbfl5.tl and sbfl5_buggy.tl

Outputs Directory: \assignment_3_231110059\Chiron-Framework-master\ChironCore\tests
There are 5 output files for each testfiles namely: 
sbfl1_buggy_spectrum.csv
sbfl1_buggy_tests-optimized_act-mat.csv
sbfl1_buggy_tests-optimized.csv
sbfl1_buggy_tests-original_act-mat.csv
sbfl1_buggy_tests-original.csv

Commands:

To run the testcases, go into assignment_3_231110059\Chiron-Framework-master\ChironCore:

python .\chiron.py --SBFL .\tests\sbfl1.tl --buggy .\tests\sbfl1_buggy.tl -vars '[\":x\", \":y\", \":z\"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

python .\chiron.py --SBFL .\tests\sbfl2.tl --buggy .\tests\sbfl2_buggy.tl -vars '[\":x\", \":y\", \":z\" ,\":p\" ,\":e\"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

python .\chiron.py --SBFL .\tests\sbfl3.tl --buggy .\tests\sbfl3_buggy.tl -vars '[\":a\", \":b\", \":c\"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

python .\chiron.py --SBFL .\tests\sbfl4.tl --buggy .\tests\sbfl4_buggy.tl -vars '[\":x\", \":y\", \":z\", \":p\"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

python .\chiron.py --SBFL .\tests\sbfl5.tl --buggy .\tests\sbfl5_buggy.tl -vars '[\":x\", \":y\", \":z\"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True