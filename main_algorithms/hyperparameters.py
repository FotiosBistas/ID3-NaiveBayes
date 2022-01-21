from getopt import getopt
import sys ,getopt
'''
Argument list should be 
Percentage of training data, approximate logs, number of vocab words, 
'''
if len(sys.argv) == 4: 
    per = float(sys.argv[1])
    approximate_logs = bool(sys.argv[2])
    number_of_vocab_words = int(sys.argv[3])
print("The percentage used will be: " + str(per))
print("Will the logs be approximated: " + str(approximate_logs))
print("The number of vocabulary keys: " + str(number_of_vocab_words))