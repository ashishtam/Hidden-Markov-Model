# Author: Ashish Tamrakar
# Date: April 10, 2016
# Python: 2.7.10
#######################################################################
# Observation Probability
# Hidden Markov Model
# Input
# 1. A string of symbols emitted from HMM (xzyyzzyzyy)
# 2. HMM's states (A B)
# 3. Symbols (x y z)
# 4. Initial Probabilities (0.5 0.5)
# 5. Transitions Probabilities ( 0.303 0.697, 0.831 0.169 )
# 6. Emission Probabilities ( 0.533 0.065 0.402, 0.342 0.334 0.324 )
# Output
# Probability of string 1.10055103197e-06
#######################################################################

import HiddenMarkovModel as hmm

# s = "xzyyzzyzyy"
# states = "A B"
# symbols = "x y z"
# initP = "0.5 0.5"
# transP = "0.303 0.697 " \
#         "0.831 0.169"
# emisP = "0.533 0.065 0.402 " \
#         "0.342 0.334 0.324"

s = "xxz"
states = "S1 S2 S3"
symbols = "x y z"
initP = "0.5 0.5 0"
transP = "0 0.333 0.667 " \
        "0.333 0 0.667 " \
        "0.333 0.333 0.333"
emisP = "0.5 0.5 0 " \
        "0 0.5 0.5 " \
        "0.5 0 0.5"

h = hmm.HMM(s, states, symbols, initP, transP, emisP)
print "Observation Probability: ", h.observationProbability()