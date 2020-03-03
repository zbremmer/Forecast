from forecast import _pipeline, _util, _models



class Forecast:
    """
    This class contains everything needed to perform forecasting. It was created to simplify the
    forecast modeling process and allow for the entire object to be saved as an artifact, including the raw data,
    model, forecasts, and other attributes.

    A class instance represents a single time series to be forecasted.
    TODO: Expand functionality to include multiple dynamic forecasting

    The data passed into the class should be a pandas dataframe structured as follows:

    1. The dataframe should have a datetime index
    2. The dataframe should have a single target column named "y"
    3. The dataframe can include additional features. Columns with a datatype of 'category' or 'object' will be treated
       as categorical features.

     TODO: Error handling, probably using decorators as described in
     https://code.tutsplus.com/tutorials/professional-error-handling-with-python--cms-25950

    Attributes
    ------------
    data : pandas.DataFrame
        A dataframe of the data to be used for forecasting
    forecast_start : str
        The start of the forecast period (should match the index of the dataframe)
    forecast_end : str
        The end of the forecast period (should match the index of the dataframe)
    lags : int
        The number of lags to generate for supervised learning (default = 90)
        TODO: This should be found using automated search in future versions of project -- only needed for supervised
        learning, not for ARIMA etc.

    """

    def __init__(self, df, forecast_start, forecast_end, lags: int = 90):

        self.data = df
        self.forecast_start = forecast_start
        self.forecast_end = forecast_end
        self.lags = lags
        self.agg_data = None
        self.train_data = None
        self.pred_data = None



    def clean_data(self):
        """
        This method adds days to the data series in order to ensure completeness. Future cleaning steps can be
        added in this method. Note that the add_days() method makes changes to the data attribute of a
        class instance in place.

        When a day is added, 0 is added to each numeric column and NaN is left in each categorical variable. This
        is done to prevent aggregation issues in generate_features(). The new 'NaN' categories will be dropped during
        feature generation.

        #TODO: Add completeness for data at different granularities (annual, monthly, hourly, etc.)

        :return:
        """
        try:
            _util.add_days(self)
            return True
        except Exception as e:
            return e


    def generate_features(self):
        """
        This method generates default features for the dataset.

        TODO: Users should be able to specify which columns are one hot encoded, which are scaled, which are
               weighted, etc.... But if none are specified, then we do it to all? << Scaling should be done by model>>

        In addition, this method will aggregate data to a daily total. There may be need to omit this in the future
        for different use cases or forecasting methods.

        Note that when a day is added in clean_data(), 0 is added to each numeric column and NaN is added to each
        categorical variable. This is done to prevent aggregation issues in generate_features(). The new 'NaN'
        categories will be dropped during feature generation.

        :return:
        """
        try:
            _util.aggregate_data(self)
            _util.split_train_pred(self)
            _util.get_lags(self)
            _util.clean_pred(self)
            _util.get_day_features(self)

            # Replace above with encode_weights() and one_hot_encode()

            return True

        except Exception as e:
            return e


    def fit_model(self, model_name):
        """

        :param model_name:
        :return:
        """

        _util.test_train_split(self)
        self.model = _util.get_model(model_name)
        self.model.fit()

        ### If the model is supervised, then should go through supervised data conversion. If it's ARIMA, etc, then
        # should go through converting to a true timeseries