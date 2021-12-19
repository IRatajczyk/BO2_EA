import numpy as np
from matplotlib import pyplot as plt
import EvolutionaryAlgorithm
import Solution
import FitnessFunction
import Selection
import Crossover
import Mutation

import numpy as np
from pmdarima import model_selection
import pmdarima as pm
import pandas as pd
from pandas import DataFrame
import datetime
from matplotlib import pyplot
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA


"""
It is worth noticing that solutions are kept in a list of lists L such that L = [solution (np.array(); size = 365) ,fitness (float)]
"""

EA_param = EvolutionaryAlgorithm.EvolutionaryAlgorithmParameters()
EA = EvolutionaryAlgorithm.EvolutionaryAlgorithm(EA_param)

Sol_param = Solution.SolutionParameters(DL_limit=50, L0=40)
Sol = Solution.Solution(Sol_param)

FF_param = FitnessFunction.FitnessFunctionParameters(cost_of_death=10, time_series=np.array([i for i in range(365)]))
FF = FitnessFunction.FitnessFunction(FF_param)

Sel_param = Selection.SelectionParameters()
Sel = Selection.Selection(Sel_param)

X_param = Crossover.CrossoverParameters()
X = Crossover.Crossover(X_param)

Mut_param = Mutation.MutationParameters()
Mut = Mutation.Mutation(Mut_param)

EA.set_solution(Sol)
EA.set_fitness_function(FF)
EA.set_selection(Sel)
EA.set_mutation(Mut)
EA.set_crossover(X)

EA.proceed()

