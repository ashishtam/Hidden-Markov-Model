class HMM:
    states = []
    symbols = []

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
        self.states = states

    def setSymbols(self, symbols):
        """
        Set HMM's symbols
        :param symbols: list
        :return: void
        """
        self.symbols = symbols

    def setInitialProbabilities(self, p):
        """
        Initial Probabilities
        :param p:
        :return:
        """
        self.initProbabilities = p

    def setTransitionProbabilites(self, t):
        """
        Transition Probabilities
        :param t:
        :return:
        """
        self.transitionProbabilites = t

    def setEmissionProbabilites(self, e):
        """
        Emission probabilities
        :param e:
        :return:
        """
        self.emissionProbabilities = e
