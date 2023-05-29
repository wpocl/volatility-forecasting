### Introduction
Volatility, a measure of deviation in a distribution over a specific time period, is commonly forecasted by analysing historical volatility as a time series. These approaches overlook the shape and characteristics of the underlying return distribution. In our project, we address this limitation by leveraging the predicted return distribution obtained from functional principle component analysis (FPCA). By incorporating the shape of the distribution, we were able to estimate monthly volatility for two currency pairs more accurately than with a conventional method. In our comparative analysis, our approach outperformed a standard baseline model, showcasing the effectiveness of our methodology.

### Methodology
Density functions don't form a vector space because they are nonnegative and integrate to one. This means that FPCA is not directly applicable. To account for this, we first transform them using the methodology described in Kokoszka et al. [1]. Then we extract the first seven principal component functions and their scores. These scores are then forecasted to produce a step-ahead prediction, which we transform backwards to obtain a forecast for the density functions.

### Data
The raw data consists of daily opening prices for the currency pairs EURUSD and USDCAD from 01/02/2001 to 30/12/2022. The data is then binned into monthly samples consisting of daily logarithmic returns over that month. This histogram data is then used to produce a discretized density function estimate, which maps a return to its (estimated) probability of observation. The models are compared based on their step-ahead forecasts over 30 months, from July 2020 to December 2022.

### Results
The predictions made by our model are compared to the true monthly volatility observations in the following figure:

<p align="center">
  <img src="figures/comparison_of_model_forecasts.png" alt="Comparison of Model Forecasts">
</p>

The forecasting error of our model is shown in the figure below, alongside a baseline ARIMA (0, 1, 1) model, as measured by the root relative mean squared error:

<p align="center">
  <img src="figures/comparison_of_model_errors.png" alt="Comparison of Model Errors">
</p>

### Conclusion and Limitations
Based on the analysis of the presented plots, the model demonstrates superior performance compared to the baseline, showcasing its potential for accurate volatility prediction. However, it is crucial to acknowledge several limitations that could affect the generalisability and effectiveness of the model.

One significant limitation is the observed tendency of the model to lag behind monthly volatility observations. To address this issue, further investigation on a larger dataset is warranted. Exploring alternative approaches to forecasting component scores or trying different transformations of the density functions that have more stable component scores could potentially enhance the model's performance in this respect. Additionally, the method employed to calculate volatility from the distribution, which is sensitive to the discretization process, can be improved. Utilising a more robust measure of spread, such as the interquartile range, could yield more reliable results. Furthermore, it is essential to note that the model has been tested only on a limited sample of two currency pairs. Expanding the analysis to include a broader range of currency pairs would provide a more comprehensive evaluation of the model's effectiveness across different market conditions.

To overcome these limitations, a significant enhancement would involve implementing a generative model. This approach aims to identify and sample from the theoretical distribution of returns in a specific month, enabling the capture of underlying trends in the theoretical distribution and making the model robust to noise related to the specific sample from this distribution that was observed. By incorporating a generative model, the model's effectiveness could be further improved, providing a more reliable framework for volatility prediction across diverse market conditions.

### References
1. Kokoszka, P., Miao, H., Petersen, A., & Shang, H. L. (2019). Forecasting of density functions with an application to cross-sectional and intraday returns. International Journal of Forecasting, 35:4, pp. 1304-1317.