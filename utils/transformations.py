from statistics import geometric_mean

import numpy as np
from skfda import FDataGrid


class CODA:
    def __init__(self):
        self._geometric_mean = None

    def fit_transform(self, fd):
        # Unpack FDataGrid
        grid_points = fd.grid_points
        data_matrix = np.squeeze(fd.data_matrix)

        # Calculate and store geometric mean 
        self._geometric_mean = np.apply_along_axis(geometric_mean, 
                                             axis=0, arr=data_matrix)
        
        # Geometric mean standardisation
        transform_functions = data_matrix / self._geometric_mean
        integral_area = (
            np.trapz(transform_functions, grid_points)
            ).reshape(-1, 1)
        transform_functions /= integral_area

        # Log-ratio transformation
        geometric_mean_like_integral = (
            np.exp(np.trapz(np.log(transform_functions), grid_points))
            ).reshape(-1, 1)
        transform_functions /= geometric_mean_like_integral
        transform_functions = np.log(transform_functions)

        # Create FDataGrid for transformed functions
        fd_transformed = FDataGrid(grid_points=grid_points,
                                   data_matrix=transform_functions)
        
        return fd_transformed
        
    def inverse_transform(self, fd_transformed_):
        # Unpack FDataGrid
        grid_points = fd_transformed_.grid_points
        data_matrix = np.squeeze(fd_transformed_.data_matrix)

        # Inverse log-ratio transformation
        inverse_of_gmli = ( # inverse of geometric_mean_like_integral
            np.trapz(np.exp(data_matrix), grid_points)
            ).reshape(-1, 1)    
        transform_functions = np.exp(data_matrix) / inverse_of_gmli

        # Inverse geometric mean standardisation
        transform_functions *= self._geometric_mean
        integral_area = ( 
            np.trapz(transform_functions, grid_points)
            ).reshape(-1, 1)
        transform_functions /= integral_area

        # Create FDataGrid for transformed functions
        fd_ = FDataGrid(grid_points=grid_points,
                        data_matrix=transform_functions)
        
        return fd_