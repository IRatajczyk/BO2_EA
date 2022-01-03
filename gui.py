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
        self.root.geometry("1200x700")

        self.frame1 = tk.Frame(self.root, width=1200, height=700)
        self.frame2 = tk.Frame(self.root, width=1200, height=700)
        self.frame1.pack()

        self.params_label = tk.Label(self.frame1, text="PARAMS").grid(row=0, column=0, padx=10, pady=10)
        self.plot_label = tk.Label(self.frame2, text="PLOT").grid(row=0, column=0, padx=10, pady=10)

        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.subplot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame2)
        self.canvas.get_tk_widget().grid()

        # BUTTONS
        self.params_to_plot_button = tk.Button(self.frame1, text="TO PLOT", command=self.params_to_plot).grid(row=0, column=3, padx=10, pady=10)
        self.plot_to_params_button = tk.Button(self.frame2, text="TO PARMAS", command=self.plot_to_params).grid(row=0, column=3, padx=10, pady=10)
        self.start_button = tk.Button(self.frame1, text="START", command=self.start).grid(row=0, column=4, padx=10, pady=10)
        self.start_button_2 = tk.Button(self.frame2, text="START", command=self.start).grid(row=0, column=4, padx=10, pady=10)

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
        self.allow_eps_ff_stop_button = tk.Checkbutton(self.frame1, text="On/ Off", variable=self.allow_eps_ff_stop_input).grid(row=2, column=1, sticky="W")

        self.eps_ff_input = tk.StringVar(self.root)
        self.eps_ff_label = tk.Label(self.frame1, text="eps ff").grid(row=3, column=0, sticky="W")
        self.eps_ff_entry = tk.Entry(self.frame1, textvariable=self.eps_ff_input).grid(row=3, column=1, sticky="W")

        self.eps_ff_type_input = tk.StringVar(self.root)
        self.eps_ff_type_label = tk.Label(self.frame1, text="eps ff type").grid(row=4, column=0, sticky="W")
        self.eps_ff_type_entry = tk.Entry(self.frame1, textvariable=self.eps_ff_type_input).grid(row=4, column=1, sticky="W")

        self.allow_no_iter_stop_input = tk.IntVar()
        self.allow_no_iter_stop_label = tk.Label(self.frame1, text="allow no iter stop").grid(row=5, column=0, sticky="W")
        self.allow_no_iter_stop_button = tk.Checkbutton(self.frame1, text="On/ Off", variable=self.allow_no_iter_stop_input).grid(row=5, column=1, sticky="W")

        self.no_iter_input = tk.StringVar(self.root)
        self.no_iter_label = tk.Label(self.frame1, text="no iter").grid(row=6, column=0, sticky="W")
        self.no_iter_entry = tk.Entry(self.frame1, textvariable=self.no_iter_input).grid(row=6, column=1, sticky="W")

        self.allow_indifferent_population_stop_input = tk.IntVar()
        self.allow_indifferent_population_stop_label = tk.Label(self.frame1, text="allow indifferent population stop").grid(row=7, column=0, sticky="W")
        self.allow_indifferent_population_stop_button = tk.Checkbutton(self.frame1, text="On/ Off", variable=self.allow_indifferent_population_stop_input).grid(row=7, column=1, sticky="W")

        self.population_diversity_measure_input = tk.StringVar(self.root)
        self.population_diversity_measure_label = tk.Label(self.frame1, text="population diversity measure").grid(row=8, column=0, sticky="W")
        self.population_diversity_measure_entry = tk.Entry(self.frame1, textvariable=self.population_diversity_measure_input).grid(row=8, column=1, sticky="W")

        self.pop_div_eps_input = tk.StringVar(self.root)
        self.pop_div_eps_label = tk.Label(self.frame1, text="pop div eps").grid(row=9, column=0, sticky="W")
        self.pop_div_eps_entry = tk.Entry(self.frame1, textvariable=self.pop_div_eps_input).grid(row=9, column=1, sticky="W")

        self.population_number_input = tk.StringVar(self.root)
        self.population_number_label = tk.Label(self.frame1, text="population number").grid(row=10, column=0, sticky="W")
        self.population_number_entry = tk.Entry(self.frame1, textvariable=self.population_number_input).grid(row=10, column=1, sticky="W")

        # Sol
        self.problem_name_input = tk.StringVar(self.root)
        self.problem_name_label = tk.Label(self.frame1, text="problem name").grid(row=2, column=3, sticky="W")
        self.problem_name_entry = tk.Entry(self.frame1, textvariable=self.problem_name_input).grid(row=2, column=4, sticky="W")

        self.create_feasible_input = tk.IntVar()
        self.create_feasible_label = tk.Label(self.frame1, text="create feasible").grid(row=3, column=3, sticky="W")
        self.create_feasible_button = tk.Checkbutton(self.frame1, text="On/ Off", variable=self.create_feasible_input).grid(row=3, column=4, sticky="W")

        self.solution_input = tk.StringVar(self.root)
        self.solution_size_label = tk.Label(self.frame1, text="solution size").grid(row=4, column=3, sticky="W")
        self.solution_size_entry = tk.Entry(self.frame1, textvariable=self.solution_input).grid(row=4, column=4, sticky="W")

        self.L_limit_input = tk.StringVar(self.root)
        self.L_limit_label = tk.Label(self.frame1, text="L limit").grid(row=5, column=3, sticky="W")
        self.L_limit_entry = tk.Entry(self.frame1, textvariable=self.L_limit_input).grid(row=5, column=4, sticky="W")

        self.DL_limit_size_input = tk.StringVar(self.root)
        self.DL_limit_size_label = tk.Label(self.frame1, text="DL limit").grid(row=6, column=3, sticky="W")
        self.DL_limit_size_entry = tk.Entry(self.frame1, textvariable=self.DL_limit_size_input).grid(row=6, column=4, sticky="W")

        self.L0_input = tk.StringVar(self.root)
        self.L0_label = tk.Label(self.frame1, text="L0").grid(row=7, column=3, sticky="W")
        self.L0_entry = tk.Entry(self.frame1, textvariable=self.L0_input).grid(row=7, column=4, sticky="W")

        # FF
        self.name_of_fitness_function_input = tk.StringVar(self.root)
        self.name_of_fitness_function_label = tk.Label(self.frame1, text="name of fitness function").grid(row=2, column=6, sticky="W")
        self.name_of_fitness_function_entry = tk.Entry(self.frame1, textvariable=self.name_of_fitness_function_input).grid(row=2, column=7, sticky="W")

        self.learning_type_input = tk.StringVar(self.root)
        self.learning_type_label = tk.Label(self.frame1, text="learning type").grid(row=3, column=6, sticky="W")
        self.learning_type_entry = tk.Entry(self.frame1, textvariable=self.learning_type_input).grid(row=3, column=7, sticky="W")

        self.worker_cost_input = tk.StringVar(self.root)
        self.worker_cost_label = tk.Label(self.frame1, text="worker cost").grid(row=4, column=6, sticky="W")
        self.worker_cost_entry = tk.Entry(self.frame1, textvariable=self.worker_cost_input).grid(row=4, column=7, sticky="W")

        self.cost_of_death_input = tk.StringVar(self.root)
        self.cost_of_death_label = tk.Label(self.frame1, text="cost_of_death").grid(row=5, column=6, sticky="W")
        self.cost_of_death_entry = tk.Entry(self.frame1, textvariable=self.cost_of_death_input).grid(row=5, column=7, sticky="W")

        self.death_probability_input = tk.StringVar(self.root)
        self.death_probability_label = tk.Label(self.frame1, text="death_probability").grid(row=6, column=6, sticky="W")
        self.death_probability_entry = tk.Entry(self.frame1, textvariable=self.death_probability_input).grid(row=6, column=7, sticky="W")

        self.training_cost_input = tk.StringVar(self.root)
        self.training_cost_label = tk.Label(self.frame1, text="training_cost").grid(row=7, column=6, sticky="W")
        self.training_cost_entry = tk.Entry(self.frame1, textvariable=self.training_cost_input).grid(row=7, column=7, sticky="W")

        self.swabs_per_day_input = tk.StringVar(self.root)
        self.swabs_per_day_label = tk.Label(self.frame1, text="swabs_per_day").grid(row=8, column=6, sticky="W")
        self.swabs_per_day_entry = tk.Entry(self.frame1, textvariable=self.swabs_per_day_input).grid(row=8, column=7, sticky="W")

        self.delay_input = tk.StringVar(self.root)
        self.delay_label = tk.Label(self.frame1, text="delay").grid(row=9, column=6, sticky="W")
        self.delay_entry = tk.Entry(self.frame1, textvariable=self.delay_input).grid(row=9, column=7, sticky="W")

        # TODO
        self.time_series_label = tk.Label(self.frame1, text="time_series").grid(row=10, column=6, sticky="W")

        self.cost_of_non_immediate_swab_input = tk.StringVar(self.root)
        self.cost_of_non_immediate_swab_label = tk.Label(self.frame1, text="cost_of_non_immediate_swab").grid(row=11, column=6, sticky="W")
        self.cost_of_non_immediate_swab_entry = tk.Entry(self.frame1, textvariable=self.cost_of_non_immediate_swab_input).grid(row=11, column=7, sticky="W")

        self.days_for_swab_input = tk.StringVar(self.root)
        self.days_for_swab_label = tk.Label(self.frame1, text="days_for_swab").grid(row=12, column=6, sticky="W")
        self.days_for_swab_entry = tk.Entry(self.frame1, textvariable=self.days_for_swab_input).grid(row=12, column=7, sticky="W")

        self.learning_parameter_input = tk.StringVar(self.root)
        self.learning_parameter_label = tk.Label(self.frame1, text="learning_parameter").grid(row=13, column=6, sticky="W")
        self.learning_parameter_entry = tk.Entry(self.frame1, textvariable=self.learning_parameter_input).grid(row=13, column=7, sticky="W")

        # Sel
        self.type_of_selection_input = tk.StringVar(self.root)
        self.type_of_selection_label = tk.Label(self.frame1, text="type_of_selection").grid(row=16, column=0, sticky="W")
        self.type_of_selection_entry = tk.Entry(self.frame1, textvariable=self.type_of_selection_input).grid(row=16, column=1, sticky="W")

        self.elite_count_input = tk.StringVar(self.root)
        self.elite_count_label = tk.Label(self.frame1, text="elite_count").grid(row=17, column=0, sticky="W")
        self.elite_count_entry = tk.Entry(self.frame1, textvariable=self.elite_count_input).grid(row=17, column=1, sticky="W")

        self.k_input = tk.StringVar(self.root)
        self.k_label = tk.Label(self.frame1, text="k").grid(row=18, column=0, sticky="W")
        self.k_entry = tk.Entry(self.frame1, textvariable=self.k_input).grid(row=18, column=1, sticky="W")

        self.p_input = tk.StringVar(self.root)
        self.p_label = tk.Label(self.frame1, text="p").grid(row=19, column=0, sticky="W")
        self.p_entry = tk.Entry(self.frame1, textvariable=self.p_input).grid(row=19, column=1, sticky="W")

        self.proportion_input = tk.StringVar(self.root)
        self.proportion_label = tk.Label(self.frame1, text="proportion").grid(row=20, column=0, sticky="W")
        self.proportion_entry = tk.Entry(self.frame1, textvariable=self.proportion_input).grid(row=20, column=1, sticky="W")

        # X
        self.type_of_crossover_input = tk.StringVar(self.root)
        self.type_of_crossover_label = tk.Label(self.frame1, text="type_of_crossover").grid(row=16, column=3, sticky="W")
        self.type_of_crossover_entry = tk.Entry(self.frame1, textvariable=self.type_of_crossover_input).grid(row=16, column=4, sticky="W")

        self.crossover_probability_input = tk.StringVar(self.root)
        self.crossover_probability_label = tk.Label(self.frame1, text="crossover_probability").grid(row=17, column=3, sticky="W")
        self.crossover_probability_entry = tk.Entry(self.frame1, textvariable=self.crossover_probability_input).grid(row=17, column=4, sticky="W")

        self.distribution_of_cut_input = tk.StringVar(self.root)
        self.distribution_of_cut_label = tk.Label(self.frame1, text="distribution_of_cut").grid(row=18, column=3, sticky="W")
        self.distribution_of_cut_entry = tk.Entry(self.frame1, textvariable=self.distribution_of_cut_input).grid(row=18, column=4, sticky="W")

        self.alpha_distribution_input = tk.StringVar(self.root)
        self.alpha_distribution_label = tk.Label(self.frame1, text="alpha_distribution").grid(row=19, column=3, sticky="W")
        self.alpha_distribution_entry = tk.Entry(self.frame1, textvariable=self.alpha_distribution_input).grid(row=19, column=4, sticky="W")

        # Mut
        self.type_of_mutation_input = tk.StringVar(self.root)
        self.type_of_mutation_label = tk.Label(self.frame1, text="type_of_mutation").grid(row=16, column=6, sticky="W")
        self.type_of_mutation_entry = tk.Entry(self.frame1, textvariable=self.type_of_mutation_input).grid(row=16, column=7, sticky="W")

        self.mutation_probability_input = tk.StringVar(self.root)
        self.mutation_probability_label = tk.Label(self.frame1, text="mutation_probability").grid(row=17, column=6, sticky="W")
        self.mutation_probability_entry = tk.Entry(self.frame1, textvariable=self.mutation_probability_input).grid(row=17, column=7, sticky="W")

        self.my_input = tk.StringVar(self.root)
        self.mu_label = tk.Label(self.frame1, text="mu").grid(row=18, column=6, sticky="W")
        self.mu_entry = tk.Entry(self.frame1, textvariable=self.mu_label).grid(row=18, column=7, sticky="W")

        self.gamma_input = tk.StringVar(self.root)
        self.gamma_label = tk.Label(self.frame1, text="gamma").grid(row=19, column=6, sticky="W")
        self.gamma_entry = tk.Entry(self.frame1, textvariable=self.gamma_input).grid(row=19, column=7, sticky="W")

        self.mean_input = tk.StringVar(self.root)
        self.mean_label = tk.Label(self.frame1, text="mean").grid(row=20, column=6, sticky="W")
        self.mean_entry = tk.Entry(self.frame1, textvariable=self.mean_input).grid(row=20, column=7, sticky="W")

        self.std_input = tk.StringVar(self.root)
        self.std_label = tk.Label(self.frame1, text="std").grid(row=21, column=6, sticky="W")
        self.std_entry = tk.Entry(self.frame1, textvariable=self.std_input).grid(row=21, column=7, sticky="W")

        self.root.mainloop()

    def make_figure(self):
        self.subplot.clear()
        self.subplot.plot(np.arange(0, 365), np.random.randint(10, size=365))

    def params_to_plot(self):
        self.frame1.pack_forget()
        self.frame2.pack()

    def plot_to_params(self):
        self.frame2.pack_forget()
        self.frame1.pack()

    def start(self):
        print("RESULT: ", self.std_input)

        self.make_figure()
        self.canvas.draw()






a = GUI()
