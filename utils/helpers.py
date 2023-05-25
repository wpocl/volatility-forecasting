import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def forecast(arr, order=(0, 1, 1)):
    model = ARIMA(arr, order=order)
    fit = model.fit()
    pred = fit.forecast(steps=1)
    return pred

days_per_month = pd.read_pickle("data/misc/days_per_month.pickle")
def monthly_vol(fd, month_and_year):
    grid_points = fd.grid_points[0]
    data_matrix = np.squeeze(fd.data_matrix)

    x_f = np.multiply(data_matrix, grid_points)
    x_x_f = np.multiply(data_matrix, grid_points ** 2)
    dev = np.sqrt(np.trapz(x_x_f, grid_points) - np.trapz(x_f, grid_points)**2)

    return dev * np.sqrt(days_per_month[month_and_year])

def rrmse(true, pred):
    rrmse = np.sqrt(sum((pred - true) ** 2) / sum(true ** 2))
    return rrmse