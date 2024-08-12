import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError('List must contain nine numbers.')

    # Convert list to 3x3 numpy array
    nparray = np.array(list).reshape(3,3)
   
    calculations = {
        'mean': calculate_mean(nparray),
        'variance': calculate_var(nparray),
        'standard deviation': calculate_std(nparray),
        'max': calculate_max(nparray),
        'min': calculate_min(nparray),
        'sum': calculate_sum(nparray)
    }

    return calculations

# Make matrix mean calculations
def calculate_mean(matrix):
    matrix_y_mean = matrix.mean(axis=0).tolist()
    matrix_x_mean = matrix.mean(axis=1).tolist()
    matrix_flat_mean = matrix.mean().tolist()
    # print('MEAN ======> ', [matrix_y_mean, matrix_x_mean, matrix_flat_mean])
    return [matrix_y_mean, matrix_x_mean, matrix_flat_mean]

# Make matrix variance calculations
def calculate_var(matrix):
    matrix_y_var = matrix.var(axis=0).tolist()
    matrix_x_var = matrix.var(axis=1).tolist()
    matrix_flat_var = matrix.var().tolist()
    # print('VAR ======> ', [matrix_y_var, matrix_x_var, matrix_flat_var])
    return [matrix_y_var, matrix_x_var, matrix_flat_var]

# Make matrix std calculations
def calculate_std(matrix):
    matrix_y_std = matrix.std(axis=0).tolist()
    matrix_x_std = matrix.std(axis=1).tolist()
    matrix_flat_std = matrix.std().tolist()
    # print('STD ======> ', [matrix_y_std, matrix_x_std, matrix_flat_std])
    return [matrix_y_std, matrix_x_std, matrix_flat_std]

# Make matrix max calculations
def calculate_max(matrix):
    matrix_y_max = matrix.max(axis=0).tolist()
    matrix_x_max = matrix.max(axis=1).tolist()
    matrix_flat_max = matrix.max().tolist()
    # print('MAX ======> ', [matrix_y_max, matrix_x_max, matrix_flat_max])
    return [matrix_y_max, matrix_x_max, matrix_flat_max]    

# Make matrix min calculations
def calculate_min(matrix):
    matrix_y_min = matrix.min(axis=0).tolist()
    matrix_x_min = matrix.min(axis=1).tolist()
    matrix_flat_min = matrix.min().tolist()
    # print('MIN ======> ', [matrix_y_min, matrix_x_min, matrix_flat_min])
    return [matrix_y_min, matrix_x_min, matrix_flat_min]

# Make matrix sum calculations
def calculate_sum(matrix):
    matrix_y_sum = matrix.sum(axis=0).tolist()
    matrix_x_sum = matrix.sum(axis=1).tolist()
    matrix_flat_sum = matrix.sum().tolist()
    # print('SUM ======> ', [matrix_y_sum, matrix_x_sum, matrix_flat_sum])
    return [matrix_y_sum, matrix_x_sum, matrix_flat_sum]

