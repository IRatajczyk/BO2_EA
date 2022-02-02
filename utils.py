import json
import numpy as np
from matplotlib import pyplot as plt
from BO2_EA.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from BO2_EA.TimeSeriesProcessing import TimeSeries


def load_config(config_path: str = "data/config.json") -> dict:
    with open(config_path) as file:
        data = json.load(file)
    return data


def proceed_test(EA: EvolutionaryAlgorithm, TS: TimeSeries, repeat: int = 10):
    solutions = []
    feasibility = []
    best_history = []
    average_history = []
    best_fitnesses = []
    for x in range(repeat):
        print(x)
        sol, feasible, bf = EA.proceed()
        solutions.append(sol)
        feasibility.append(feasible)
        best_history.append(EA.best_fitness_history)
        average_history.append(EA.average_fitness_history)
        best_fitnesses.append(bf)
        plt.figure()
        plt.plot(range(EA.solution_parameters.solution_size), TS.get_forecast(), label='COV19 cases prediction')
        plt.plot(range(EA.solution_parameters.solution_size), sol, label='medics needed (sol)')
        plt.grid()
        plt.legend()
        plt.ylabel("no. of people")
        plt.xlabel("week")
        plt.title("Time series - solution " + str(x + 1))
        plt.show()
        EA.clear()
    print(feasibility)
    print(best_fitnesses)
    print(np.average(best_fitnesses))
    plt.plot(np.average(best_history, axis=0), label='best')
    plt.plot(np.average(average_history, axis=0), label='average')
    plt.grid()
    plt.legend()
    plt.title("Fitness history")
    plt.show()
