import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Badania Operacyjne 2')
        self.root.geometry("1400x700")

        self.frame1 = tk.Frame(self.root, width=1400, height=700)
        self.frame2 = tk.Frame(self.root, width=1400, height=700)
        self.frame1.pack()

        self.params_label = tk.Label(self.frame1, text="PARAMS").grid(row=0, column=0, padx=10, pady=10)
        self.plot_label = tk.Label(self.frame2, text="PLOT").grid(row=0, column=0, padx=10, pady=10)

        # OTHERS
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.subplot = self.figure.add_subplot(211)
        self.subplot2 = self.figure.add_subplot(212)
        self.subplot.set_ylim([0, 5])
        self.subplot.set_xlim([0, 5])
        self.subplot2.set_ylim([5, 10])
        self.subplot2.set_xlim([2, 8])

        self.canvas = FigureCanvasTkAgg(self.figure, self.frame2)
        self.canvas.get_tk_widget().grid()

        # BUTTONS
        self.params_to_plot_button = tk.Button(self.frame1, text="TO PLOT", command=self.params_to_plot).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=10)
        self.plot_to_params_button = tk.Button(self.frame2, text="TO PARMAS", command=self.plot_to_params).grid(row=0,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=10)
        self.start_button = tk.Button(self.frame1, text="START", command=self.start).grid(row=0, column=4, padx=10,
                                                                                          pady=10)
        self.start_button_2 = tk.Button(self.frame2, text="START", command=self.start).grid(row=0, column=4, padx=10,
                                                                                            pady=10)

        # PARAMS LABELS
        self.ea_param_label = tk.Label(self.frame1, text="EA params").grid(row=1, column=0, sticky="W", pady=10)
        self.sol_param_label = tk.Label(self.frame1, text="Sol params").grid(row=1, column=3, sticky="W")
        self.ff_param_label = tk.Label(self.frame1, text="FF params").grid(row=1, column=6, sticky="W")
        self.sel_param_label = tk.Label(self.frame1, text="Sel params").grid(row=15, column=0, sticky="W")
        self.x_param_label = tk.Label(self.frame1, text="X params").grid(row=15, column=3, sticky="W")
        self.mut_param_label = tk.Label(self.frame1, text="Mut params").grid(row=15, column=6, sticky="W", pady=10)

        # EMPTY
        self.empty_1_label = tk.Label(self.frame1, text="").grid(row=0, column=2, sticky="W", pady=20, padx=50)
        self.empty_1_label = tk.Label(self.frame1, text="").grid(row=0, column=5, sticky="W", pady=20, padx=50)

        # EA
        self.allow_eps_ff_stop_input = tk.IntVar()
        self.allow_eps_ff_stop_label = tk.Label(self.frame1, text="allow eps ff stop").grid(row=2, column=0, sticky="W")
        self.allow_eps_ff_stop_button = tk.Checkbutton(self.frame1, text="",
                                                       variable=self.allow_eps_ff_stop_input).grid(row=2, column=1,
                                                                                                   sticky="W")

        self.eps_ff_input = tk.DoubleVar(self.root)
        self.eps_ff_input.set(1e-3)
        self.eps_ff_label = tk.Label(self.frame1, text="eps ff").grid(row=3, column=0, sticky="W")
        self.eps_ff_entry = tk.Entry(self.frame1, textvariable=self.eps_ff_input).grid(row=3, column=1, sticky="W")

        self.eps_ff_type_input = tk.StringVar(self.root)
        self.eps_ff_type_input.set('Average')
        self.eps_ff_type_label = tk.Label(self.frame1, text="eps ff type").grid(row=4, column=0, sticky="W")
        self.eps_ff_type_entry = tk.OptionMenu(self.frame1, self.eps_ff_type_input, 'Average').grid(row=4, column=1,
                                                                                                    sticky="W")

        self.allow_no_iter_stop_input = tk.IntVar()
        self.allow_no_iter_stop_input.set(1)
        self.allow_no_iter_stop_label = tk.Label(self.frame1, text="allow no iter stop").grid(row=5, column=0,
                                                                                              sticky="W")
        self.allow_no_iter_stop_button = tk.Checkbutton(self.frame1, text="",
                                                        variable=self.allow_no_iter_stop_input).grid(row=5, column=1,
                                                                                                     sticky="W")

        self.no_iter_input = tk.DoubleVar(self.root)
        self.no_iter_input.set(500)
        self.no_iter_label = tk.Label(self.frame1, text="no iter").grid(row=6, column=0, sticky="W")
        self.no_iter_entry = tk.Entry(self.frame1, textvariable=self.no_iter_input).grid(row=6, column=1, sticky="W")

        self.allow_indifferent_population_stop_input = tk.IntVar()
        self.allow_indifferent_population_stop_label = tk.Label(self.frame1,
                                                                text="allow indifferent population stop").grid(row=7,
                                                                                                               column=0,
                                                                                                               sticky="W")
        self.allow_indifferent_population_stop_button = tk.Checkbutton(self.frame1, text="",
                                                                       variable=self.allow_indifferent_population_stop_input).grid(
            row=7, column=1, sticky="W")

        self.population_diversity_measure_input = tk.StringVar(self.root)
        self.population_diversity_measure_input.set('Std of FF')
        self.population_diversity_measure_label = tk.Label(self.frame1, text="population diversity measure").grid(row=8,
                                                                                                                  column=0,
                                                                                                                  sticky="W")
        self.type_of_selection_entry = tk.OptionMenu(self.frame1, self.population_diversity_measure_input, 'Roulette',
                                                     'Std of FF', ).grid(row=8, column=1, sticky="W")

        self.pop_div_eps_input = tk.DoubleVar(self.root)
        self.pop_div_eps_input.set(1e-2)
        self.pop_div_eps_label = tk.Label(self.frame1, text="pop div eps").grid(row=9, column=0, sticky="W")
        self.pop_div_eps_entry = tk.Entry(self.frame1, textvariable=self.pop_div_eps_input).grid(row=9, column=1,
                                                                                                 sticky="W")

        self.population_number_input = tk.DoubleVar(self.root)
        self.population_number_input.set(50)
        self.population_number_label = tk.Label(self.frame1, text="population number").grid(row=10, column=0,
                                                                                            sticky="W")
        self.population_number_entry = tk.Entry(self.frame1, textvariable=self.population_number_input).grid(row=10,
                                                                                                             column=1,
                                                                                                             sticky="W")

        # Sol
        self.problem_name_input = tk.StringVar(self.root)
        self.problem_name_input.set('TSOCOV19D')
        self.problem_name_label = tk.Label(self.frame1, text="problem name").grid(row=2, column=3, sticky="W")
        self.problem_name_entry = tk.OptionMenu(self.frame1, self.problem_name_input, 'TSOCOV19D').grid(
            row=2, column=4, sticky="W")

        self.create_feasible_input = tk.IntVar()
        self.create_feasible_label = tk.Label(self.frame1, text="create feasible").grid(row=3, column=3, sticky="W")
        self.create_feasible_button = tk.Checkbutton(self.frame1, text="",
                                                     variable=self.create_feasible_input).grid(row=3, column=4,
                                                                                               sticky="W")

        self.solution_input = tk.DoubleVar(self.root)
        self.solution_input.set(356)
        self.solution_size_label = tk.Label(self.frame1, text="solution size").grid(row=4, column=3, sticky="W")
        self.solution_size_entry = tk.Entry(self.frame1, textvariable=self.solution_input).grid(row=4, column=4,
                                                                                                sticky="W")

        self.L_limit_input = tk.DoubleVar(self.root)
        self.L_limit_input.set(0)
        self.L_limit_label = tk.Label(self.frame1, text="L limit").grid(row=5, column=3, sticky="W")
        self.L_limit_entry = tk.Entry(self.frame1, textvariable=self.L_limit_input).grid(row=5, column=4, sticky="W")

        self.DL_limit_size_input = tk.DoubleVar(self.root)
        self.DL_limit_size_input.set(50)
        self.DL_limit_size_label = tk.Label(self.frame1, text="DL limit").grid(row=6, column=3, sticky="W")
        self.DL_limit_size_entry = tk.Entry(self.frame1, textvariable=self.DL_limit_size_input).grid(row=6, column=4,
                                                                                                     sticky="W")

        self.L0_input = tk.DoubleVar(self.root)
        self.L0_input.set(40)
        self.L0_label = tk.Label(self.frame1, text="L0").grid(row=7, column=3, sticky="W")
        self.L0_entry = tk.Entry(self.frame1, textvariable=self.L0_input).grid(row=7, column=4, sticky="W")

        # FF
        self.name_of_fitness_function_input = tk.StringVar(self.root)
        self.name_of_fitness_function_input.set('TimeSeriesCovidProblemNaive')
        self.name_of_fitness_function_label = tk.Label(self.frame1, text="name of fitness function").grid(row=2,
                                                                                                          column=6,
                                                                                                          sticky="W")
        self.name_of_fitness_function_entry = tk.OptionMenu(self.frame1, self.name_of_fitness_function_input,
                                                            'TimeSeriesCovidProblemNaive',
                                                            'TimeSeriesCovidProblem').grid(row=2, column=7, sticky="W")

        self.learning_type_input = tk.StringVar(self.root)
        self.learning_type_label = tk.Label(self.frame1, text="learning type").grid(row=3, column=6, sticky="W")
        # self.learning_type_entry = tk.Entry(self.frame1, textvariable=self.learning_type_input).grid(row=3, column=7,
        #                                                                                              sticky="W")

        self.worker_cost_input = tk.DoubleVar(self.root)
        self.worker_cost_input.set(50)
        self.worker_cost_label = tk.Label(self.frame1, text="worker cost").grid(row=4, column=6, sticky="W")
        self.worker_cost_entry = tk.Entry(self.frame1, textvariable=self.worker_cost_input).grid(row=4, column=7,
                                                                                                 sticky="W")

        self.cost_of_death_input = tk.DoubleVar(self.root)
        self.cost_of_death_input.set(0)
        self.cost_of_death_label = tk.Label(self.frame1, text="cost_of_death").grid(row=5, column=6, sticky="W")
        self.cost_of_death_entry = tk.Entry(self.frame1, textvariable=self.cost_of_death_input).grid(row=5, column=7,
                                                                                                     sticky="W")

        self.death_probability_input = tk.DoubleVar(self.root)
        self.death_probability_input.set(0.05)
        self.death_probability_label = tk.Label(self.frame1, text="death_probability").grid(row=6, column=6, sticky="W")
        self.death_probability_entry = tk.Entry(self.frame1, textvariable=self.death_probability_input).grid(row=6,
                                                                                                             column=7,
                                                                                                             sticky="W")

        self.training_cost_input = tk.DoubleVar(self.root)
        self.training_cost_input.set(200)
        self.training_cost_label = tk.Label(self.frame1, text="training_cost").grid(row=7, column=6, sticky="W")
        self.training_cost_entry = tk.Entry(self.frame1, textvariable=self.training_cost_input).grid(row=7, column=7,
                                                                                                     sticky="W")

        self.swabs_per_day_input = tk.DoubleVar(self.root)
        self.swabs_per_day_input.set(50)
        self.swabs_per_day_label = tk.Label(self.frame1, text="swabs_per_day").grid(row=8, column=6, sticky="W")
        self.swabs_per_day_entry = tk.Entry(self.frame1, textvariable=self.swabs_per_day_input).grid(row=8, column=7,
                                                                                                     sticky="W")

        self.delay_input = tk.DoubleVar(self.root)
        self.delay_input.set(1)
        self.delay_label = tk.Label(self.frame1, text="delay").grid(row=9, column=6, sticky="W")
        self.delay_entry = tk.Entry(self.frame1, textvariable=self.delay_input).grid(row=9, column=7, sticky="W")

        self.cost_of_non_immediate_swab_input = tk.DoubleVar(self.root)
        self.cost_of_non_immediate_swab_input.set(100)
        self.cost_of_non_immediate_swab_label = tk.Label(self.frame1, text="cost_of_non_immediate_swab").grid(row=10,
                                                                                                              column=6,
                                                                                                              sticky="W")
        self.cost_of_non_immediate_swab_entry = tk.Entry(self.frame1,
                                                         textvariable=self.cost_of_non_immediate_swab_input).grid(
            row=10, column=7, sticky="W")

        self.days_for_swab_input = tk.DoubleVar(self.root)
        self.days_for_swab_input.set(14)
        self.days_for_swab_label = tk.Label(self.frame1, text="days_for_swab").grid(row=11, column=6, sticky="W")
        self.days_for_swab_entry = tk.Entry(self.frame1, textvariable=self.days_for_swab_input).grid(row=11, column=7,
                                                                                                     sticky="W")

        self.learning_parameter_input = tk.DoubleVar(self.root)
        self.learning_parameter_input.set(0.2)
        self.learning_parameter_label = tk.Label(self.frame1, text="learning_parameter").grid(row=12, column=6,
                                                                                              sticky="W")
        self.learning_parameter_entry = tk.Entry(self.frame1, textvariable=self.learning_parameter_input).grid(row=12,
                                                                                                               column=7,
                                                                                                               sticky="W")

        # Sel
        self.type_of_selection_input = tk.StringVar(self.root)
        self.type_of_selection_input.set('Roulette')
        self.type_of_selection_label = tk.Label(self.frame1, text="type_of_selection").grid(row=16, column=0,
                                                                                            sticky="W")
        self.type_of_selection_entry = tk.OptionMenu(self.frame1, self.type_of_selection_input, 'Roulette',
                                                     'Tournament', 'Boltzmann').grid(row=16, column=1, sticky="W")

        self.elite_input = tk.IntVar()
        self.elite_input.set(1)
        self.elite_label = tk.Label(self.frame1, text="elite").grid(row=17, column=0, sticky="W")
        self.elite_button = tk.Checkbutton(self.frame1, text="", variable=self.elite_input).grid(row=17,
                                                                                                 column=1,
                                                                                                 sticky="W")
        self.truncation_input = tk.IntVar()
        self.truncation_label = tk.Label(self.frame1, text="truncation").grid(row=18, column=0, sticky="W")
        self.truncation_button = tk.Checkbutton(self.frame1, text="", variable=self.truncation_input).grid(
            row=18, column=1,
            sticky="W")

        self.elite_count_input = tk.StringVar(self.root)
        self.elite_count_input.set(10)
        self.elite_count_label = tk.Label(self.frame1, text="elite_count").grid(row=19, column=0, sticky="W")
        self.elite_count_entry = tk.Entry(self.frame1, textvariable=self.elite_count_input).grid(row=19, column=1,
                                                                                                 sticky="W")

        self.k_input = tk.DoubleVar(self.root)
        self.k_input.set(10)
        self.k_label = tk.Label(self.frame1, text="k").grid(row=20, column=0, sticky="W")
        self.k_entry = tk.Entry(self.frame1, textvariable=self.k_input).grid(row=20, column=1, sticky="W")

        self.p_input = tk.DoubleVar(self.root)
        self.p_input.set(0.7)
        self.p_label = tk.Label(self.frame1, text="p").grid(row=21, column=0, sticky="W")
        self.p_entry = tk.Entry(self.frame1, textvariable=self.p_input).grid(row=21, column=1, sticky="W")

        self.proportion_input = tk.DoubleVar(self.root)
        self.proportion_input.set(0.25)
        self.proportion_label = tk.Label(self.frame1, text="proportion").grid(row=22, column=0, sticky="W")
        self.proportion_entry = tk.Entry(self.frame1, textvariable=self.proportion_input).grid(row=22, column=1,
                                                                                               sticky="W")

        # X
        self.type_of_crossover_input = tk.StringVar(self.root)
        self.type_of_crossover_input.set('One Point')
        self.type_of_crossover_label = tk.Label(self.frame1, text="type_of_crossover").grid(row=16, column=3,
                                                                                            sticky="W")
        self.type_of_crossover_entry = tk.OptionMenu(self.frame1, self.type_of_crossover_input, 'One Point',
                                                     'Two Points', 'Average', 'Convex Combination', 'Uniform').grid(
            row=16, column=4, sticky="W")

        self.crossover_probability_input = tk.DoubleVar(self.root)
        self.crossover_probability_input.set(0.3)
        self.crossover_probability_label = tk.Label(self.frame1, text="crossover_probability").grid(row=17, column=3,
                                                                                                    sticky="W")
        self.crossover_probability_entry = tk.Entry(self.frame1, textvariable=self.crossover_probability_input).grid(
            row=17, column=4, sticky="W")

        self.distribution_of_cut_input = tk.StringVar(self.root)
        self.distribution_of_cut_input.set('Uniform')
        self.distribution_of_cut_label = tk.Label(self.frame1, text="distribution_of_cut").grid(row=18, column=3,
                                                                                                sticky="W")

        self.distribution_of_cut_entry = tk.OptionMenu(self.frame1, self.distribution_of_cut_input, 'Uniform').grid(
            row=18, column=4, sticky="W")

        self.alpha_distribution_input = tk.StringVar(self.root)
        self.alpha_distribution_input.set('Uniform')
        self.alpha_distribution_label = tk.Label(self.frame1, text="alpha_distribution").grid(row=19, column=3,
                                                                                              sticky="W")
        self.alpha_distribution_entry = tk.OptionMenu(self.frame1, self.alpha_distribution_input, 'Uniform',
                                                      'Arcsine').grid(row=19, column=4, sticky="W")

        # Mut
        self.type_of_mutation_input = tk.StringVar(self.root)
        self.type_of_mutation_input.set('Cauchy')
        self.type_of_mutation_label = tk.Label(self.frame1, text="type_of_mutation").grid(row=16, column=6, sticky="W")
        self.type_of_mutation_entry = tk.OptionMenu(self.frame1, self.type_of_mutation_input, 'Cauchy',
                                                    'Gaussian').grid(row=16, column=7, sticky="W")

        self.mutation_probability_input = tk.DoubleVar(self.root)
        self.mutation_probability_input.set(0.3)
        self.mutation_probability_label = tk.Label(self.frame1, text="mutation_probability").grid(row=17, column=6,
                                                                                                  sticky="W")
        self.mutation_probability_entry = tk.Entry(self.frame1, textvariable=self.mutation_probability_input).grid(
            row=17, column=7, sticky="W")

        self.mu_input = tk.DoubleVar(self.root)
        self.mu_input.set(0)
        self.mu_label = tk.Label(self.frame1, text="mu").grid(row=18, column=6, sticky="W")
        self.mu_entry = tk.Entry(self.frame1, textvariable=self.mu_input).grid(row=18, column=7, sticky="W")

        self.gamma_input = tk.DoubleVar(self.root)
        self.gamma_input.set(10)
        self.gamma_label = tk.Label(self.frame1, text="gamma").grid(row=19, column=6, sticky="W")
        self.gamma_entry = tk.Entry(self.frame1, textvariable=self.gamma_input).grid(row=19, column=7, sticky="W")

        self.mean_input = tk.DoubleVar(self.root)
        self.mean_input.set(0)
        self.mean_label = tk.Label(self.frame1, text="mean").grid(row=20, column=6, sticky="W")
        self.mean_entry = tk.Entry(self.frame1, textvariable=self.mean_input).grid(row=20, column=7, sticky="W")

        self.std_input = tk.DoubleVar(self.root)
        self.std_input.set(10)
        self.std_label = tk.Label(self.frame1, text="std").grid(row=21, column=6, sticky="W")
        self.std_entry = tk.Entry(self.frame1, textvariable=self.std_input).grid(row=21, column=7, sticky="W")

        self.root.mainloop()

    def make_figure(self):
        self.subplot.clear()
        self.subplot.set_ylim([0, 5])
        self.subplot.set_xlim([0, 5])
        self.subplot.scatter([float(self.std_input.get())], [float(self.mean_input.get())])

        self.subplot2.plot(np.arange(0, 365), np.random.randint(10, size=365))

    def params_to_plot(self):
        self.frame1.pack_forget()
        self.frame2.pack()

    def plot_to_params(self):
        self.frame2.pack_forget()
        self.frame1.pack()

    def start(self):
        print("RESULT: ", self.std_input.get())
        # self.result.set(str(np.random.rand(10)))
        # self.result_label.update_idletasks()
        self.make_figure()
        self.canvas.draw()

    def get_params(self):
        return {"allow_eps_ff_stop": bool(self.allow_eps_ff_stop_input.get()),
                "eps_ff": float(self.eps_ff_input.get()),
                "eps_ff_type": str(self.eps_ff_type_input.get()),
                "allow_no_iter_stop": bool(self.allow_no_iter_stop_input.get()),
                "no_iter": float(self.no_iter_input.get()),
                "allow_indifferent_population_stop": bool(self.allow_indifferent_population_stop_input.get()),
                "population_diversity_measure": str(self.population_diversity_measure_input.get()),
                "pop_div_eps": float(self.pop_div_eps_input.get()),
                "population_number": float(self.population_number_input.get()),

                "problem_name": str(self.problem_name_input.get()),
                "create_feasible": bool(self.create_feasible_input.get()),
                "solution_size": float(self.solution_input.get()),
                "L_limit": float(self.L_limit_input.get()),
                "DL_limit": float(self.DL_limit_size_input.get()),
                "L0": float(self.L0_input.get()),

                "name_of_fitness_function": str(self.name_of_fitness_function_input.get()),
                "worker_cost": float(self.worker_cost_input.get()),
                "death_probability": float(self.death_probability_input.get()),
                "cost_of_death": float(self.cost_of_death_input.get()),
                "training_cost": float(self.training_cost_input.get()),
                "swabs_per_day": float(self.swabs_per_day_input.get()),
                "delay": float(self.delay_input.get()),
                "cost_of_non_immediate_swab": float(self.cost_of_non_immediate_swab_input.get()),
                "days_for_swab": float(self.days_for_swab_input.get()),
                "delayed_cost": bool(self.delay_input.get()),
                "learning_type": str(self.learning_type_input.get()),
                "learning_parameter": float(self.learning_parameter_input.get()),

                "type_of_selection": str(self.type_of_selection_input.get()),
                "elite": bool(self.elite_input.get()),
                "truncation": bool(self.truncation_input.get()),
                "elite_count": float(self.elite_count_input.get()),
                "k": float(self.k_input.get()),
                "p": float(self.p_input.get()),
                "proportion": float(self.proportion_input.get()),

                "type_of_crossover": str(self.type_of_crossover_input.get()),
                "crossover_probability": float(self.crossover_probability_input.get()),
                "distribution_of_cut": str(self.distribution_of_cut_input.get()),
                "alpha_distribution": str(self.alpha_distribution_input.get()),

                "type_of_mutation": "Gaussian",
                "mutation_probability": float(self.mutation_probability_input.get()),
                "mu": float(self.mu_input.get()),
                "gamma": float(self.gamma_input.get()),
                "mean": float(self.mean_input.get()),
                "std": float(self.std_input.get())
                }


gui = GUI()
