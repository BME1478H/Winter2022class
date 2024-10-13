import numpy as np
import pandas as ps


# define a function that calculates mean squared error
def squared_error(prediction, data):
        residual = prediction - data
        mse = (residual**2).mean()
        return mse
    
def main():
    # read in the data from the .csv passed to our script
    filename = "bacteria.csv"
    start = 0.1
    stop = 1 
    step=0.1
    rate_params = [start, stop, step]

    experiment_data = ps.read_csv(filename, header=None).values.flatten()

    print("Experiment Data:", experiment_data)

    range_rate = np.arange(float(start), float(stop), float(step))
    

    mse = [] 
    print(mse)
    N0 = experiment_data[0] 
    t = np.linspace(0, 10, len(experiment_data)) 
    for r in range_rate: 
        prediction = N0 * np.exp(r * t) 
        mse.append(squared_error(prediction, experiment_data))

    best_fit = range_rate[np.argmin(mse)]

    print('We predict the rate of growth of this bacterial population to be',best_fit)

main()
