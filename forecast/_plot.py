"""
This file contains various plotting functions to be used in both the Forecast and model classes.

"""
import altair

def plot_series(obj, **kwargs):
    """This method will plot the data stored in obj.data

    :param obj:
    :return:
    """


def plot_diagnostics(obj, **kwargs):
    """This method will plot the diagnostic data about a time series, including ACF / PACF, correlation, etc.

    :param obj:
    :param kwargs:
    :return:
    """


def plot_decomp(obj, **kwargs):
    """This method will decompose and plot the time series elements: trend, seasonality / cycle, and residuals.

    :param obj:
    :param kwargs:
    :return:
    """


def plot_prediction(obj, **kwargs):
    """This method will plot the actuals and predictions made by a given model.

    :param obj:
    :param kwargs:
    :return:
    """



####################
#
# The methods below may make more sense to live within the model class objects.
# It only makes sense to include them here if they are the same across all models -- but
# I won't know that until I build out those classes.
#
####################

def plot_importances(obj, **kwargs):
    """This method will plot the feature importances of a given model.

    :param obj:
    :param kwargs:
    :return:
    """


def plot_metrics(obj, **kwargs):
    """This method will plot metrics associated with the given model.

    :param obj:
    :param kwargs:
    :return:
    """