import numpy as np
from matplotlib import pyplot as plt
import EvolutionaryAlgorithm
import Solution
import FitnessFunction
import Selection
import Crossover
import Mutation
import utils
import os

"""
It is worth noticing that solutions are kept in a list of lists L such that L = [solution (np.array(); size = 365) ,fitness (float)]
"""

if __name__ == "__main__":
    params = utils.load_config() if os.path.isfile("config.json") else dict()

    EA_param = EvolutionaryAlgorithm.EvolutionaryAlgorithmParameters(**params)
    EA = EvolutionaryAlgorithm.EvolutionaryAlgorithm(EA_param)

    Sol_param = Solution.SolutionParameters(**params)
    Sol = Solution.Solution(Sol_param)

    FF_param = FitnessFunction.FitnessFunctionParameters(**params)
    FF = FitnessFunction.FitnessFunction(FF_param)

    Sel_param = Selection.SelectionParameters(**params)
    Sel = Selection.Selection(Sel_param)

    X_param = Crossover.CrossoverParameters(**params)
    X = Crossover.Crossover(X_param)

    Mut_param = Mutation.MutationParameters(**params)
    Mut = Mutation.Mutation(Mut_param)

    EA.set_solution(Sol)
    EA.set_fitness_function(FF)
    EA.set_selection(Sel)
    EA.set_mutation(Mut)
    EA.set_crossover(X)

    EA.proceed()
