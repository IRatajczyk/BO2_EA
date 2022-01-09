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
def proceed_test(EA: EvolutionaryAlgorithm, TS, repeat = 10):
    solutions = []
    feasibility = []
    best_history = []
    average_history = []
    for x in range(repeat):
        print(x)
        sol, feasible = EA.proceed()
        solutions.append(sol)
        feasibility.append(feasible)
        best_history.append(EA.best_fitness_history)
        average_history.append(EA.average_fitness_history)
        plt.figure()
        plt.plot(range(EA.solution_parameters.solution_size), TS.get_forecast(), label='prediction')
        plt.plot(range(EA.solution_parameters.solution_size), sol, label='found solution')
        plt.grid()
        plt.legend()
        plt.title("Time series"+str(x))
        plt.show()
        EA.clear()
    print(feasibility)
    plt.plot(range(EA.get_time()), np.average(best_history, axis = 0), label='best')
    plt.plot(range(EA.get_time()), np.averag(average_history, axis = 0), label='average')
    plt.grid()
    plt.legend()
    plt.title("Fitness history")
    plt.show()



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

    proceed_test(EA,TS,10)
    print("DONE")
    # sol__ = EA.proceed()
    # print(sol__)
    # plt.plot(range(EA.get_time()), EA.best_fitness_history, label='best')
    # plt.plot(range(EA.get_time()), EA.average_fitness_history, label='average')
    # plt.grid()
    # plt.legend()
    # plt.title("Fitness history")
    # plt.show()
    # plt.figure()
    # plt.plot(range(EA.solution_parameters.solution_size), TS.get_forecast(), label='prediction')
    # plt.plot(range(EA.solution_parameters.solution_size), sol__, label='found solution')
    # plt.grid()
    # plt.legend()
    # plt.title("Time series")
    # plt.show()
    # print(EA.average_fitness_history)
