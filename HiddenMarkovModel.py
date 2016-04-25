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
        self.string = x

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
        """
        Calculate the alpha1 for the first character of the string
        :return:
        """
        if (len(self.initProbabilities) > 0 and len(self.emissionProbabilities) > 0):
            print "Calculating initial probabilities"
            for i in range(0, len(self.states)):
                self.alpha.append(float(self.initProbabilities[i]) * float(self.emissionProbabilities[i][0]))
            print "alpha1\t:", self.alpha

    def calculateAlpha(self):
        """
        Calculate the values of alpha from the 2nd character to the end of the string.
        :return:
        """
        for c in range(1, len(self.string)):
            m = []
            for j in range(0, len(self.states)):
                mul = 0
                for i in range(0, len(self.states)):
                    mul += float(self.transitionProbabilites[i][j]) * float(self.emissionProbabilities[j][self.symbols.index(self.string[c])]) * float(self.alpha[i])
                m.append(mul)
            print "alpha%d\t:" %(c+1), m
            self.alpha = m
        return self.alpha

    def observationProbability(self):
        """
        Returns the observation probability.
        """
        print "String: ", self.string
        print "Initial Probabilities: ", self.initProbabilities, "\nEmission Probabilities: " , self.emissionProbabilities
        print "Transition Probabilities: ", self.transitionProbabilites
        self.calculateAlphaFirst()
        self.calculateAlpha()
        print "Observation Probability: ", sum(self.alpha)