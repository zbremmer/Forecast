# Forecast
A convenience class for forecasting tasks

The goal of this class is to simplify tasks of forecasting. Users should be able to get up to speed quickly using the 
methods of the class. This is not meant to replace more advanced functionality of timeseries analysis, but rather is a 
way to explore the data, quickly prototype and test models, and determine which direction more in-depth analysis should 
take. 

# Model Classes

Each model should be created as a separate class. The models will exist as independent objects so that more than one can
be created by a user. 

All models should be built with the following assumptions: 
1. The instance of forecast will have a dataframe with a datetime index, a target field labeled y, and various features
2. The forecast start and end will be provided in the forecast_start and forecast_end attributes
3. The timeseries will be complete with no missing time steps (completed in clean_data() step)

All models should contain at minimum the following methods:
1. prepare_data() : This will handle scaling, lag generation, and test / train split
2. train() : This will train the model on the data and create a trained model, stored as self.model.model
3. predict() : This will run predictions for the forecast period, with forecast stored as self.model.predictions
4. plot_prediction() : This will plot the original time series and the prediction 

Additionally, models should take **kwargs in case users want to specify any additional criteria (scaling method, etc.)

## Notes
- How will this handle data at different time granularities (hourly, monthly, annual, etc)?


## Todo
- Build a simple EDA process to analyze the time series, plot ACF/PACF, cross-corelation (if exists), decomp, etc.
- Build plotting capabilities. Should include timeseries plotting and diagnostics (ACF/PACF), decomp, etc.
- Restructure so everything no in util
