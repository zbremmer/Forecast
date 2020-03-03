# Forecast
A convenience class for forecasting tasks

The goal of this class is to simplify tasks of forecasting. Users should be able to get up to speed quickly using the 
methods of the class. This is not meant to replace more advanced functionality of timeseries analysis, but rather is a 
way to explore the data, quickly prototype and test models, and determine which direction more in-depth analysis should 
take. 


## Notes
- How will this handle data at different time granularities (hourly, monthly, annual, etc)?


## Todo
- Build plotting capabilities using altair. Should include timeseries plotting and diagnostics (ACF/PACF), decomp, etc.
- Restructure so everything no in util
- Move test / train split and some feature generation (lags, scaling) to models
- Add models (SARIMAX, prophet?, surprise?)