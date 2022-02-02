from timeit import timeit

import numpy as np
from matplotlib import pyplot as plt
import EvolutionaryAlgorithm
import Solution
import FitnessFunction
import Selection
import Crossover
import Mutation
import HybridOptimizer
import utils
import os
import TimeSeriesProcessing

"""
Cogito cogito ergo cogito sum.
"""


"""
It is worth noticing that solutions are kept in a list of lists L such that L = [solution (np.array(); size = 365) ,fitness (float)]
"""

if __name__ == "__main__":
    TS_param = TimeSeriesProcessing.TimeSeriesProcessingParameters(model_type="ARIMA")
    TS = TimeSeriesProcessing.TimeSeries(TS_param)

    params = utils.load_config() if os.path.isfile("data/config.json") else dict()
    params["time_series"] = TS.get_forecast()

    EA_param = EvolutionaryAlgorithm.EvolutionaryAlgorithmParameters(**params)
    EA = EvolutionaryAlgorithm.EvolutionaryAlgorithm(EA_param)

    Sol_param = Solution.SolutionParameters(**params)
    Sol = Solution.Solution(Sol_param)

    FF_param = FitnessFunction.FitnessFunctionParameters(**params)
    FF = FitnessFunction.FitnessFunction(FF_param, Sol)

    Sel_param = Selection.SelectionParameters(**params)
    Sel = Selection.Selection(Sel_param)

    X_param = Crossover.CrossoverParameters(**params)
    X = Crossover.Crossover(X_param)

    Mut_param = Mutation.MutationParameters(**params)
    Mut = Mutation.Mutation(Mut_param)

    Hybrid_param = HybridOptimizer.HybridOptimizerParameters(**params)
    H = HybridOptimizer.HybridOptimizer(Hybrid_param, Sol, FF)

    EA.set_solution(Sol)
    EA.set_fitness_function(FF)
    EA.set_selection(Sel)
    EA.set_mutation(Mut)
    EA.set_crossover(X)
    EA.set_hybrid_optimizer(H)

    utils.proceed_test(EA, TS, 10)
    print("DONE")