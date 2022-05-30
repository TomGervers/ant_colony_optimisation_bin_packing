"""
    Python program to find the the fitness values for bin packing problems with set number of bins using the ant
    colony optimisation algorithm.
"""


"""
    Import external modules used.
"""
import random
import numpy as np
import time


'''
    Finds the best fitness for the ant colony optimisation algorithm for the bin packing problem 1. Fitness is the
    difference between the sum of values in the maximum and minimum bins.

    :param paths: the number of paths as an int.
    :param evaporation_rate: the rate at which nodes evaporate.
    :returns: The fitness value of the best path found.
'''
def ACOBPP1(paths, evaporation_rate):
    # Set the parameters for BPP1.
    bins = 10 # Number of bins set to 10.
    items = [i + 1 for i in range(500)] # Items set as every value from 1 to 500.
    fitness_evaluations = 10000 # The number of fitness evaluations is set to 10,000.

    # Randomly distribute the pheromones on each of the nodes that the ant can take through the bins.
    pheromone_paths = [[random.uniform(0,1) for i in range(len(items))] for x in range(bins)]

    fitness_best = sum(items) # Best at start is set to the sum of all the values as this is the worst possible outcome.
    min_bins = [] # List that stores the bins that at which the best fitness is found.

    runthroughs = int(fitness_evaluations / paths) # Calculate number of times to run through so that the 10,000
                                                   # fitness evaluations have been carried out.
    
    for run_num in range(runthroughs): # For each run in the required number of runthroughs.

        fitness_list = [] # List of all the fitness values calculated.
        path_list = [] # List of all the paths taken by the ant.

        for path in range(paths): # Iterate through each path in the required number of paths.
            
            path = choosePath(items, pheromone_paths, bins) # Uses the choosePath function to find the path used.

            path_list.append(path) # Add this path to the list of paths.

            curr_bin_list = [0 for y in range(bins)] # Set weight of all bins to 0.
            for i in range(len(path)): # For every bin
                curr_bin_list[path[i]] += items[i] # Add the weight of the item to the correct bin for each path stage.

            fitness_list.append(max(curr_bin_list) - min(curr_bin_list)) # Calculate the fitness value for this path.

        curr_path = 0 # Store the current path.
        for path in path_list: # For every path.

            curr_path_node = 0 # Set the current node of the path to 0.
            pheromone_update = (100 / fitness_list[curr_path]) # Calculate the overall fitness of the current path.

            for decision in path: # For every decision made in the path.
                pheromone_paths[decision][curr_path_node] += pheromone_update # Update the pheromone.
                curr_path_node += 1 # Iterate current path node by 1.

            curr_path += 1 # Iterate current path by 1.
            run_num += 1 # Iterate run number by 1.

        pheromone_paths = evaporatePheromones(pheromone_paths, evaporation_rate) # Evaporate all pheromones.

        # Checking if the fitness for this iteration is better than the global best (not used for actual result)
        if (max(curr_bin_list) - min(curr_bin_list)) < fitness_best: # If current fitness better than best fitness.
            min_bins = curr_bin_list # Set list of minimum bins to current bin list.
            fitness_best = (max(curr_bin_list) - min(curr_bin_list)) # Set best as the current value.
            #print("New found with bins:", min_bins, 'as fitness value:', fitness_best) # Print update.

    #print(min_bins) # Print list of minimum bins.
    return fitness_best # Return the best fitness value.


'''
    Finds the best fitness for the ant colony optimisation algorithm for the bin packing problem 2. Fitness is the
    difference between the sum of values in the maximum and minimum bins.

    :param paths: the number of paths as an int.
    :param evaporation_rate: the rate at which nodes evaporate.
    :returns: The fitness value of the best path found.
'''
def ACOBPP2(paths, evaporation_rate):
    # Set the parameters for BPP2.  
    bins = 50 # Number of bins set to 50.
    items = [((i+1) ** 2 / 2) for i in range(500)] # Items set as every value from 1 to 500.
    fitness_evaluations = 10000 # The number of fitness evaluations is set to 10,000.

    # Randomly distribute the pheromones on each of the nodes that the ant can take through the bins.
    pheromone_paths = [[random.uniform(0,1) for i in range(len(items))] for x in range(bins)]

    fitness_best = sum(items) # Best at start is set to the sum of all the values as this is the worst possible outcome.
    min_bins = [] # List that stores the bins that at which the best fitness is found.

    runthroughs = int(fitness_evaluations / paths) # Calculate number of times to run through so that the 10,000
                                                   # fitness evaluations have been carried out.
    
    for run_num in range(runthroughs): # For each run in the required number of runthroughs.

        fitness_list = [] # List of all the fitness values calculated.
        path_list = [] # List of all the paths taken by the ant.

        for path in range(paths): # Iterate through each path in the required number of paths.
            
            path = choosePath(items, pheromone_paths, bins) # Uses the choosePath function to find the path used.

            path_list.append(path) # Add this path to the list of paths.

            curr_bin_list = [0 for y in range(bins)] # Set weight of all bins to 0.
            for i in range(len(path)): # For every bin
                curr_bin_list[path[i]] += items[i] # Add the weight of the item to the correct bin for each path stage.

            fitness_list.append(max(curr_bin_list) - min(curr_bin_list)) # Calculate the fitness value for this path.

        curr_path = 0 # Store the current path.
        for path in path_list: # For every path.

            curr_path_node = 0 # Set the current node of the path to 0.
            pheromone_update = (100 / fitness_list[curr_path]) # Calculate the overall fitness of the current path.

            for decision in path: # For every decision made in the path.
                pheromone_paths[decision][curr_path_node] += pheromone_update # Update the pheromone.
                curr_path_node += 1 # Iterate current path node by 1.

            curr_path += 1 # Iterate current path by 1.
            run_num += 1 # Iterate run number by 1.

        pheromone_paths = evaporatePheromones(pheromone_paths, evaporation_rate) # Evaporate all pheromones.

        # Checking if the fitness for this iteration is better than the global best (not used for actual result)
        if (max(curr_bin_list) - min(curr_bin_list)) < fitness_best: # If current fitness better than best fitness.
            min_bins = curr_bin_list # Set list of minimum bins to current bin list.
            fitness_best = (max(curr_bin_list) - min(curr_bin_list)) # Set best as the current value.
            #print("New found with bins:", min_bins, 'as fitness value:', fitness_best) # Print update.

    #print(min_bins) # Print list of minimum bins.
    return fitness_best # Return the best fitness value.


'''
    Choose the path of the ant based on the values of the pheromones.

    :param items: the items that are to be placed into the bins.
    :param pheromones: the pheromones for each path node.
    :param bins: the number of bins used.
    :returns: The path the ant takes through the bins as it deposits the items.
'''
def choosePath(items, pheromones, bins): 
    path = []

    # Iterate through the items, choosing which bin to put the item in.
    for j in range(len(items)): # For each item in the list of items.

        bin_probs = [bin_probability[j] for bin_probability in pheromones] # Find probability for bins next in the path.

        sum_items = sum(bin_probs) # Sum the items as sum of probability.
        choice = random.uniform(0, sum_items) # Choose using random number between 0 and sum of item probability.
        counter = 0 # Initialise counter variable.
    
        # Choose a bin based on its probability
        for n in range(len(bin_probs)): # 
            
            counter += bin_probs[n]

            if choice <= counter:
                path.append(n)
                break

    return path


'''
    Evaporates all nodes in the list of pheromones.

    :param pheromones: the list of pheromones to be updated.
    :param evaporation_rate: multiplier value for the pheromones.
    :returns: Pheromones multiplied by the evaporation rate.
'''
def evaporatePheromones(pheromones, evaporation_rate):
    for pheromone in pheromones: # For each value in the list.abs(n)
        pheromone[:] = [(x * evaporation_rate) for x in pheromone] # Multiply by the evaporation rate.
    
    return pheromones # Return the updated values.


'''
    Carries out the specified experiment on BPP1.

    :param experimentNum: the experiment number to be carried out.
    :returns: List of fitness values of the five trials as a list.
'''
def bpp1Experiment(experimentNum):
    start_time = time.time() # Record the starting time.
    ex_bpp1 = [] # List to store the experiment results.
    if experimentNum == 1: # Experiment 1
        for i in range(5): # Carry out 5 trials.
            ex_bpp1.append(ACOBPP1(100, 0.90)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    elif experimentNum == 2: # Experiment 2
        for i in range(5): # Carry out 5 trials.
            ex_bpp1.append(ACOBPP1(100, 0.50)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    elif experimentNum == 3: # Experiment 3
        for i in range(5): # Carry out 5 trials.
            ex_bpp1.append(ACOBPP1(10, 0.90)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    elif experimentNum == 4: # Experiment 4
        for i in range(5): # Carry out 5 trials.
            ex_bpp1.append(ACOBPP1(10, 0.50)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    else: # If the experiment number was wrong.
        print('Please specify an experiment number 1 to 4.') # Output correction message.
    print('Fitness values for five trials: ',ex_bpp1) # Print the list of result fitness values.
    print('Best: ',min(ex_bpp1)) # Print the best value from the 5 trials.
    print('Worst: ',max(ex_bpp1)) # Print the worst value from the 5 trials.
    print('Time elapsed: ',time.time() - start_time,' seconds') # Print the time taken for the experiment.
    return ex_bpp1 # Return the list of values.


'''
    Carries out the specified experiment on BPP2.

    :param experimentNum: the experiment number to be carried out.
    :returns: List of fitness values of the five trials as a list.
'''
def bpp2Experiment(experimentNum):
    start_time = time.time() # Record the starting time.
    ex_bpp2 = [] # List to store the experiment results.
    if experimentNum == 1: # Experiment 1
        for i in range(5): # Carry out 5 trials.
            ex_bpp2.append(ACOBPP2(100, 0.90)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    elif experimentNum == 2: # Experiment 2
        for i in range(5): # Carry out 5 trials.
            ex_bpp2.append(ACOBPP2(100, 0.50)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    elif experimentNum == 3: # Experiment 3
        for i in range(5): # Carry out 5 trials.
            ex_bpp2.append(ACOBPP2(10, 0.90)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    elif experimentNum == 4: # Experiment 4
        for i in range(5): # Carry out 5 trials.
            ex_bpp2.append(ACOBPP2(10, 0.50)) # Add result of this trial to the results list.
            print('Trial ',i+1,' complete') # Print that a trial was completed.
    else: # If the experiment number was wrong.
        print('Please specify an experiment number 1 to 4.') # Output correction message.
    print('Fitness values for five trials: ',ex_bpp2) # Print the list of result fitness values.
    print('Best: ',min(ex_bpp2)) # Print the best value from the 5 trials.
    print('Worst: ',max(ex_bpp2)) # Print the worst value from the 5 trials.
    print('Time elapsed: ',time.time() - start_time,' seconds') # Print the time taken for the experiment.
    return ex_bpp2 # Return the list of values.

if __name__ == "__main__":
    """
        BPP1 experiments, uncomment as needed, experiments are commented due to taking a long time to run all of them.
    """
    #print('Bpp1 - Experiment 1: ')
    #bpp1Experiment(1)

    #print('Bpp1 - Experiment 2: ')
    #bpp1Experiment(2)

    #print('Bpp1 - Experiment 3: ')
    #bpp1Experiment(3)

    print('Bpp1 - Experiment 4: ')
    bpp1Experiment(4)
    
    """
        BPP2 experiments, uncomment as needed, experiments are commented due to taking a long time to run all of them.
    """
    #print('Bpp2 - Experiment 1: ')
    #bpp2Experiment(1)

    #print('Bpp2 - Experiment 2: ')
    #bpp2Experiment(2)

    #print('Bpp2 - Experiment 3: ')
    #bpp2Experiment(3)

    #print('Bpp2 - Experiment 4: ')
    #bpp2Experiment(4)
