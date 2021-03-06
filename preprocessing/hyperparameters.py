from getopt import getopt
import sys 
'''
Argument list should be 
Percentage of training data, approximate logs, number of vocab words, 
'''

if len(sys.argv) == 4: 
    
    per = float(sys.argv[1])/100
    approximate_logs = sys.argv[2] == "True"
    number_of_vocab_words = int(sys.argv[3])
    '''
    per = 50/100
    approximate_logs = False
    number_of_vocab_words = 80
    '''
    
print("The percentage used will be: " + str(per))
print("Will the logs be approximated: " + str(approximate_logs))
print("The number of vocabulary keys: " + str(number_of_vocab_words))
