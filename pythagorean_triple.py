import numpy as np
import itertools

def checkPythagorasTriple(triple):
    '''
    @brief This function checks whether the triple a,b,c achieves a^2+b^2=c^2
    @param triple Triple to be checked
    @return True or False depending wether the triple is a Pythagoras Triple
    or not
    '''
    return triple[0]**2 + triple[1]**2 == triple[2]**2

def checkPythagorasTripleArray(triple_array):
    '''
    @brief Function that uses numpy to check in a vectorized way wether the triples
    in triple_array are Pythagoras triples.
    @param triple_array Numpy array with the triples to be checked
    @return Returns an array with true or false for each triple introduced
    '''
    return np.power(np.array([t[0] for t in triple_array]),2) + np.power(np.array([t[1] for t in triple_array]),2) == np.power(np.array([t[2] for t in triple_array]),2)

def discoverPythagorasTriples(limit):
    '''
    @brief Function that discovers Pythagoras triples up to the maximum value of
    limit in one of the positions a,b,c. It prints the Pythagoras triples discovered.
    @param limit Integer that represents the limit for a,b, and c
    '''
    all_choices = np.array(list(itertools.product(list(range(limit)), repeat=3)))
    results = checkPythagorasTripleArray(all_choices)
    for i in range(len(results)):
        if results[i]:
            print("The triple (" + str(all_choices[i][0]) + "," + str(all_choices[i][1]) + "," + str(all_choices[i][2]) + ") is Pythagoric")
