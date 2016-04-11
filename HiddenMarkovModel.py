import ast
import sys

class HMM:
    states = []
    symbols = []
    emissionProbabilities = []
    transitionProbabilites = []
    alpha = []

    def __init__(self, string, states, symbols, initP, transP, emisP):
        self.setString(string)
        self.setStates(states)
        self.setSymbols(symbols)
        self.setInitialProbabilities(initP)
        self.setTransitionProbabilites(transP)
        self.setEmissionProbabilites(emisP)


    def setString(self, x):
        """
        Sets the string x of symbols emitted from HMM
        :param x: string
        :return: void
        """
        self.string = x;

    def setStates(self, states):
        """
        Sets the HMM's states
        :param states: list
        :return: void
        """
        self.states = self.splitString(states)

    def setSymbols(self, symbols):
        """
        Set HMM's symbols
        :param symbols: list
        :return: void
        """
        self.symbols = self.splitString(symbols)

    def setInitialProbabilities(self, p):
        """
        Initial Probabilities
        :param p:
        :return:
        """
        self.initProbabilities = self.splitString(p)

    def setTransitionProbabilites(self, t):
        """
        Transition Probabilities
        :param t:
        :return:
        """
        t = self.splitString(t)
        stLen = len(self.states)
        for i in range(0, stLen):
            self.transitionProbabilites.append(t[i*stLen:(i+1)*stLen])


    def setEmissionProbabilites(self, e):
        """
        Emission probabilities
        :param e:
        :return:
        """
        symLen = len(self.symbols)
        e = self.splitString(e)
        for i in range(0, len(self.states)):
            self.emissionProbabilities.append(e[i*symLen:(i+1)*symLen])

    def splitString(self, s):
        return s.split(' ')

    def calculateAlphaFirst(self):
        if (len(self.initProbabilities) > 0 and len(self.emissionProbabilities) > 0):
            print "Calculating initial probabilities"
            for i in range(0, len(self.states)):
                self.alpha.append(ast.literal_eval(self.initProbabilities[i]) * ast.literal_eval(self.emissionProbabilities[i][0]))
            print "I: ", self.initProbabilities, "E: " , self.emissionProbabilities
            print "alphaF: ", self.alpha

    def calculateAlpha(self):
        for c in range(1, len(self.string)):
            m = []
            for j in range(0, len(self.states)):
                mul = 0
                for i in range(0, len(self.states)):
                    # print "alpha", j, i
                    # print self.string[c-1]
                    # print self.symbols.index(self.string[c-1])
                    # print "============="
                    # print i+1,j+1, "T|", self.transitionProbabilites[i][j]
                    # print j+1,'X', "E|", self.emissionProbabilities[j][self.symbols.index(self.string[c-1])]
                    # print '1', j+1, self.alpha[i]

                    mul += float(self.transitionProbabilites[i][j]) * float(self.emissionProbabilities[j][self.symbols.index(self.string[c-1])]) * float(self.alpha[i])
                    # print mul
                    # print "=============="
                m.append(mul)
            print m
            self.alpha = m
        return self.alpha
        # # print self.alpha
        # print "Alpha: ", self.alpha
        # print "Final Probability:", sum(self.alpha)
        # print "Result: ", len(self.symbols-1), (self.alpha)[str(len(self.symbols)-1)]


    def observationProbability(self):
        self.calculateAlphaFirst()
        self.calculateAlpha()
        return sum(self.alpha)