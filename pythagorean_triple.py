import numpy as np

def checkPythagorasTriple(triple):
    '''
    @brief This function checks whether the triple a,b,c achieves a^2+b^2=c^2
    @param triple Triple to be checked
    @return True or False depending wether the triple is a Pythagoras Triple
    or not
    '''
    return triple[0]**2 + triple[1]**2 == triple[2]**2
