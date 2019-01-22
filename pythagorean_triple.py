import numpy as np

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
    return np.power(np.choose(0,triple_array),2) + np.power(np.choose(1,triple_array),2) == np.power(np.choose(2,triple_array),2)
